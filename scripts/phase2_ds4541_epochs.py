#!/usr/bin/env python3
"""Phase 2 — ds004541 anesthesia EEG: epoch extraction + observables.

Per session, epochs from events.tsv:
  pre         [baseline+5 .. start-5]      awake baseline
  maintenance [max(loc,start)+45 .. end-45]  deep GA
  emergence   [end+30 .. roc-30]           transition
  recovery    [roc+30 .. roc+270]          awake again
Range-requested from the S3 EDF; parsed (field-contiguous header);
good EEG channels only; avg reference; 1-45 Hz bandpass; decimate to 250 Hz.

Observables per epoch: Welch PSD grand mean; FOOOF peaks (alpha CF);
per-channel block-DFA of the alpha-band Hilbert envelope (1-30 s);
per-channel normalized Lempel-Ziv complexity (LZc, Schartner-style
median-binarization, normalized by 5 circular shuffles).

CLI: python3 phase2_ds4541_epochs.py SESSIONS_PER_CALL_INDEX
"""
import json
import os
import sys
import subprocess
sys.path.insert(0, "/home/z/my-project/scripts")
import numpy as np

OUT = "/home/z/my-project/glm agent 2/research/phase2/ds004541"
BASE = "https://s3.amazonaws.com/openneuro.org/ds004541"
FS_T = 250.0

SESSIONS = [
    "sub-02/ses-01", "sub-03/ses-01", "sub-04/ses-01", "sub-07/ses-01",
    "sub-08/ses-01", "sub-09/ses-01", "sub-10/ses-01", "sub-11/ses-01",
    "sub-11/ses-02",
]


