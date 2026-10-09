#!/usr/bin/env python3
"""Phase 1 (Level-2 protocol) — fit the operating point, critical regime,
distance-to-ridge, beta estimate, and produce figures + JSON summary.

Inputs:  research/phase1/meg_obs.npz/.json, sweep_half{0,1}.npz,
         slice_<subj>.npz (optional), sigmasweep.json (optional),
         nulls.json (optional)
Outputs: research/phase1/figs/*.png, phase1_results.json, console summary
"""
import json
import glob
import numpy as np
from scipy.stats import pearsonr

OUT = "/home/z/my-project/glm agent 2/research/phase1"
FIG = f"{OUT}/figs"
SUBJECTS = ["101309", "102311", "102816", "131217", "211619", "213522", "377451"]

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.dpi": 130, "font.size": 8.5})


def load_sweep():
    fps = sorted(glob.glob(f"{OUT}/sweep_part*.npz"))
    if not fps:
        raise SystemExit("no sweep_part*.npz found")
    parts = [np.load(fp) for fp in fps]
    keys = parts[0].files
    merged = {}
    for k in keys:
        arrs = [p[k] for p in parts]
        if arrs[0].ndim == 0 or k == "psd_freqs":
            merged[k] = arrs[0]            # constant across parts
        else:
            merged[k] = np.concatenate(arrs)
    return merged


def _load_slices(s):
    fps = sorted(glob.glob(f"{OUT}/slice_{s}_part*.npz"))
    if not fps:
        raise FileNotFoundError(s)
    parts = [np.load(fp) for fp in fps]
    keys = parts[0].files
    merged = {}
    for k in keys:
        arrs = [p[k] for p in parts]
        if arrs[0].ndim == 0 or k == "psd_freqs":
            merged[k] = arrs[0]
        else:
            merged[k] = np.concatenate(arrs)
    return merged


def psd_fit_surfaces(sw, meg):
    """PSD match criteria per combo, sensor-space instantiation:
    r_raw (linear Pearson, Myrov's literal criterion), r_shape (log-log
    detrended: 1/f-removed peak-structure match), r_periodic (vs FOOOF
    periodic PSD), and model alpha-peak frequency."""
    mf = sw["psd_freqs"]
    msel = (mf >= 3) & (mf <= 30)
    mf_sel = mf[msel]
    meg_f = meg["run1_freqs"]
    rsel = (meg_f >= 3) & (meg_f <= 30)
    meg_raw = meg["run1_psd_mean"][rsel]
    x = np.log10(meg_f[rsel])
    ye = np.log10(meg_raw)
    ye_d = ye - np.polyval(np.polyfit(x, ye, 1), x)
    meg_per = meg["run1_fooof_periodic"]
    pf = meg["run1_fooof_freqs"]
    psel = (pf >= 3) & (pf <= 30)
    meg_per = meg_per[psel]
    C = len(sw["K"])
    r_raw = np.zeros(C)
    r_shape = np.zeros(C)
    r_per = np.zeros(C)
    peak = np.zeros(C)
    for ci in range(C):
        mp = sw["psd"][ci][msel]
        mi = np.interp(meg_f[rsel], mf_sel, mp)
        r_raw[ci] = pearsonr(mi, meg_raw).statistic
        ym = np.log10(mi + 1e-12)
        ym_d = ym - np.polyval(np.polyfit(x, ym, 1), x)
        r_shape[ci] = pearsonr(ym_d, ye_d).statistic
        mpi = np.interp(pf[psel], mf_sel, mp)
        r_per[ci] = pearsonr(mpi, meg_per).statistic
        band = (mf_sel >= 6) & (mf_sel <= 14)
        peak[ci] = mf_sel[band][np.argmax(mp[band])]
    return r_raw, r_shape, r_per, peak


def kl_map(ax, K, L, V, title, op=None, contour=None, cmap="viridis",
           cbar=True, fmt="{:.2f}"):
    im = ax.tricontourf(K, L, V, levels=14, cmap=cmap)
    if contour is not None:
        ax.tricontour(K, L, contour, levels=[0.10], colors="w", linewidths=1.6)
    if op is not None:
        ax.plot(op[0], op[1], "r*", ms=13, mec="k", mew=0.6, zorder=5)
    ax.set_xlabel("local coupling K (rad/s)")
    ax.set_ylabel("global coupling L (rad/s)")
    ax.set_title(title)
    if cbar:
        plt.colorbar(im, ax=ax, fraction=0.046)
    return im


