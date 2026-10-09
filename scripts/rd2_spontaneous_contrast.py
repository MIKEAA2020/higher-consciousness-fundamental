#!/usr/bin/env python3
"""Round 21 — spontaneous-LZ contrast (Farnes et al. 2020 main finding).

Awake vs ketamine spontaneous EEG (first two recordings awake, last two
ketamine per readme), eyes open/closed, per subject. Instrument = the
Phase-2-established Farnes/Reynante port (Hilbert envelope, mean-binarize,
LZW, 5-shuffle normalization) at the native 8-s epoching (pnts=2000 @ 250 Hz).

Usage: python3 rd2_spontaneous_contrast.py <subj_start> <subj_end>
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from rd2_evoked_contrast import fast_lzw_count, lz_norm
from rd2_lib import SUBJECTS, spontaneous_files, load_set_fdt

OUT = "/home/z/my-project/glm agent 2/research/phase2/farnes"
os.makedirs(OUT, exist_ok=True)

MAX_EPOCHS = 10          # 80 s per file (files have 14-15 x 8 s)
N_SHUF = 5


def analyse_file(path, cond, eyes, subject):
    t0 = time.time()
    data, meta = load_set_fdt(path)
    n_ep = min(data.shape[2], MAX_EPOCHS)
    X = data[:, :, :n_ep]                      # (62, 2000, n_ep)
    fs = meta["srate"]
    seed = int(subject) * 4 + (0 if cond == "awake" else 2) + \
        (0 if eyes == "open" else 1) + 21
    rng = np.random.default_rng(seed)

    res = dict(file=os.path.basename(path), condition=cond, eyes=eyes,
               subject=subject, srate=fs, nbchan=meta["nbchan"],
               epochs=n_ep, duration_s=float(n_ep * X.shape[1] / fs))

    # --- sanity: alpha peak of mean PSD (Welch over epochs) ---
    from scipy.signal import welch
    f, P = welch(X.reshape(X.shape[0], -1), fs=fs, nperseg=int(4 * fs),
                 noverlap=int(2 * fs), axis=1)
    Pm = P.mean(axis=0)
    res["psd"] = dict(freqs=f.tolist(), psd=Pm.tolist())
    m = (f >= 7) & (f <= 13)
    if Pm[m].any():
        res["alpha_cf"] = float(f[m][int(Pm[m].argmax())])
    m1 = (f >= 1) & (f <= 45)
    res["psd_1_45_total"] = float(Pm[m1].sum())

    # --- Hilbert envelope once for the whole file (per channel) ---
    from scipy.signal import hilbert
    amp = np.abs(hilbert(X, axis=1))           # (62, 2000, n_ep)
    bin_env = amp > amp.mean(axis=1, keepdims=True)
    bin_raw = X > X.mean(axis=1, keepdims=True)

    # LZs: per-channel per-epoch envelope LZ
    vals = []
    for i in range(X.shape[0]):
        for j in range(n_ep):
            vals.append(lz_norm(bin_env[i, :, j].astype(np.uint8), rng))
    res["lzs_env"] = dict(median=float(np.median(vals)),
                          q25=float(np.percentile(vals, 25)),
                          q75=float(np.percentile(vals, 75)), n=len(vals))

    # LZc (envelope instrument): concatenated channels per epoch
    vals = []
    for j in range(n_ep):
        cat = np.concatenate([bin_env[i, :, j] for i in range(X.shape[0])]).astype(np.uint8)
        vals.append(lz_norm(cat, rng))
    res["lzc_env"] = dict(median=float(np.median(vals)),
                          q25=float(np.percentile(vals, 25)),
                          q75=float(np.percentile(vals, 75)), n=len(vals))

    # LZc (raw-waveform Schartner variant)
    vals = []
    for j in range(n_ep):
        cat = np.concatenate([bin_raw[i, :, j] for i in range(X.shape[0])]).astype(np.uint8)
        vals.append(lz_norm(cat, rng))
    res["lzc_wave"] = dict(median=float(np.median(vals)),
                           q25=float(np.percentile(vals, 25)),
                           q75=float(np.percentile(vals, 75)), n=len(vals))
    res["runtime_s"] = round(time.time() - t0, 1)
    return res


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for s in SUBJECTS[lo:hi]:
        for cond, eyes, p in spontaneous_files(s):
            outp = os.path.join(OUT, f"spont_{s}_{cond}_{eyes}.json")
            if os.path.exists(outp):
                print("skip existing", outp)
                continue
            r = analyse_file(p, cond, eyes, s)
            with open(outp, "w") as f:
                json.dump(r, f, indent=1)
            print(f"{s} {cond} {eyes}: LZc_env={r['lzc_env']['median']:.4f} "
                  f"LZs_env={r['lzs_env']['median']:.4f} alpha={r.get('alpha_cf')} "
                  f"({r['runtime_s']}s)")


if __name__ == "__main__":
    main()
