#!/usr/bin/env python3
"""Round 21 shared library — Raw_data_2 loaders (Farnes et al. 2020 corpus).

Evoked: MAT5 var Y, dims (60 ch, 251 samples, N trials) column-major.
CORRECTION vs Round 20: the flat double stream must be reshaped with
order='F' (MATLAB column-major). Round 20's row-major reshape(n,60,251)+
transpose scrambled channels/samples -- documented as repair R32.

Spontaneous: EEGLAB .set (MAT) + .fdt (float32 stream, column-major
(nbchan, pnts, trials)); first two recordings = awake, last two = ketamine.
"""
import os
import struct
import zlib
import numpy as np

BASE = "/home/z/my-project/glm agent 2/research/rawdata2"
EV = os.path.join(BASE, "evoked")
SP = os.path.join(BASE, "spontaneous")

SUBJECTS = ["210", "219", "249", "251", "265", "271", "282", "300", "313", "318"]
FS_EV = 312.5          # evoked sampling rate
PULSE_SAMPLE = 126     # readme: TMS pulse occurred at the 126th sample (1-based -> idx 125)
NCH_EV = 60
NSAMP_EV = 251

_miT = {1: 'miINT8', 2: 'miUINT8', 3: 'miINT16', 4: 'miUINT16', 5: 'miINT32',
        6: 'miUINT32', 7: 'miSINGLE', 9: 'miDOUBLE', 14: 'miMATRIX', 15: 'miCOMPRESSED'}


def _decompress_chunked(data):
    d = zlib.decompressobj()
    out = bytearray()
    step = 1 << 20
    i = 0
    while i < len(data):
        try:
            out.extend(d.decompress(data[i:i + step]))
        except Exception:
            break
        i += step
    try:
        out.extend(d.flush())
    except Exception:
        pass
    return bytes(out)


def load_evoked(path):
    """Robust MAT5 loader for the EVKD files.

    Returns dict(arr (60, 251, ntr_complete) float64 in CORRECT order,
    dims, n_declared, n_recovered, n_complete, truncated_bool).
    """
    raw = open(path, 'rb').read()
    pos = 128
    while pos < len(raw):
        if pos + 8 > len(raw):
            break
        dtype, nbytes = struct.unpack('<II', raw[pos:pos + 8])
        if dtype & 0xFFFF0000:            # small element
            pos += 8
            continue
        if dtype == 15:                   # miCOMPRESSED
            comp = raw[pos + 8:pos + 8 + nbytes]
            out = _decompress_chunked(comp)
            return _parse_matrix(out)
        pos += 8 + nbytes + ((8 - nbytes % 8) % 8 if nbytes % 8 else 0)
    raise ValueError(f"no matrix element in {path}")