def curl(url, dest, rng=None, timeout=300):
    cmd = ["curl", "-sS", "-L", "-m", str(timeout)]
    if rng:
        cmd += ["-r", rng]
    cmd += ["-o", dest, "-w", "%{http_code} %{size_download}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 30)
    return r.stdout


def parse_edf_header(path):
    raw = open(path, "rb").read()
    n_rec = int(raw[236:244].decode().strip())
    rec_dur = float(raw[244:252].decode().strip())
    n_sig = int(raw[252:256].decode().strip())
    hdr_bytes = 256 + n_sig * 256
    a = 256
    lab = [raw[a + i * 16:a + (i + 1) * 16].decode().strip() for i in range(n_sig)]
    a += n_sig * 16
    a += n_sig * 80                     # transducers (skipped)
    a += n_sig * 8                      # phys dims (skipped)
    pmin = [float(raw[a + i * 8:a + (i + 1) * 8].decode().strip()) for i in range(n_sig)]
    a += n_sig * 8
    pmax = [float(raw[a + i * 8:a + (i + 1) * 8].decode().strip()) for i in range(n_sig)]
    a += n_sig * 8
    dmin = [float(raw[a + i * 8:a + (i + 1) * 8].decode().strip()) for i in range(n_sig)]
    a += n_sig * 8
    dmax = [float(raw[a + i * 8:a + (i + 1) * 8].decode().strip()) for i in range(n_sig)]
    a += n_sig * 8
    a += n_sig * 80                     # prefilters (skipped)
    sprs = [int(raw[a + i * 8:a + (i + 1) * 8].decode().strip()) for i in range(n_sig)]
    recbytes = sum(sprs) * 2
    return dict(hdr_bytes=hdr_bytes, n_rec=n_rec, rec_dur=rec_dur, n_sig=n_sig,
                labels=lab, sprs=sprs, pmin=pmin, pmax=pmax, dmin=dmin,
                dmax=dmax, recbytes=recbytes)


def read_events(sess):
    p = f"{OUT}/{sess.replace('/', '_')}_events.tsv"
    ev = {}
    with open(p) as f:
        next(f)
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 3:
                ev[parts[2]] = float(parts[0])
    return ev


def channel_types(sess):
    chf = f"{OUT}/{sess.replace('/', '_')}_channels.tsv"
    if not os.path.exists(chf):
        p = f"{sess}/eeg/{sess.replace('/', '_')}_task-anesthesia_channels.tsv"
        curl(f"{BASE}/{p}", chf)
    types, status = {}, {}
    with open(chf) as f:
        next(f)
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 8:
                types[parts[0].lstrip('\ufeff')] = parts[1]
                status[parts[0].lstrip('\ufeff')] = parts[7]
    return types, status


def fetch_epoch(sess, hdr, t0, t1):
    """Returns (names, data_uV (nch, nsamp), fs, t_actual0)"""
    p = f"{sess}/eeg/{sess.replace('/', '_')}_task-anesthesia_eeg.edf"
    r0 = int(np.floor(t0 / hdr["rec_dur"]))
    r1 = min(int(np.ceil(t1 / hdr["rec_dur"])), hdr["n_rec"])
    if r1 - r0 < 300:      # < 120 s at 0.4 s records
        return None
    b0 = hdr["hdr_bytes"] + r0 * hdr["recbytes"]
    b1 = hdr["hdr_bytes"] + r1 * hdr["recbytes"] - 1
    tmp = "/tmp/edf_chunk.bin"
    curl(f"{BASE}/{p}", tmp, rng=f"{b0}-{b1}", timeout=280)
    raw = np.fromfile(tmp, dtype="<i2")
    nrec = r1 - r0
    raw = raw[:nrec * hdr["recbytes"] // 2].reshape(nrec, -1)
    spr_max = max(hdr["sprs"])
    offs = np.cumsum([0] + hdr["sprs"])
    names, cols = [], []
    for i, lab in enumerate(hdr["labels"]):
        if lab in ("EDF Annotations", "Trigger", "EKG", "EMG", "ECG"):
            continue
        if hdr["sprs"][i] != spr_max:
            continue
        x = raw[:, offs[i]:offs[i + 1]].astype(np.float64)
        span = hdr["pmax"][i] - hdr["pmin"][i]
        dig = hdr["dmax"][i] - hdr["dmin"][i]
        x = hdr["pmin"][i] + (x - hdr["dmin"][i]) * span / max(dig, 1)
        names.append(lab)
        cols.append(x.T.reshape(-1))
    data = np.stack(cols)
    fs = spr_max / hdr["rec_dur"]
    return names, data, fs, r0 * hdr["rec_dur"]


def preprocess(names, data, types, status):
    """Data-driven QC (the dataset's channels.tsv status markings proved
    unreliable: channels marked good include huge-amplitude artifact
    channels; channels marked bad include clean ones). QC: drop non-EEG
    types; bandpass+decimate; drop channels whose robust std is outside
    [1/4, 4]x the channel-median std or whose kurtosis exceeds 30."""
    from scipy.signal import resample_poly, butter, sosfiltfilt
    cand = [i for i, n in enumerate(names) if types.get(n, "EEG") == "EEG"]
    X = data[cand]
    sos = butter(4, [1.0, 45.0], btype="band", fs=1000.0, output="sos")
    Xf = sosfiltfilt(sos, X, axis=1)
    Xd = resample_poly(Xf, 1, 4, axis=1)
    # robust scale QC: surgical EEG has a bimodal channel-amplitude
    # distribution (clean low-amplitude cluster + huge-artifact cluster).
    # 2-cluster k-means on log10(std); keep the LOW cluster; drop spiky.
    ls = np.log10(np.maximum(Xd.std(axis=1), 1e-9))
    order = np.argsort(ls)
    lss = ls[order]
    # largest gap split (1-D two-means equivalent)
    gaps = np.diff(lss)
    gi = int(np.argmax(gaps)) if len(gaps) else 0
    if len(gaps) and gaps[gi] > 0.4:      # meaningful bimodality only
        thr = (lss[gi] + lss[gi + 1]) / 2
        low = ls <= thr
    else:
        low = np.ones(len(ls), bool)
    kurt = ((Xd - Xd.mean(axis=1, keepdims=True)) ** 4).mean(axis=1) / (Xd.var(axis=1) ** 2 + 1e-12)
    ok = low & (kurt < 30) & (Xd.std(axis=1) > 0)
    if ok.sum() < 12:                      # fall back: bottom-half amplitude
        ok = ls <= np.median(ls)
    keep = [i for i, o in zip(cand, ok) if o]
    Xd = Xd[ok]
    Xd = Xd - Xd.mean(axis=0, keepdims=True)       # avg reference over QC-passing
    return [names[i] for i in keep], Xd


# ---------------- observables ----------------

def block_dfa(x, fs, wins=(1, 2, 4, 8, 16, 30)):
    """Block DFA of a 1-D envelope series; returns exponent or nan."""
    n = len(x)
    sizes = [int(w * fs) for w in wins if int(w * fs) < n // 4]
    if len(sizes) < 3:
        return np.nan
    F = []
    for s in sorted(set(sizes)):
        nb = n // s
        seg = x[:nb * s].reshape(nb, s)
        # cumulative profile per segment, linear detrend
        t = np.arange(s)
        prof = np.cumsum(seg - seg.mean(axis=1, keepdims=True), axis=1)
        # detrend via polyfit per segment (vectorized)
        A = np.stack([np.ones(s), t], axis=1)
        coef, *_ = np.linalg.lstsq(A, prof.T, rcond=None)
        resid = prof.T - A @ coef
        F.append(np.sqrt((resid ** 2).sum(axis=1).mean() / s))
    F = np.array(F)
    szs = np.array(sorted(set(sizes)))
    ok = np.isfinite(np.log(F))
    if ok.sum() < 3:
        return np.nan
    sl = np.polyfit(np.log(szs[ok]), np.log(F[ok]), 1)[0]
    return float(sl)


def alpha_dfa(X, fs, peak_cf):
    """DFA of the peak-band Hilbert envelope per channel, matching Phase-1
    MEG exactly (raw envelope decimated to 50 Hz, phase1_meg.dfa)."""
    from scipy.signal import hilbert, butter, sosfiltfilt
    from phase1_meg import dfa as p1_dfa
    lo, hi = max(peak_cf - 2.0, 2.0), min(peak_cf + 2.0, 40.0)
    sos = butter(4, [lo, hi], btype="band", fs=fs, output="sos")
    env = np.abs(hilbert(sosfiltfilt(sos, X, axis=1), axis=1))
    dec = int(fs / 50)
    env50 = env[:, ::dec]
    return np.array([p1_dfa(env50[i], 50.0) for i in range(env50.shape[0])])


def lzw_count(b):
    """Port of the Farnes/Reynante lzw.m: LZW dictionary word count of a
    binary sequence (dictionary pre-seeded with '0','1')."""
    d = {"0", "1"}
    sub = str(int(b[0]))
    n = len(b)
    e = 1
    while e < n:
        sub += str(int(b[e]))
        if sub not in d:
            d.add(sub)
            sub = str(int(b[e]))
        e += 1
    return len(d)


def lz_norm_binary(b, n_shuffle=5, rng=None):
    """Port of lzwNormalised.m: LZW count normalized by the mean count of
    shuffled versions. (Their code used nr_shuffles=1; 5 used here for
    stability -- documented deviation.)"""
    rng = rng or np.random.default_rng(0)
    c = lzw_count(b)
    Ls = [lzw_count(rng.permutation(b)) for _ in range(n_shuffle)]
    return c / max(np.mean(Ls), 1.0)


def lz_epoch_channels(X, fs, epoch_s=8.0, n_shuffle=5):
    """Farnes-Reynante LZs: Hilbert amplitude, mean-binarize per channel,
    LZW per 8-s epoch, shuffle-normalized; returns (LZs_median, LZc_median).
    LZc: channels' binary sequences concatenated per epoch (Schartner-style),
    same normalization."""
    from scipy.signal import hilbert
    rng = np.random.default_rng(42)
    n_ep = int(epoch_s * fs)
    neps = X.shape[1] // n_ep
    if neps < 1:
        return np.nan, np.nan
    amp = np.abs(hilbert(X[:, :neps * n_ep], axis=1))
    bin_ = amp > amp.mean(axis=1, keepdims=True)
    lzs = []
    for i in range(bin_.shape[0]):
        for j in range(neps):
            lzs.append(lz_norm_binary(bin_[i, j * n_ep:(j + 1) * n_ep].astype(np.uint8),
                                      n_shuffle, rng))
    lzc = []
    for j in range(neps):
        cat = np.concatenate([bin_[i, j * n_ep:(j + 1) * n_ep]
                              for i in range(bin_.shape[0])]).astype(np.uint8)
        lzc.append(lz_norm_binary(cat, n_shuffle, rng))
    return float(np.nanmedian(lzs)), float(np.nanmedian(lzc))


def epoch_observables(X, fs):
    from scipy.signal import welch
    f, P = welch(X, fs=fs, nperseg=int(4 * fs), noverlap=int(2 * fs), axis=1)
    Pm = P.mean(axis=0)
    res = {"psd_freqs": f.tolist(), "psd": Pm.tolist()}
    # FOOOF on 3-30
    try:
        from fooof import FOOOF
        m = (f >= 3) & (f <= 30)
        fm = FOOOF(peak_width_limits=[0.5, 12.0], max_n_peaks=8,
                   min_peak_height=0.05, verbose=False)
        fm.fit(f[m], Pm[m])
        peaks = sorted(zip(fm.peak_params_[:, 1], fm.peak_params_[:, 0]),
                       key=lambda t: -t[0]) if hasattr(fm, "peak_params_") else []
        alpha = [cf for pw, cf in [(p[1], p[0]) for p in fm.peak_params_]
                 if 7 <= cf <= 13]
        res["alpha_cf"] = float(max(alpha, key=lambda c: 0)) if alpha else None
        res["peaks"] = fm.peak_params_.tolist()
        res["offset"], res["exponent"] = float(fm.aperiodic_params_[0]), float(fm.aperiodic_params_[1])
    except Exception as e:
        res["alpha_cf"] = None
        res["fooof_err"] = str(e)[:120]
    # band powers
    def bp(lo, hi):
        m = (f >= lo) & (f <= hi)
        return float(Pm[m].sum())
    res["pow_delta"] = bp(1, 4); res["pow_theta"] = bp(4, 8)
    res["pow_alpha"] = bp(8, 13); res["pow_beta"] = bp(13, 30)
    # DFA at alpha band (or 8-12 if no peak)
    cf = res.get("alpha_cf") or 10.0
    dfa = alpha_dfa(X, fs, cf)
    res["dfa_ch"] = [float(v) for v in dfa]
    res["dfa_median"] = float(np.nanmedian(dfa))
    res["dfa_frac065"] = float(np.mean(dfa > 0.65))
    # broadband (1-30 Hz) envelope DFA -- robust secondary when alpha weak
    from scipy.signal import butter, sosfiltfilt, hilbert
    from phase1_meg import dfa as p1_dfa
    sos_bb = butter(4, [1.0, 30.0], btype="band", fs=fs, output="sos")
    envbb = np.abs(hilbert(sosfiltfilt(sos_bb, X, axis=1), axis=1))
    dec = int(fs / 50)
    dfabb = [p1_dfa(envbb[i, ::dec], 50.0) for i in range(envbb.shape[0])]
    res["dfa_bb_median"] = float(np.nanmedian(dfabb))
    res["dfa_bb_ch"] = [float(v) for v in dfabb]
    # LZ: Farnes-Reynante LZs (per-channel) + LZc (concatenated)
    lzs, lzc = lz_epoch_channels(X, fs)
    res["lzs_median"] = lzs
    res["lzc_median"] = lzc
    return res


def epochs_for(sess, ev, dur):
    CAP = 600.0     # cap fetched duration (bandwidth + processing)

    def cap(t0, t1):
        return (t0, min(t1, t0 + CAP))
    out = {}
    pre0 = ev.get("baseline", 0.0) + 5
    pre1 = ev.get("start", 120.0) - 5
    out["pre"] = cap(pre0, pre1)
    loc = ev.get("loc"); start = ev.get("start", 0.0)
    m0 = (max(loc, start) if loc else start) + 45
    m1 = ev.get("end", dur - 60) - 45
    out["maintenance"] = cap(m0, m1)
    e0 = ev.get("end", dur - 60) + 30
    e1 = ev.get("roc", dur) - 30
    out["emergence"] = cap(e0, e1)
    r0 = ev.get("roc", dur) + 30
    out["recovery"] = cap(r0, min(r0 + 240, dur - 5))
    return out


def main(part):
    sessions = SESSIONS[3 * part:3 * part + 3]
    results = {}
    for sess in sessions:
        sid = sess.replace("/", "_")
        ev = read_events(sess)
        hdr = parse_edf_header(f"{OUT}/{sid}_edfheader.bin")
        dur = hdr["n_rec"] * hdr["rec_dur"]
        types, status = channel_types(sess)
        eps = epochs_for(sess, ev, dur)
        results[sid] = {"events": ev, "duration": dur, "epochs": {}}
        for name, (t0, t1) in eps.items():
            if t1 - t0 < 120:
                results[sid]["epochs"][name] = {"skipped": f"only {t1-t0:.0f}s"}
                continue
            got = fetch_epoch(sess, hdr, t0, t1)
            if got is None:
                results[sid]["epochs"][name] = {"skipped": "fetch fail"}
                continue
            names, data, fs, ta = got
            names2, X = preprocess(names, data, types, status)
            if X.shape[0] < 16 or X.shape[1] < int(120 * FS_T):
                results[sid]["epochs"][name] = {"skipped": f"ch={X.shape[0]} n={X.shape[1]}"}
                continue
            obs = epoch_observables(X, FS_T)
            obs["t0_actual"] = ta; obs["dur"] = float(t1 - t0)
            obs["nch"] = int(X.shape[0])
            results[sid]["epochs"][name] = obs
            print(f"{sid} {name}: {t1-t0:.0f}s dfa_med={obs['dfa_median']:.3f} "
                  f"alpha={obs.get('alpha_cf')} lzs={obs['lzs_median']:.3f} lzc={obs['lzc_median']:.3f} "
                  f"beta/alpha={obs['pow_beta']/max(obs['pow_alpha'],1e-12):.2f}", flush=True)
        with open(f"{OUT}/obs_part{part}.json", "w") as f:
            json.dump(results, f, indent=1)
    print("saved obs_part%d.json" % part)


if __name__ == "__main__":
    main(int(__import__("sys").argv[1]))
