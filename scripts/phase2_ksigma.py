#!/usr/bin/env python3
"""Phase 2 — the (K, sigma) model surface under the PRIMARY Phase-1
convention (physical rad/s, row-normalized W, omega = MEG-peak-sampled
2*pi*f, L = L* = 40 rad/s), for the per-sedation-level beta-hat fits.

Grid: K in {5, 10, ..., 40} rad/s (8) x sigma in {0.5, 1, 2, 3, 4, 6, 8,
12} (8) = 64 combos, T = 90 s (20 warm-up + 70 analysis), seed 800.

CLI: phase2_ksigma.py CHUNK     (9 combos per chunk, 8 chunks)
     phase2_ksigma.py combine
"""
import json
import sys
import time
import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from phase1_kuramoto import load_sc, run_sim, PSD_BLOCK

OUT = "/home/z/my-project/glm agent 2/research/phase2/ksigma"
import os
os.makedirs(OUT, exist_ok=True)
SUBJ = "101309"
LSTAR = 40.0
T_SIM = 90.0
WARM = 20.0
CHUNK = 9

KS = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]
SIGMAS = [0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0]
COMBOS = [(k, s) for s in SIGMAS for k in KS]     # sigma-major


def build_omega(seed=7):
    """Primary-convention omega: MEG-peak-sampled Hz * 2*pi (rad/s)."""
    from phase1_kuramoto import load_peak_params
    rng = np.random.default_rng(seed)
    peaks = load_peak_params()
    if len(peaks) == 0:
        peaks = np.array([[10.0, 1.0, 2.0]])
    prob = peaks[:, 1] / peaks[:, 1].sum()
    freqs = np.empty((94, 50), dtype=np.float32)
    for n in range(94):
        kk = rng.choice(len(peaks), p=prob)
        cf, bw = float(peaks[kk, 0]), max(float(peaks[kk, 2]), 1.0)
        freqs[n] = np.clip(rng.normal(cf, bw, 50), 3.0, 30.0)
    return (2.0 * np.pi * freqs).astype(np.float32)


def main_chunk(i):
    lo, hi = CHUNK * i, min(CHUNK * (i + 1), len(COMBOS))
    sel = COMBOS[lo:hi]
    Ks = np.array([c[0] for c in sel], dtype=np.float32)
    Ss = [c[1] for c in sel]
    omega = build_omega()
    W_ext, W_sym, strength = load_sc(SUBJ)        # row-normalized (primary)
    out = {"K": [], "sigma": [], "dfa_median": [], "frac065": [],
           "mean_order": [], "alpha_hz": []}
    for j, (k, s) in enumerate(sel):
        res = run_sim(W_ext, omega, np.array([k], dtype=np.float32),
                      np.array([LSTAR], dtype=np.float32), s, T_s=T_SIM,
                      warmup_s=WARM, seed=800, want_matrices=False,
                      progress_every=0)
        psd = res["psd"][0]
        f = res["psd_freqs"]
        m = (f >= 3) & (f <= 30)
        # model alpha peak: strongest 7-13 Hz rise over the 1/f-ish local slope
        fm, pm = f[m], psd[m]
        lpm = np.log(pm + 1e-30)
        peak_hz = None
        try:
            from fooof import FOOOF
            fg = FOOOF(peak_width_limits=[0.5, 12.0], max_n_peaks=8,
                       min_peak_height=0.05, verbose=False)
            fg.fit(fm, pm)
            cfs = [p[0] for p in fg.peak_params_]
            inband = [c for c in cfs if 7 <= c <= 13]
            peak_hz = float(min(inband, key=lambda c: abs(c - 10))) if inband else None
        except Exception:
            pass
        out["K"].append(float(k)); out["sigma"].append(float(s))
        out["dfa_median"].append(float(np.nanmedian(res["dfa"][0])))
        out["frac065"].append(float(res["frac065"][0]))
        out["mean_order"].append(float(res["mean_order"][0].mean()))
        out["alpha_hz"].append(peak_hz)
        print(f"K={k:5.1f} sig={s:5.1f}: dfa_med={out['dfa_median'][-1]:.3f} "
              f"alpha={peak_hz} order={out['mean_order'][-1]:.3f}", flush=True)
    def clean(v):
        a = np.array(v, dtype=object) if any(x is None for x in v) else np.array(v)
        if a.dtype == object:
            a = np.array([np.nan if x is None else float(x) for x in v])
        return a
    np.savez(f"{OUT}/part{i:02d}.npz", **{k: clean(v) for k, v in out.items()})


def main_combine():
    import glob
    parts = sorted(glob.glob(f"{OUT}/part*.npz"))
    acc = {}
    for p in parts:
        d = np.load(p, allow_pickle=True)
        for k in d.files:
            acc.setdefault(k, []).append(d[k])
    merged = {k: np.concatenate(v) for k, v in acc.items()}
    np.savez(f"{OUT}/ksigma_surface.npz", **merged)
    print("combos:", len(merged["K"]))
    print("dfa_median range:", float(np.nanmin(merged["dfa_median"])),
          float(np.nanmax(merged["dfa_median"])))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "chunk":
        main_chunk(int(sys.argv[2]))
    else:
        main_combine()
