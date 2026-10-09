#!/usr/bin/env python3
"""Phase 2 — per-level beta-hat fits on the (K, sigma) model surface
(primary convention, L*=40), and the preregistered ORDERING TEST:
"beta estimates must order correctly across sedation levels within
subject, or the beta row is marked Unvalidated" (7th Ed. 5.2).

Fit per level: composite misfit over the 64-point surface
  misfit = |dfa_model - dfa_level| / 0.1 + |alpha_model - alpha_level| / 1.0 Hz
(model alpha None -> 8.5 neutral fallback, documented). beta-hat =
sigma*/K* at the argmin. Also recorded: K* vs the Phase-1 critical band
[15, 35] rad/s (in/out), and the LZ trajectory (does LZ fall as the fit
exits the band).

Levels: ds005620 (awake_EC vs sed_rest_r1, 8 subjects); ds004541
(pre / maintenance / emergence / recovery, 9 sessions); MEG bst_resting
(healthy reference, run1/run2).
"""
import json
import glob
import numpy as np

OUT = "/home/z/my-project/glm agent 2/research/phase2"
S = np.load(f"{OUT}/ksigma/ksigma_surface.npz", allow_pickle=True)
Kg, Sg = S["K"], S["sigma"]
DFAg, ALPha = S["dfa_median"], S["alpha_hz"]
K_BAND = (15.0, 35.0)


def fit_level(dfa_level, alpha_level):
    mis = np.full(len(Kg), np.inf)
    for i in range(len(Kg)):
        am = ALPha[i]
        am = 8.5 if (am is None or np.isnan(am)) else float(am)
        al = alpha_level if alpha_level is not None else 8.5
        mis[i] = abs(DFAg[i] - dfa_level) / 0.1 + abs(am - al) / 1.0
    j = int(np.argmin(mis))
    return {"K_star": float(Kg[j]), "sigma_star": float(Sg[j]),
            "beta_hat": float(Sg[j] / Kg[j]), "misfit": float(mis[j]),
            "dfa_model": float(DFAg[j]),
            "in_band": bool(K_BAND[0] <= Kg[j] <= K_BAND[1])}


def load_jsons(pat):
    out = {}
    for p in sorted(glob.glob(pat)):
        with open(p) as f:
            d = json.load(f)
        out.update(d)
    return out


def main():
    results = {"levels": [], "convention": "primary (rad/s, row-norm W, L*=40)"}

    # --- ds005620: awake vs sed ---
    d56 = load_jsons(f"{OUT}/ds005620/obs_part*.json")
    n_ord = n_tot = 0
    for sub, conds in sorted(d56.items()):
        row = {"corpus": "ds005620", "subject": sub}
        for cond in ("awake_EC", "sed_rest_r1"):
            o = conds.get(cond)
            if not o or "dfa_median" not in o:
                continue
            f = fit_level(o["dfa_median"], o.get("alpha_cf"))
            f.update({"dfa_level": o["dfa_median"],
                      "alpha_level": o.get("alpha_cf"),
                      "lzs": o.get("lzs_median"), "lzc": o.get("lzc_median")})
            row[cond] = f
        if "awake_EC" in row and "sed_rest_r1" in row:
            n_tot += 1
            ok = row["sed_rest_r1"]["beta_hat"] > row["awake_EC"]["beta_hat"]
            row["beta_order_correct"] = bool(ok)
            n_ord += int(ok)
        results["levels"].append(row)
    results["ds005620_ordering"] = {"n": n_tot, "beta_sed_gt_awake": n_ord}

    # --- ds004541: 4 levels ---
    d45 = load_jsons(f"{OUT}/ds004541/obs_part*.json")
    order_counts = {"maintenance>pre": 0, "n_pre_maint": 0,
                    "recovery<maintenance": 0, "n_rec_maint": 0}
    for sess, eps in sorted(d45.items()):
        row = {"corpus": "ds004541", "subject": sess}
        for lev in ("pre", "maintenance", "emergence", "recovery"):
            o = eps.get("epochs", {}).get(lev)
            if not o or "dfa_median" not in o:
                continue
            f = fit_level(o["dfa_median"], o.get("alpha_cf"))
            f.update({"dfa_level": o["dfa_median"],
                      "alpha_level": o.get("alpha_cf"),
                      "lzs": o.get("lzs_median"), "lzc": o.get("lzc_median")})
            row[lev] = f
        if "pre" in row and "maintenance" in row:
            order_counts["n_pre_maint"] += 1
            order_counts["maintenance>pre"] += int(
                row["maintenance"]["beta_hat"] > row["pre"]["beta_hat"])
        if "recovery" in row and "maintenance" in row:
            order_counts["n_rec_maint"] += 1
            order_counts["recovery<maintenance"] += int(
                row["recovery"]["beta_hat"] < row["maintenance"]["beta_hat"])
        results["levels"].append(row)
    results["ds004541_ordering"] = order_counts

    # --- MEG reference ---
    mo = np.load("/home/z/my-project/glm agent 2/research/phase1/meg_obs.npz")
    for run in ("run1", "run2"):
        dfa = float(np.median(mo[f"{run}_dfa_ch"]))
        f = fit_level(dfa, None)
        f["dfa_level"] = dfa
        results["levels"].append({"corpus": "MEG_bst_resting", "subject": run, "level": f})
    results["meg_reference"] = {
        "run1": results["levels"][-2]["level"], "run2": results["levels"][-1]["level"]}

    # --- LZ tracking test (the spec's failure condition) ---
    # does LZ fall as the fitted K* exits the Phase-1 critical band?
    pairs = []
    for row in results["levels"]:
        for cond in ("awake_EC", "sed_rest_r1", "pre", "maintenance",
                     "emergence", "recovery"):
            if cond in row and row[cond].get("lzs") is not None:
                pairs.append((row[cond]["K_star"], row[cond]["in_band"], row[cond]["lzs"]))
    inb = [p[2] for p in pairs if p[1]]
    outb = [p[2] for p in pairs if not p[1]]
    results["lz_tracking"] = {
        "n_in_band": len(inb), "n_out_band": len(outb),
        "mean_lz_in_band": float(np.mean(inb)) if inb else None,
        "mean_lz_out_band": float(np.mean(outb)) if outb else None,
        "note": "LZ (Farnes instrument) mean inside vs outside the "
                "Phase-1 critical K-band; the spec's coherence-threshold "
                "prediction: LZ falls as the operating point exits the band"}

    with open(f"{OUT}/phase2_fits.json", "w") as f:
        json.dump(results, f, indent=1)
    print(json.dumps({k: v for k, v in results.items() if k != "levels"}, indent=1))
    print("levels fitted:", len(results["levels"]))


if __name__ == "__main__":
    main()
