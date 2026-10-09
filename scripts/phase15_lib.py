#!/usr/bin/env python3
"""Phase 1.5 — Fiedler-boundary test library (the P2 instrument).

Predictions under test (user's Round-22 separation):
  P2 (domain structure): the domains the decombination model predicts are the
  sign regions of the graph Fiedler vector psi^(2); predicted boundary
  dA = {i: psi_i ~ 0}. If the graph-decombination mechanism has empirical
  teeth, psi^(2) of the REAL connectome aligns with functional geometry
  (network boundaries, sensory->transmodal axis, DID key regions) MORE than
  psi^(2) of degree-preserving rewired nulls. If real == rewired, the
  generic-criticality reading suffices and P2 is unsupported at this
  granularity.

Conventions:
  - L_sym = I - D^{-1/2} W D^{-1/2} (primary); unnormalized L = D - W
    (sensitivity arm).
  - Sign of psi fixed per subject so Spearman(psi, axis) > 0; all reported
    statistics are sign-invariant anyway.
  - W = symmetrized raw DTI_CM fiber counts (primary); log1p(W) sensitivity.
"""
import numpy as np
from scipy.io import loadmat

SCDIR = "/home/z/my-project/glm agent 2/research/phase1/sc"
SUBJECTS = ["101309", "102311", "102816", "131217", "211619", "213522",
            "377451"]


def load_sc(subject, transform="raw"):
    W = loadmat(f"{SCDIR}/{subject}_DTI_CM.mat")["sc"].astype(np.float64)
    W = 0.5 * (W + W.T)                      # symmetrize (tiny asymmetries)
    np.fill_diagonal(W, 0.0)
    if transform == "log1p":
        W = np.log1p(W)
    return W


def laplacian_sym(W):
    d = W.sum(axis=1)
    dinv = np.where(d > 0, 1.0 / np.sqrt(np.maximum(d, 1e-12)), 0.0)
    return np.eye(len(W)) - (dinv[:, None] * W * dinv[None, :])


def laplacian_unnorm(W):
    return np.diag(W.sum(axis=1)) - W


def fiedler(W, lap="sym"):
    """Return (all eigenvalues sorted, psi) where psi = the Fiedler vector
    (2nd smallest eigenvector = mode 2). Full eigh (94x94)."""
    L = laplacian_sym(W) if lap == "sym" else laplacian_unnorm(W)
    ev, V = np.linalg.eigh(L)
    order = np.argsort(ev)
    ev, V = ev[order], V[:, order]
    return ev, V[:, 1].astype(np.float64)


def spectrum(W, lap="sym", kmax=6):
    """Return (ev[:kmax+1], Vmodes) where Vmodes[:, j] = mode j+2
    (column 0 = the Fiedler vector / mode 2)."""
    L = laplacian_sym(W) if lap == "sym" else laplacian_unnorm(W)
    ev, V = np.linalg.eigh(L)
    order = np.argsort(ev)
    ev, V = ev[order], V[:, order]
    return ev[:kmax + 1], V[:, 1:kmax + 1].astype(np.float64)


def rewire2(W, n_swap_factor=10, rng=None):
    """Clean degree-preserving rewiring (binary Maslov-Sneppen with weight
    carry). This is the version used by the battery."""
    rng = rng or np.random.default_rng(0)
    n = len(W)
    A = W.copy()
    iu = np.triu_indices(n, 1)
    nz = A[iu] > 0
    edge_list = list(zip(iu[0][nz], iu[1][nz]))
    m = len(edge_list)
    n_swaps = int(n_swap_factor * m)
    ei = np.array([e[0] for e in edge_list])
    ej = np.array([e[1] for e in edge_list])
    for _ in range(n_swaps):
        a, b = rng.integers(0, m, 2)
        i, j = ei[a], ej[a]
        k, l = ei[b], ej[b]
        if len({i, j, k, l}) != 4:
            continue
        # canonical orientation (i<j, k<l enforced by construction)
        if A[i, l] > 0 or A[j, k] > 0:
            continue
        w1, w2 = A[i, j], A[k, l]
        if w1 == 0 or w2 == 0:
            continue
        A[i, j] = A[j, i] = 0.0
        A[k, l] = A[l, k] = 0.0
        A[i, l] = A[l, i] = w1
        A[j, k] = A[k, j] = w2
        ei[a], ej[a] = i, l
        ei[b], ej[b] = j, k
    return A


