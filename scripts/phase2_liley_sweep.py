#!/usr/bin/env python3
"""Phase 2 — Bojak-Liley / Steyn-Ross mean-field anesthesia sweep (v3, final).

Full second-order-PSP macrocolumn; units ms / mV / spikes/ms.
Disambiguated units (documented): gamma in ms^-1 (Table A); S_max and the
exogenous p's are SPIKES/SECOND (Table A's 'ms-1' is internally
inconsistent with its own equations; the /s reading puts the waking
equilibrium in the sigmoid's active range -- the only self-consistent
choice; the /ms reading drives he past reversal and diverges).

Filter: d2I_jk/dt2 + 2*gamma_jk dI_jk/dt + gamma_jk^2 I_jk
        = gamma_jk * G_jk * e * R_jk(t),   R_jk = N^beta S_j + N^alpha S_e + p_jk
(DC gain G e / gamma -> IPSP charge; per-pulse peak amplitude = G.)

Propofol (Liang et al. 2015 / Steyn-Ross): gamma_i -> gamma_i / lambda
(IPSP duration x lambda; charge x lambda; peak unchanged).

EEG = -he at 1 kHz; Welch PSD; 2-20 Hz peak per lambda = the spec's
discriminating observable (alpha-peak trajectory under inhibition).

Outputs: research/phase2/liley/liley_sweep.npz + .json
"""
import json
import os
import numpy as np
from scipy.signal import welch

OUT = "/home/z/my-project/glm agent 2/research/phase2/liley"
os.makedirs(OUT, exist_ok=True)

G_e, G_i = 0.18, 0.37
gam_e, gam_i0 = 0.3, 0.065
h_rest = -70.0
h_e_rev, h_i_rev = 45.0, -90.0
Nbee, Nbei = 3034.0, 3034.0
Nbie, Nbii = 536.0, 536.0
Nae, Naei = 4000.0, 2000.0
g_e, g_i = 0.28, 0.14
Smax = 1.1 / 1000.0          # spikes/ms (Table A 1.1, read as /s)
TAU = 40.0
THETA = -60.0
PEE, PIE = 1.1 / 1000.0, 1.6 / 1000.0
PEI, PII = 1.6 / 1000.0, 1.1 / 1000.0
ALPHA_N = 0.05
DT = 0.1
T_WARM = 20000.0
T_SIM = 80000.0
LAMS = np.round(np.arange(1.0, 1.51, 0.05), 3)
EULERC = 2.71828


