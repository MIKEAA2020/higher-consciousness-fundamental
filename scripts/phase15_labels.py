#!/usr/bin/env python3
"""Phase 1.5 — AAL2 (94-region) functional mapping for the Fiedler-boundary test.

Region list = neurolib's canonical AAL2 ordering (atlases.py, indices 1-94,
LRLR interleaved), verified against the hcp-dataset DTI_CM matrices by the
homotopic-FC check in phase15_fc.py.

Assignments are ANATOMICAL APPROXIMATIONS of the Yeo-7 cortical networks and
the Margulies-style sensory->transmodal gradient, hand-mapped for the 94
AAL2 regions. They are coarse by construction; every statistic computed
against them is null-referenced (degree-preserving rewiring + label
permutation), and a sensitivity arm excludes the explicitly ambiguous
regions (AMBIGUOUS below) and re-runs every network-level statistic.

Sources for the mapping decisions (standing corpus): Yeo et al. 2011 network
anatomy; Margulies et al. 2016 sensory-transmodal gradient; the corpus's own
Preller 2018 / Avram 2024 / Bedford 2023 anchors for the thalamocortical and
sensory/association axes; Schlumpf thesis Exp. 2 for the DID key sets.
"""
import numpy as np

AAL2 = [
    "Precentral_L", "Precentral_R",
    "Frontal_Sup_2_L", "Frontal_Sup_2_R",
    "Frontal_Mid_2_L", "Frontal_Mid_2_R",
    "Frontal_Inf_Oper_L", "Frontal_Inf_Oper_R",
    "Frontal_Inf_Tri_L", "Frontal_Inf_Tri_R",
    "Frontal_Inf_Orb_2_L", "Frontal_Inf_Orb_2_R",
    "Rolandic_Oper_L", "Rolandic_Oper_R",
    "Supp_Motor_Area_L", "Supp_Motor_Area_R",
    "Olfactory_L", "Olfactory_R",
    "Frontal_Sup_Medial_L", "Frontal_Sup_Medial_R",
    "Frontal_Med_Orb_L", "Frontal_Med_Orb_R",
    "Rectus_L", "Rectus_R",
    "OFCmed_L", "OFCmed_R",
    "OFCant_L", "OFCant_R",
    "OFCpost_L", "OFCpost_R",
    "OFClat_L", "OFClat_R",
    "Insula_L", "Insula_R",
    "Cingulate_Ant_L", "Cingulate_Ant_R",
    "Cingulate_Mid_L", "Cingulate_Mid_R",
    "Cingulate_Post_L", "Cingulate_Post_R",
    "Hippocampus_L", "Hippocampus_R",
    "ParaHippocampal_L", "ParaHippocampal_R",
    "Amygdala_L", "Amygdala_R",
    "Calcarine_L", "Calcarine_R",
    "Cuneus_L", "Cuneus_R",
    "Lingual_L", "Lingual_R",
    "Occipital_Sup_L", "Occipital_Sup_R",
    "Occipital_Mid_L", "Occipital_Mid_R",
    "Occipital_Inf_L", "Occipital_Inf_R",
    "Fusiform_L", "Fusiform_R",
    "Postcentral_L", "Postcentral_R",
    "Parietal_Sup_L", "Parietal_Sup_R",
    "Parietal_Inf_L", "Parietal_Inf_R",
    "SupraMarginal_L", "SupraMarginal_R",
    "Angular_L", "Angular_R",
    "Precuneus_L", "Precuneus_R",
    "Paracentral_Lobule_L", "Paracentral_Lobule_R",
    "Caudate_L", "Caudate_R",
    "Putamen_L", "Putamen_R",
    "Pallidum_L", "Pallidum_R",
    "Thalamus_L", "Thalamus_R",
    "Heschl_L", "Heschl_R",
    "Temporal_Sup_L", "Temporal_Sup_R",
    "Temporal_Pole_Sup_L", "Temporal_Pole_Sup_R",
    "Temporal_Mid_L", "Temporal_Mid_R",
    "Temporal_Pole_Mid_L", "Temporal_Pole_Mid_R",
    "Temporal_Inf_L", "Temporal_Inf_R",
]
assert len(AAL2) == 94

