#!/usr/bin/env python3
"""Round 21 — inspect Raw_data_2 assets: evoked .mat recoverability + .set headers."""
import os
import struct
import zlib
import numpy as np

try:
    from scipy.io import loadmat
except ImportError:
    loadmat = None

EV = "/home/z/my-project/glm agent 2/research/rawdata2/evoked"
SP = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous"

miTYPES = {1: 'miINT8', 2: 'miUINT8', 3: 'miINT16', 4: 'miUINT16', 5: 'miINT32',
           6: 'miUINT32', 7: 'miSINGLE', 9: 'miDOUBLE', 14: 'miMATRIX',
           15: 'miCOMPRESSED'}


def parse_mat(raw):
    """Walk top-level MAT5 elements; return (elements list, dims, name) for the
    first matrix-bearing element, plus its full decompressed inner buffer."""
    pos = 128
    elements = []
    while pos < len(raw):
        if pos + 8 > len(raw):
            break
        dtype, nbytes = struct.unpack('<II', raw[pos:pos + 8])
        if dtype & 0xFFFF0000:
            dtype_s = dtype >> 16
            nbytes_s = dtype & 0xFFFF
            elements.append((pos, dtype_s, nbytes_s, raw[pos + 4:pos + 4 + nbytes_s], True))
            pos += 8
        else:
            elements.append((pos, dtype, nbytes, raw[pos + 8:pos + 8 + nbytes], False))
            pos += 8 + nbytes + ((8 - nbytes % 8) % 8 if nbytes % 8 else 0)
    for (p, t, n, data, small) in elements:
        if t != 15:
            continue
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
        out = bytes(out)
        if len(out) < 8:
            continue
        t2, n2 = struct.unpack('<II', out[:8])
        inner = out[8:8 + n2]
        # walk sub-elements
        q = 0
        dims = None
        name = None
        numeric_offset = None
        numeric_type = None
        numeric_avail = 0
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
            nm = miTYPES.get(dt2, dt2)
            if nm == 'miUINT32' and len(payload) >= 8 and dims is None:
                v = struct.unpack('<II', payload[:8])
                if v[0] in (6, 7, 9) or len(payload) // 4 <= 4:  # plausible dims
                    dims = struct.unpack(f'<{len(payload)//4}I', payload[:len(payload)//4*4])
            elif nm == 'miINT8' and name is None and len(payload) < 64:
                name = payload.decode('latin1', 'ignore')
            if dt2 in (9, 7):
                numeric_type = dt2
                numeric_offset = data_off
                numeric_avail = len(inner) - data_off
            q += adv
        return dict(dims=dims, name=name, numeric_type=numeric_type,
                    numeric_offset=numeric_offset, numeric_avail=numeric_avail,
                    inner_len=len(inner), truncated=n2 > len(inner) - 0)
    return None


print("=== EVOKED .mat files ===")
for fn in sorted(os.listdir(EV)):
    p = os.path.join(EV, fn)
    raw = open(p, 'rb').read()
    info = parse_mat(raw)
    sz = len(raw)
    if info is None:
        print(f"{fn}: NO MATRIX ELEMENT ({sz:,} bytes)")
        continue
    dims, name = info['dims'], info['name']
    decl = int(np.prod(dims)) if dims else 0
    # numeric payload length available in decompressed buffer
    navail = info['numeric_avail']
    nvals = navail // 8 if info['numeric_type'] == 9 else navail // 4
    # n2 = declared inner bytes; inner_len = actually decompressed
    pct = 100.0 * nvals / max(1, decl)
    print(f"{fn}: {sz:,}B var={name} dims={dims} decl={decl:,} "
          f"recov={nvals:,} ({pct:.1f}%) type={miTYPES.get(info['numeric_type'])}")

print()
print("=== SPONTANEOUS .set headers (first 2) ===")
sets = sorted(f for f in os.listdir(SP) if f.endswith(".set"))
for fn in sets[:2]:
    p = os.path.join(SP, fn)
    try:
        m = loadmat(p, squeeze_me=True, struct_as_record=False)
        eeg = m.get('EEG')
        if eeg is None:
            print(f"{fn}: keys={list(m.keys())}")
            continue
        fields = ['nbchan', 'srate', 'pnts', 'trials', 'xmin', 'xmax', 'data',
                  'setname', 'filename', 'ref']
        print(f"{fn}:")
        for f in fields:
            v = getattr(eeg, f, '<absent>')
            print(f"   {f} = {v!r}"[:150])
        ch = getattr(eeg, 'chanlocs', None)
        if ch is not None:
            try:
                labels = [getattr(c, 'labels', '?') for c in np.atleast_1d(ch)][:70]
                print("   chanlocs[0:8]:", labels[:8], f"... total {len(labels)}")
            except Exception as ex:
                print("   chanlocs err:", ex)
    except Exception as ex:
        print(f"{fn}: loadmat failed: {ex}")