def run():
    def sig_e(h):
        return Smax / (1.0 + np.exp(-g_e * (h - THETA)))

    def sig_i(h):
        return Smax / (1.0 + np.exp(-g_i * (h - THETA)))

    # single-column SR treatment: long-range input exogenous, frozen at the
    # waking fixed-point firing rate (recurrent N^alpha destabilizes the
    # single macrocolumn; standard single-column reduction, documented)
    SE0 = Smax / (1.0 + np.exp(-g_e * (-64.0 - THETA)))

    nL = len(LAMS)
    gam_i = gam_i0 / LAMS
    rng = np.random.default_rng(9)
    he = np.full(nL, -64.0)
    hi = np.full(nL, -64.0)
    Iee = np.zeros(nL); dIee = np.zeros(nL)
    Iei = np.zeros(nL); dIei = np.zeros(nL)
    Iie = np.zeros(nL); dIie = np.zeros(nL)
    Iii = np.zeros(nL); dIii = np.zeros(nL)

    n_steps = int((T_WARM + T_SIM) / DT)
    warm_steps = int(T_WARM / DT)
    n_store = int(T_SIM / DT)
    store = np.zeros((nL, n_store))

    for step in range(n_steps):
        Se = sig_e(he); Si = sig_i(hi)
        Pee = PEE * (1.0 + ALPHA_N * rng.standard_normal(nL))
        Pei = PEI * (1.0 + ALPHA_N * rng.standard_normal(nL))
        Pie = PIE * (1.0 + ALPHA_N * rng.standard_normal(nL))
        Pii = PII * (1.0 + ALPHA_N * rng.standard_normal(nL))

        # linear-probe noise: multiplicative on the full pulse-train drive
        # (the S1 p-only noise is dynamically invisible at these gains;
        # documented deviation -- the probe exists to reveal the resonance)
        R_ee = (Nbee * Se + Nae * SE0 + PEE) * (1.0 + ALPHA_N * rng.standard_normal(nL))
        R_ei = (Nbei * Se + Naei * SE0 + PEI) * (1.0 + ALPHA_N * rng.standard_normal(nL))
        R_ie = (Nbie * Si + PIE) * (1.0 + ALPHA_N * rng.standard_normal(nL))
        R_ii = (Nbii * Si + PII) * (1.0 + ALPHA_N * rng.standard_normal(nL))

        # IPSPs are hyperpolarizing: inhibitory filter inputs carry the
        # negative sign (G_i is the IPSP magnitude)
        ddIee = gam_e * G_e * EULERC * R_ee - 2 * gam_e * dIee - gam_e ** 2 * Iee
        ddIei = gam_e * G_e * EULERC * R_ei - 2 * gam_e * dIei - gam_e ** 2 * Iei
        ddIie = -gam_i * G_i * EULERC * R_ie - 2 * gam_i * dIie - gam_i ** 2 * Iie
        ddIii = -gam_i * G_i * EULERC * R_ii - 2 * gam_i * dIii - gam_i ** 2 * Iii

        psi_ee = (h_e_rev - he) / (h_e_rev - h_rest)
        psi_ei = (h_e_rev - hi) / (h_e_rev - h_rest)
        psi_ie = (h_i_rev - he) / (h_i_rev - h_rest)
        psi_ii = (h_i_rev - hi) / (h_i_rev - h_rest)

        F1 = (h_rest - he + psi_ee * Iee + psi_ie * Iie) / TAU
        F2 = (h_rest - hi + psi_ei * Iei + psi_ii * Iii) / TAU

        he += F1 * DT; hi += F2 * DT
        Iee += dIee * DT; dIee += ddIee * DT
        Iei += dIei * DT; dIei += ddIei * DT
        Iie += dIie * DT; dIie += ddIie * DT
        Iii += dIii * DT; dIii += ddIii * DT

        if step >= warm_steps:
            k = step - warm_steps
            if k < n_store:
                store[:, k] = -he

    fs = 1000.0
    f, P = welch(store, fs=fs, nperseg=16384, axis=1)
    out = {"lambda": LAMS.tolist(), "peak_hz": [], "he_eq": [], "he_std": [],
           "alpha_pow": [], "delta_pow": []}
    for j in range(nL):
        m = (f >= 2) & (f <= 20)
        pk = float(f[m][int(np.argmax(P[j][m]))])
        pa = float(P[j][(f >= 8) & (f <= 15)].sum())
        pd = float(P[j][(f >= 1) & (f <= 4)].sum())
        out["peak_hz"].append(pk)
        out["he_eq"].append(float(store[j].mean()))
        out["he_std"].append(float(store[j].std()))
        out["alpha_pow"].append(pa)
        out["delta_pow"].append(pd)
        print(f"lambda={LAMS[j]:.2f}: peak={pk:5.2f} Hz he_eq={store[j].mean():7.2f} "
              f"he_std={1000*store[j].std():6.1f} uV a/d={pa/max(pd,1e-30):6.2f}", flush=True)
    np.savez(f"{OUT}/liley_sweep.npz", lam=LAMS, freqs=f, psd=P)
    with open(f"{OUT}/liley_sweep.json", "w") as fj:
        json.dump(out, fj, indent=1)
    print("saved liley_sweep.npz/.json")


if __name__ == "__main__":
    run()
