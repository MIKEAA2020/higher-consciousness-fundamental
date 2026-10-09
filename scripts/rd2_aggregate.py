#!/usr/bin/env python3
"""Round 21 aggregate — evoked + spontaneous contrast statistics, Round-20
recovery validation, figures, summary JSON (Farnes et al. 2020 completion)."""
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
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

from scipy.stats import wilcoxon, rankdata

from rd2_lib import SUBJECTS, FS_EV, PULSE_SAMPLE, evoked_paths, load_evoked

OUT = "/home/z/my-project/glm agent 2/research/phase2/farnes"
FIG = os.path.join(OUT, "figs")
os.makedirs(FIG, exist_ok=True)


def evoked(subj, cond):
    with open(os.path.join(OUT, f"evoked_{subj}_{cond}.json")) as f:
        return json.load(f)


def spont(subj, cond, eyes):
    with open(os.path.join(OUT, f"spont_{subj}_{cond}_{eyes}.json")) as f:
        return json.load(f)


def paired_stats(vals_a, vals_k, n_boot=10000, seed=11):
    a = np.asarray(vals_a, float)
    k = np.asarray(vals_k, float)
    d = k - a
    n = len(d)
    out = dict(n=n, awake_median=float(np.median(a)), ket_median=float(np.median(k)),
               delta_median=float(np.median(d)), delta_mean=float(d.mean()),
               delta_sd=float(d.std(ddof=1)), n_increase=int((d > 0).sum()),
               n_decrease=int((d < 0).sum()))
    try:
        st = wilcoxon(a, k, zero_method="wilcox", alternative="two-sided",
                      mode="exact")
        out["wilcoxon_p"] = float(st.pvalue)
    except Exception:
        st = wilcoxon(a, k, zero_method="wilcox", alternative="two-sided")
        out["wilcoxon_p"] = float(st.pvalue)
    # rank-biserial from positive ranks
    nz = d != 0
    r = rankdata(np.abs(d[nz]))
    Wp = float(r[d[nz] > 0].sum())
    T = float(r.sum())
    out["rank_biserial"] = float((Wp - (T - Wp)) / T) if T > 0 else 0.0
    rng = np.random.default_rng(seed)
    boots = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        boots.append(np.mean(d[idx]))
    out["delta_mean_ci95"] = [float(np.percentile(boots, 2.5)),
                              float(np.percentile(boots, 97.5))]
    return out


summary = {"corpus": "Farnes et al. 2020 PLOS ONE 15(11):e0242056, Raw_data_2 release",
           "n_subjects": 10, "conditions": {"31": "awake (placebo)", "32": "ketamine"}}

# ---------------- evoked ----------------
metrics_ev = ["lzc_env_pre", "lzc_wave_pre", "lzs_env_pre", "lzs_wave_pre",
              "lzc_env_post", "lzc_wave_post", "lzs_env_post", "lzs_wave_post",
              "lzc_env_full", "lzc_wave_full", "lzs_env_full", "lzs_wave_full"]
ev_stats = {}
for m in metrics_ev:
    a = [evoked(s, "awake")[m]["median"] for s in SUBJECTS]
    k = [evoked(s, "ketamine")[m]["median"] for s in SUBJECTS]
    ev_stats[m] = paired_stats(a, k)
    print(f"EVOKED {m}: awake={ev_stats[m]['awake_median']:.4f} "
          f"ket={ev_stats[m]['ket_median']:.4f} d={ev_stats[m]['delta_mean']:+.4f} "
          f"[{ev_stats[m]['delta_mean_ci95'][0]:+.4f},{ev_stats[m]['delta_mean_ci95'][1]:+.4f}] "
          f"p={ev_stats[m]['wilcoxon_p']:.3f} up={ev_stats[m]['n_increase']}/{ev_stats[m]['n']}")
ev_stats["gfp_peak_uv2"] = paired_stats(
    [evoked(s, "awake")["gfp_peak_uv2"] for s in SUBJECTS],
    [evoked(s, "ketamine")["gfp_peak_uv2"] for s in SUBJECTS])

# background-corrected evoked contrast: (post_k - post_a) - (pre_k - pre_a)
for m in ("lzc_env", "lzs_env", "lzc_wave"):
    dd = [(evoked(s, "ketamine")[f"{m}_post"]["median"] -
           evoked(s, "awake")[f"{m}_post"]["median"]) -
          (evoked(s, "ketamine")[f"{m}_pre"]["median"] -
           evoked(s, "awake")[f"{m}_pre"]["median"]) for s in SUBJECTS]
    a0 = [evoked(s, "awake")[f"{m}_pre"]["median"] for s in SUBJECTS]
    st = paired_stats(a0, [a0[i] + dd[i] for i in range(len(dd))])
    st["delta_mean"] = float(np.mean(dd))
    st["delta_median"] = float(np.median(dd))
    rng = np.random.default_rng(11)
    boots = [np.mean([dd[j] for j in rng.integers(0, len(dd), len(dd))])
             for _ in range(10000)]
    st["delta_mean_ci95"] = [float(np.percentile(boots, 2.5)),
                             float(np.percentile(boots, 97.5))]
    ev_stats[f"{m}_bgcorrected"] = st
    print(f"EVOKED {m}_bgcorrected (post-contrast minus pre-contrast): "
          f"d={st['delta_mean']:+.4f} [{st['delta_mean_ci95'][0]:+.4f},"
          f"{st['delta_mean_ci95'][1]:+.4f}] p={st['wilcoxon_p']:.3f} "
          f"up={st['n_increase']}/{st['n']}")
