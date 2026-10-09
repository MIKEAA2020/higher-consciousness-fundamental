#!/usr/bin/env python3
"""Phase 2 figures (5 panels) + Myrov-grid figures (2 panels)."""
import json
import glob
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
for f in ["/usr/share/fonts/truetype/chinese/NotoSansSC-Regular.ttf",
          "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
    try:
        fm.fontManager.addfont(f)
    except Exception:
        pass
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Noto Sans SC"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/z/my-project/glm agent 2/research/phase2"
FIG = f"{OUT}/figs"
import os
os.makedirs(FIG, exist_ok=True)


def load_jsons(pat):
    out = {}
    for p in sorted(glob.glob(pat)):
        with open(p) as fh:
            out.update(json.load(fh))
    return out


# ---------------- Fig 1: EEG observables per level ----------------
def fig_eeg_levels():
    d56 = load_jsons(f"{OUT}/ds005620/obs_part*.json")
    d45 = load_jsons(f"{OUT}/ds004541/obs_part*.json")
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), constrained_layout=True)
    # DFA
    aw = [v["awake_EC"]["dfa_median"] for v in d56.values() if "dfa_median" in v.get("awake_EC", {})]
    sd = [v["sed_rest_r1"]["dfa_median"] for v in d56.values() if "dfa_median" in v.get("sed_rest_r1", {})]
    ax = axes[0]
    ax.boxplot([aw, sd], tick_labels=["awake EC", "propofol sed"], widths=0.55)
    for i, (a, s) in enumerate(zip(aw, sd)):
        ax.plot([1, 2], [a, s], ".", color="gray", alpha=0.5, ms=4)
    ax.set_ylabel("alpha-envelope DFA (median)")
    ax.set_title("A  DFA: awake vs light sedation (ds005620, n=8)")
    # LZs
    awl = [v["awake_EC"]["lzs_median"] for v in d56.values() if "lzs_median" in v.get("awake_EC", {})]
    sdl = [v["sed_rest_r1"]["lzs_median"] for v in d56.values() if "lzs_median" in v.get("sed_rest_r1", {})]
    ax = axes[1]
    ax.boxplot([awl, sdl], tick_labels=["awake EC", "propofol sed"], widths=0.55)
    for a, s in zip(awl, sdl):
        ax.plot([1, 2], [a, s], ".", color="gray", alpha=0.5, ms=4)
    ax.set_ylabel("LZs (Farnes LZW instrument)")
    ax.set_title("B  LZ complexity: awake vs sedation")
    # alpha peak
    awa = [v["awake_EC"]["alpha_cf"] for v in d56.values() if v.get("awake_EC", {}).get("alpha_cf")]
    sda = [v["sed_rest_r1"]["alpha_cf"] for v in d56.values() if v.get("sed_rest_r1", {}).get("alpha_cf")]
    ax = axes[2]
    ax.boxplot([awa, sda], tick_labels=["awake EC", "propofol sed"], widths=0.55)
    ax.set_ylabel("FOOOF alpha-peak CF (Hz)")
    ax.set_title("C  alpha peak: biphasic acceleration")
    fig.savefig(f"{FIG}/phase2_eeg_levels.png", dpi=150)
    plt.close(fig)

    # ds004541 levels
    levs = ["pre", "maintenance", "emergence", "recovery"]
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), constrained_layout=True)
    dfa_l = [[e["dfa_median"] for e in [v["epochs"].get(l) for v in d45.values()]
              if e and "dfa_median" in e] for l in levs]
    lzs_l = [[e["lzs_median"] for e in [v["epochs"].get(l) for v in d45.values()]
              if e and "lzs_median" in e] for l in levs]
    axes[0].boxplot([x for x in dfa_l if x], tick_labels=[l for l, x in zip(levs, dfa_l) if x])
    axes[0].set_ylabel("alpha-envelope DFA")
    axes[0].set_title("A  ds004541 surgical GA: DFA per level")
    axes[1].boxplot([x for x in lzs_l if x], tick_labels=[l for l, x in zip(levs, lzs_l) if x])
    axes[1].set_ylabel("LZs")
    axes[1].set_title("B  ds004541: LZ per level")
    fig.savefig(f"{FIG}/phase2_ds4541_levels.png", dpi=150)
    plt.close(fig)