def shuffle_full(W, rng=None):
    """Same weight multiset, random topology (destroys degree too)."""
    rng = rng or np.random.default_rng(0)
    n = len(W)
    iu = np.triu_indices(n, 1)
    vals = W[iu]
    perm = rng.permutation(len(vals))
    A = np.zeros_like(W)
    A[iu] = vals[perm]
    A[(iu[1], iu[0])] = A[iu]
    return A


# ------------------------- the statistic battery -------------------------

def spearman(a, b):
    from scipy.stats import spearmanr
    m = np.isfinite(a) & np.isfinite(b)
    if m.sum() < 3:
        return np.nan
    return float(spearmanr(a[m], b[m]).statistic)


def battery_light(W, M, lap="sym", kmax=6):
    """Fiedler + mode-profile statistics only (no KMeans, no psi storage) —
    the null-loop workhorse."""
    evall, Vm = spectrum(W, lap=lap, kmax=kmax)
    strength = W.sum(axis=1)
    psi = Vm[:, 0]
    if spearman(psi, M["axis"]) < 0:
        psi = -psi
    cort = M["iscort"]
    out = {
        "eigengap": float(evall[2] - evall[1]),
        "hemi_align": abs(spearman(psi, M["hemi"].astype(float))),
        "subcort_align": abs(spearman(psi, (~cort).astype(float))),
        "axis_align": abs(spearman(psi[cort], M["axis"][cort])),
        "net_contrast": _net_contrast(psi, M),
        "did_sep": float(abs(psi[M["did_ep"]].mean() - psi[M["did_anp"]].mean())
                         / max(psi.std(), 1e-12)),
        "strength_rho_fiedler": spearman(psi, strength),
    }
    for net in M["networks"]:
        out[f"bipart_{net}"] = _bipart_agree(psi, M["net"] == net)
    out["mode_profile"] = {}
    for k in range(2, kmax + 2):
        v = Vm[:, k - 2]
        out["mode_profile"][str(k)] = {
            "hemi_align": abs(spearman(v, M["hemi"].astype(float))),
            "axis_align": abs(spearman(v[cort], M["axis"][cort])),
            "net_contrast": _net_contrast(v, M),
            "did_sep": float(abs(v[M["did_ep"]].mean()
                                 - v[M["did_anp"]].mean())
                             / max(v.std(), 1e-12)),
            "strength_rho": spearman(v, strength),
        }
    out["eigengaps"] = [float(evall[i + 1] - evall[i]) for i in
                        range(1, len(evall) - 1)]
    return out


def ari_stats(W, M, lap="sym"):
    """Spectral-embedding partition agreement with Yeo networks."""
    from sklearn.cluster import KMeans
    from sklearn.metrics import adjusted_rand_score
    evall, Vm = spectrum(W, lap=lap, kmax=4)
    cort = M["iscort"]
    cortlab = M["net"][cort]
    Em = Vm[:, :4]                       # modes 2..5
    out = {}
    for kpart in (2, 4, 7):
        lab = KMeans(n_clusters=kpart, n_init=10,
                     random_state=0).fit_predict(Em)
        out[f"ari_{kpart}"] = float(adjusted_rand_score(cortlab, lab[cort]))
    return out


