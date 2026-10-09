#!/usr/bin/env python3
"""Round 20 compute — FULL Myrov-convention grid (Level-2 protocol, the
convention-sensitivity arm of Phase 1 completed into a full plane).

Convention (inferred Myrov et al., per R19 §2.5):
  - oscillator frequencies: numeric Hz values used directly as angular
    rates (omega NOT multiplied by 2*pi; per-node omega std ~2.6)
  - W = max-normalized structural connectome WITHOUT row normalization
  - K, L on the [0,8]-style scale (extended to K<=10 to cover the
    DFA-matched operating point that extrapolated to K~9-9.5)
  - sigma = 0.2

Grid: K in {0, 0.5, 1.0, ..., 10.0} (21 values)
      L in {0, 2, 4, 6, 8} (5 values)  -> 105 combos
      T = 120 s per combo (30 s warm-up + 90 s analysis)
Outputs per combo: mean node order, node DFA distribution (median,
frac>0.65), grand-mean PSD (3-30 Hz band, both Hz and convention units),
PLV, envelope CC, structure-function correlations (order~strength,
DFA~strength, PLV~W, CC~W).

CLI:
  chunk i      run combos [9*i, 9*i+9) (12 chunks)
  combine      merge parts -> myrov_grid.npz + myrov_grid.json
"""
import json
import sys
import time
import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from phase1_kuramoto import (load_sc, load_peak_params, run_sim, sf_surfaces,
                             PSD_BLOCK)

OUT = "/home/z/my-project/glm agent 2/research/phase2"
GRID_DIR = f"{OUT}/grid"
SUBJ = "101309"
SIGMA = 0.2
T_SIM = 120.0
WARM = 30.0
CHUNK = 9

KS = [round(0.5 * i, 2) for i in range(21)]        # 0 .. 10 step 0.5
LS = [0.0, 2.0, 4.0, 6.0, 8.0]
COMBOS = [(k, l) for l in LS for k in KS]          # L-major order

FREQS_100 = np.fft.rfftfreq(PSD_BLOCK, 0.01)       # 100 Hz sampling of z


def build_omega(seed=7):
    rng = np.random.default_rng(seed)
    peaks = load_peak_params()
    if len(peaks) == 0:
        peaks = np.array([[10.0, 1.0, 2.0]])
    prob = peaks[:, 1] / peaks[:, 1].sum()
    freqs = np.empty((94, 50), dtype=np.float32)
    for n in range(94):
        k = rng.choice(len(peaks), p=prob)
        cf, bw = float(peaks[k, 0]), max(float(peaks[k, 2]), 1.0)
        freqs[n] = np.clip(rng.normal(cf, bw, 50), 3.0, 30.0)
    return freqs.astype(np.float32)


def main_chunk(i):
    import os
    os.makedirs(GRID_DIR, exist_ok=True)
    lo, hi = CHUNK * i, min(CHUNK * (i + 1), len(COMBOS))
    sel = COMBOS[lo:hi]
    Ks = np.array([c[0] for c in sel], dtype=np.float32)
    Ls = np.array([c[1] for c in sel], dtype=np.float32)

    omega = build_omega()
    W_ext, W_sym, strength = load_sc(SUBJ, row_normalize=False)

    t0 = time.time()
    res = run_sim(W_ext, omega, Ks, Ls, SIGMA, T_s=T_SIM, warmup_s=WARM,
                  seed=500, want_matrices=True, progress_every=0)
    sf = sf_surfaces(W_sym, res)
    dt = time.time() - t0

    out = {
        "K": Ks.astype(np.float64), "L": Ls.astype(np.float64),
        "mean_order": res["mean_order"].mean(axis=1).astype(np.float64),
        "dfa_median": np.nanmedian(res["dfa"], axis=1),
        "dfa_mean": np.nanmean(res["dfa"], axis=1),
        "frac065": res["frac065"].astype(np.float64),
        "mean_plv": res["mean_plv"].astype(np.float64),
        "mean_cc": res["mean_cc"].astype(np.float64),
        "psd": res["psd"].astype(np.float64),           # (C, F) grand-mean node PSD
        "psd_freqs": res["psd_freqs"].astype(np.float64),
        "order_strength_rho": sf["order_strength_rho"].astype(np.float64),
        "dfa_strength_rho": sf["dfa_strength_rho"].astype(np.float64),
        "plv_edge_rho": sf["plv_edge_rho"].astype(np.float64),
        "cc_edge_rho": sf["cc_edge_rho"].astype(np.float64),
        "sim_seconds": dt,
    }
    np.savez_compressed(f"{GRID_DIR}/part{i:02d}.npz", **out)
    for j in range(len(sel)):
        print(f"K={Ks[j]:5.2f} L={Ls[j]:4.1f}: order={out['mean_order'][j]:.3f} "
              f"dfa_med={out['dfa_median'][j]:.3f} frac065={out['frac065'][j]:.3f} "
              f"ord~str={sf['order_strength_rho'][j]:+.3f} plv~W={sf['plv_edge_rho'][j]:+.3f}",
              flush=True)
    print(f"[chunk {i}] {len(sel)} combos in {dt:.0f}s -> part{i:02d}.npz", flush=True)


def main_combine():
    import glob
    parts = sorted(glob.glob(f"{GRID_DIR}/part*.npz"))
    print("parts:", len(parts))
    allk, alll, keys = [], [], []
    acc = {}
    for p in parts:
        d = np.load(p)
        allk.append(d["K"]); alll.append(d["L"])
        for k in d.files:
            if k in ("K", "L", "sim_seconds"):
                continue
            acc.setdefault(k, []).append(d[k])
    K = np.concatenate(allk); L = np.concatenate(alll)
    merged = {k: np.concatenate(v) for k, v in acc.items()}
    np.savez_compressed(f"{GRID_DIR}/myrov_grid.npz", K=K, L=L, **merged)

    # MEG match: DFA-median surfaces; targets from meg_obs
    mo = np.load("/home/z/my-project/glm agent 2/research/phase1/meg_obs.npz")
    dfa_t1 = float(np.median(mo["run1_dfa_ch"]))
    dfa_t2 = float(np.median(mo["run2_dfa_ch"]))
    print("meg_obs DFA targets:", dfa_t1, dfa_t2)
    summary = {
        "n_combos": int(len(K)),
        "sigma": SIGMA, "T_s": T_SIM, "subject": SUBJ,
        "K_range": [float(K.min()), float(K.max())],
        "L_values": sorted(set(float(x) for x in L)),
        "dfa_median_range": [float(np.nanmin(merged["dfa_median"])),
                              float(np.nanmax(merged["dfa_median"]))],
        "frac065_max": float(merged["frac065"].max()),
        "order_range": [float(merged["mean_order"].min()),
                        float(merged["mean_order"].max())],
    }
    with open(f"{GRID_DIR}/myrov_grid.json", "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "chunk"
    if cmd == "chunk":
        main_chunk(int(sys.argv[2]))
    elif cmd == "combine":
        main_combine()
