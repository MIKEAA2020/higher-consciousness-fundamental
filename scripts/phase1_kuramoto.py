#!/usr/bin/env python3
"""Phase 1 (Level-2 protocol) — Myrov-style hierarchical Kuramoto on a real
connectome, batched over the (K, L) plane, with online observables.

Model (Myrov et al., bioRxiv 2024.05.08.593146, Materials & Methods):
  dphi_i^n/dt = Natural + Internal + External + Noise
  Natural   = omega_i^n
  Internal  = K * Im( z_n * e^{-i phi_i} ),   z_n = (1/M) sum_q e^{i phi_q^n}
  External  = L * Im( e^{i phi_i} * conj(U_n) ),  U_n = sum_j W_nj z_j
              (W = structural connectome, max-normalized, symmetric;
               sum_j W_nj R_j sin(phi_i - Phi_j) = Im(e^{i phi_i} conj(U_n)))
  Noise     = eta_i^n (white, amplitude sigma)

Supplementary Table 1 (oscillator count, dt, noise) is not public; values
used here are documented assumptions: M = 50 oscillators/node, dt = 1 ms
(omega_max*dt <= 0.19 rad), sigma calibrated so the critical regime occupies
a comparable fraction of the [0,8]^2 plane as in the source figures.

Observables per (K,L) combo (online accumulators, z sampled at 100 Hz):
  mean node order R_n; per-node DFA of |z_n| (1-30 s windows, block DFA);
  fraction of nodes with DFA > 0.65 (Myrov's rule); PLV matrix from node
  phases; envelope cross-correlation matrix; grand-mean PSD of z
  (rfft blocks, Hann); structure-function correlations.

CLI:
  calibrate              quick sigma calibration + speed benchmark
  sweep [subject]        full 9x9 (K,L) grid, primary treatment
  slice subject K* L*    K-slice at L* and L-slice at K* (6 other subjects)
  nulls K* L* sigma*     shuffled-SC and random-SC at the operating point
"""
import json
import sys
import time
import glob
import numpy as np
from scipy.io import loadmat

SCDIR = "/home/z/my-project/glm agent 2/research/phase1/sc"
OUT = "/home/z/my-project/glm agent 2/research/phase1"

SUBJECTS = ["101309", "102311", "102816", "131217", "211619", "213522", "377451"]
PRIMARY = "101309"

N_OSC = 50
DT = 0.001
STRIDE = 10                    # z sampled every 10 steps -> 100 Hz
FREQ_RANGE = (3.0, 30.0)
PSD_BLOCK = 512                # samples @ 100 Hz per periodogram block
DFA_WINS_FULL = [100, 178, 316, 562, 1000, 1778, 3000]   # 1-30 s @ 100 Hz
DFA_WINS_CAL = [100, 178, 316, 562, 1000]                # 1-10 s (short runs)
DFA_CHUNK_FULL = 3000
DFA_CHUNK_CAL = 1000
WARMUP_S = 30.0
T_SWEEP_S = 150.0       # per-chunk sim time (30 s warm-up + 120 s analysis)
T_SLICE_S = 150.0
T_NULL_S = 150.0
CHUNK = 9               # combos per synchronous tool call (10-min limit)


def load_sc(subject, log_transform=False, row_normalize=True):
    """Returns (W_ext, W_sym, strength).
    W_sym: symmetric max-normalized connectome (for structure measures).
    W_ext: row-normalized version for the External coupling term
    (each node's incoming weights sum to 1, so L acts at the same scale
    as K — required for the diagonal critical ridge in the (K,L) plane)."""
    C = loadmat(f"{SCDIR}/{subject}_DTI_CM.mat")["sc"].astype(np.float64)
    np.fill_diagonal(C, 0.0)
    C = 0.5 * (C + C.T)
    if log_transform:
        C = np.log1p(C)
    W_sym = C / C.max()
    strength = W_sym.sum(axis=1)
    if row_normalize:
        rs = W_sym.sum(axis=1, keepdims=True)
        W_ext = np.where(rs > 0, W_sym / np.maximum(rs, 1e-12), 0.0)
    else:
        W_ext = W_sym
    return W_ext.astype(np.float32), W_sym.astype(np.float32), strength


def load_freq_pdf():
    d = np.load(f"{OUT}/meg_obs.npz")
    f = d["run1_fooof_freqs"]
    p = d["run1_fooof_periodic"]
    m = (f >= FREQ_RANGE[0]) & (f <= FREQ_RANGE[1])
    f, p = f[m], p[m]
    return f, p / p.sum()


