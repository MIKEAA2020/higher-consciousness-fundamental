#!/usr/bin/env python3
"""Round 21 probe — validate the corrected evoked reshape on subject 210.

Checks: dims/trial counts, ERP morphology (pre-pulse flat vs post-pulse
deflection around pulse sample idx 125), trial amplitude hygiene.
"""
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
import numpy as np
from rd2_lib import load_evoked, evoked_paths, FS_EV, PULSE_SAMPLE

for cond in ("awake", "ketamine"):
    p = evoked_paths("210", cond)
    d = load_evoked(p)
    arr = d["arr"]                    # (60, 251, ntr)
    print(f"\n=== 210 {cond} ({p.split('/')[-1]}) ===")
    print(f"dims={d['dims']} declared={d['n_declared']:,} recovered={d['n_recovered']:,} "
          f"complete_trials={d['n_complete']} truncated={d['truncated']}")
    print(f"amplitude range: {arr.min():.1f} .. {arr.max():.1f} uV")
    t = np.arange(arr.shape[1]) / FS_EV * 1000.0
    pulse_ms = (PULSE_SAMPLE - 1) / FS_EV * 1000.0
    # trial hygiene
    mabs = np.abs(arr).max(axis=(0, 1))
    print(f"per-trial max|amp|: median {np.median(mabs):.1f} uV, "
          f"p95 {np.percentile(mabs, 95):.1f}, max {mabs.max():.1f}; "
          f"trials>150uV: {(mabs > 150).sum()}/{arr.shape[2]}")
    # grand-average ERP (all trials, correct order)
    erp = arr.mean(axis=2)            # (60, 251)
    gm = erp.mean(axis=0)
    pre = slice(0, PULSE_SAMPLE - 1)
    post = slice(PULSE_SAMPLE, 251)
    print(f"pulse at sample idx {PULSE_SAMPLE - 1} = {pulse_ms:.0f} ms from epoch start")
    print(f"grand-mean ERP: pre-pulse RMS {np.sqrt((gm[pre] ** 2).mean()):.3f} uV, "
          f"post-pulse RMS {np.sqrt((gm[post] ** 2).mean()):.3f} uV")
    pk = int(np.abs(gm[post]).argmax()) + PULSE_SAMPLE
    print(f"grand-mean peak {gm[pk]:.2f} uV at {t[pk]:.0f} ms "
          f"({t[pk] - pulse_ms:.0f} ms post-pulse)")
    # GFP
    gfp = (erp ** 2).mean(axis=0)
    pk2 = int(gfp[post].argmax()) + PULSE_SAMPLE
    print(f"GFP peak {gfp[pk2]:.2f} uV^2 at {t[pk2]:.0f} ms ({t[pk2] - pulse_ms:.0f} ms post-pulse)")
    # per-channel peak latency relative to pulse (post window only)
    lat = []
    for c in range(erp.shape[0]):
        j = int(np.abs(erp[c][post]).argmax()) + PULSE_SAMPLE
        lat.append(t[j] - pulse_ms)
    print(f"per-channel peak latency post-pulse: median {np.median(lat):.0f} ms, "
          f"IQR [{np.percentile(lat, 25):.0f}, {np.percentile(lat, 75):.0f}]")

# Round-20 comparison: wrong-order scramble on the SAME complete awake file
d = load_evoked(evoked_paths("210", "awake"))
flat = d["arr"].flatten(order="F")
n = d["n_complete"]
X_wrong = flat[:n * 60 * 251].reshape(n, 60, 251)
X_wrong = np.transpose(X_wrong, (1, 0, 2))      # Round-20 mapping
erp_w = X_wrong.mean(axis=1)
gm_w = erp_w.mean(axis=0)
print(f"\nRound-20 wrong-order mapping check: grand-mean peak {gm_w[np.abs(gm_w).argmax()]:.2f} uV "
      f"at {t[np.abs(gm_w).argmax()]:.0f} ms (pre-pulse structure expected = scrambling signature)")
