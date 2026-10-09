#!/usr/bin/env python3
"""Phase 1.5 — dynamic leg: domain-structure strength in spontaneous EEG
under the psychedelic condition (Farnes 2020 Raw_data_2 corpus).

Model prediction tested (domain merging): if sub-anaesthetic ketamine
reduces effective coupling J, the leading functional domain structure
should WEAKEN — measured as the eigengap lambda3-lambda2 of the Laplacian
of the band-limited amplitude-envelope FC (sensor level, 60 EEG channels).

Instrument caveats (documented): sensor-level FC is inflated by volume
conduction; envelope-FC on the 8-30 Hz band mitigates but does not remove
it. The statistic is a within-subject CONTRAST (awake vs ketamine, same
instrument), which cancels the fixed volume-conduction bias to first order.
Also recorded: geometry stability — Spearman(psi_awake, psi_ketamine):
does the domain geometry persist across state while its strength changes?

Usage: phase15_eeg.py <subj_start> <subj_end>   (0..9)
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from rd2_lib import SUBJECTS, spontaneous_files, load_set_fdt

OUT = "/home/z/my-project/glm agent 2/research/phase15"
os.makedirs(OUT, exist_ok=True)

BAND = (8.0, 30.0)


def envelope_fc(data, fs):
    """data: (nch, T) -> envelope FC (Pearson of Hilbert envelopes)."""
    from scipy.signal import hilbert, butter, sosfiltfilt
    sos = butter(4, BAND, btype="bandpass", fs=fs, output="sos")
    Xf = sosfiltfilt(sos, data, axis=1)
    env = np.abs(hilbert(Xf, axis=1))
    # decimate envelope to ~25 Hz for speed
    dec = max(1, int(fs // 25))
    env = env[:, ::dec]
    return np.corrcoef(env)


def fc_domain_stats(FC):
    """Eigengap + leading-mode geometry of the FC Laplacian."""
    W = (FC + 1.0) / 2.0                       # similarity in [0, 1]
    n = len(W)
    d = W.sum(axis=1)
    dinv = 1.0 / np.sqrt(np.maximum(d, 1e-12))
    Lsym = np.eye(n) - dinv[:, None] * W * dinv[None, :]
    ev, V = np.linalg.eigh(Lsym)
    o = np.argsort(ev)
    ev, V = ev[o], V[:, o]
    # eigengap after mode 2 (bipartition strength)
    gap = float(ev[2] - ev[1])
    # participation: variance share of the leading nontrivial mode
    lam2 = float(ev[1])
    return {"eigengap": gap, "lambda2": lam2, "psi": V[:, 1].tolist()}


def analyse(subject):
    files = spontaneous_files(subject)
    out = []
    for cond, eyes, path in files:
        data, meta = load_set_fdt(path)          # (nbchan, pnts, trials)
        types = meta.get("types", ["EEG"] * data.shape[0])
        labels = meta.get("labels", [])
        keep = np.array([t.lower() in ("eeg", "eegdata", "data")
                         for t in types])
        if keep.sum() == 0:
            keep = np.ones(data.shape[0], dtype=bool)
        X = data[keep]                            # (nch, pnts, trials)
        fs = meta["srate"]
        # concatenate epochs into one continuous series per channel
        Xc = X.reshape(X.shape[0], -1)
        if Xc.shape[1] < 4 * fs:
            continue
        FC = envelope_fc(Xc, fs)
        st = fc_domain_stats(FC)
        st.update(file=os.path.basename(path), condition=cond, eyes=eyes,
                  subject=subject, nch=int(keep.sum()))
        out.append(st)
        print(f"  [{subject}] {cond}/{eyes}: eigengap={st['eigengap']:.4f} "
              f"lambda2={st['lambda2']:.4f} nch={st['nch']}", flush=True)
    return out


def main(a, b):
    from scipy.stats import wilcoxon
    results = {}
    path = os.path.join(OUT, "eeg_domain.json")
    if os.path.exists(path):
        try:
            results = json.load(open(path))
        except Exception:
            results = {}
    for si in range(a, b):
        subj = SUBJECTS[si]
        if subj in results:
            print(f"[{subj}] cached", flush=True)
            continue
        print(f"[{subj}] loading...", flush=True)
        results[subj] = analyse(subj)
        with open(path, "w") as f:
            json.dump(results, f, indent=1)
    # contrast (only when the file has all 10 subjects)
    if len(results) == 10:
        gaps = {}
        for subj, recs in results.items():
            for r in recs:
                gaps[(subj, r["condition"], r["eyes"])] = r["eigengap"]
        pairs = []
        stab = []
        for subj in results:
            recs = {r["condition"] + "_" + r["eyes"]: r
                    for r in results[subj]}
            for eyes in ("open", "closed"):
                ka, kk = f"awake_{eyes}", f"ketamine_{eyes}"
                if ka in recs and kk in recs:
                    pairs.append((recs[ka]["eigengap"],
                                  recs[kk]["eigengap"]))
                    from scipy.stats import spearmanr
                    stab.append(abs(spearmanr(
                        recs[ka]["psi"], recs[kk]["psi"]).statistic))
        if pairs:
            aw = np.array([p[0] for p in pairs])
            ke = np.array([p[1] for p in pairs])
            w = wilcoxon(aw, ke, alternative="greater")
            summary = {
                "n_pairs": len(pairs),
                "awake_mean": float(aw.mean()),
                "ketamine_mean": float(ke.mean()),
                "wilcoxon_awake_gt_ketamine_p": float(w.pvalue),
                "frac_ketamine_lower": float((ke < aw).mean()),
                "psi_stability_abs_rho_mean": float(np.mean(stab)),
                "psi_stability_sd": float(np.std(stab)),
            }
            with open(os.path.join(OUT, "eeg_domain_summary.json"), "w") as f:
                json.dump(summary, f, indent=1)
            print("SUMMARY:", json.dumps(summary, indent=1))


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