def _parse_matrix(out):
    if len(out) < 8:
        raise ValueError("empty decompressed buffer")
    t2, n2 = struct.unpack('<II', out[:8])
    inner = out[8:8 + n2]
    q = 0
    dims = None
    name = None
    seen_flags = False
    numeric = None          # (dtype, payload_bytes)
    while q + 8 <= len(inner):
        dt, nb = struct.unpack('<II', inner[q:q + 8])
        if dt & 0xFFFF0000:
            dt2 = dt >> 16
            nb2 = dt & 0xFFFF
            data_off = q + 4
            adv = 8
            payload = inner[q + 4:q + 4 + nb2]
        else:
            dt2, nb2 = dt, nb
            data_off = q + 8
            adv = 8 + nb2 + ((8 - nb2 % 8) % 8 if nb2 % 8 else 0)
            payload = inner[q + 8:q + 8 + nb2]
        nm = _miT.get(dt2, dt2)
        if nm == 'miUINT32' and not seen_flags and nb2 == 8:
            seen_flags = True              # array flags (class word; this writer
        elif nm in ('miUINT32', 'miINT32') and dims is None:
            # dims element -- miINT32 in these files (writer convention), both legal
            dims = struct.unpack(f'<{len(payload)//4}I', payload[:len(payload)//4 * 4])
        elif nm == 'miINT8' and name is None and len(payload) < 64:
            name = payload.decode('latin1', 'ignore')
        elif dt2 in (9, 7):
            numeric = (dt2, payload[:nb2])
        q += adv
    if numeric is None or dims is None:
        raise ValueError(f"parse failed: dims={dims} numeric={numeric is not None}")
    dt2, payload = numeric
    if dt2 == 9:
        flat = np.frombuffer(payload, dtype='<f8').copy()
    else:
        flat = np.frombuffer(payload, dtype='<f4').astype(np.float64)
    n_declared = int(np.prod(dims))
    n_recovered = len(flat)
    per = int(np.prod(dims[:2])) if len(dims) >= 3 else n_declared
    n_complete = n_recovered // per if per else 0
    arr = flat[:n_complete * per].reshape((int(dims[0]), int(dims[1]), n_complete), order='F')
    return dict(arr=arr, dims=tuple(int(x) for x in dims), name=name,
                n_declared=n_declared, n_recovered=n_recovered,
                n_complete=n_complete, truncated=(n_recovered < n_declared))


def load_set_fdt(setpath):
    """EEGLAB .set + .fdt loader -> (data (nbchan, pnts, trials), meta dict).

    Tolerant: if scipy's strict loadmat fails (char-element corruption in one
    210_0006eyesOpen .set), falls back to the manually-derived sidecar JSON
    (nbchan/srate/pnts from the same subject's other recordings; trials from
    the sha256-verified .fdt size)."""
    from scipy.io import loadmat
    try:
        m = loadmat(setpath, squeeze_me=True, struct_as_record=False)
    except Exception as ex:
        side = setpath[:-4] + "_fixed.json"
        import json
        if not os.path.exists(side):
            raise
        meta_s = json.load(open(side))
        nbchan = int(meta_s["nbchan"])
        srate = float(meta_s["srate"])
        pnts = int(meta_s["pnts"])
        ntr = int(meta_s["trials"])
        fdt = os.path.join(os.path.dirname(setpath),
                           os.path.basename(setpath)[:-4] + ".fdt")
        flat = np.fromfile(fdt, dtype="<f4")
        n_ok = len(flat) // (nbchan * pnts)
        data = flat[:n_ok * nbchan * pnts].reshape((nbchan, pnts, n_ok),
                                                   order="F").astype(np.float64)
        return data, dict(nbchan=nbchan, srate=srate, pnts=pnts, trials=ntr,
                          labels=[f"ch{i}" for i in range(nbchan)],
                          types=["EEG"] * nbchan, fdt_ok=n_ok,
                          setname=os.path.basename(setpath),
                          expected_samples=nbchan * pnts * ntr,
                          got_samples=len(flat),
                          fallback="sidecar (set char corruption: " + str(ex)[:60] + ")")
    eeg = m['EEG']
    nbchan = int(eeg.nbchan)
    srate = float(eeg.srate)
    pnts = int(eeg.pnts)
    ntr = int(np.atleast_1d(eeg.trials)[0]) if np.ndim(eeg.trials) else int(eeg.trials)
    fdt = os.path.join(os.path.dirname(setpath), str(eeg.data))
    flat = np.fromfile(fdt, dtype='<f4')
    expect = nbchan * pnts * ntr
    n_ok = len(flat) // (nbchan * pnts)
    data = flat[:n_ok * nbchan * pnts].reshape((nbchan, pnts, n_ok), order='F').astype(np.float64)
    labels, types = [], []
    ch = np.atleast_1d(eeg.chanlocs)
    for c in ch:
        labels.append(str(getattr(c, 'labels', '?')))
        types.append(str(getattr(c, 'type', getattr(c, 'types', '?'))))
    return data, dict(nbchan=nbchan, srate=srate, pnts=pnts, trials=ntr,
                      labels=labels, types=types, fdt_ok=n_ok,
                      setname=str(getattr(eeg, 'setname', '')),
                      expected_samples=expect, got_samples=len(flat))


def spontaneous_files(subject):
    """Ordered [(condition, eyes, setpath)] with first two recordings = awake,
    last two = ketamine (readme). Eyes state parsed from filename."""
    pat = [f for f in sorted(os.listdir(SP))
           if f.startswith(subject + "_") and f.endswith(".set")]
    if len(pat) != 4:
        raise ValueError(f"{subject}: expected 4 .set files, got {len(pat)}")
    out = []
    for i, fn in enumerate(pat):
        cond = "awake" if i < 2 else "ketamine"
        low = fn.lower()
        eyes = "closed" if ("closed" in low or "cloed" in low) else "open"
        out.append((cond, eyes, os.path.join(SP, fn)))
    return out


def evoked_paths(subject, cond):
    """cond: 'awake' (recording 31) or 'ketamine' (recording 32)."""
    rid = "31" if cond == "awake" else "32"
    fn = f"{subject}_{rid}_EVKD_312Hz.mat"
    p = os.path.join(EV, fn)
    if not os.path.exists(p):
        raise ValueError(f"missing {p}")
    return p