summary["evoked"] = ev_stats

# ---------------- spontaneous ----------------
sp_stats = {}
for eyes in ("closed", "open"):
    for m in ("lzc_env", "lzs_env", "lzc_wave"):
        key = f"{m}_{eyes}"
        a = [spont(s, "awake", eyes)[m]["median"] for s in SUBJECTS]
        k = [spont(s, "ketamine", eyes)[m]["median"] for s in SUBJECTS]
        sp_stats[key] = paired_stats(a, k)
        print(f"SPONT {key}: awake={sp_stats[key]['awake_median']:.4f} "
              f"ket={sp_stats[key]['ket_median']:.4f} "
              f"d={sp_stats[key]['delta_mean']:+.4f} "
              f"[{sp_stats[key]['delta_mean_ci95'][0]:+.4f},{sp_stats[key]['delta_mean_ci95'][1]:+.4f}] "
              f"p={sp_stats[key]['wilcoxon_p']:.4f} up={sp_stats[key]['n_increase']}/{sp_stats[key]['n']}")
# alpha descriptive
al = {}
for eyes in ("closed", "open"):
    aa = [spont(s, "awake", eyes).get("alpha_cf") for s in SUBJECTS]
    kk = [spont(s, "ketamine", eyes).get("alpha_cf") for s in SUBJECTS]
    al[eyes] = dict(awake=[x for x in aa if x], ketamine=[x for x in kk if x])
summary["spontaneous"] = sp_stats
# eyes-open vs eyes-closed within each condition (paper's secondary finding)
eoec = {}
for cond in ("awake", "ketamine"):
    eoec[cond] = paired_stats(
        [spont(s, cond, "closed")["lzc_env"]["median"] for s in SUBJECTS],
        [spont(s, cond, "open")["lzc_env"]["median"] for s in SUBJECTS])
    print(f"SPONT eyes-open>closed ({cond}): d={eoec[cond]['delta_mean']:+.4f} "
          f"p={eoec[cond]['wilcoxon_p']:.4f} up={eoec[cond]['n_increase']}/{eoec[cond]['n']}")
summary["eyes_open_vs_closed"] = eoec
summary["alpha_cf"] = al

# ---------------- Round-20 recovery validation (subject 210 awake) ----------------
from rd2_evoked_contrast import fast_lzw_count
from scipy.signal import hilbert

d = load_evoked(evoked_paths("210", "awake"))
flatF = d["arr"].flatten(order="F")
n_complete = d["n_complete"]

def lz20(b, rng, n_sh=3):
    c = fast_lzw_count(b)
    Ls = [fast_lzw_count(rng.permutation(b)) for _ in range(n_sh)]
    return c / max(float(np.mean(Ls)), 1.0)

def round20_metrics(flat, n_tr, order_wrong):
    rng = np.random.default_rng(7)
    if order_wrong:
        X = flat[:n_tr * 60 * 251].reshape(n_tr, 60, 251)
        X = np.transpose(X, (1, 0, 2))
    else:
        X = flat[:n_tr * 60 * 251].reshape((60, 251, n_tr), order="F")
        X = np.transpose(X, (0, 2, 1))          # -> (60, n_tr, 251) same layout
    ntr = min(n_tr, 120)
    lw = []
    for t in range(ntr):
        for c in range(0, 60, 3):
            b = (X[c, t] > X[c, t].mean()).astype(np.uint8)
            lw.append(lz20(b, rng))
    le = []
    for t in range(0, ntr, 2):
        for c in range(0, 60, 3):
            amp = np.abs(hilbert(X[c, t]))
            b = (amp > amp.mean()).astype(np.uint8)
            le.append(lz20(b, rng))
    return float(np.median(lw)), float(np.median(le))

n20 = 4296981 // (60 * 251)            # Round-20 recovered trials = 285
w_t = round20_metrics(flatF, n20, order_wrong=True)
c_t = round20_metrics(flatF, n20, order_wrong=False)
c_c = round20_metrics(flatF, n_complete, order_wrong=False)
summary["recovery_validation_210_awake"] = dict(
    round20_reported=dict(lz_wave=0.855, lz_env=0.881),
    reproduced_round20_wrongorder_truncated=dict(lz_wave=w_t[0], lz_env=w_t[1],
                                                 n_trials=n20),
    correct_order_truncated=dict(lz_wave=c_t[0], lz_env=c_t[1], n_trials=n20),
    correct_order_complete=dict(lz_wave=c_c[0], lz_env=c_c[1],
                                n_trials=n_complete))