def main():
    import os
    os.makedirs(FIG, exist_ok=True)
    meg = np.load(f"{OUT}/meg_obs.npz")
    megj = json.load(open(f"{OUT}/meg_obs.json"))
    sw = load_sweep()
    K, L = sw["K"], sw["L"]
    res = {"grid": "K,L in {0..40} rad/s, 9x9, sigma0=3.0 (sweep)",
           "meg": {k: megj["run1"][k] for k in
                   ["alpha_peak_hz", "dfa_median", "dfa_mean", "dfa_pct_gt_065",
                    "wpli_mean", "cc_mean", "cc_vs_dist_rho"]},
           "meg_run2": {k: megj["run2"][k] for k in
                        ["alpha_peak_hz", "dfa_median", "wpli_mean"]},
           "surrogate_dfa_p95": megj["wn_dfa_p95"]}

    # ---- fit surfaces + composite operating point ----
    r_raw, r_shape, r_per, mpeak = psd_fit_surfaces(sw, meg)
    meg_peak = megj["run1"]["alpha_peak_hz"]
    meg_med = megj["run1"]["dfa_median"]
    med_dfa = np.nanmedian(sw["dfa"], axis=1)
    d_dfa = np.abs(med_dfa - meg_med) / 0.1
    d_pk = np.abs(mpeak - meg_peak) / 1.0
    d_sh = 1.0 - r_shape
    score = d_dfa + d_pk + d_sh
    res["fit"] = {
        "criterion": "composite = |med DFA - MEG med|/0.1 + |peak-8.12Hz|/1Hz "
                     "+ (1 - r_shape); sensor-space instantiation",
        "r_raw_best": float(np.nanmax(r_raw)),
        "r_shape_best": float(np.nanmax(r_shape)),
        "r_periodic_best": float(np.nanmax(r_per)),
        "score_best": float(np.nanmin(score)),
    }
    ci_star = int(np.nanargmin(score))
    Ks, Ls = float(K[ci_star]), float(L[ci_star])
    res["operating_point"] = {
        "K_star": Ks, "L_star": Ls,
        "composite_score": float(score[ci_star]),
        "components": {"d_dfa": float(d_dfa[ci_star]),
                        "d_peak": float(d_pk[ci_star]),
                        "d_shape": float(d_sh[ci_star])},
        "r_raw": float(r_raw[ci_star]),
        "r_shape": float(r_shape[ci_star]),
        "r_periodic": float(r_per[ci_star]),
        "model_alpha_peak": float(mpeak[ci_star]),
        "meg_alpha_peak": meg_peak,
        "peak_distance_hz": float(abs(mpeak[ci_star] - meg_peak)),
        "mean_order": float(sw["mean_order"][ci_star].mean()),
        "mean_dfa": float(np.nanmean(sw["dfa"][ci_star])),
        "frac065": float(sw["frac065"][ci_star]),
        "frac_p95": float(sw["frac_p95"][ci_star]),
        "mean_plv": float(sw["mean_plv"][ci_star]),
        "mean_cc": float(sw["mean_cc"][ci_star]),
        "sf": {k: float(sw[k][ci_star]) for k in
               ["order_strength_rho", "dfa_strength_rho", "plv_edge_rho",
                "cc_edge_rho"]},
    }

    # ---- critical regime + distance to ridge ----
    f65 = sw["frac065"]
    d = {}
    # L-axis (inter-node coupling; the GL J-analog) at K=K*
    maskK = np.isclose(K, Ks)
    Lline, fline = L[maskK], f65[maskK]
    o = np.argsort(Lline)
    Lline, fline = Lline[o], fline[o]
    inL = [ll for ll, ff in zip(Lline, fline) if ff >= 0.10]
    if inL:
        d["L_band_at_Kstar"] = [float(min(inL)), float(max(inL))]
        d["L_star_inside_band"] = bool(min(inL) <= Ls <= max(inL))
        if Ls < min(inL):
            d["distance_L_norm"] = float((min(inL) - Ls) / min(inL))
            d["side_L"] = "subcritical"
        elif Ls > max(inL):
            d["distance_L_norm"] = float((max(inL) - Ls) / max(inL))
            d["side_L"] = "supercritical"
        else:
            d["distance_L_norm"] = 0.0
            d["side_L"] = "inside the extended critical regime (band spans L)"
    else:
        d["L_band_at_Kstar"] = None
        d["distance_L_norm"] = None
        d["side_L"] = "critical band not present at K* within the plane"
    # K-axis (the transition axis in this instantiation) at L=L*
    maskL = np.isclose(L, Ls)
    Kline, kline = K[maskL], f65[maskL]
    o = np.argsort(Kline)
    Kline, kline = Kline[o], kline[o]
    inside = [kk for kk, ff in zip(Kline, kline) if ff >= 0.10]
    if inside:
        Kc_lo, Kc_hi = min(inside), max(inside)
        d["K_band_at_Lstar"] = [float(Kc_lo), float(Kc_hi)]
        d["K_star_inside_band"] = bool(Kc_lo <= Ks <= Kc_hi)
        if Ks < Kc_lo:
            d["distance_K_norm"] = float((Kc_lo - Ks) / Kc_lo)
            d["side_K"] = "subcritical"
        elif Ks > Kc_hi:
            d["distance_K_norm"] = float((Kc_hi - Ks) / Kc_hi)
            d["side_K"] = "supercritical"
        else:
            d["distance_K_norm"] = 0.0
            d["side_K"] = "inside the extended critical regime"
            d["margin_to_subcritical_edge"] = float((Ks - Kc_lo) / Kc_lo)
            d["margin_to_supercritical_edge"] = float((Kc_hi - Ks) / Kc_hi)
    else:
        d["K_band_at_Lstar"] = None
        d["distance_K_norm"] = None
        d["side_K"] = "critical band not present at L* within the plane"
    d["note"] = ("In this parameterization the DFA-defined critical regime is "
                 "a K-band extended across L (as in Myrov et al. Fig. 2); the "
                 "K axis is the transition axis, the L axis the inter-node "
                 "(J-analog) coupling.")
    res["critical_regime"] = d

    # ---- sigma sweep / beta ----
    try:
        ssw = json.load(open(f"{OUT}/sigmasweep.json"))
        med_meg = megj["run1"]["dfa_median"]
        meds = np.array(ssw["dfa_median"])
        sgrid = ssw["sigma_grid"]
        # interpolate sigma* matching median DFA
        if meds.max() >= med_meg >= meds.min():
            sig_star = float(np.interp(med_meg, meds, sgrid))
        else:
            j = int(np.argmin(np.abs(meds - med_meg)))
            sig_star = float(sgrid[j])
        res["beta"] = {
            "sigma_star": sig_star, "K_star": Ks,
            "beta_hat": sig_star / Ks,
            "definition": "beta = sigma*/K* (noise amplitude / local coupling "
                          "at the MEG-matched operating point)",
            "dfa_median_curve": [float(x) for x in meds],
            "sigma_grid": [float(x) for x in sgrid],
            "meg_dfa_median": med_meg,
        }
    except FileNotFoundError:
        res["beta"] = None

    # ---- nulls ----
    try:
        res["nulls"] = json.load(open(f"{OUT}/nulls.json"))
    except FileNotFoundError:
        res["nulls"] = None

    # ---- per-subject slices (composite criterion, as primary) ----
    subj = {}
    x = np.log10(meg["run1_freqs"][(meg["run1_freqs"] >= 3) & (meg["run1_freqs"] <= 30)])
    ye = np.log10(meg["run1_psd_mean"][(meg["run1_freqs"] >= 3) & (meg["run1_freqs"] <= 30)])
    ye_d = ye - np.polyval(np.polyfit(x, ye, 1), x)
    for s in SUBJECTS[1:]:
        try:
            d = _load_slices(s)
        except FileNotFoundError:
            continue
        mf = d["psd_freqs"]
        msel = (mf >= 3) & (mf <= 30)
        mf_sel = mf[msel]
        meg_f = meg["run1_freqs"]
        rsel = (meg_f >= 3) & (meg_f <= 30)
        meg_raw = meg["run1_psd_mean"][rsel]
        C = len(d["K"])
        rr = np.zeros(C)
        score_s = np.zeros(C)
        pk_s = np.zeros(C)
        for ci in range(C):
            mi = np.interp(meg_f[rsel], mf_sel, d["psd"][ci][msel])
            rr[ci] = pearsonr(mi, meg_raw).statistic
            ym = np.log10(mi + 1e-12)
            ym_d = ym - np.polyval(np.polyfit(x, ym, 1), x)
            rsh = pearsonr(ym_d, ye_d).statistic
            band = (mf_sel >= 6) & (mf_sel <= 14)
            pk_s[ci] = mf_sel[band][np.argmax(d["psd"][ci][msel][band])]
            med = np.nanmedian(d["dfa"][ci])
            score_s[ci] = (abs(med - meg_med) / 0.1 + abs(pk_s[ci] - meg_peak) / 1.0
                           + (1.0 - rsh))
        ci_s = int(np.nanargmin(score_s))
        mK = np.isclose(d["L"], Ls)
        fK = d["frac065"][mK]
        KKs = d["K"][mK]
        o = np.argsort(KKs)
        KKs, fK = KKs[o], fK[o]
        inside = [kk for kk, ff in zip(KKs, fK) if ff >= 0.10]
        dK = None
        if inside:
            klo, khi = min(inside), max(inside)
            ks = float(d["K"][ci_s])
            if ks < klo:
                dK = (klo - ks) / klo
            elif ks > khi:
                dK = (khi - ks) / khi
            else:
                dK = 0.0
        subj[s] = {
            "K_op": float(d["K"][ci_s]), "L_op": float(d["L"][ci_s]),
            "composite_score": float(score_s[ci_s]),
            "r_raw": float(rr[ci_s]),
            "model_peak": float(pk_s[ci_s]),
            "Kband_at_Lstar": [float(min(inside)), float(max(inside))] if inside else None,
            "distance_K_norm": None if dK is None else float(dK),
            "frac065_at_op": float(d["frac065"][ci_s]),
        }
    res["subjects"] = subj

    # ================= FIGURES =================
    fig, ax = plt.subplots(2, 3, figsize=(11.5, 7.2), constrained_layout=True)
    kl_map(ax[0, 0], K, L, sw["mean_order"].mean(axis=1), "mean node order R",
           op=(Ks, Ls))
    kl_map(ax[0, 1], K, L, np.nanmean(sw["dfa"], axis=1), "mean DFA exponent",
           op=(Ks, Ls), contour=f65)
    kl_map(ax[0, 2], K, L, f65, "fraction of nodes DFA>0.65\n(white: 10% band edge)",
           op=(Ks, Ls), cmap="magma")
    kl_map(ax[1, 0], K, L, score, "composite misfit (lower = better)\nDFA+peak+shape",
           op=(Ks, Ls), cmap="viridis_r")
    kl_map(ax[1, 1], K, L, sw["order_strength_rho"], "structure-function:\norder ~ node strength",
           cmap="RdBu_r")
    kl_map(ax[1, 2], K, L, sw["dfa_strength_rho"], "structure-function:\nDFA ~ node strength",
           op=(Ks, Ls), cmap="RdBu_r")
    fig.suptitle("Phase 1 — hierarchical Kuramoto on HCP connectome 101309 "
                 "(K,L in rad/s; sigma=3; white contour = Myrov critical regime)")
    fig.savefig(f"{FIG}/phase1_kl_surfaces.png")
    plt.close(fig)

    # PSD-criteria maps
    fig, ax = plt.subplots(1, 3, figsize=(11.5, 3.6), constrained_layout=True)
    kl_map(ax[0], K, L, r_raw, "PSD Pearson r (raw)", op=(Ks, Ls), cmap="cividis")
    kl_map(ax[1], K, L, r_shape, "PSD shape r (1/f-removed)", op=(Ks, Ls), cmap="cividis")
    kl_map(ax[2], K, L, mpeak, "model alpha-peak (Hz)", op=(Ks, Ls), cmap="plasma")
    fig.suptitle(f"PSD fit criteria (MEG peak {meg_peak} Hz marked by construction)")
    fig.savefig(f"{FIG}/phase1_psd_criteria.png")
    plt.close(fig)

    # PSD overlay at operating point
    fig, ax = plt.subplots(figsize=(5.6, 4.0), constrained_layout=True)
    msel = (sw["psd_freqs"] >= 3) & (sw["psd_freqs"] <= 30)
    ax.loglog(sw["psd_freqs"][msel], sw["psd"][ci_star][msel], lw=1.6,
              label=f"model at (K*,L*)=({Ks:.0f},{Ls:.0f})")
    meg_f = meg["run1_freqs"]
    rsel = (meg_f >= 3) & (meg_f <= 30)
    ax.loglog(meg_f[rsel], meg["run1_psd_mean"][rsel], lw=1.6, label="MEG grand mean (run 1)")
    ax.axvline(meg_peak, color="gray", ls=":", lw=1)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("PSD")
    ax.set_title(f"PSD match at the operating point  (r={r_raw[ci_star]:.3f})")
    ax.legend()
    fig.savefig(f"{FIG}/phase1_psd_match.png")
    plt.close(fig)

    # DFA distributions
    fig, ax = plt.subplots(figsize=(5.6, 4.0), constrained_layout=True)
    ax.hist(meg["run1_dfa_ch"], bins=28, range=(0.2, 1.4), alpha=0.6,
            density=True, label=f"MEG sensors (med={megj['run1']['dfa_median']})")
    ax.hist(sw["dfa"][ci_star], bins=28, range=(0.2, 1.4), alpha=0.6,
            density=True, label=f"model nodes at op point, sigma=3 "
                                f"(med={np.nanmedian(sw['dfa'][ci_star]):.3f})")
    ax.axvline(0.65, color="k", ls="--", lw=1, label="Myrov threshold 0.65")
    ax.axvline(megj["wn_dfa_p95"], color="gray", ls=":", lw=1,
               label=f"white-noise p95={megj['wn_dfa_p95']}")
    ax.set_xlabel("DFA exponent")
    ax.set_ylabel("density")
    ax.set_title("DFA distributions: MEG sensors vs model nodes")
    ax.legend(fontsize=7)
    fig.savefig(f"{FIG}/phase1_dfa_dist.png")
    plt.close(fig)

    # sigma sweep / beta
    if res.get("beta"):
        fig, ax = plt.subplots(figsize=(5.2, 3.8), constrained_layout=True)
        ax.plot(res["beta"]["sigma_grid"], res["beta"]["dfa_median_curve"], "o-")
        ax.axhline(res["beta"]["meg_dfa_median"], color="r", ls="--",
                   label="MEG median DFA")
        ax.axvline(res["beta"]["sigma_star"], color="k", ls=":",
                   label=f"sigma*={res['beta']['sigma_star']:.2f}")
        ax.set_xlabel("noise amplitude sigma (rad/s^1/2)")
        ax.set_ylabel("model median DFA")
        ax.set_title(f"beta fit: sigma*/K* = {res['beta']['beta_hat']:.3f}")
        ax.legend(fontsize=7)
        fig.savefig(f"{FIG}/phase1_beta.png")
        plt.close(fig)

    # nulls bar chart
    if res.get("nulls"):
        nl = res["nulls"]
        fig, ax = plt.subplots(figsize=(5.6, 3.8), constrained_layout=True)
        keys = ["order_strength_rho", "dfa_strength_rho", "plv_edge_rho", "cc_edge_rho"]
        labs = ["order~strength", "DFA~strength", "PLV~edge W", "CC~edge W"]
        x = np.arange(len(keys))
        for i, (case, col) in enumerate([("real", "C0"), ("shuffled", "C1"),
                                         ("random", "C3")]):
            v = [nl[case].get(k, np.nan) for k in keys]
            ax.bar(x + (i - 1) * 0.25, v, width=0.24, label=case, color=col)
        ax.set_xticks(x)
        ax.set_xticklabels(labs)
        ax.set_ylabel("Spearman rho")
        ax.set_title("Structure-function coupling: real vs null connectomes")
        ax.legend()
        fig.savefig(f"{FIG}/phase1_nulls.png")
        plt.close(fig)

    # per-subject summary
    if subj:
        fig, ax = plt.subplots(figsize=(5.6, 4.0), constrained_layout=True)
        names = list(subj.keys())
        dd = [subj[n]["distance_K_norm"] if subj[n]["distance_K_norm"] is not None
              else np.nan for n in names]
        rr = [subj[n]["r_raw"] for n in names]
        ax.bar(names, dd, color="C0", alpha=0.8)
        ax.axhline(0, color="k", lw=1)
        ax.set_ylabel("signed distance to critical band (K axis)")
        ax.set_title("Per-connectome distance at the MEG-matched operating point\n"
                     "(negative = subcritical side)")
        ax.tick_params(axis="x", rotation=45)
        fig.savefig(f"{FIG}/phase1_subjects.png")
        plt.close(fig)

    with open(f"{OUT}/phase1_results.json", "w") as f:
        json.dump(res, f, indent=1, default=float)
    print(json.dumps({k: res[k] for k in ["operating_point", "critical_regime",
                                          "beta"]}, indent=1, default=float))
    print("figures in", FIG)


if __name__ == "__main__":
    main()
