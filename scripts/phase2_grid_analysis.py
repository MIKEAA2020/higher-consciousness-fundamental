#!/usr/bin/env python3
"""Myrov-convention grid analysis: op-point fit, sigma sweep, structure-function nulls.

Modes:
  fit          interpolate DFA-median surfaces -> MEG-matched K* per L; op point
  sigma i      sigma-sweep chunk at (K*, L*) : sigmas[i]
  nulls        shuffled/random SC at the op point with permutation tests
"""
import json
import sys
import numpy as np

sys.path.insert(0, "/home/z/my-project/scripts")
from phase1_kuramoto import load_sc, run_sim, sf_surfaces

GRID = "/home/z/my-project/glm agent 2/research/phase2/grid"
SUBJ = "101309"
T_SIM = 120.0
WARM = 30.0


def grid_data():
    d = np.load(f"{GRID}/myrov_grid.npz")
    return d


def meg_targets():
    mo = np.load("/home/z/my-project/glm agent 2/research/phase1/meg_obs.npz")
    return float(np.median(mo["run1_dfa_ch"])), float(np.median(mo["run2_dfa_ch"]))


def main_fit():
    d = grid_data()
    t1, t2 = meg_targets()
    K, L, dfa = d["K"], d["L"], d["dfa_median"]
    res = {"dfa_targets": [t1, t2], "slices": {}}
    print(f"MEG DFA targets: run1={t1:.3f} run2={t2:.3f}")
    for Lv in sorted(set(L)):
        m = (L == Lv)
        k = np.sort(K[m]); v = dfa[m][np.argsort(K[m])]
        # interpolate K where dfa crosses each target (all crossings)
        for tgt, name in [(t1, "run1"), (t2, "run2")]:
            sgn = np.sign(v - tgt)
            cross = []
            for i in range(len(k) - 1):
                if sgn[i] == 0:
                    cross.append(float(k[i]))
                elif sgn[i] * sgn[i + 1] < 0:
                    # linear interpolation
                    kk = k[i] + (tgt - v[i]) / (v[i + 1] - v[i]) * (k[i + 1] - k[i])
                    cross.append(round(float(kk), 2))
            res["slices"][f"L={Lv}"] = res["slices"].get(f"L={Lv}", {})
            res["slices"][f"L={Lv}"][name] = cross
            print(f"L={Lv}: DFA(K) range [{v.min():.3f},{v.max():.3f}]; "
                  f"{name} target {tgt:.3f} crossings at K={cross}")
    # op point: at L=8 (the convention test's matched L), pick the
    # HIGHEST-K crossing within the sampled plane (the R19 extrapolation
    # placed the brain at/just beyond the synchronized edge)
    c1 = res["slices"]["L=8.0"]["run1"]
    c2 = res["slices"]["L=8.0"]["run2"]
    k1 = max(c1) if c1 else None
    k2 = max(c2) if c2 else None
    res["op_point"] = {"L": 8.0, "K_run1": k1, "K_run2": k2,
                       "beta_run1": round(0.2 / k1, 4) if k1 else None,
                       "beta_run2": round(0.2 / k2, 4) if k2 else None}
    print("op point (sigma=0.2):", res["op_point"])
    # structure-function summary at the matched region
    m8 = (L == 8)
    k8 = K[m8]
    for key in ["order_strength_rho", "plv_edge_rho", "cc_edge_rho", "dfa_strength_rho"]:
        v = d[key][m8][np.argsort(k8)]
        print(f"L=8 {key}: K=7..10 mean {v[(np.argsort(k8)>=14)].mean() if len(v)>14 else float('nan'):.3f}")
    with open(f"{GRID}/myrov_fit.json", "w") as f:
        json.dump(res, f, indent=1)


SIGMAS = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]


