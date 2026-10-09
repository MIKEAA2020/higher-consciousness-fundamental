#!/usr/bin/env python3
"""Phase 2 supplementary — the user-supplied evoked EEG file (210_31_EVKD_312Hz.mat).

Recovered array Y (60 ch, 251 samples, ~285 complete trials of 293) at 312.5 Hz.
Computes: per-trial per-channel LZ (waveform mean-threshold + Hilbert-envelope
variants, Farnes-instrument normalization), grand-average ERP morphology, and
reports the evoked-LZ reference point (single condition; no placebo contrast
possible from this file).
"""
import numpy as np
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
from phase2_ds4541_epochs import lzw_count

FS = 312.5
Y = np.load("/home/z/my-project/glm agent 2/research/phase2/eeg/Y_partial.npy")
n_full = len(Y) // (60 * 251)
print("recovered doubles:", len(Y), "-> full trials:", n_full, "of 293")
X = Y[:n_full * 60 * 251].reshape(n_full, 60, 251)   # (trials, ch, time) column-major
X = np.transpose(X, (1, 0, 2))                       # (ch, trials, time)
print("X:", X.shape, "range:", X.min(), X.max())

rng = np.random.default_rng(7)

def lz_norm(b, n_sh=5):
    c = lzw_count(b)
    Ls = [lzw_count(rng.permutation(b)) for _ in range(n_sh)]
    return c / max(np.mean(Ls), 1.0)

# 1) per-trial waveform LZ (mean threshold), all 60 channels, cap at 120 trials
ntr = min(n_full, 120)
lz_wave = []
for t in range(ntr):
    for c in range(0, 60, 3):                        # every 3rd channel for speed
        b = (X[c, t] > X[c, t].mean()).astype(np.uint8)
        lz_wave.append(lz_norm(b, 3))
lz_wave = np.array(lz_wave)
print("waveform LZ: median %.3f IQR [%.3f, %.3f]" % (np.median(lz_wave),
      np.percentile(lz_wave, 25), np.percentile(lz_wave, 75)))

# 2) per-trial Hilbert-envelope LZ (the Farnes spontaneous instrument applied to evoked)
from scipy.signal import hilbert
lz_env = []
for t in range(0, ntr, 2):
    for c in range(0, 60, 3):
        amp = np.abs(hilbert(X[c, t]))
        b = (amp > amp.mean()).astype(np.uint8)
        lz_env.append(lz_norm(b, 3))
lz_env = np.array(lz_env)
print("envelope LZ: median %.3f IQR [%.3f, %.3f]" % (np.median(lz_env),
      np.percentile(lz_env, 25), np.percentile(lz_env, 75)))

# 3) grand-average ERP
erp = X.mean(axis=1)                                  # (ch, time)
t = np.arange(251) / FS
gm = erp.mean(axis=0)
peak_i = int(np.abs(gm).argmax())
print("grand-mean ERP: peak %.1f uV at %.0f ms (t=0 = epoch start)" %
      (gm[peak_i], 1000 * t[peak_i]))
# per-channel peak latency distribution
peaks = [1000 * t[int(np.abs(erp[c]).argmax())] for c in range(60)]
print("per-channel peak latency: median %.0f ms, IQR [%.0f, %.0f]" %
      (np.median(peaks), np.percentile(peaks, 25), np.percentile(peaks, 75)))

# 4) response-locked power: mean spectrum across trials (Welch on zero-padded trials)
from scipy.signal import welch
f, P = welch(X[:, :ntr], fs=FS, nperseg=128, axis=2)
Pm = P.mean(axis=(0, 1))
m = (f >= 2) & (f <= 40)
top = f[m][np.argsort(Pm[m])[-5:][::-1]]
print("evoked power peaks (Hz):", [round(float(x), 1) for x in top])

np.savez("/home/z/my-project/glm agent 2/research/phase2/eeg/farnes_evoked_obs.npz",
         lz_wave_median=np.median(lz_wave), lz_wave_q25=np.percentile(lz_wave, 25),
         lz_wave_q75=np.percentile(lz_wave, 75), lz_env_median=np.median(lz_env),
         erp=erp.astype(np.float32), gm=gm.astype(np.float32),
         n_trials=ntr)
print("saved farnes_evoked_obs.npz")