# ---------------- Fig 2: beta-hat ordering ----------------
def fig_beta():
    R = json.load(open(f"{OUT}/phase2_fits.json"))
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), constrained_layout=True)
    ax = axes[0]
    xs, ys, ks = [], [], []
    for row in R["levels"]:
        if row["corpus"] == "ds005620" and row.get("awake_EC") and row.get("sed_rest_r1"):
            xs.append(row["awake_EC"]["beta_hat"])
            ys.append(row["sed_rest_r1"]["beta_hat"])
            ks.append(row["subject"])
    ax.scatter(xs, ys, c="tab:blue", zorder=3)
    lim = [0.01, 1.6]
    ax.plot(lim, lim, "k--", lw=0.8, alpha=0.6)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(lim); ax.set_ylim(lim)
    ax.set_xlabel("beta-hat awake")
    ax.set_ylabel("beta-hat sedated")
    ax.set_title("A  beta-hat ordering, ds005620 (6/8 above diagonal;\n"
                 "2 exceptions = artifact-flagged subjects)")
    for x, y, k in zip(xs, ys, ks):
        if k in ("1033", "1060"):
            ax.annotate(k, (x, y), fontsize=7, color="firebrick")
    # ds004541
    ax = axes[1]
    levs = ["pre", "maintenance", "emergence", "recovery"]
    data = {l: [] for l in levs}
    for row in R["levels"]:
        if row["corpus"] == "ds004541":
            for l in levs:
                if row.get(l):
                    data[l].append(row[l]["beta_hat"])
    labs = [l for l in levs if data[l]]
    vals = [data[l] for l in levs if data[l]]
    ax.boxplot(vals, tick_labels=labs)
    ax.set_yscale("log")
    ax.set_ylabel("beta-hat (sigma*/K*)")
    ax.set_title("B  beta-hat per GA level, ds004541\n(maintenance > pre in 3/4)")
    fig.savefig(f"{FIG}/phase2_beta_ordering.png", dpi=150)
    plt.close(fig)


# ---------------- Fig 3: K-sigma surface + LZ tracking ----------------
def fig_surface():
    S = np.load(f"{OUT}/ksigma/ksigma_surface.npz", allow_pickle=True)
    R = json.load(open(f"{OUT}/phase2_fits.json"))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4), constrained_layout=True)
    # DFA surface
    KS = sorted(set(S["K"].tolist()))
    SS = sorted(set(S["sigma"].tolist()))
    Z = np.full((len(SS), len(KS)), np.nan)
    for k, s, d in zip(S["K"], S["sigma"], S["dfa_median"]):
        Z[SS.index(s), KS.index(k)] = d
    ax = axes[0]
    pc = ax.pcolormesh(KS, SS, Z, cmap="viridis", shading="nearest")
    fig.colorbar(pc, ax=ax, label="model DFA median")
    ax.axvspan(15, 35, color="white", alpha=0.0)
    for lv in ("awake_EC", "sed_rest_r1"):
        for row in R["levels"]:
            if row["corpus"] == "ds005620" and row.get(lv):
                ax.plot(row[lv]["K_star"], row[lv]["sigma_star"], "o" if lv == "awake_EC" else "s",
                        color="white" if lv == "awake_EC" else "firebrick",
                        mec="k", ms=6, alpha=0.9)
    ax.plot([], [], "o", color="white", mec="k", label="awake fits")
    ax.plot([], [], "s", color="firebrick", mec="k", label="sedated fits")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlabel("K (rad/s)"); ax.set_ylabel("sigma")
    ax.set_title("A  Model (K, sigma) surface + level fits (L*=40)")
    # LZ tracking within-subject
    ax = axes[1]
    cats = ["fit stays\nin band", "fit exits\nband"]
    fell = [2, 4]; tot = [4, 4]
    ax.bar(cats, [f / t for f, t in zip(fell, tot)], color=["tab:gray", "tab:blue"])
    for i, (f, t) in enumerate(zip(fell, tot)):
        ax.text(i, f / t + 0.03, f"{f}/{t}", ha="center", fontsize=10)
    ax.set_ylim(0, 1.25)
    ax.set_ylabel("fraction of subjects with LZ fall (awake->sed)")
    ax.set_title("B  LZ fall vs band exit (ds005620, within-subject)")
    fig.savefig(f"{FIG}/phase2_ksigma_fits.png", dpi=150)
    plt.close(fig)


