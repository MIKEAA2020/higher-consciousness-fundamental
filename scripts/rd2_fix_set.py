#!/usr/bin/env python3
"""Fix 210_20161207_0006eyesOpen_afterICA.set (scipy loadmat char-element quirk).

Strategy: decompress its top-level miCOMPRESSED elements, re-serialize as an
uncompressed MAT5 with trailing zero padding (brute-force the padding size
until scipy parses). Char fields needing the pad get trailing NULs -- harmless
for the fields we consume (nbchan/srate/pnts/trials/data/chanlocs).
"""
import os
import struct
import sys

sys.path.insert(0, "/home/z/my-project/scripts")
from scipy.io import loadmat
from rd2_lib import _decompress_chunked

SRC = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA.set"
DST = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA_fixed.set"

raw = open(SRC, "rb").read()
header = raw[:128]
pos = 128
elems = []
while pos + 8 <= len(raw):
    dtype, nbytes = struct.unpack("<II", raw[pos:pos + 8])
    if dtype & 0xFFFF0000:
        pos += 8
        continue
    payload = raw[pos + 8:pos + 8 + nbytes]
    elems.append((dtype, payload))
    pos += 8 + nbytes + ((8 - nbytes % 8) % 8 if nbytes % 8 else 0)
print(f"top-level elements: {[(t, len(p)) for t, p in elems]}")

mat = [(t, p) for t, p in elems if t == 14][0]
inner = mat[1]
print(f"miMATRIX payload: {len(inner):,} bytes")

for pad in (0, 8, 64, 512, 4096, 65536, 1 << 20):
    content = inner + b"\x00" * pad
    with open(DST, "wb") as f:
        f.write(header)
        f.write(struct.pack("<II", 14, len(content)))
        f.write(content)
    try:
        m = loadmat(DST, squeeze_me=True, struct_as_record=False)
        eeg = m["EEG"]
        print(f"pad={pad}: SUCCESS -- nbchan={eeg.nbchan} srate={eeg.srate} "
              f"pnts={eeg.pnts} trials={eeg.trials} data={eeg.data}")
        print("fixed .set written:", DST)
        break
    except Exception as e:
        print(f"pad={pad}: {str(e)[:70]}")
else:
    print("ALL PADS FAILED -- needs manual field extraction")
