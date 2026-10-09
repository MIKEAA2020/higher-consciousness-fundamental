#!/usr/bin/env python3
"""Round 21 — evoked-LZ contrast (Farnes et al. 2020 completion).

Awake (recording 31) vs ketamine (recording 32) TMS-evoked responses,
10 subjects, within-subject contrast on the Phase-2-established LZ
instrument (Farnes/Reynante lzw.m + lzwNormalised.m port), now applied
with the CORRECT column-major channel/time mapping (repair R32).

Usage: python3 rd2_evoked_contrast.py <subj_start> <subj_end>
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from phase2_ds4541_epochs import lzw_count as lzw_count_ref
from rd2_lib import SUBJECTS, FS_EV, PULSE_SAMPLE, evoked_paths, load_evoked

OUT = "/home/z/my-project/glm agent 2/research/phase2/farnes"
os.makedirs(OUT, exist_ok=True)

POST0 = PULSE_SAMPLE          # first post-pulse sample idx (pulse = idx 125)
CH_STEP = 3                   # every 3rd channel for per-channel LZs
TRIAL_STEP_ENV = 2            # every 2nd trial for envelope LZs
N_SHUF = 5


def fast_lzw_count(b):
    """Vectorized-string equivalent of the ported lzw_count (verified below)."""
    s = (48 + np.asarray(b, dtype=np.uint8)).tobytes().decode()
    d = {"0", "1"}
    sub = s[0]
    n = len(s)
    e = 1
    while e < n:
        sub += s[e]
        if sub not in d:
            d.add(sub)
            sub = s[e]
        e += 1
    return len(d)


def _verify_fast():
    rng = np.random.default_rng(0)
    for L in (40, 125, 251, 500, 2000):
        for k in range(50):
            b = (rng.random(L) > 0.5).astype(np.uint8)
            assert fast_lzw_count(b) == lzw_count_ref(b), f"mismatch L={L} k={k}"
    print("fast_lzw_count verified identical to ported lzw_count (250 random cases)")


def lz_norm(b, rng, n_shuf=N_SHUF):
    c = fast_lzw_count(b)
    Ls = [fast_lzw_count(rng.permutation(b)) for _ in range(n_shuf)]
    return c / max(float(np.mean(Ls)), 1.0)


def analyse_file(path, cond, subject):
    t0 = time.time()
    d = load_evoked(path)
    arr = d["arr"]                       # (60, 251, ntr) correct order
    ntr = arr.shape[2]
    # trial hygiene: reject |amp| > 150 uV (recorded; expected 0)
    mabs = np.abs(arr).max(axis=(0, 1))
    keep = mabs <= 150.0
    arr = arr[:, :, keep]
    ntr_ok = arr.shape[2]
    seed = int(subject) * 2 + (0 if cond == "awake" else 1) + 21
    rng = np.random.default_rng(seed)

    res = dict(file=os.path.basename(path), condition=cond, subject=subject,
               dims=list(d["dims"]), n_declared=d["n_declared"],
               n_recovered=d["n_recovered"], n_trials=ntr, n_trials_ok=ntr_ok,
               n_rejected=int((~keep).sum()))

    # --- ERP morphology (correct mapping) ---
    erp = arr.mean(axis=2)               # (60, 251)
    gfp = (erp ** 2).mean(axis=0)
    t_ms = np.arange(arr.shape[1]) / FS_EV * 1000.0
    pre = slice(0, POST0)
    post = slice(POST0, arr.shape[1])
    gfp_peak_i = int(gfp[post].argmax()) + POST0
    res["gfp_peak_uv2"] = float(gfp[gfp_peak_i])
    res["gfp_peak_latency_ms_post"] = float(t_ms[gfp_peak_i] -
                                            (PULSE_SAMPLE - 1) / FS_EV * 1000.0)
    res["pre_rms_uv"] = float(np.sqrt((erp.mean(axis=0)[pre] ** 2).mean()))
    res["post_rms_uv"] = float(np.sqrt((erp.mean(axis=0)[post] ** 2).mean()))

    def windows():
        yield "pre", slice(0, POST0)             # 400 ms background before pulse
        yield "post", slice(POST0, arr.shape[1])
        yield "full", slice(0, arr.shape[1])

    from scipy.signal import hilbert

    for wname, w in windows():
        # (a) per-channel waveform LZs -- every 3rd channel, all trials
        vals = []
        chs = list(range(0, arr.shape[0], CH_STEP))
        for ti in range(arr.shape[2]):
            for c in chs:
                seg = arr[c, w, ti]
                b = (seg > seg.mean()).astype(np.uint8)
                vals.append(lz_norm(b, rng))
        res[f"lzs_wave_{wname}"] = dict(median=float(np.median(vals)),
                                        q25=float(np.percentile(vals, 25)),
                                        q75=float(np.percentile(vals, 75)),
                                        n=len(vals))
        # (b) per-channel Hilbert-envelope LZs -- every 2nd trial
        vals = []
        for ti in range(0, arr.shape[2], TRIAL_STEP_ENV):
            for c in chs:
                seg = arr[c, w, ti]
                amp = np.abs(hilbert(seg))
                b = (amp > amp.mean()).astype(np.uint8)
                vals.append(lz_norm(b, rng))
        res[f"lzs_env_{wname}"] = dict(median=float(np.median(vals)),
                                       q25=float(np.percentile(vals, 25)),
                                       q75=float(np.percentile(vals, 75)),
                                       n=len(vals))
        # (c) LZc -- all channels concatenated per trial (Schartner/Farnes)
        vals = []
        for ti in range(arr.shape[2]):
            seg = arr[:, w, ti]                       # (ch, nsamp)
            binm = seg > seg.mean(axis=1, keepdims=True)
            cat = np.concatenate([binm[c] for c in range(seg.shape[0])]).astype(np.uint8)
            vals.append(lz_norm(cat, rng))
        res[f"lzc_wave_{wname}"] = dict(median=float(np.median(vals)),
                                        q25=float(np.percentile(vals, 25)),
                                        q75=float(np.percentile(vals, 75)),
                                        n=len(vals))
        # (d) LZc on Hilbert envelope concatenation (the supplied-instrument variant)
        vals = []
        for ti in range(0, arr.shape[2], 2):
            seg = arr[:, w, ti]
            amp = np.abs(hilbert(seg, axis=1))
            binm = amp > amp.mean(axis=1, keepdims=True)
            cat = np.concatenate([binm[c] for c in range(seg.shape[0])]).astype(np.uint8)
            vals.append(lz_norm(cat, rng))
        res[f"lzc_env_{wname}"] = dict(median=float(np.median(vals)),
                                       q25=float(np.percentile(vals, 25)),
                                       q75=float(np.percentile(vals, 75)),
                                       n=len(vals))
    res["runtime_s"] = round(time.time() - t0, 1)
    return res


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    _verify_fast()
    for s in SUBJECTS[lo:hi]:
        for cond in ("awake", "ketamine"):
            outp = os.path.join(OUT, f"evoked_{s}_{cond}.json")
            if os.path.exists(outp):
                print("skip existing", outp)
                continue
            r = analyse_file(evoked_paths(s, cond), cond, s)
            with open(outp, "w") as f:
                json.dump(r, f, indent=1)
            print(f"{s} {cond}: LZc_wave_post={r['lzc_wave_post']['median']:.4f} "
                  f"LZc_env_post={r['lzc_env_post']['median']:.4f} "
                  f"LZs_env_post={r['lzs_env_post']['median']:.4f} "
                  f"GFPpeak={r['gfp_peak_uv2']:.1f}uv2 @{r['gfp_peak_latency_ms_post']:.0f}ms "
                  f"({r['runtime_s']}s)")


if __name__ == "__main__":
    main()