# ---------------- Fig 4: BOLD + Liley ----------------
def fig_bold_liley():
    d31 = load_jsons(f"{OUT}/ds003171/obs_part*.json")
    levs = ["restawake", "restlight", "restdeep", "restrecovery"]
    lz = {l: [] for l in levs}
    for v in d31.values():
        for l in levs:
            r = v.get(l)
            if r and "lzc" in r:
                lz[l].append(r["lzc"])
    L = json.load(open(f"{OUT}/liley/liley_sweep.json"))
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
    ax = axes[0]
    labs = [l.replace("rest", "") for l in levs]
    vals = [lz[l] for l in levs]
    bp = ax.boxplot(vals, tick_labels=labs)
    ax.set_ylabel("BOLD LZc (parcel-group, LZW)")
    ax.set_title(f"A  ds003171 BOLD LZc per level (6 subjects)\n"
                 f"light < awake in 5/6; deep heterogeneous")
    ax = axes[1]
    ax.plot(L["lambda"], [-e for e in L["he_eq"]], "o-", color="tab:blue")
    ax.set_xlabel("lambda (IPSP lengthening = propofol)")
    ax.set_ylabel("he (mV)")
    ax.set_title("B  Steyn-Ross/Liang macrocolumn equilibrium:\n"
                 "lambda hyperpolarizes he monotonically (no alpha resonance\n"
                 "reproducible from the printed parameters)")
    ax.invert_yaxis()
    fig.savefig(f"{FIG}/phase2_bold_liley.png", dpi=150)
    plt.close(fig)


# ---------------- Fig 5-6: Myrov-convention grid ----------------
def fig_myrov():
    G = np.load(f"{OUT}/grid/myrov_grid.npz")
    K, L = G["K"], G["L"]
    KS = sorted(set(K.tolist()))
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.4), constrained_layout=True)
    for ax, key, title, cmap in [
            (axes[0], "dfa_median", "A  DFA median (Myrov convention)", "viridis"),
            (axes[1], "order_strength_rho", "B  order~strength rho", "coolwarm"),
            (axes[2], "plv_edge_rho", "C  PLV~edge-weight rho", "coolwarm")]:
        LS = sorted(set(L.tolist()))
        Z = np.full((len(LS), len(KS)), np.nan)
        V = G[key]
        for k, l, v in zip(K, L, V):
            Z[LS.index(l), KS.index(k)] = v
        vmax = np.nanmax(np.abs(Z)) if "rho" in key else None
        pc = ax.pcolormesh(KS, LS, Z, cmap=cmap, shading="nearest",
                           vmin=-vmax if vmax else None, vmax=vmax if vmax else None)
        fig.colorbar(pc, ax=ax)
        ax.set_xlabel("K (convention units)")
        ax.set_ylabel("L")
        ax.set_title(title)
    # MEG DFA targets on the L=8 slice
    ax = axes[0]
    ax.plot(KS, [np.nan] * len(KS))  # keep limits
    fig.savefig(f"{FIG}/myrov_grid_surfaces.png", dpi=150)
    plt.close(fig)

    # L=8 slice with targets + nulls bar
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
    m8 = (L == 8.0)
    k8 = K[m8]
    ax = axes[0]
    for key, lab in [("dfa_median", "DFA median"), ("frac065", "frac DFA>0.65")]:
        v = G[key][m8]
        o = np.argsort(k8)
        ax.plot(k8[o], v[o], "o-", ms=3, label=lab)
    ax.axhline(0.632, color="r", ls="--", lw=0.8, label="MEG run1 (0.632)")
    ax.axhline(0.686, color="darkred", ls=":", lw=0.8, label="MEG run2 (0.686)")
    ax.set_xlabel("K (convention units)")
    ax.set_title("A  Myrov-convention L=8 slice vs MEG targets")
    ax.legend(fontsize=8)
    NU = json.load(open(f"{OUT}/grid/myrov_nulls.json"))
    ax = axes[1]
    labs = ["real", "shuffled", "random"]
    ordv = [NU["cases"][l]["order_strength_rho"] for l in labs]
    plvv = [NU["cases"][l]["plv_edge_rho"] for l in labs]
    x = np.arange(3)
    ax.bar(x - 0.18, ordv, 0.36, label="order~strength")
    ax.bar(x + 0.18, plvv, 0.36, label="PLV~W")
    ax.set_xticks(x, labs)
    ax.legend(fontsize=8)
    ax.set_title(f"B  Nulls at op point (K={NU['K']:.1f}): shuffled NOT destroyed\n"
                 "(coupling is generic, not topology-specific)")
    fig.savefig(f"{FIG}/myrov_slice_nulls.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    fig_eeg_levels()
    fig_beta()
    fig_surface()
    fig_bold_liley()
    fig_myrov()
    print("figures written:", sorted(os.listdir(FIG)))
