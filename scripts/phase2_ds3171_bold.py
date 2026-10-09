#!/usr/bin/env python3
"""Phase 2 — ds003171 BOLD complexity leg (4 sedation levels, eyes... rest runs).

Per level (restawake / restlight / restdeep / restrecovery): download the
BOLD nii.gz, take the top-K-variance voxels, binarize each voxel's BOLD at
its median, compute (a) concatenated LZW complexity (Schartner-style,
shuffle-normalized -- the same instrument family as the EEG LZc), (b)
median per-voxel temporal LZs.

CLI: phase2_ds3171_bold.py PART   (2 subjects per part; 4 levels each)
"""
import json
import os
import subprocess
import numpy as np
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
from phase2_ds4541_epochs import lzw_count

OUT = "/home/z/my-project/glm agent 2/research/phase2/ds003171"
os.makedirs(OUT, exist_ok=True)
BASE = "https://s3.amazonaws.com/openneuro.org/ds003171"
SUBJECTS = ["02CB", "04HD", "04SG", "08BC", "08VR", "10JR"]
LEVELS = ["restawake", "restlight", "restdeep", "restrecovery"]
NVOX = 200


def fetch(sub, level, tmp="/tmp/bold.nii.gz"):
    p = f"sub-{sub}/func/sub-{sub}_task-{level}_run-01_bold.nii.gz"
    r = subprocess.run(["curl", "-sS", "-L", "-m", "300", "-o", tmp,
                        "-w", "%{http_code} %{size_download}",
                        f"{BASE}/{p}"], capture_output=True, text=True, timeout=330)
    return r.stdout


def analyze(sub, level):
    """Parcel-group estimator: gray-ish voxels (moderate variance) randomly
    partitioned into G groups; group-mean BOLD series linearly detrended,
    median-binarized; LZs per group + concatenated LZc (the same LZW
    instrument family as the EEG leg)."""
    import nibabel as nib
    img = nib.load("/tmp/bold.nii.gz")
    dat = np.asanyarray(img.dataobj, dtype=np.float32)     # (x, y, z, t)
    if dat.ndim != 4:
        return {"error": f"ndim={dat.ndim}"}
    tr = float(img.header.get_zooms()[3]) if len(img.header.get_zooms()) > 3 else 2.0
    X = dat.reshape(-1, dat.shape[-1])                    # (voxels, t)
    mean = X.mean(axis=1)
    v = X.var(axis=1)
    fin = np.isfinite(mean) & np.isfinite(v) & (v > 0)
    good = fin & (mean > np.percentile(mean[fin], 30))
    vg = v[good]
    lo, hi = np.percentile(vg, [20, 80])
    stable = good & (v >= lo) & (v <= hi)
    Xg = X[stable]
    if Xg.shape[0] < 5000:
        return {"error": "too few voxels"}
    rng = np.random.default_rng(3)
    G = 60
    idx = rng.permutation(Xg.shape[0])[: (Xg.shape[0] // G) * G].reshape(G, -1)
    P = np.stack([Xg[idx[g]].mean(axis=0) for g in range(G)])   # (G, t)
    # linear detrend
    tvec = np.arange(P.shape[1])
    A = np.stack([np.ones_like(tvec), tvec - tvec.mean()], axis=1)
    coef, *_ = np.linalg.lstsq(A, P.T, rcond=None)
    Pd = (P.T - A @ coef).T
    med = np.median(Pd, axis=1, keepdims=True)
    B = (Pd > med).astype(np.uint8)                       # (G, t)

    def lzn(b, n_sh=5):
        c = lzw_count(b)
        Ls = [lzw_count(rng.permutation(b)) for _ in range(n_sh)]
        return c / max(np.mean(Ls), 1.0)

    cat = np.concatenate([B[i] for i in range(B.shape[0])]).astype(np.uint8)
    lzc = lzn(cat)
    lzs = [lzn(B[i], 3) for i in range(B.shape[0])]
    gmean = Xg.mean(axis=0)
    return {"lzc": float(lzc), "lzs_median": float(np.median(lzs)),
            "n_voxels_total": int(Xg.shape[0]), "n_timepoints": int(dat.shape[-1]),
            "tr": tr, "n_groups": G,
            "gmean_std": float(gmean.std())}


def main(part):
    subs = SUBJECTS[2 * part:2 * part + 2]
    results = {}
    for sub in subs:
        results[sub] = {}
        for lev in LEVELS:
            try:
                st = fetch(sub, lev)
                r = analyze(sub, lev)
                r["download"] = st
                results[sub][lev] = r
                print(f"sub-{sub} {lev}: lzc={r.get('lzc')} lzs={r.get('lzs_median')} "
                      f"T={r.get('n_timepoints')} TR={r.get('tr')}", flush=True)
            except Exception as e:
                results[sub][lev] = {"error": str(e)[:150]}
                print(f"sub-{sub} {lev} ERROR {e}", flush=True)
        with open(f"{OUT}/obs_part{part}.json", "w") as f:
            json.dump(results, f, indent=1)
    print("saved", f"{OUT}/obs_part{part}.json")


if __name__ == "__main__":
    main(int(sys.argv[1]))
