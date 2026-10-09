#!/usr/bin/env python3
"""Manual MAT 5.0 parser with fault-tolerant zlib recovery for 210_31_EVKD_312Hz.mat.
Goal: find the Y variable element, decompress as much as possible, report recovery."""
import zlib, struct
import numpy as np

F = "/home/z/my-project/glm agent 2/research/phase2/eeg/210_31_EVKD_312Hz.mat"
raw = open(F, 'rb').read()
print('file size:', len(raw))

pos = 128  # skip header
miTYPES = {1:'miINT8',2:'miUINT8',3:'miINT16',4:'miUINT16',5:'miINT32',6:'miUINT32',
           7:'miSINGLE',9:'miDOUBLE',12:'miINT64',13:'miUINT64',14:'miMATRIX',15:'miCOMPRESSED',16:'miUTF8',17:'miUTF16',18:'miUTF32'}

elements = []
while pos < len(raw):
    if pos + 8 > len(raw):
        print('truncated tag at', pos); break
    b = raw[pos:pos+8]
    dtype, nbytes = struct.unpack('<II', b)
    if dtype & 0xFFFF0000:  # small-element format: high 16 bits = data
        dtype_s = dtype >> 16; nbytes_s = dtype & 0xFFFF
        elements.append((pos, dtype_s, nbytes_s, raw[pos+4:pos+4+nbytes_s], True))
        pos += 8
    else:
        elements.append((pos, dtype, nbytes, raw[pos+8:pos+8+nbytes], False))
        pos += 8 + nbytes + ((8 - nbytes % 8) % 8 if nbytes % 8 else 0)

for (p, t, n, data, small) in elements:
    print(f'element @{p}: {miTYPES.get(t,t)} bytes={n} small={small}')

# The matrix element (probably miCOMPRESSED=15 containing miMATRIX=14)
mat_el = [e for e in elements if e[1] in (14, 15)]
print('\nmatrix-bearing elements:', len(mat_el))
for (p, t, n, data, small) in mat_el:
    if t == 15:
        d = zlib.decompressobj()
        try:
            out = d.decompress(data)
            print(f'compressed element @{p}: decompressed fully, {len(out)} bytes')
        except Exception as e:
            print(f'compressed element @{p}: zlib error: {e}')
            d = zlib.decompressobj()
            out = b''
            try:
                out = d.decompress(data)
            except Exception as e2:
                out = d.flush() if hasattr(d,'flush') else out
                print('  partial before error:', len(out))
            # manual chunked decompression
            d = zlib.decompressobj()
            out = bytearray()
            step = 1 << 20
            i = 0
            while i < len(data):
                chunk = data[i:i+step]
                try:
                    out.extend(d.decompress(chunk))
                except Exception as ee:
                    print(f'  stream died at input offset ~{i}, recovered output: {len(out)} bytes')
                    break
                i += step
            out = bytes(out)
        # parse the miMATRIX inside
        if len(out) >= 8:
            t2, n2 = struct.unpack('<II', out[:8])
            print('inner element:', miTYPES.get(t2,t2), 'bytes', n2, 'total inner buffer', len(out))
            inner = out[8:8+n2]
            # walk sub-elements of miMATRIX
            q = 0
            dims = None; name = None; real_tag = None; real_data_len = 0
            while q < len(inner):
                if q + 8 > len(inner): break
                dt, nb = struct.unpack('<II', inner[q:q+8])
                if dt & 0xFFFF0000:
                    dt2 = dt >> 16; nb2 = dt & 0xFFFF
                    payload = inner[q+4:q+4+nb2]; adv = 8
                else:
                    dt2, nb2 = dt, nb
                    payload = inner[q+8:q+8+nb2]
                    adv = 8 + nb2 + ((8 - nb2 % 8) % 8 if nb2 % 8 else 0)
                nm = miTYPES.get(dt2, dt2)
                if nm == 'miUINT32' and len(payload) >= 8 and dims is None:
                    dims = struct.unpack(f'<{len(payload)//4}I', payload[:len(payload)//4*4])
                elif nm == 'miINT8' and name is None and len(payload) < 64:
                    name = payload.decode('latin1', 'ignore')
                print(f'  sub @{q}: {nm} n={nb2} name={name} dims={dims}')
                if nm in ('miDOUBLE','miSINGLE') or (name == 'Y' and nm == 'miUINT32' and len(payload)>=8 and struct.unpack('<II', payload[:8])[0]==6):
                    pass
                q += adv
            # locate real numeric part: last miDOUBLE sub-element
            q = 0; numeric_offset = None; numeric_type = None
            while q + 8 <= len(inner):
                dt, nb = struct.unpack('<II', inner[q:q+8])
                if dt & 0xFFFF0000:
                    dt2 = dt >> 16; nb2 = dt & 0xFFFF; data_off = q+4; adv = 8
                else:
                    dt2, nb2 = dt, nb; data_off = q+8
                    adv = 8 + nb2 + ((8 - nb2 % 8) % 8 if nb2 % 8 else 0)
                if dt2 in (9, 7):  # double or single
                    numeric_type = dt2; numeric_offset = data_off
                    print(f'  numeric payload @{data_off} type={miTYPES[dt2]} declared={nb2} available={len(inner)-data_off}')
                q += adv
            if numeric_offset is not None and numeric_type == 9:
                avail = inner[numeric_offset:]
                nvals = len(avail)//8
                arr = np.frombuffer(avail[:nvals*8], dtype='<f8').copy()
                print(f'  RECOVERED {nvals} doubles of declared {np.prod(dims) if dims else "?"} ({100*nvals/max(1,np.prod(dims) if dims else 1):.1f}%)')
                np.save('/home/z/my-project/glm agent 2/research/phase2/eeg/Y_partial.npy', arr)
                print('  saved Y_partial.npy; stats:', float(arr.min()), float(arr.max()), float(arr.mean()))
