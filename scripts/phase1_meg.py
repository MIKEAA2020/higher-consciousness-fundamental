#!/usr/bin/env python3
"""Phase 1 (Level-2 protocol) — MEG observables from open resting-state data.

Dataset: Brainstorm bst_resting (subj002), eyes-closed resting MEG,
2 x 600 s runs, 272 CTF magnetometers, 2400 Hz.
Sensor-space instantiation (documented deviation from Myrov et al.'s
source-parcel space: no openly available individual dMRI<->MEG pairing).

Memory-safe design (3 GB machine): 4-channel chunks read from disk,
in-place filtering, per-chunk Welch accumulation, envelope/phase stored
at 50 Hz (float32).

Outputs (research/phase1/meg_obs.npz + meg_obs.json):
  - grand-mean PSD per run (0.5-45 Hz, Welch, Hann 4 s / 2 s)
  - FOOOF aperiodic + periodic PSD (3-30 Hz), alpha peak frequency
  - per-channel DFA of the narrowband (peak+-2 Hz) amplitude envelope
  - wPLI matrix (alpha band), mean value
  - envelope cross-correlation matrix (alpha band), CC-vs-distance stat
  - white-noise DFA surrogate threshold (95th pct, Myrov's rule input)
"""
import json
import numpy as np
import mne
from scipy.signal import welch, hilbert
from scipy.stats import spearmanr

mne.set_log_level("ERROR")
BASE = "/home/z/mne_data/MNE-brainstorm-data/bst_resting/MEG/bst_resting"
OUT = "/home/z/my-project/glm agent 2/research/phase1"
RUNS = ["subj002_spontaneous_20111102_01_AUX.ds",
        "subj002_spontaneous_20111102_02_AUX.ds"]


def dfa(x, fs, win_s=(1.0, 30.0)):
    """DFA exponent of 1-D series; windows 1-30 s, robust log-log fit."""
    x = np.asarray(x, dtype=np.float64)
    n = len(x)
    y = np.cumsum(x - x.mean())
    sizes = np.unique(np.round(np.geomspace(win_s[0] * fs, min(win_s[1] * fs, n / 4))).astype(int))
    F = []
    ws = []
    for w in sizes:
        nseg = n // w
        if nseg < 2:
            continue
        seg = y[:nseg * w].reshape(nseg, w)
        t = np.arange(w)
        tm = t.mean()
        d = (t - tm)
        den = (d ** 2).sum()
        slope = ((seg - seg.mean(axis=1, keepdims=True)) * d).sum(axis=1) / den
        inter = seg.mean(axis=1) - slope * tm
        resid = seg - (inter[:, None] + slope[:, None] * t[None, :])
        F.append(np.sqrt((resid ** 2).mean()))
        ws.append(w)
    F, ws = np.array(F), np.array(ws)
    lx, ly = np.log(ws), np.log(F)
    keep = np.ones(len(F), bool)
    for _ in range(3):
        if keep.sum() < 3:
            break
        c = np.polyfit(lx[keep], ly[keep], 1)
        r = ly - np.polyval(c, lx)
        s = 1.4826 * np.median(np.abs(r[keep] - np.median(r[keep])))
        keep = np.abs(r - np.median(r[keep])) <= max(2.5 * s, 1e-12)
    return float(np.polyfit(lx[keep], ly[keep], 1)[0])


def wpli_from_phase(phase):
    n_ch, n_t = phase.shape
    num = np.zeros((n_ch, n_ch))
    den = np.zeros((n_ch, n_ch))
    B = 2000
    for i0 in range(0, n_t, B):
        p = phase[:, i0:i0 + B]
        s, c = np.sin(p), np.cos(p)
        D = s @ c.T - c @ s.T  # sin(phi_i - phi_j)
        num += D
        den += np.abs(D)
    return np.where(den > 0, np.abs(num) / np.maximum(den, 1e-12), 0.0)


