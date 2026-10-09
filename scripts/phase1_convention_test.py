#!/usr/bin/env python3
"""Convention-sensitivity test for Phase 1.

The primary run uses physical rad/s frequencies + row-normalized W (puts the
transition inside the [0,40] rad/s plane) — but row normalization equalizes
each node's total incoming weight, which plausibly suppresses structure-
function coupling (node strength no longer modulates input strength).

Myrov et al.'s own convention (inferred): oscillator frequencies with
numeric Hz values used directly as angular rates, W max-normalized WITHOUT
row normalization, K,L in [0,8]. This test runs that convention at a few
(K,L) points and reports the structure-function correlations.

Run: python3 phase1_convention_test.py
"""
import sys
import numpy as np
sys.path.insert(0, "/home/z/my-project/scripts")
from phase1_kuramoto import load_sc, load_peak_params, run_sim, sf_surfaces

N_OSC_HZ = 50
rng = np.random.default_rng(7)

# Myrov-convention omega: numeric Hz values as angular rates
peaks = load_peak_params()
if len(peaks) == 0:
    peaks = np.array([[10.0, 1.0, 2.0]])
prob = peaks[:, 1] / peaks[:, 1].sum()
freqs = np.empty((94, N_OSC_HZ), dtype=np.float32)
for n in range(94):
    k = rng.choice(len(peaks), p=prob)
    cf, bw = float(peaks[k, 0]), max(float(peaks[k, 2]), 1.0)
    freqs[n] = np.clip(rng.normal(cf, bw, N_OSC_HZ), 3.0, 30.0)
omega_hz = freqs.astype(np.float32)          # NOT multiplied by 2*pi

# raw max-normalized SC (no row normalization)
W_ext, W_sym, strength = load_sc("101309", row_normalize=False)

print("per-node omega std (Hz-units):", round(float(omega_hz.std(axis=1).mean()), 2))
for (K, L, sig) in [(1.0, 4.0, 0.2), (2.0, 4.0, 0.2), (3.0, 4.0, 0.2),
                    (3.0, 8.0, 0.2), (5.0, 8.0, 0.2),
                    (6.0, 8.0, 0.2), (7.0, 8.0, 0.2), (8.0, 8.0, 0.2)]:
    r = run_sim(W_ext, omega_hz, np.array([K]), np.array([L]), sig,
                T_s=150.0, warmup_s=30.0, seed=500, want_matrices=True,
                progress_every=0)
    sf = sf_surfaces(W_sym, r)
    print(f"K={K} L={L} sigma={sig}: order={r['mean_order'][0].mean():.3f} "
          f"dfa_med={np.nanmedian(r['dfa'][0]):.3f} frac065={r['frac065'][0]:.3f} "
          f"ord~str={sf['order_strength_rho'][0]:+.3f} "
          f"dfa~str={sf['dfa_strength_rho'][0]:+.3f} "
          f"plv~W={sf['plv_edge_rho'][0]:+.3f} cc~W={sf['cc_edge_rho'][0]:+.3f}",
          flush=True)
