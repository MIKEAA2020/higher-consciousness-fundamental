#!/usr/bin/env python3
"""Locate + patch the oversized nested char element in the quirked .set.

Recursive walk of miMATRIX sub-elements; find char (miINT8/miUTF8) elements
whose declared data extends past their parent's end; patch the tag's nb down
to the available bytes; re-serialize; verify with loadmat.
"""
import struct
import sys

sys.path.insert(0, "/home/z/my-project/scripts")
from scipy.io import loadmat

SRC = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA.set"
DST = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA_fixed.set"

raw = open(SRC, "rb").read()
header = raw[:128]
t, nb = struct.unpack("<II", raw[128:136])
buf = bytearray(raw[136:136 + nb])
end = len(buf)
print(f"miMATRIX declared {nb:,}, file body {len(buf):,}")

CHAR_TYPES = {1, 16, 17, 18}
patches = []


def walk(parent, pstart, pend, depth, path):
    p = pstart
    while p + 8 <= pend:
        dt, nnb = struct.unpack("<II", parent[p:p + 8])
        small = bool(dt & 0xFFFF0000)
        if small:
            dt2 = dt >> 16
            nb2 = dt & 0xFFFF
            data_off = p + 4
            data_end = p + 4 + nb2
            adv = 8
        else:
            dt2, nb2 = dt, nnb
            data_off = p + 8
            data_end = p + 8 + nb2
            adv = 8 + nb2 + ((8 - nb2 % 8) % 8 if nb2 % 8 else 0)
        if data_end > pend:
            # culprit: declared data passes the parent's end
            avail = pend - data_off
            print(f"  CULPRIT depth={depth} path={path} type={dt2} declared={nb2} "
                  f"avail={avail} at offset {p} (small={small})")
            if avail < 0:
                print("  negative availability -- abort")
                return False
            patches.append((p, small, dt2, nb2, avail))
            return False          # stop walking this branch
        if dt2 == 14:             # nested miMATRIX -> recurse
            ok = walk(parent, data_off, data_end, depth + 1, path + [p])
            if not ok:
                return False
        p += adv
    return True


ok = walk(buf, 0, end, 0, [])
print("walk clean:", ok, "| patches:", len(patches))

if patches:
    p, small, dt2, nb2, avail = patches[0]
    # patch: normal-format tag with nb reduced to available (rounded to <= avail)
    new_nb = avail - (avail % 8) if avail >= 8 else min(avail, 4)
    if small:
        # cannot express > 4 bytes in small format; convert to normal tag
        buf[p:p + 8] = struct.pack("<II", dt2, new_nb) + b"\x00" * 0
        # small->normal conversion: tag becomes 8 bytes + data; total length
        # grows by (new_nb - 4) ... too invasive; instead zero the declared nb
        # to 0 (empty char) if new_nb <= 0
        print("  (small-format culprit; zeroing)")
        buf[p:p + 4] = struct.pack("<I", (dt2 << 16) | 0)
    else:
        buf[p + 4:p + 8] = struct.pack("<I", new_nb)
        print(f"  patched tag @ {p}: nb {nb2} -> {new_nb}")

with open(DST, "wb") as f:
    f.write(header)
    f.write(struct.pack("<II", 14, len(buf)))
    f.write(bytes(buf))
try:
    m = loadmat(DST, squeeze_me=True, struct_as_record=False)
    eeg = m["EEG"]
    print(f"FIXED: nbchan={eeg.nbchan} srate={eeg.srate} pnts={eeg.pnts} "
          f"trials={eeg.trials} data={eeg.data}")
except Exception as e:
    print("still failing:", str(e)[:90])
