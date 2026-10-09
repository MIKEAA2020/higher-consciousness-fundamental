#!/usr/bin/env python3
"""Smoke test for phase1_kuramoto: (1) online block-DFA vs offline DFA on
known signals; (2) tiny simulation run for numerical sanity."""
import numpy as np
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
from phase1_kuramoto import run_sim, load_sc, sample_omega, _block_dfa, _dfa_from_acc, DFA_WINS_FULL, DFA_CHUNK_FULL
from phase1_meg import dfa

rng = np.random.default_rng(5)

# --- 1. DFA cross-validation on synthetic signals ---
for name, sig in [("white", rng.standard_normal(24000)),
                  ("fBm-H0.7", np.cumsum(0.7 and None or None) if False else None)]:
    if name == "fBm-H0.7":
        # fractional noise with H~0.7 -> DFA ~0.7: AR-like long memory approx
        z = rng.standard_normal(24000)
        x = np.zeros(24000)
        for i in range(1, 24000):
            x[i] = 0.995 * x[i - 1] + z[i] * 0.1 + 0.05 * z[i - 1]
        sig = x
    acc = {"sum_var": np.zeros((1, 1, len(DFA_WINS_FULL))),
           "counts": np.zeros((1, 1, len(DFA_WINS_FULL)))}
    # _block_dfa expects PROFILE samples (running cumsum), as in the simulator
    prof = np.cumsum(sig - sig.mean())
    Pbuf = prof[:len(prof) // DFA_CHUNK_FULL * DFA_CHUNK_FULL].reshape(1, 1, -1)
    for i0 in range(0, Pbuf.shape[2], DFA_CHUNK_FULL):
        _block_dfa(Pbuf[:, :, i0:i0 + DFA_CHUNK_FULL], acc, DFA_WINS_FULL, DFA_CHUNK_FULL)
    online = float(_dfa_from_acc(acc, DFA_WINS_FULL)[0, 0])
    offline = dfa(sig, 100.0)
    print(f"{name:10s} online={online:.3f} offline={offline:.3f}")

# --- 2. tiny sim sanity: order should rise with K; PLV rise with L ---
W_ext, W_sym, strength = load_sc("101309")
omega = sample_omega(rng)
r = run_sim(W_ext, omega, np.array([5.0, 30.0]), np.array([5.0, 30.0]), 5.0,
            T_s=15.0, warmup_s=5.0, dfa_wins=[100, 178, 316, 562, 1000],
            dfa_chunk=1000, seed=3, progress_every=0)
print("K,L=(5,5):   order", round(float(r['mean_order'][0].mean()), 3),
      "| dfa", round(float(np.nanmean(r['dfa'][0])), 3),
      "| plv", round(float(r['mean_plv'][0]), 3))
print("K,L=(30,30): order", round(float(r['mean_order'][1].mean()), 3),
      "| dfa", round(float(np.nanmean(r['dfa'][1])), 3),
      "| plv", round(float(r['mean_plv'][1]), 3))
print("psd freqs:", np.round(r['psd_freqs'][:5], 2), "...", np.round(r['psd_freqs'][-1], 1))
print("psd peak (combo1):", round(float(r['psd_freqs'][np.argmax(r['psd'][1])]), 2), "Hz")
