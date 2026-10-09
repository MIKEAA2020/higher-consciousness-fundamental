#!/usr/bin/env python3
"""Inspect the user-supplied EEG release asset 210_31_EVKD_312Hz.mat"""
import numpy as np
import scipy.io as sio
import json

F = "/home/z/my-project/glm agent 2/research/phase2/eeg/210_31_EVKD_312Hz.mat"

m = sio.loadmat(F, variable_names=['Y'])
Y = m['Y']
print('shape:', Y.shape, 'dtype:', Y.dtype)
print('nan count:', int(np.isnan(Y).sum()), 'inf count:', int(np.isinf(Y).sum()))

# stats per axis to guess the time axis
for ax, name in [(0, 'axis0'), (1, 'axis1'), (2, 'axis2')]:
    v = np.nanstd(Y, axis=ax)
    print(f'{name}: std-of-stds={v.std():.4g} mean-std={v.mean():.4g}')

# assume time axis = axis1 (251 pts) -> test PSD periodicity
fs = 312.5
Yc = np.nan_to_num(Y)

# 1) treat axis1 as time: average PSD over all other dims
X = Yc.reshape(-1, Yc.shape[1])
X = X - X.mean(axis=1, keepdims=True)
from numpy.fft import rfft
P = np.abs(rfft(X, axis=1))**2
P = P.mean(axis=0)
f = np.fft.rfftfreq(Yc.shape[1], 1/fs)
top = np.argsort(P[1:])[-8:][::-1] + 1
print('PSD peaks (axis1 as time):', [(round(float(f[i]),1), round(float(P[i]/P[1:].max()),3)) for i in top])

# 2) treat axis2 as time: concatenate axis1?
X2 = Yc.transpose(0,2,1).reshape(-1, Yc.shape[1])
X2 = X2 - X2.mean(axis=1, keepdims=True)
P2 = np.abs(rfft(X2, axis=1))**2
P2 = P2.mean(axis=0)
top2 = np.argsort(P2[1:])[-8:][::-1] + 1
print('PSD peaks (axis2 as time):', [(round(float(f[i]),1), round(float(P2[i]/P2[1:].max()),3)) for i in top2])

# 3) grand average across trials (axis2) -> 'ERP-like' check per axis0 channel if time=axis1
erp = Yc.mean(axis=2)  # (60, 251)
peak_lat = np.abs(erp).argmax(axis=1)
amp = erp.max(axis=1) - erp.min(axis=1)
print('if time=axis1: peak latency distribution (samples):', np.percentile(peak_lat, [10,50,90]))
print('if time=axis1: ERP amplitude percentiles:', np.percentile(amp, [10,50,90]))

# 4) if time = axis2 (293), per-axis0 channel
erp2 = Yc.mean(axis=1)  # (60, 293)
amp2 = erp2.max(axis=1) - erp2.min(axis=1)
print('if time=axis2: ERP amplitude percentiles:', np.percentile(amp2, [10,50,90]))

print('value range:', float(Yc.min()), float(Yc.max()))
print('mean overall:', float(Yc.mean()))