def load_peak_params():
    """Re-fit FOOOF on the stored grand-mean PSD to recover peak
    (CF, PW, BW) parameters for per-node frequency-band sampling."""
    from fooof import FOOOF
    d = np.load(f"{OUT}/meg_obs.npz")
    f = d["run1_freqs"]
    p = d["run1_psd_mean"]
    m = (f >= 3) & (f <= 30)
    fm = FOOOF(peak_width_limits=[0.5, 12.0], max_n_peaks=8, min_peak_height=0.05,
               verbose=False)
    fm.fit(f[m], p[m])
    return fm.peak_params_          # (n_peaks, 3): CF, PW, BW


def sample_omega(rng):
    """Per-node oscillator frequencies (rad/s). Each node is assigned a
    peak band (probability ~ peak power); its oscillators are drawn from
    N(CF, BW) clipped to [3,30] Hz — the sensor-space analogue of Myrov's
    per-parcel PSD sampling. Converted to rad/s for physical integration."""
    peaks = load_peak_params()
    N = 94
    if len(peaks) == 0:
        peaks = np.array([[10.0, 1.0, 2.0]])
    prob = peaks[:, 1] / peaks[:, 1].sum()
    freqs = np.empty((N, N_OSC), dtype=np.float32)
    for n in range(N):
        k = rng.choice(len(peaks), p=prob)
        cf, bw = float(peaks[k, 0]), max(float(peaks[k, 2]), 1.0)
        freqs[n] = np.clip(rng.normal(cf, bw, N_OSC), 3.0, 30.0)
    return (2 * np.pi * freqs).astype(np.float32)