def main_sigma(i):
    """Chunk i: 3 sigmas at (K*, L*) — K* from fit."""
    with open(f"{GRID}/myrov_fit.json") as f:
        fit = json.load(f)
    k_star = fit["op_point"]["K_run1"] or 9.5
    sel = SIGMAS[3 * i:3 * i + 3]
    import phase2_grid_myrov as g
    omega = g.build_omega()
    W_ext, W_sym, strength = load_sc(SUBJ, row_normalize=False)
    Ks = np.array([k_star] * len(sel), dtype=np.float32)
    Ls = np.array([8.0] * len(sel), dtype=np.float32)
    out = {"sigma": np.array(sel), "K": Ks.astype(float), "L": Ls.astype(float)}
    for j, s in enumerate(sel):
        res = run_sim(W_ext, omega, Ks[j:j + 1], Ls[j:j + 1], s, T_s=T_SIM,
                      warmup_s=WARM, seed=600, want_matrices=True, progress_every=0)
        sf = sf_surfaces(W_sym, res)
        out.setdefault("dfa_median", []).append(float(np.nanmedian(res["dfa"][0])))
        out.setdefault("frac065", []).append(float(res["frac065"][0]))
        out.setdefault("mean_order", []).append(float(res["mean_order"][0].mean()))
        out.setdefault("order_strength_rho", []).append(float(sf["order_strength_rho"][0]))
        out.setdefault("plv_edge_rho", []).append(float(sf["plv_edge_rho"][0]))
        print(f"sigma={s}: dfa_med={out['dfa_median'][-1]:.3f} "
              f"frac065={out['frac065'][-1]:.3f} ord~str={out['order_strength_rho'][-1]:+.3f}",
              flush=True)
    np.savez(f"{GRID}/sigma_part{i}.npz",
             **{k: np.array(v) for k, v in out.items()})


def main_nulls():
    """Structure-function nulls at the Myrov-convention op point."""
    from scipy.stats import spearmanr
    with open(f"{GRID}/myrov_fit.json") as f:
        fit = json.load(f)
    k_star = fit["op_point"]["K_run1"] or 9.5
    import phase2_grid_myrov as g
    omega = g.build_omega()
    W_ext, W_sym, strength = load_sc(SUBJ, row_normalize=False)
    rng = np.random.default_rng(11)

    # shuffled-label SC
    perm = rng.permutation(W_sym.shape[0])
    W_shuf = W_sym[np.ix_(perm, perm)]
    W_shuf_ext = W_shuf  # raw convention: W_ext == W_sym (max-normalized)
    # random uniform SC
    W_rand = rng.random(W_sym.shape).astype(np.float32)
    W_rand = 0.5 * (W_rand + W_rand.T)
    np.fill_diagonal(W_rand, 0)

    cases = [("real", W_ext, W_sym), ("shuffled", W_shuf_ext, W_shuf),
             ("random", W_rand, W_rand)]
    out = {}
    for label, W_e, W_s in cases:
        res = run_sim(W_e, omega, np.array([k_star], dtype=np.float32),
                      np.array([8.0], dtype=np.float32), 0.2, T_s=T_SIM,
                      warmup_s=WARM, seed=700, want_matrices=True, progress_every=0)
        sf = sf_surfaces(W_s, res)
        s = W_s.sum(axis=1)
        iu = np.triu_indices(W_s.shape[0], 1)
        # permutation p for order~strength
        rho = sf["order_strength_rho"][0]
        n_perm = 200
        cnt = 0
        for _ in range(n_perm):
            p = rng.permutation(len(s))
            r2 = spearmanr(res["mean_order"][0][p], s).statistic
            if abs(r2) >= abs(rho):
                cnt += 1
        out[label] = {"order_strength_rho": float(rho),
                      "order_strength_p": cnt / n_perm,
                      "dfa_strength_rho": float(sf["dfa_strength_rho"][0]),
                      "plv_edge_rho": float(sf["plv_edge_rho"][0]),
                      "cc_edge_rho": float(sf["cc_edge_rho"][0]),
                      "dfa_median": float(np.nanmedian(res["dfa"][0])),
                      "mean_order": float(res["mean_order"][0].mean())}
        print(label, json.dumps(out[label]), flush=True)
    with open(f"{GRID}/myrov_nulls.json", "w") as f:
        json.dump({"K": k_star, "L": 8.0, "sigma": 0.2, "cases": out}, f, indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "fit":
        main_fit()
    elif cmd == "sigma":
        main_sigma(int(sys.argv[2]))
    elif cmd == "nulls":
        main_nulls()