print("VALIDATION 210 awake: R20 reported 0.855/0.881 | reproduced (wrong-order, "
      f"285tr) {w_t[0]:.3f}/{w_t[1]:.3f} | correct-order 285tr {c_t[0]:.3f}/{c_t[1]:.3f} "
      f"| correct-order complete {c_c[0]:.3f}/{c_c[1]:.3f}")

# ---------------- figures ----------------
def paired_panel(ax, a, k, title, ylabel, m="o"):
    for i, (x, y) in enumerate(zip(a, k)):
        ax.plot([1, 2], [x, y], "-", color="#9ca3af", lw=0.8, alpha=0.8, zorder=1)
        ax.plot([1], [x], "o", color="#2563eb", ms=5, zorder=2)
        ax.plot([2], [y], "o", color="#dc2626", ms=5, zorder=2)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["awake (31)", "ketamine (32)"])
    ax.set_xlim(0.7, 2.3)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontsize=11)
    ax.grid(axis="y", alpha=0.3)

# Fig 1: evoked contrast
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3), constrained_layout=True)
a = [evoked(s, "awake")["lzc_env_post"]["median"] for s in SUBJECTS]
k = [evoked(s, "ketamine")["lzc_env_post"]["median"] for s in SUBJECTS]
paired_panel(axes[0], a, k,
             "A  Evoked LZc (envelope, post-pulse), n=10",
             "LZc (shuffle-normalized)")
a = [evoked(s, "awake")["lzs_env_post"]["median"] for s in SUBJECTS]
k = [evoked(s, "ketamine")["lzs_env_post"]["median"] for s in SUBJECTS]
paired_panel(axes[1], a, k,
             "B  Evoked LZs (envelope, post-pulse), n=10",
             "LZs (shuffle-normalized)")
# grand GFP curves across subjects
gfp_curves = {"awake": [], "ketamine": []}
for cond in ("awake", "ketamine"):
    for s in SUBJECTS:
        dd = load_evoked(evoked_paths(s, cond))
        erp = dd["arr"].mean(axis=2)
        gfp_curves[cond].append(np.sqrt((erp ** 2).mean(axis=0)))
t_ms = (np.arange(251) / FS_EV * 1000.0) - (PULSE_SAMPLE - 1) / FS_EV * 1000.0
ax = axes[2]
for cond, col in (("awake", "#2563eb"), ("ketamine", "#dc2626")):
    G = np.array(gfp_curves[cond])
    ax.plot(t_ms, G.mean(axis=0), color=col, lw=1.6, label=cond)
    ax.fill_between(t_ms, G.mean(axis=0) - G.std(axis=0) / np.sqrt(10),
                    G.mean(axis=0) + G.std(axis=0) / np.sqrt(10),
                    color=col, alpha=0.18)
ax.axvline(0, color="k", lw=0.8, ls="--")
ax.set_xlabel("time from TMS pulse (ms)")
ax.set_ylabel("GFP (uV), grand mean +/- s.e.")
ax.set_title("C  TMS-evoked GFP (10 subj x 2 cond)", fontsize=11)
ax.legend(frameon=False, fontsize=9)
ax.grid(alpha=0.3)
fig.savefig(os.path.join(FIG, "farnes_evoked_contrast.png"), dpi=200)
plt.close(fig)

# Fig 2: spontaneous contrast
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3), constrained_layout=True)
a = [spont(s, "awake", "closed")["lzc_env"]["median"] for s in SUBJECTS]
k = [spont(s, "ketamine", "closed")["lzc_env"]["median"] for s in SUBJECTS]
paired_panel(axes[0], a, k,
             "A  Spontaneous LZc (eyes closed), n=10", "LZc (shuffle-normalized)")
a = [spont(s, "awake", "open")["lzc_env"]["median"] for s in SUBJECTS]
k = [spont(s, "ketamine", "open")["lzc_env"]["median"] for s in SUBJECTS]
paired_panel(axes[1], a, k,
             "B  Spontaneous LZc (eyes open), n=10", "LZc (shuffle-normalized)")
# delta bar chart eyes closed
d = np.array([spont(s, "ketamine", "closed")["lzc_env"]["median"] -
              spont(s, "awake", "closed")["lzc_env"]["median"] for s in SUBJECTS])
ax = axes[2]
ax.bar(range(1, 11), d, color=["#dc2626" if x > 0 else "#2563eb" for x in d])
ax.axhline(0, color="k", lw=0.8)
ax.set_xticks(range(1, 11))
ax.set_xticklabels(SUBJECTS, fontsize=8)
ax.set_xlabel("subject")
ax.set_ylabel("Delta LZc (ketamine - awake), eyes closed")
ax.set_title("C  Within-subject deltas", fontsize=11)
ax.grid(axis="y", alpha=0.3)
fig.savefig(os.path.join(FIG, "farnes_spont_contrast.png"), dpi=200)
plt.close(fig)

with open(os.path.join(OUT, "farnes_contrast_summary.json"), "w") as f:
    json.dump(summary, f, indent=1)
print("\nfigures + summary written to", OUT)