def run_sim(W, omega, Ks, Ls, sigma, T_s, warmup_s=60.0,
            dfa_wins=None, dfa_chunk=None, seed=0, want_matrices=False,
            progress_every=30000):
    """Batched hierarchical Kuramoto. Ks, Ls: per-combo scalars (len C).
    Returns dict of per-combo observables."""
    C, N, M = len(Ks), W.shape[0], omega.shape[1]
    dfa_wins = dfa_wins or DFA_WINS_FULL
    dfa_chunk = dfa_chunk or DFA_CHUNK_FULL
    rng = np.random.default_rng(seed)
    phi = (rng.random((C, N, M), dtype=np.float32) * 2 * np.pi)
    Kc = np.asarray(Ks, dtype=np.float32)
    Lc = np.asarray(Ls, dtype=np.float32)
    n_steps = int(T_s / DT)
    warm_steps = int(warmup_s / DT)
    sqrt_dt_sigma = sigma * np.sqrt(DT)

    sumR = np.zeros((C, N))
    sumR2 = np.zeros((C, N))
    msum = np.zeros((C, N), dtype=np.complex128)
    nT = 0
    acc = {"sum_var": np.zeros((C, N, len(dfa_wins))),
           "counts": np.zeros((C, N, len(dfa_wins)))}
    psd_acc = np.zeros((C, N, PSD_BLOCK // 2 + 1))
    psd_n = 0
    cc_acc = np.zeros((C, N, N))
    cc_n = 0
    Pbuf = np.zeros((C, N, dfa_chunk))     # profile buffer (float64)
    buf_fill = 0
    prof = np.zeros((C, N))                 # running integrated profile
    zb = np.empty((C, N, PSD_BLOCK), dtype=np.complex64)  # z block buffer
    zb_fill = 0
    CB = 8                                  # combo sub-batch for FFT/CC
    # Hann window for PSD blocks
    win = np.hanning(PSD_BLOCK).astype(np.float32)
    rfft_len = PSD_BLOCK // 2 + 1
    import scipy.fft as sp_fft

    t0 = time.time()
    for step in range(n_steps):
        E = np.exp(1j * phi)                     # complex64 (C,N,M)
        z = E.mean(axis=2)                       # (C,N)
        U = np.einsum("nj,cj->cn", W, z)
        cph, sph = E.real, E.imag
        dphi = omega[None] \
            + Kc[:, None, None] * (z.imag[:, :, None] * cph - z.real[:, :, None] * sph) \
            + Lc[:, None, None] * (sph * U.real[:, :, None] - cph * U.imag[:, :, None])
        noise = rng.standard_normal((C, N, M), dtype=np.float32)
        phi += dphi * DT
        phi += sqrt_dt_sigma * noise

        if step >= warm_steps and (step - warm_steps) % STRIDE == 0:
            R = np.abs(z).astype(np.float32)
            sumR += R
            sumR2 += R.astype(np.float64) ** 2
            msum += z.astype(np.complex128)
            nT += 1
            prof += R
            Pbuf[:, :, buf_fill] = prof
            buf_fill += 1
            if buf_fill == dfa_chunk:
                _block_dfa(Pbuf, acc, dfa_wins, dfa_chunk)
                buf_fill = 0
            zc = z.astype(np.complex64)
            zb[:, :, zb_fill] = zc
            zb_fill += 1
            if zb_fill == PSD_BLOCK:
                zb_fill = 0
                for c0 in range(0, C, CB):
                    c1 = min(c0 + CB, C)
                    blk = zb[c0:c1]                       # (cb,N,512) complex64
                    bR = np.abs(blk).astype(np.float64)
                    cent = bR - bR.mean(axis=2, keepdims=True)
                    cc_acc[c0:c1] += np.einsum("cnt,cmt->cnm", cent, cent)
                    # PSD of z: scipy fft preserves complex64 (memory-safe)
                    zf = sp_fft.fft(blk * win[None, None, :], axis=2)[..., :rfft_len]
                    psd_acc[c0:c1] += (np.abs(zf) ** 2).astype(np.float64)
                    del blk, bR, cent, zf
                cc_n += PSD_BLOCK
                psd_n += 1
        if progress_every and step % progress_every == 0 and step:
            el = time.time() - t0
            print(f"  step {step}/{n_steps} ({el:.0f}s, {el/step*1000:.1f} ms/step)",
                  flush=True)

    # flush partial DFA buffer
    if buf_fill > 0:
        _block_dfa(Pbuf[:, :, :buf_fill], acc, dfa_wins, dfa_chunk)
    dfa_exp = _dfa_from_acc(acc, dfa_wins)
    meanR = sumR / nT
    varR = np.maximum(sumR2 / nT - meanR ** 2, 1e-12)
    PLV = np.abs(msum[:, :, None] * np.conj(msum[:, None, :])) / nT
    cov = cc_acc / np.maximum(cc_n - 1, 1)
    CCm = cov / np.sqrt(np.maximum(np.einsum("cii->ci", cov)[:, :, None]
                                  * np.einsum("cii->ci", cov)[:, None, :], 1e-20))
    psd_mean = psd_acc.mean(axis=1) / max(psd_n, 1)      # (C, rfft_len)
    freqs = np.fft.rfftfreq(PSD_BLOCK, d=STRIDE * DT)  # 100 Hz
    return dict(K=np.asarray(Ks, float), L=np.asarray(Ls, float), sigma=sigma,
                mean_order=meanR, dfa=dfa_exp, mean_dfa=dfa_exp.mean(axis=1),
                frac065=(dfa_exp > 0.65).mean(axis=1),
                frac_p95=None,  # filled by caller with surrogate threshold
                mean_plv=PLV.reshape(C, -1).mean(axis=1),
                mean_cc=CCm.reshape(C, -1).mean(axis=1),
                psd=psd_mean, psd_freqs=freqs, nT=nT,
                plv_mat=PLV if want_matrices else None,
                cc_mat=CCm if want_matrices else None,
                cov_diag=np.einsum("cii->ci", cov))


def _block_dfa(Pbuf, acc, dfa_wins, dfa_chunk):
    """Pbuf: (C, N, chunk) float64 PROFILE samples (running cumsum of the
    signal, globally continuous). Accumulates per-window-size variances."""
    C, N, T = Pbuf.shape
    t = np.arange(dfa_chunk, dtype=np.float64)
    tm, d = t.mean(), t - t.mean()
    den = (d ** 2).sum()
    for iw, w in enumerate(dfa_wins):
        if w > T:
            continue
        nw = T // w
        seg = Pbuf[:, :, :nw * w].reshape(C, N, nw, w)
        tw = t[:w]
        tmw = tw.mean()
        dw = tw - tmw
        den_w = (dw ** 2).sum()
        mean = seg.mean(axis=3, keepdims=True)
        slope = ((seg - mean) * dw[None, None, None, :]).sum(axis=3) / den_w
        inter = mean[..., 0] - slope * tmw
        resid = seg - (inter[:, :, :, None] + slope[:, :, :, None] * tw[None, None, None, :])
        # per-window variance (mean over time), summed over windows
        acc["sum_var"][:, :, iw] += (resid ** 2).mean(axis=3).sum(axis=2)
        acc["counts"][:, :, iw] += nw


def _dfa_from_acc(acc, dfa_wins):
    sv, ct = acc["sum_var"], acc["counts"]
    F = np.sqrt(sv / np.maximum(ct, 1))
    ws = np.array(dfa_wins, dtype=np.float64)
    lx = np.log(ws)
    ly = np.log(np.maximum(F, 1e-12))
    x = lx - lx.mean()
    beta = (ly * x[None, None, :]).sum(-1) / (x ** 2).sum()
    return beta


def structure_function(W, res, ci):
    """Myrov Fig-3 criteria at combo index ci: correlations of node/edge
    observables with structural measures. Returns dict."""
    from scipy.stats import spearmanr
    s = W.sum(axis=1)
    iu = np.triu_indices(W.shape[0], 1)
    order = res["mean_order"][ci]
    dfa = res["dfa"][ci]
    plv = res["plv_mat"][ci] if res["plv_mat"] is not None else None
    cc = res["cc_mat"][ci] if res["cc_mat"] is not None else None
    out = {
        "order_strength_rho": float(spearmanr(order, s).statistic),
        "dfa_strength_rho": float(spearmanr(dfa, s).statistic),
    }
    if plv is not None:
        out["plv_edge_rho"] = float(spearmanr(plv[iu], W[iu]).statistic)
    if cc is not None:
        out["cc_edge_rho"] = float(spearmanr(cc[iu], W[iu]).statistic)
    return out


def main_calibrate():
    W_ext, W_sym, strength = load_sc(PRIMARY)
    rng = np.random.default_rng(7)
    omega = sample_omega(rng)
    print("per-node omega std (rad/s):", round(float(omega.std(axis=1).mean()), 1))
    Ks, Ls = np.meshgrid([5.0, 20.0, 35.0], [5.0, 20.0, 35.0])
    for sigma in [2.0, 5.0, 10.0, 20.0]:
        t0 = time.time()
        r = run_sim(W_ext, omega, Ks.ravel(), Ls.ravel(), sigma, T_s=30.0,
                    warmup_s=8.0, dfa_wins=DFA_WINS_CAL, dfa_chunk=DFA_CHUNK_CAL,
                    seed=1, progress_every=0)
        print(f"sigma={sigma}: mean_order={np.round(r['mean_order'].mean(1), 3)} "
              f"mean_dfa={np.round(r['mean_dfa'], 3)} "
              f"mean_plv={np.round(r['mean_plv'], 3)} ({time.time()-t0:.0f}s, "
              f"{(time.time()-t0) / (30 / DT) * 1000:.1f} ms/step)", flush=True)


GRID = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]  # rad/s
SIGMA_SWEEP = 3.0


def sf_surfaces(W_sym, res):
    """Structure-function correlation surfaces (Myrov Fig-3 criteria) for
    every combo. Uses per-combo PLV and CC matrices."""
    from scipy.stats import spearmanr
    s = W_sym.sum(axis=1).astype(np.float64)
    iu = np.triu_indices(W_sym.shape[0], 1)
    W_edge = W_sym[iu].astype(np.float64)
    C = len(res["K"])
    out = {k: np.zeros(C) for k in ["order_strength_rho", "dfa_strength_rho",
                                    "plv_edge_rho", "cc_edge_rho"]}
    for ci in range(C):
        out["order_strength_rho"][ci] = spearmanr(res["mean_order"][ci], s).statistic
        out["dfa_strength_rho"][ci] = spearmanr(res["dfa"][ci], s).statistic
        out["plv_edge_rho"][ci] = spearmanr(res["plv_mat"][ci][iu], W_edge).statistic
        out["cc_edge_rho"][ci] = spearmanr(res["cc_mat"][ci][iu], W_edge).statistic
    return out


def surrogate_thr():
    with open(f"{OUT}/meg_obs.json") as f:
        return json.load(f)["wn_dfa_p95"]


def all_combos():
    return [(k, l) for l in GRID for k in GRID]


def main_chunk(i):
    """Run grid chunk i (CHUNK combos) of the primary subject sweep."""
    W_ext, W_sym, strength = load_sc(PRIMARY)
    omega = sample_omega(np.random.default_rng(7))
    combos = all_combos()[CHUNK * int(i): CHUNK * (int(i) + 1)]
    if not combos:
        raise SystemExit(f"chunk {i} empty")
    Ks = np.array([c[0] for c in combos])
    Ls = np.array([c[1] for c in combos])
    print(f"chunk {i}: {len(Ks)} combos K={Ks} L={Ls}", flush=True)
    r = run_sim(W_ext, omega, Ks, Ls, SIGMA_SWEEP, T_s=T_SWEEP_S, warmup_s=WARMUP_S,
                seed=100 + int(i), want_matrices=True, progress_every=0)
    sf = sf_surfaces(W_sym, r)
    thr = surrogate_thr()
    np.savez_compressed(
        f"{OUT}/sweep_part{i:02d}.npz",
        K=r["K"], L=r["L"], sigma=r["sigma"],
        mean_order=r["mean_order"], dfa=r["dfa"],
        frac065=r["frac065"], frac_p95=(r["dfa"] > thr).mean(axis=1),
        mean_plv=r["mean_plv"], mean_cc=r["mean_cc"],
        psd=r["psd"], psd_freqs=r["psd_freqs"],
        plv_mat=r["plv_mat"].astype(np.float32),
        cc_mat=r["cc_mat"].astype(np.float32), **sf)
    print(f"saved sweep_part{i:02d}.npz", flush=True)


def main_slice(subject, k_star, l_star, sigma, part):
    """K-slice at L* and L-slice at K* for one subject, in two parts."""
    W_ext, W_sym, strength = load_sc(subject)
    omega = sample_omega(np.random.default_rng(11))
    k_star, l_star, sigma = float(k_star), float(l_star), float(sigma)
    combos = [(k, l_star) for k in GRID] + [(k_star, l) for l in GRID if l != l_star]
    part = int(part)
    combos = combos[CHUNK * part: CHUNK * (part + 1)]
    if not combos:
        raise SystemExit("slice part empty")
    Ks = np.array([c[0] for c in combos])
    Ls = np.array([c[1] for c in combos])
    print(f"slice {subject} part {part}: {len(Ks)} combos", flush=True)
    r = run_sim(W_ext, omega, Ks, Ls, sigma, T_s=T_SLICE_S, warmup_s=WARMUP_S,
                seed=200, want_matrices=True, progress_every=0)
    sf = sf_surfaces(W_sym, r)
    thr = surrogate_thr()
    np.savez_compressed(
        f"{OUT}/slice_{subject}_part{part}.npz",
        K=r["K"], L=r["L"], sigma=sigma,
        mean_order=r["mean_order"], dfa=r["dfa"],
        frac065=r["frac065"], frac_p95=(r["dfa"] > thr).mean(axis=1),
        mean_plv=r["mean_plv"], mean_cc=r["mean_cc"],
        psd=r["psd"], psd_freqs=r["psd_freqs"],
        plv_mat=r["plv_mat"].astype(np.float32),
        cc_mat=r["cc_mat"].astype(np.float32), **sf)
    print(f"saved slice_{subject}_part{part}.npz", flush=True)


def main_nulls(k_star, l_star, sigma):
    """Shuffled-SC and random-uniform-SC nulls at the operating point."""
    from scipy.stats import spearmanr
    W_ext, W_sym, strength = load_sc(PRIMARY)
    omega = sample_omega(np.random.default_rng(7))
    k_star, l_star, sigma = float(k_star), float(l_star), float(sigma)
    rng = np.random.default_rng(42)

    def run_case(W_ext_x, W_sym_x, label, seed):
        r = run_sim(W_ext_x, omega, np.array([k_star]), np.array([l_star]), sigma,
                    T_s=T_NULL_S, warmup_s=WARMUP_S, seed=seed,
                    want_matrices=True, progress_every=0)
        sf = sf_surfaces(W_sym_x, r)
        out = {k: float(v[0]) for k, v in sf.items()}
        out.update(order=float(r["mean_order"][0].mean()),
                   dfa=float(np.nanmean(r["dfa"][0])),
                   frac065=float(r["frac065"][0]))
        print(label, out, flush=True)
        return out

    # real SC reference (short run, same seeds as nulls for comparability)
    real = run_case(W_ext, W_sym, "real", 300)
    # shuffled labels
    perm = rng.permutation(W_sym.shape[0])
    W_sym_s = W_sym[np.ix_(perm, perm)]
    rs = W_sym_s.sum(axis=1, keepdims=True)
    W_ext_s = (W_sym_s / np.maximum(rs, 1e-12)).astype(np.float32)
    shuf = run_case(W_ext_s, W_sym_s, "shuffled", 300)
    # random uniform weights, same row normalization
    A = rng.random((94, 94))
    A = np.triu(A, 1)
    W_sym_r = (A + A.T).astype(np.float64)
    rr = W_sym_r.sum(axis=1, keepdims=True)
    W_ext_r = (W_sym_r / np.maximum(rr, 1e-12)).astype(np.float32)
    rand = run_case(W_ext_r.astype(np.float32), W_sym_r.astype(np.float32), "random", 300)

    # label-permutation test on the real-SC correlations (1000 perms)
    s = W_sym.sum(axis=1).astype(np.float64)
    perm_p = {}
    iu = np.triu_indices(94, 1)
    # find operating point combo in stored sweep parts
    res = {"order": None}
    for fp in sorted(glob.glob(f"{OUT}/sweep_part*.npz")):
        dd = np.load(fp)
        m = (np.isclose(dd["K"], k_star)) & (np.isclose(dd["L"], l_star))
        if m.any():
            res["order"] = dd["mean_order"][m][0]
            res["dfa"] = dd["dfa"][m][0]
            res["plv"] = dd["plv_mat"][m][0].astype(np.float64)
            res["cc"] = dd["cc_mat"][m][0].astype(np.float64)
            res["sigma"] = float(dd["sigma"])
    prng = np.random.default_rng(5150)
    nperm = 1000
    for key, obs, meas in [("order", res["order"], s),
                           ("dfa", res["dfa"], s),
                           ("plv", res["plv"][iu], W_sym[iu].astype(np.float64)),
                           ("cc", res["cc"][iu], W_sym[iu].astype(np.float64))]:
        rho0 = spearmanr(obs, meas).statistic
        cnt = 0
        for _ in range(nperm):
            p = prng.permutation(len(obs))
            if abs(spearmanr(obs[p], meas).statistic) >= abs(rho0):
                cnt += 1
        perm_p[f"{key}_perm_p"] = cnt / nperm
        print(f"perm test {key}: rho={rho0:.3f} p={cnt/nperm:.3f}", flush=True)
    out = {"real": real, "shuffled": shuf, "random": rand, **perm_p,
           "K_star": k_star, "L_star": l_star, "sigma": sigma}
    with open(f"{OUT}/nulls.json", "w") as f:
        json.dump(out, f, indent=1)
    print("saved nulls.json", flush=True)


SIGMA_GRID = [0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0]


def main_sigmasweep(k_star, l_star):
    """Noise sweep at the operating point: fits sigma so the model's DFA
    distribution matches the MEG sensor DFA distribution (median)."""
    W_ext, W_sym, strength = load_sc(PRIMARY)
    omega = sample_omega(np.random.default_rng(7))
    k_star, l_star = float(k_star), float(l_star)
    out = {"K_star": k_star, "L_star": l_star, "sigma_grid": SIGMA_GRID,
           "dfa_median": [], "dfa_mean": [], "frac065": [], "mean_order": [],
           "psd": [], "psd_freqs": None}
    for sigma in SIGMA_GRID:
        r = run_sim(W_ext, omega, np.array([k_star]), np.array([l_star]), sigma,
                    T_s=T_SWEEP_S, warmup_s=WARMUP_S, seed=400,
                    want_matrices=False, progress_every=0)
        out["dfa_median"].append(float(np.nanmedian(r["dfa"][0])))
        out["dfa_mean"].append(float(np.nanmean(r["dfa"][0])))
        out["frac065"].append(float(r["frac065"][0]))
        out["mean_order"].append(float(r["mean_order"][0].mean()))
        out["psd"].append(r["psd"][0].tolist())
        out["psd_freqs"] = r["psd_freqs"].tolist()
        print(f"sigma={sigma}: dfa_med={out['dfa_median'][-1]:.3f} "
              f"frac065={out['frac065'][-1]:.3f} order={out['mean_order'][-1]:.3f}",
              flush=True)
    with open(f"{OUT}/sigmasweep.json", "w") as f:
        json.dump(out, f, indent=1)
    print("saved sigmasweep.json", flush=True)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "calibrate"
    if mode == "calibrate":
        main_calibrate()
    elif mode == "chunk":
        main_chunk(int(sys.argv[2]))
    elif mode == "slice":
        main_slice(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif mode == "nulls":
        main_nulls(sys.argv[2], sys.argv[3], sys.argv[4])
    elif mode == "sigmasweep":
        main_sigmasweep(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit(f"unknown mode {mode}")
