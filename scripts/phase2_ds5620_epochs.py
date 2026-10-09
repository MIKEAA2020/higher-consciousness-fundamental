#!/usr/bin/env python3
"""Phase 2 — ds005620 propofol light-sedation EEG (clean lab corpus).

Per subject: awake EC (first 150 s) vs task-sed_acq-rest run-1 (first 150 s),
range-requested from S3 BrainVision .eeg (float32 multiplexed, 65 ch,
5000 Hz). QC -> avg ref -> decimate to 250 Hz -> same observables as
ds004541 (PSD/FOOOF, alpha-band DFA, broadband DFA, Farnes LZs/LZc).

CLI: phase2_ds5620_epochs.py PART   (2 subjects per part)
"""
import json
import os
import subprocess
import numpy as np

sys_path = "/home/z/my-project/scripts"
import sys
sys.path.insert(0, sys_path)
import phase2_ds4541_epochs as D
from phase2_ds4541_epochs import (epoch_observables, FS_T)

OUT = "/home/z/my-project/glm agent 2/research/phase2/ds005620"
os.makedirs(OUT, exist_ok=True)
BASE = "https://s3.amazonaws.com/openneuro.org/ds005620"
SUBJECTS = ["1010", "1016", "1022", "1024", "1033", "1045", "1057", "1060"]
NCH = 65
FS = 5000.0
T_FETCH = 150.0


def fetch_bv(sub, task, acq, run, t_s=T_FETCH, tmp="/tmp/bv_chunk.bin"):
    if task == "awake":
        fn = f"sub-{sub}_task-{task}_acq-{acq}_eeg.eeg"      # no run suffix
    else:
        fn = f"sub-{sub}_task-{task}_acq-{acq}_run-{run}_eeg.eeg"
    path = f"sub-{sub}/eeg/{fn}"
    nbytes = int(NCH * 4 * FS * t_s)
    url = f"{BASE}/{path}"
    r = subprocess.run(["curl", "-sS", "-L", "-m", "400", "-r", f"0-{nbytes-1}",
                        "-o", tmp, "-w", "%{http_code} %{size_download}", url],
                       capture_output=True, text=True, timeout=450)
    raw = np.fromfile(tmp, dtype="<f4")
    n_samp = len(raw) // NCH
    X = raw[:n_samp * NCH].reshape(n_samp, NCH).T.astype(np.float64)  # (ch, t)
    return X


def channels(sub):
    """Channel names from the awake vhdr ordering (Iz, O2, Oz, ... + VEOG/HEOG/EMG)."""
    chf = f"{OUT}/sub-{sub}_channels.txt"
    if not os.path.exists(chf):
        p = f"sub-{sub}/eeg/sub-{sub}_task-awake_acq-EC_channels.tsv"
        subprocess.run(["curl", "-sS", "-L", "-m", "60", "-o", chf,
                        f"{BASE}/{p}"], capture_output=True, timeout=90)
    names, types = [], []
    with open(chf) as f:
        next(f)
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                names.append(parts[0].lstrip('\ufeff'))
                types.append(parts[1] if len(parts) > 1 else "EEG")
    return names, types


def preprocess(X, types):
    from scipy.signal import resample_poly, butter, sosfiltfilt
    cand = [i for i, t in enumerate(types) if t == "EEG" and i < X.shape[0]]
    Xc = X[cand]
    sos = butter(4, [1.0, 45.0], btype="band", fs=FS, output="sos")
    # block filtering (memory)
    out = []
    for a in range(0, Xc.shape[0], 8):
        b = min(a + 8, Xc.shape[0])
        xf = sosfiltfilt(sos, Xc[a:b], axis=1)
        out.append(resample_poly(xf, 1, 20, axis=1))
    Xd = np.concatenate(out)
    ls = np.log10(np.maximum(Xd.std(axis=1), 1e-9))
    order = np.argsort(ls)
    lss = ls[order]
    gaps = np.diff(lss)
    gi = int(np.argmax(gaps)) if len(gaps) else 0
    if len(gaps) and gaps[gi] > 0.4:
        low = ls <= (lss[gi] + lss[gi + 1]) / 2
    else:
        low = np.ones(len(ls), bool)
    kurt = ((Xd - Xd.mean(axis=1, keepdims=True)) ** 4).mean(axis=1) / (Xd.var(axis=1) ** 2 + 1e-12)
    ok = low & (kurt < 30) & (Xd.std(axis=1) > 0)
    if ok.sum() < 12:
        ok = ls <= np.median(ls)
    keep = [i for i, o in zip(cand, ok) if o]
    Xd = Xd[ok]
    Xd = Xd - Xd.mean(axis=0, keepdims=True)
    return keep, Xd


def main(part):
    subs = SUBJECTS[2 * part:2 * part + 2]
    results = {}
    for sub in subs:
        results[sub] = {}
        names, types = channels(sub)
        for cond, spec in [("awake_EC", ("awake", "EC", "1")),
                           ("sed_rest_r1", ("sed", "rest", "1"))]:
            try:
                X = fetch_bv(sub, *spec)
                keep, Xd = preprocess(X, types)
                if Xd.shape[0] < 16 or Xd.shape[1] < int(120 * FS_T):
                    results[sub][cond] = {"skipped": f"ch={Xd.shape[0]} n={Xd.shape[1]}"}
                    continue
                obs = epoch_observables(Xd, FS_T)
                obs["nch"] = int(Xd.shape[0])
                results[sub][cond] = obs
                print(f"sub-{sub} {cond}: dfa={obs['dfa_median']:.3f} "
                      f"dfa_bb={obs['dfa_bb_median']:.3f} alpha={obs.get('alpha_cf')} "
                      f"lzs={obs['lzs_median']:.3f} lzc={obs['lzc_median']:.3f} "
                      f"b/a={obs['pow_beta']/max(obs['pow_alpha'],1e-12):.2f}", flush=True)
            except Exception as e:
                results[sub][cond] = {"error": str(e)[:150]}
                print(f"sub-{sub} {cond} ERROR {e}", flush=True)
        with open(f"{OUT}/obs_part{part}.json", "w") as f:
            json.dump(results, f, indent=1)
    print("saved", f"{OUT}/obs_part{part}.json")


if __name__ == "__main__":
    main(int(sys.argv[1]))