def process_run(fname, ri):
    raw = mne.io.read_raw_ctf(f"{BASE}/{fname}", preload=False, verbose="ERROR")
    raw.pick("mag")
    sf = raw.info["sfreq"]  # 2400
    ch_names = list(raw.ch_names)
    n_ch = len(ch_names)
    pos = np.array([ch["loc"][:3] for ch in raw.info["chs"]])
    n_t = raw.n_times

    # First pass on ONE chunk to get the alpha peak we will narrowband later:
    # -> use a broad provisional alpha peak = run-1's value or default 10 Hz,
    #    refined after the full PSD pass. Two-pass: pass A = PSD; pass B = narrowband.
    # PASS A: Welch accumulation over channel chunks.
    seg = int(4 * sf)
    psd_sum = None
    freqs = None
    nper = int(4 * sf)
    for a in range(0, n_ch, 8):
        b = min(a + 8, n_ch)
        x = raw.get_data(picks=range(a, b))  # (k, n_t) float64 from disk
        x = mne.filter.filter_data(x, sf, 1.0, 45.0, verbose="ERROR")
        f, p = welch(x, fs=sf, nperseg=nper, noverlap=nper // 2, axis=1)
        psd_sum = p.sum(axis=0) if psd_sum is None else psd_sum + p.sum(axis=0)
        freqs = f
        del x, p
    msk = (freqs >= 0.5) & (freqs <= 45)
    gpsd = psd_sum / n_ch

    # FOOOF on 3-30 Hz
    from fooof import FOOOF
    fm = FOOOF(peak_width_limits=[0.5, 12.0], max_n_peaks=8, min_peak_height=0.05, verbose=False)
    sel = (freqs >= 3) & (freqs <= 30)
    fm.fit(freqs[sel], gpsd[sel])
    ap, per = fm._ap_fit, np.maximum(gpsd[sel] - fm._ap_fit, 0.0)
    peaks = fm.peak_params_
    alpha = [p for p in peaks if 6 <= p[0] <= 14]
    pk = max(alpha, key=lambda p: p[1]) if alpha else (
        peaks[np.argmax(peaks[:, 1])] if len(peaks) else np.array([10.0, 0.0, 2.0]))
    f_peak = float(pk[0])

    # PASS B: narrowband (f_peak +- 2 Hz) envelope + phase at 50 Hz, per 4-ch chunk
    lo, hi = max(1.5, f_peak - 2.0), f_peak + 2.0
    dec = int(sf / 50)  # 48
    env50 = np.zeros((n_ch, n_t // dec), dtype=np.float32)
    ph50 = np.zeros((n_ch, n_t // dec), dtype=np.float32)
    for a in range(0, n_ch, 4):
        b = min(a + 4, n_ch)
        x = raw.get_data(picks=range(a, b))
        x = mne.filter.filter_data(x, sf, 1.0, 45.0, verbose="ERROR")
        x = mne.filter.filter_data(x, sf, lo, hi, verbose="ERROR")
        z = hilbert(x, axis=1)
        env50[a:b] = np.abs(z)[:, ::dec].astype(np.float32)
        ph50[a:b] = np.angle(z)[:, ::dec].astype(np.float32)
        del x, z

    # DFA per channel (envelope at 50 Hz)
    dfa_ch = np.array([dfa(env50[c], 50.0) for c in range(n_ch)])

    # wPLI + CC
    w = wpli_from_phase(ph50.astype(np.float64))
    off = ~np.eye(n_ch, dtype=bool)
    ez = (env50 - env50.mean(axis=1, keepdims=True)) / (env50.std(axis=1, keepdims=True) + 1e-12)
    cc = (ez @ ez.T) / ez.shape[1]
    d = np.sqrt(((pos[:, None, :] - pos[None, :, :]) ** 2).sum(-1))

    res = {
        f"alpha_peak_hz": round(f_peak, 2),
        f"n_peaks_3_30": int(len(peaks)),
        f"peaks_cf_hz": [round(float(p[0]), 2) for p in peaks],
        f"dfa_median": round(float(np.nanmedian(dfa_ch)), 3),
        f"dfa_mean": round(float(np.nanmean(dfa_ch)), 3),
        f"dfa_pct_gt_065": round(float(np.nanmean(dfa_ch > 0.65)), 3),
        f"wpli_mean": round(float(w[off].mean()), 3),
        f"cc_mean": round(float(cc[off].mean()), 3),
        f"cc_vs_dist_rho": round(float(spearmanr(d[off], cc[off]).statistic), 3),
        f"n_ch": n_ch, f"n_t_50hz": int(env50.shape[1]),
    }
    store = {
        "freqs": freqs[msk], "psd_mean": gpsd[msk],
        "fooof_freqs": freqs[sel], "fooof_aperiodic": ap, "fooof_periodic": per,
        "dfa_ch": dfa_ch, "wpli": w.astype(np.float32), "cc": cc.astype(np.float32),
        "sensor_pos": pos, "env50_mean": env50.mean(axis=1),
    }
    return res, store


def main():
    all_res, all_store = {}, {}
    for ri, fname in enumerate(RUNS, 1):
        res, store = process_run(fname, ri)
        all_res[f"run{ri}"] = res
        for k, v in store.items():
            all_store[f"run{ri}_{k}"] = v
        print(f"run{ri}:", {k: v for k, v in res.items() if k != 'peaks_cf_hz'})

    # white-noise DFA surrogate threshold (Myrov's critical-regime rule)
    rng = np.random.default_rng(1234)
    L = all_store["run1_env50_mean"].shape[0] and 30000
    thr = np.array([dfa(rng.standard_normal(L), 50.0) for _ in range(300)])
    all_res["wn_dfa_p95"] = round(float(np.nanpercentile(thr, 95)), 3)
    all_res["wn_dfa_median"] = round(float(np.nanmedian(thr)), 3)
    all_res["analysis"] = dict(
        dataset="Brainstorm bst_resting subj002, eyes-closed rest, 2x600 s, 272 CTF mags",
        pipeline="1-45 Hz FIR (chunked, in place); Welch 4 s Hann 50% ov; "
                 "narrowband peak+-2 Hz Hilbert; envelope/phase at 50 Hz",
        dfa="windows 1-30 s (~10 geom sizes), robust log-log fit",
    )
    np.savez_compressed(f"{OUT}/meg_obs.npz", **all_store)
    with open(f"{OUT}/meg_obs.json", "w") as f:
        json.dump(all_res, f, indent=1)
    print("surrogate DFA p95:", all_res["wn_dfa_p95"], "| median:", all_res["wn_dfa_median"])
    print("saved:", f"{OUT}/meg_obs.npz")


if __name__ == "__main__":
    main()
