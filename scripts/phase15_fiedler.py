#!/usr/bin/env python3
"""Phase 1.5 — chunked runner: Fiedler-boundary battery on HCP connectomes.

Executes the P2 test the user specified (Round 22): Fiedler vector psi^(2)
per connectome, predicted domains/boundary, alignment battery vs functional
geometry (network boundaries, sensory->transmodal axis, hemispheres,
subcortical, DID key regions, spectral-embedding ARI), with degree-preserving
rewiring nulls (200/subject), full-topology shuffle nulls, label-permutation
nulls (10k), and sensitivity arms (unnormalized Laplacian, log1p weights,
ambiguous-region exclusion).

Usage:  phase15_fiedler.py CHUNK        (0..6, one subject per chunk)
        phase15_fiedler.py sens         (sensitivity arms, fast)
        phase15_fiedler.py aggregate    (group stats + figures)
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from phase15_labels import AAL2, build
import phase15_lib as L

OUT = "/home/z/my-project/glm agent 2/research/phase15"
FIGS = os.path.join(OUT, "figs")
os.makedirs(FIGS, exist_ok=True)

N_SHUFFLE = 200
N_PERM = 10000


def run_subject(si):
    M = build()
    subj = L.SUBJECTS[si]
    t0 = time.time()
    W = L.load_sc(subj)
    real = L.battery(W, M, lap="sym")
    ari = L.ari_stats(W, M, lap="sym")
    nulls = L.battery_nulls(W, M, lap="sym", n_shuffle=N_SHUFFLE,
                            n_perm=N_PERM, seed=si * 7 + 1)
    stats = summarize(real, nulls)
    # mode-profile null-referenced stats (shuffle + block + perm)
    mode_stats = {}
    for k in range(2, 8):
        ms = {}
        for s in ["hemi_align", "axis_align", "net_contrast", "did_sep"]:
            rv = real["mode_profile"][str(k)][s]
            ms[s] = {
                "real": rv,
                "shuffle_mean": float(np.nanmean(
                    nulls["mode_shuffle"][str(k)][s])),
                "shuffle_p": L.emp_p(rv, nulls["mode_shuffle"][str(k)][s]),
                "block_mean": float(np.nanmean(
                    nulls["mode_block"][str(k)][s])),
                "block_p": L.emp_p(rv, nulls["mode_block"][str(k)][s]),
            }
            pm = {"net_contrast": "net_contrast", "axis_align": "axis_align",
                  "did_sep": "did_sep"}.get(s)
            if pm:
                pmv = nulls["perm_mode"][str(k)][pm]
                ms[s]["perm_mean"] = float(np.nanmean(pmv))
                ms[s]["perm_p"] = L.emp_p(rv, pmv)
        mode_stats[str(k)] = ms
    # strength confound controls
    strength = W.sum(axis=1)
    partials = {"fiedler_axis_partial_strength": L.partial_spearman(
        np.array(real["psi"]), M["axis"], strength)}
    for k in range(2, 8):
        evall, Vm = L.spectrum(W, kmax=7)
        v = Vm[:, k - 2]
        partials[f"mode{k}_axis_partial_strength"] = L.partial_spearman(
            v, M["axis"], strength)
    partials["strength_axis_rho"] = L.spearman(strength, M["axis"])
    out = {"subject": subj, "battery": real, "ari": ari, "stats": stats,
           "mode_stats": mode_stats, "partials": partials}
    path = os.path.join(OUT, f"subj_{subj}.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    f2 = stats["hemi_align"]; nc = stats["net_contrast"]; ds = stats["did_sep"]
    print(f"[{subj}] Fiedler hemi|rho|={real['hemi_align']:.3f} "
          f"(shuffle p={f2['shuffle_p']:.4f}) | netC={real['net_contrast']:.3f} "
          f"(perm p={nc['perm_p']:.4f}) | didSep={real['did_sep']:.3f} "
          f"(perm p={ds['perm_p']:.4f}) | ARI7={ari['ari_7']:.3f} | "
          f"{time.time()-t0:.0f}s", flush=True)
    print("  modes(netC/permP/blockP): " + " ".join(
        f"M{k}({real['mode_profile'][str(k)]['net_contrast']:.2f}/"
        f"{mode_stats[str(k)]['net_contrast'].get('perm_p', float('nan')):.3f}/"
        f"{mode_stats[str(k)]['net_contrast']['block_p']:.3f})"
        for k in range(2, 8)), flush=True)
    print("  modes(did/permP/blockP): " + " ".join(
        f"M{k}({real['mode_profile'][str(k)]['did_sep']:.2f}/"
        f"{mode_stats[str(k)]['did_sep'].get('perm_p', float('nan')):.3f}/"
        f"{mode_stats[str(k)]['did_sep']['block_p']:.3f})"
        for k in range(2, 8)), flush=True)


def summarize(real, nulls):
    keys = ["hemi_align", "subcort_align", "axis_align", "net_contrast",
            "did_sep"] + [f"bipart_{n}" for n in
                          list(build()["networks"])]
    s = {}
    for k in keys:
        null_shu = np.asarray(nulls["shuffle"][k], dtype=float)
        null_blk = np.asarray(nulls["block"][k], dtype=float)
        perm_key = {"net_contrast": "net_contrast",
                    "axis_align": "axis_align",
                    "did_sep": "did_sep"}.get(k)
        entry = {
            "real": real[k],
            "shuffle_mean": float(np.nanmean(null_shu)),
            "shuffle_p": L.emp_p(real[k], null_shu),
            "block_mean": float(np.nanmean(null_blk)),
            "block_p": L.emp_p(real[k], null_blk),
        }
        if perm_key:
            pmv = nulls["perm_mode"]["2"][perm_key]
            entry["perm_mean"] = float(np.nanmean(pmv))
            entry["perm_p"] = L.emp_p(real[k], pmv)
        s[k] = entry
    return s


def run_sens():
    """Sensitivity arms: unnormalized Laplacian, log1p weights,
    ambiguous-exclusion. Values only (nulls only on primary arm)."""
    M = build()
    keep = M["iscort"] & ~M["ambiguous"] & np.isfinite(M["axis"])
    M2 = dict(M)
    M2["net"] = np.where(keep, M["net"], "EXCL")
    M2["iscort"] = keep.copy()
    M2["axis"] = np.where(keep, M["axis"], np.nan)
    out = {}
    for tag, fn in {
        "unnorm": lambda W, s: L.battery_light(W, M, lap="unnorm"),
        "log1p": lambda W, s: L.battery_light(
            L.load_sc(s, transform="log1p"), M, lap="sym"),
        "noambiguous": lambda W, s: L.battery_light(W, M2, lap="sym"),
    }.items():
        arm = {}
        for subj in L.SUBJECTS:
            W = L.load_sc(subj)
            arm[subj] = fn(W, subj)
        out[tag] = arm
        print(f"[sens {tag}] done", flush=True)
    with open(os.path.join(OUT, "sensitivity.json"), "w") as f:
        json.dump(out, f, indent=1)


def aggregate():
    """Group-level stats + figures from the per-subject JSONs."""
    from scipy.stats import wilcoxon
    M = build()
    subs = [L.SUBJECTS[i] for i in range(7)
            if os.path.exists(os.path.join(OUT, f"subj_{L.SUBJECTS[i]}.json"))]
    data = {s: json.load(open(os.path.join(OUT, f"subj_{s}.json")))
            for s in subs}

    def grp(k, src="stats", field="real"):
        return np.array([data[s][src][k] if src == "ari" else
                         data[s][src][k][field] for s in subs])

    keys = ["hemi_align", "subcort_align", "axis_align", "net_contrast",
            "did_sep"] + [f"bipart_{n}" for n in M["networks"]]
    g = {}
    for k in keys:
        real = np.array([data[s]["stats"][k]["real"] for s in subs])
        shu = np.array([data[s]["stats"][k]["shuffle_mean"] for s in subs])
        blk = np.array([data[s]["stats"][k]["block_mean"] for s in subs])
        try:
            ws = float(wilcoxon(real, shu, alternative="greater").pvalue)
        except Exception:
            ws = float("nan")
        try:
            wb = float(wilcoxon(real, blk, alternative="greater").pvalue)
        except Exception:
            wb = float("nan")
        g[k] = {"real_mean": float(real.mean()),
                "real_sd": float(real.std()),
                "shuffle_mean": float(shu.mean()),
                "block_mean": float(blk.mean()),
                "wilcoxon_real_gt_shuffle_p": ws,
                "wilcoxon_real_gt_block_p": wb,
                "per_subject": {s: {"real": data[s]["stats"][k]["real"],
                                    "shuffle_p": data[s]["stats"][k]["shuffle_p"],
                                    "block_p": data[s]["stats"][k]["block_p"]}
                                for s in subs}}
    # ARI group stats (real values; random-topology ARI has expectation ~0)
    gari = {}
    for k in ["ari_2", "ari_4", "ari_7"]:
        real = np.array([data[s]["ari"][k] for s in subs])
        try:
            wp = float(wilcoxon(real, np.zeros_like(real),
                                alternative="greater").pvalue)
        except Exception:
            wp = float("nan")
        gari[k] = {"real_mean": float(real.mean()),
                   "real_sd": float(real.std()),
                   "wilcoxon_gt0_p": wp,
                   "per_subject": {s: data[s]["ari"][k] for s in subs}}
    gmode = {}
    for k in range(2, 8):
        gmode[str(k)] = {}
        for s_ in ["hemi_align", "axis_align", "net_contrast", "did_sep"]:
            real = np.array([data[s]["mode_stats"][str(k)][s_]["real"]
                             for s in subs])
            shu = np.array([data[s]["mode_stats"][str(k)][s_]["shuffle_mean"]
                            for s in subs])
            blk = np.array([data[s]["mode_stats"][str(k)][s_]["block_mean"]
                            for s in subs])
            try:
                ws = float(wilcoxon(real, shu, alternative="greater").pvalue)
            except Exception:
                ws = float("nan")
            try:
                wb = float(wilcoxon(real, blk, alternative="greater").pvalue)
            except Exception:
                wb = float("nan")
            gmode[str(k)][s_] = {"real_mean": float(real.mean()),
                                 "shuffle_mean": float(shu.mean()),
                                 "block_mean": float(blk.mean()),
                                 "wilcoxon_gt_shuffle_p": ws,
                                 "wilcoxon_gt_block_p": wb}

    out = {"subjects": subs, "group": g, "group_ari": gari,
           "group_mode": gmode,
           "op_point_phase1": {"mean_order": 0.4977, "mean_plv": 0.0098,
                               "beta_hat": 0.12, "K_star": 25.0,
                               "sigma_star": 3.0}}
    with open(os.path.join(OUT, "phase15_results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("aggregated", len(subs), "subjects")
    make_figures(data, subs, M, g, gmode)


def make_figures(data, subs, M, g, gmode):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    for fp in ("/usr/share/fonts/truetype/chinese/NotoSansSC-Regular.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            fm.fontManager.addfont(fp)
        except Exception:
            pass
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Noto Sans SC"]
    plt.rcParams["axes.unicode_minus"] = False

    NETCOL = {"Visual": "#4d79c4", "SomMot": "#5aa85a", "DorsalAttn": "#3f9f8f",
              "VentralAttn": "#e0a33c", "Limbic": "#d95f6a", "Cont": "#9d7bbd",
              "Default": "#8a6d4f", "Subcortical": "#7f7f7f",
              "EXCL": "#cccccc"}

    # Fig 1: Fiedler vector across the axis, 2 subjects, colored by network
    order = np.argsort(np.where(M["iscort"], M["axis"], np.nan))
    fig, axes = plt.subplots(2, 1, figsize=(9.5, 7.4), sharex=True,
                             constrained_layout=True)
    for ax, subj in zip(axes, subs[:2]):
        psi = np.array(data[subj]["battery"]["psi"])[order]
        net = M["net"][order]
        ax.bar(range(94), psi, color=[NETCOL[n] for n in net], width=0.85)
        ax.axhline(0, color="k", lw=0.8)
        ax.set_ylabel(r"$\psi^{(2)}$")
        ax.set_title(f"Subject {subj}: Fiedler vector, regions ordered along "
                     f"the sensory$\\to$transmodal axis "
                     f"(the leading cut is hemispheric, not transmodal)",
                     fontsize=9)
    handles = [plt.Rectangle((0, 0), 1, 1, color=NETCOL[n]) for n in NETCOL
               if n != "EXCL"]
    axes[1].legend(handles, [n for n in NETCOL if n != "EXCL"], fontsize=7,
                   ncol=8, loc="lower left", framealpha=0.9)
    axes[1].set_xticks(range(94))
    axes[1].set_xticklabels([AAL2[i].replace("_", " ") for i in order],
                            rotation=90, fontsize=3.2)
    fig.savefig(os.path.join(FIGS, "phase15_psi_axis.png"), dpi=200)
    plt.close(fig)

    # Fig 2: group battery — real vs shuffled-topology null
    from scipy.stats import wilcoxon
    keys = ["hemi_align", "net_contrast", "axis_align", "did_sep",
            "subcort_align"]
    labels = ["hemisphere\n|Spearman|", "network\nboundary contrast",
              "transmodal axis\n|Spearman|", "DID separation\n(sigma units)",
              "subcortical\n|Spearman|"]
    real = np.array([[data[s]["stats"][k]["real"] for s in subs]
                     for k in keys])
    shu = np.array([[data[s]["stats"][k]["shuffle_mean"] for s in subs]
                    for k in keys])
    fig, ax = plt.subplots(figsize=(9.5, 4.8), constrained_layout=True)
    x = np.arange(len(keys))
    for i in range(len(subs)):
        ax.scatter(x - 0.24 + (i - 3) * 0.03, real[:, i], s=13,
                   color="#c44e52", zorder=3)
        ax.scatter(x + 0.24 + (i - 3) * 0.03, shu[:, i], s=13,
                   color="#555555", zorder=3, marker="x")
    bp1 = ax.boxplot(real.T, positions=x - 0.24, widths=0.2,
                     patch_artist=True)
    bp2 = ax.boxplot(shu.T, positions=x + 0.24, widths=0.2,
                     patch_artist=True)
    for b in bp1["boxes"]:
        b.set_facecolor("#e6a2a5")
    for b in bp2["boxes"]:
        b.set_facecolor("#d9d9d9")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_title("Phase 1.5 (P2 test): Fiedler alignment of real connectomes "
                 "(red) vs random-topology nulls (grey), 7 subjects")
    ymax = np.nanmax(np.vstack([real, shu]))
    for xi, k in zip(x, keys):
        try:
            p = wilcoxon(real[keys.index(k)], shu[keys.index(k)],
                         alternative="greater").pvalue
        except Exception:
            p = float("nan")
        ax.text(xi, ymax * 1.02, f"p={p:.3f}" if np.isfinite(p) else "n/a",
                ha="center", fontsize=8)
    ax.set_ylim(None, ymax * 1.10)
    fig.savefig(os.path.join(FIGS, "phase15_battery.png"), dpi=200)
    plt.close(fig)

    # Fig 3: mode profile (the domain hierarchy)
    fig, ax = plt.subplots(figsize=(9.5, 4.6), constrained_layout=True)
    mk = list(range(2, 8))
    for stat, lbl, col in [("net_contrast", "network boundary contrast",
                            "#4d79c4"),
                           ("did_sep", "DID separation (sigma)", "#d95f6a"),
                           ("axis_align", "transmodal axis |rho|", "#5aa85a"),
                           ("hemi_align", "hemisphere |rho|", "#9d7bbd")]:
        r = [gmode[str(k)][stat]["real_mean"] for k in mk]
        n1 = [gmode[str(k)][stat]["shuffle_mean"] for k in mk]
        n2 = [gmode[str(k)][stat]["block_mean"] for k in mk]
        ax.plot(mk, r, "o-", color=col, label=lbl, lw=1.6, ms=5)
        ax.plot(mk, n1, "x--", color=col, alpha=0.45, lw=1.2, ms=5)
        ax.plot(mk, n2, "^:", color=col, alpha=0.45, lw=1.2, ms=5)
    ax.set_xlabel("spectral mode (2 = Fiedler / coarsest cut)")
    ax.set_ylabel("statistic (group mean, 7 subjects)")
    ax.set_title("Domain hierarchy: alignment of successive Laplacian modes\n"
                 "(solid = real, dashed = random-topology null, "
                 "dotted = hemispheric-block null)")
    ax.legend(fontsize=8)
    ax.set_xticks(mk)
    fig.savefig(os.path.join(FIGS, "phase15_modes.png"), dpi=200)
    plt.close(fig)
    print("figures saved")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "0"
    if what == "sens":
        run_sens()
    elif what == "aggregate":
        aggregate()
    else:
        run_subject(int(what))
