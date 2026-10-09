#!/usr/bin/env python3
"""Phase 1.5 — FC legs: empirical BOLD structure vs the SC spectral domains.

Data: the same 7 HCP subjects' TC_rsfMRI_REST1_LR (94 x 1200 BOLD, AAL2).

Legs:
  1. Label-order validation — homotopic pairs (i, i+1) must be among the
     strongest FC edges; validates the AAL2 LRLR ordering assumption.
  2. FC structure: PC1 (leading eigenvector of FC = gradient-1 proxy) and
     psi_FC (Fiedler of the FC Laplacian). Sanity: PC1 must align with the
     sensory->transmodal axis (the canonical Margulies result) — this
     validates the entire mapping.
  3. THE P2 structure-function test at domain granularity:
     Spearman(psi_SC modes, PC1 / psi_FC) per subject, against label
     permutation nulls. Does the SC domain hierarchy predict the FC domain
     hierarchy?
  4. Classic edge-level SC-FC correlation (context).
"""
import json
import os
import sys

import numpy as np
from scipy.io import loadmat

sys.path.insert(0, "/home/z/my-project/scripts")
from phase15_labels import build
import phase15_lib as L

OUT = "/home/z/my-project/glm agent 2/research/phase15"
TC = os.path.join(OUT, "tc")
N_PERM = 10000


def load_tc(subj):
    d = loadmat(os.path.join(TC, f"TC_{subj}.mat"))["tc"].astype(np.float64)
    # z-score each region (removes mean/variance differences)
    d = (d - d.mean(axis=1, keepdims=True)) / (
        d.std(axis=1, keepdims=True) + 1e-12)
    return d


def main():
    M = build()
    res = {}
    partial = os.path.join(OUT, "fc_results.json")
    if os.path.exists(partial):
        try:
            res = json.load(open(partial))
        except Exception:
            res = {}
    for subj in L.SUBJECTS:
        if subj in res:
            print(f"[{subj}] cached, skip", flush=True)
            continue
        X = load_tc(subj)
        FC = np.corrcoef(X)                       # (94, 94)
        W = L.load_sc(subj)

        # ---- 1. homotopic validation ----
        iu = np.triu_indices(94, 1)
        r = FC[iu]
        homotopic = np.array([FC[i, i + 1] for i in range(0, 94, 2)])
        rank = int((r >= np.median(homotopic)).sum()) / len(r)
        # ---- 4. edge-level SC-FC ----
        sc_fc = L.spearman(W[iu], FC[iu])

        # ---- 2. FC structure ----
        ev_fc, V_fc = np.linalg.eigh(FC)
        o = np.argsort(ev_fc)[::-1]
        ev_fc, V_fc = ev_fc[o], V_fc[:, o]
        pc1 = V_fc[:, 0]
        if L.spearman(pc1, M["axis"]) < 0:
            pc1 = -pc1
        Wfc = np.clip(FC, 0, None)                # positive similarity
        ev_l, psi_fc = L.fiedler(Wfc)             # FC Fiedler

        # ---- 3. SC modes vs FC structure ----
        evall, Vm = L.spectrum(W, kmax=6)
        modes = {"2": Vm[:, 0], "3": Vm[:, 1], "4": Vm[:, 2],
                 "5": Vm[:, 3], "6": Vm[:, 4]}
        cort = M["iscort"]
        entry = {
            "homotopic_median_r": float(np.median(homotopic)),
            "homotopic_vs_all_percentile": float(rank),
            "sc_fc_edge_spearman": float(sc_fc),
            "pc1_axis_rho": L.spearman(pc1[cort], M["axis"][cort]),
            "psi_fc_axis_rho": L.spearman(psi_fc[cort], M["axis"][cort]),
            "psi_fc_hemi_align": abs(L.spearman(psi_fc, M["hemi"].astype(float))),
            "pc1_hemi_align": abs(L.spearman(pc1, M["hemi"].astype(float))),
        }
        for k, v in modes.items():
            entry[f"mode{k}_pc1_rho"] = L.spearman(v, pc1)
            entry[f"mode{k}_psifc_rho"] = L.spearman(v, psi_fc)
        # nulls: label permutation for the mode-PC1 / mode-psiFC correlations
        rng = np.random.default_rng(11)
        for k, v in list(modes.items()):
            nulls_pc1, nulls_psifc = [], []
            for _ in range(N_PERM):
                pv = rng.permutation(pc1)
                nulls_pc1.append(abs(L.spearman(v, pv)))
                nulls_psifc.append(abs(L.spearman(v, rng.permutation(psi_fc))))
            entry[f"mode{k}_pc1_rho_p"] = L.emp_p(
                abs(entry[f"mode{k}_pc1_rho"]), nulls_pc1)
            entry[f"mode{k}_psifc_rho_p"] = L.emp_p(
                abs(entry[f"mode{k}_psifc_rho"]), nulls_psifc)
        # psi values for the report figure
        entry["pc1"] = pc1.tolist()
        entry["psi_fc"] = psi_fc.tolist()
        res[subj] = entry
        with open(partial, "w") as f:      # incremental save
            json.dump(res, f, indent=1)
        print(f"[{subj}] homotop r={entry['homotopic_median_r']:.3f} "
              f"(pct {rank:.2f}) | PC1-axis rho={entry['pc1_axis_rho']:.3f} | "
              f"SC-FC edge rho={sc_fc:.3f} | "
              f"M2~PC1={entry['mode2_pc1_rho']:.3f}(p={entry['mode2_pc1_rho_p']:.3f}) "
              f"M3~PC1={entry['mode3_pc1_rho']:.3f}(p={entry['mode3_pc1_rho_p']:.4f}) "
              f"M5~PC1={entry['mode5_pc1_rho']:.3f}(p={entry['mode5_pc1_rho_p']:.4f}) "
              f"| psiFC-hemi={entry['psi_fc_hemi_align']:.3f} "
              f"psiFC-axis={entry['psi_fc_axis_rho']:.3f}", flush=True)

    with open(os.path.join(OUT, "fc_results.json"), "w") as f:
        json.dump(res, f, indent=1)
    print("saved fc_results.json")

    # group summary
    grp = {}
    for k in ["homotopic_median_r", "pc1_axis_rho", "psi_fc_axis_rho",
              "psi_fc_hemi_align", "pc1_hemi_align", "sc_fc_edge_spearman"] + \
            [f"mode{k}_pc1_rho" for k in range(2, 7)] + \
            [f"mode{k}_pc1_rho_p" for k in range(2, 7)] + \
            [f"mode{k}_psifc_rho" for k in range(2, 7)]:
        vals = [res[s][k] for s in L.SUBJECTS]
        grp[k] = {"mean": float(np.mean(vals)), "sd": float(np.std(vals))}
    with open(os.path.join(OUT, "fc_group.json"), "w") as f:
        json.dump(grp, f, indent=1)
    print(json.dumps({k: round(v["mean"], 3) for k, v in grp.items()},
                     indent=1))


if __name__ == "__main__":
    main()