def battery(W, M, lap="sym", kmax=6):
    """All sign-invariant statistics of psi against the functional map M.

    Primary: the Fiedler vector psi^(2) (the user-specified P2 test).
    Extended: the first kmax nontrivial modes — because the leading cut of
    these connectomes is interhemispheric, the finer domain geometry
    (network level) lives in higher modes; each mode gets the same
    alignment statistics so the domain hierarchy can be read off.
    """
    ev, psi = fiedler(W, lap=lap)
    # sign convention: transmodal-positive
    if spearman(psi, M["axis"]) < 0:
        psi = -psi
    cort = M["iscort"]
    out = {
        "eigenvalues": ev[:6].tolist(),
        "eigengap": float(ev[2] - ev[1]),
        "hemi_align": abs(spearman(psi, M["hemi"].astype(float))),
        "subcort_align": abs(spearman(psi, (~cort).astype(float))),
        "axis_align": abs(spearman(psi[cort], M["axis"][cort])),
        "net_contrast": _net_contrast(psi, M),
        "did_sep": float(abs(psi[M["did_ep"]].mean() - psi[M["did_anp"]].mean())
                         / max(psi.std(), 1e-12)),
        "psi": psi.tolist(),
    }
    for net in M["networks"]:
        out[f"bipart_{net}"] = _bipart_agree(psi, M["net"] == net)

    # ---- extended multi-mode profile (modes 2..kmax+1) ----
    evall, Vm = spectrum(W, lap=lap, kmax=kmax)
    out["mode_profile"] = {}
    out["eigengaps"] = [float(evall[i + 1] - evall[i]) for i in
                        range(1, len(evall) - 1)]
    for k in range(2, kmax + 2):
        v = Vm[:, k - 2]                      # mode k
        out["mode_profile"][str(k)] = {
            "hemi_align": abs(spearman(v, M["hemi"].astype(float))),
            "axis_align": abs(spearman(v[cort], M["axis"][cort])),
            "net_contrast": _net_contrast(v, M),
            "did_sep": float(abs(v[M["did_ep"]].mean()
                                 - v[M["did_anp"]].mean())
                             / max(v.std(), 1e-12)),
        }
    # spectral-embedding partition agreement (k-means on modes 2..5)
    try:
        from sklearn.cluster import KMeans
        from sklearn.metrics import adjusted_rand_score
        Em = Vm[:, :4]                       # modes 2..5
        for kpart in (2, 4, 7):
            lab = KMeans(n_clusters=kpart, n_init=25,
                         random_state=0).fit_predict(Em)
            # agreement with Yeo networks at that granularity (cortical)
            cortlab = M["net"][cort]
            out[f"ari_{kpart}"] = float(adjusted_rand_score(cortlab, lab[cort]))
    except Exception as ex:
        out["ari_error"] = str(ex)
    return out


def _net_contrast(psi, M):
    """(mean |dpsi| cross-network - within-network) / std, cortical only."""
    cort = np.where(M["iscort"])[0]
    net = M["net"][cort]
    p = psi[cort]
    same = net[:, None] == net[None, :]
    iu = np.triu_indices(len(cort), 1)
    d = np.abs(p[iu[0]] - p[iu[1]])
    s = same[iu[0], iu[1]]
    if s.sum() == 0 or (~s).sum() == 0:
        return np.nan
    return float((d[~s].mean() - d[s].mean()) / max(p.std(), 1e-12))


def _bipart_agree(psi, memb):
    """Best-sign-flip agreement fraction with a membership bipartition."""
    b = psi > 0
    a1 = (b == memb).mean()
    a2 = (b == ~memb).mean()
    return float(max(a1, a2))


def block_shuffle(W, hemi, rng=None):
    """Hemisphere-block-preserving weight shuffle (the dense-graph null for
    FINER-than-hemispheric structure): shuffles the edge weights separately
    within the intra-L, intra-R and inter-hemispheric blocks, so the coarse
    hemispheric block structure (and each block's weight distribution) is
    preserved exactly while finer topology is randomized.

    Rationale: these DTI connectomes are FULLY DENSE (4371/4371 nonzero
    pairs), so Maslov-Sneppen degree-preserving edge swaps are formally
    inapplicable (every swap is rejected) — the R22 first run's 'rewire'
    null was a silent no-op (all p=1.000), caught and documented."""
    rng = rng or np.random.default_rng(0)
    n = len(W)
    A = np.zeros_like(W)
    groups = {"LL": [], "RR": [], "LR": []}
    for i in range(n):
        for j in range(i + 1, n):
            tag = ("LL" if hemi[i] == 0 and hemi[j] == 0 else
                   "RR" if hemi[i] == 1 and hemi[j] == 1 else "LR")
            groups[tag].append((i, j))
    for tag, pairs in groups.items():
        vals = np.array([W[i, j] for i, j in pairs])
        vals = vals[rng.permutation(len(vals))]
        for (i, j), v in zip(pairs, vals):
            A[i, j] = A[j, i] = v
    return A


def partial_spearman(a, b, c):
    """Partial Spearman correlation of a vs b controlling for c (rank
    regression residuals)."""
    from scipy.stats import spearmanr
    m = np.isfinite(a) & np.isfinite(b) & np.isfinite(c)
    a, b, c = a[m], b[m], c[m]
    if len(a) < 4:
        return np.nan
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    rc = np.argsort(np.argsort(c)).astype(float)

    def resid(x, y):
        beta = np.polyfit(y, x, 1)
        return x - np.polyval(beta, y)
    return float(spearmanr(resid(ra, rc), resid(rb, rc)).statistic)