# Yeo-7-style assignment (cortical) + Subcortical class.
NET = {
    "Visual": ["Calcarine", "Cuneus", "Lingual", "Occipital_Sup", "Occipital_Mid",
               "Occipital_Inf"],
    "SomMot": ["Precentral", "Postcentral", "Supp_Motor_Area", "Rolandic_Oper",
               "Paracentral_Lobule", "Heschl", "Temporal_Sup"],
    "DorsalAttn": ["Parietal_Sup", "Parietal_Inf"],
    "VentralAttn": ["Frontal_Inf_Oper", "SupraMarginal", "Temporal_Inf",
                    "Insula"],
    "Limbic": ["Olfactory", "Frontal_Med_Orb", "Rectus", "OFCmed", "OFCant",
               "OFCpost", "OFClat", "Frontal_Inf_Orb_2", "Hippocampus",
               "ParaHippocampal", "Amygdala", "Temporal_Pole_Sup",
               "Temporal_Pole_Mid"],
    "Cont": ["Frontal_Mid_2", "Frontal_Inf_Tri", "Cingulate_Mid"],
    "Default": ["Frontal_Sup_2", "Frontal_Sup_Medial", "Cingulate_Ant",
                "Cingulate_Post", "Angular", "Precuneus", "Temporal_Mid",
                "Fusiform"],
    "Subcortical": ["Caudate", "Putamen", "Pallidum", "Thalamus"],
}

# Sensory->transmodal axis score (Margulies-style coarse ordering).
AXIS_SCORE = {
    "Visual": 0.0,
    "SomMot": 0.15,       # includes primary auditory (Heschl, Temporal_Sup)
    "DorsalAttn": 1.0,
    "VentralAttn": 1.0,
    "Limbic": 1.5,
    "Cont": 2.0,
    "Default": 3.0,
    "Subcortical": np.nan,  # excluded from axis statistics
}

# Regions whose network assignment is explicitly uncertain (mid-gradient or
# genuinely mixed in the literature). Excluded in the sensitivity arm.
AMBIGUOUS = {
    "Fusiform", "Cingulate_Mid", "Insula", "Temporal_Sup",
    "Temporal_Pole_Sup", "Temporal_Pole_Mid", "Frontal_Inf_Orb_2",
}

# DID key sets (Schlumpf thesis, Experiment 2):
#   DIDep > DIDanp perfusion: primary somatosensory, primary motor, premotor /
#   pre-SMA, DMPFC  -> the "EP cluster"
#   DIDanp > DIDep perfusion: bilateral thalamus -> the "ANP marker"
DID_EP = ["Postcentral_L", "Postcentral_R", "Precentral_L", "Precentral_R",
          "Supp_Motor_Area_L", "Supp_Motor_Area_R",
          "Frontal_Sup_Medial_L", "Frontal_Sup_Medial_R"]
DID_ANP = ["Thalamus_L", "Thalamus_R"]


def build():
    """Return (names, net_labels, axis, hemi, iscort, idx dicts)."""
    net_of, axis_of = {}, {}
    for net, bases in NET.items():
        for b in bases:
            for suffix in ("_L", "_R"):
                net_of[b + suffix] = net
    missing = [n for n in AAL2 if n not in net_of]
    assert not missing, f"unmapped regions: {missing}"
    net_labels = np.array([net_of[n] for n in AAL2])
    axis = np.array([AXIS_SCORE[net_of[n]] for n in AAL2], dtype=float)
    hemi = np.array([0 if n.endswith("_L") else 1 for n in AAL2])
    iscort = np.array([net_of[n] != "Subcortical" for n in AAL2])
    ambiguous = np.array([n.split("_L")[0].split("_R")[0] in AMBIGUOUS or
                          n in AMBIGUOUS for n in AAL2])
    idx = {n: i for i, n in enumerate(AAL2)}
    return {
        "names": AAL2, "net": net_labels, "axis": axis, "hemi": hemi,
        "iscort": iscort, "ambiguous": ambiguous, "idx": idx,
        "did_ep": np.array([idx[n] for n in DID_EP]),
        "did_anp": np.array([idx[n] for n in DID_ANP]),
        "networks": list(NET.keys()),
    }


if __name__ == "__main__":
    m = build()
    from collections import Counter
    print(Counter(m["net"]).most_common())
    print("cortical:", m["iscort"].sum(), "| axis defined:",
          np.isfinite(m["axis"]).sum())
    print("EP set:", [AAL2[i] for i in m["did_ep"]])
    print("ANP set:", [AAL2[i] for i in m["did_anp"]])