def battery_nulls(W, M, lap="sym", n_shuffle=200, n_perm=10000, seed=0):
    """Null distributions for every battery statistic (dense-graph version).

    Null families (Maslov-Sneppen rewiring is inapplicable: the connectomes
    are fully dense — documented above):
      shuffle — random topology with the same weight multiset (destroys all
                geometry; the generic-weighted-graph null)
      block   — hemispheric-block-preserving weight shuffle (preserves the
                coarse cut exactly; the null for finer-than-hemispheric
                structure — the mode-3+ domain geometry)
      perm    — label permutation (region-identity null, the primary P2
                reference: keeps psi values, reassigns region identities)
      bipart  — random size-matched bipartitions (for agreement stats)
    """
    rng = np.random.default_rng(seed)
    stats = ["hemi_align", "subcort_align", "axis_align", "net_contrast",
             "did_sep", "eigengap"] + [f"bipart_{n}" for n in M["networks"]]
    mode_stats = ["hemi_align", "axis_align", "net_contrast", "did_sep"]
    nulls = {k: [] for k in stats}
    nulls["shuffle"] = {k: [] for k in stats}
    nulls["block"] = {k: [] for k in stats}
    nulls["mode"] = {str(k): {s: [] for s in mode_stats}
                     for k in range(2, 8)}
    nulls["mode_shuffle"] = {str(k): {s: [] for s in mode_stats}
                             for k in range(2, 8)}
    nulls["mode_block"] = {str(k): {s: [] for s in mode_stats}
                           for k in range(2, 8)}
    for r in range(n_shuffle):
        Ws = shuffle_full(W, rng=rng)
        bs = battery_light(Ws, M, lap=lap)
        for k in stats:
            nulls["shuffle"][k].append(bs[k])
        for k in range(2, 8):
            for s in mode_stats:
                nulls["mode_shuffle"][str(k)][s].append(
                    bs["mode_profile"][str(k)][s])
        Wb = block_shuffle(W, M["hemi"], rng=rng)
        bb = battery_light(Wb, M, lap=lap)
        for k in stats:
            nulls["block"][k].append(bb[k])
        for k in range(2, 8):
            for s in mode_stats:
                nulls["mode_block"][str(k)][s].append(
                    bb["mode_profile"][str(k)][s])

    # label-permutation nulls, per mode (region-identity null)
    cort = np.where(M["iscort"])[0]
    net_cort = M["net"][cort]
    evall, Vm = spectrum(W, lap=lap, kmax=7)
    n_c = len(cort)
    iu = np.triu_indices(n_c, 1)
    for k in range(2, 8):
        v = Vm[:, k - 2]
        p = v[cort]
        perm_nc, perm_ax, perm_did = [], [], []
        for _ in range(n_perm):
            lab = rng.permutation(net_cort)
            same = lab[:, None] == lab[None, :]
            d = np.abs(p[iu[0]] - p[iu[1]])
            s = same[iu[0], iu[1]]
            perm_nc.append((d[~s].mean() - d[s].mean()) / max(p.std(), 1e-12))
            perm_ax.append(abs(spearman(p, rng.permutation(M["axis"][cort]))))
            pe = rng.permutation(len(v))
            ep = v[pe[:8]]
            an = v[pe[8:10]]
            perm_did.append(abs(ep.mean() - an.mean()) / max(v.std(), 1e-12))
        nulls.setdefault("perm_mode", {})[str(k)] = {
            "net_contrast": perm_nc, "axis_align": perm_ax,
            "did_sep": perm_did}

    # bipartition nulls: random size-matched splits
    for net in M["networks"]:
        memb = M["net"] == net
        k_true = int(memb.sum())
        n_all = len(memb)
        vals = []
        for _ in range(2000):
            rnd = np.zeros(n_all, dtype=bool)
            rnd[rng.permutation(n_all)[:k_true]] = True
            b = Vm[:, 0] > 0
            vals.append(max((b == rnd).mean(), (b == ~rnd).mean()))
        nulls.setdefault("bipart_null", {})[net] = vals
    return nulls


def emp_p(real, null):
    null = np.asarray(null, dtype=float)
    null = null[np.isfinite(null)]
    if len(null) == 0:
        return np.nan
    return float((1 + (null >= real).sum()) / (1 + len(null)))
