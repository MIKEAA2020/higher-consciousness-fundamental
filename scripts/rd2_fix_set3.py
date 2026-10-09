#!/usr/bin/env python3
"""Manual field extraction for the quirked 210_0006eyesOpen .set.

Parses the EEG struct's field names + the numeric fields we need with a
tolerant walker (the corrupted char element is skipped, not patched).
Falls back to sibling-file conventions + .fdt size for anything unreadable.
"""
import struct
import sys

sys.path.insert(0, "/home/z/my-project/scripts")

SRC = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA.set"
FDT = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA.fdt"
DST = "/home/z/my-project/glm agent 2/research/rawdata2/spontaneous/210_20161207_0006eyesOpen_afterICA_fixed.json"

raw = open(SRC, "rb").read()
t, nb = struct.unpack("<II", raw[128:136])
buf = raw[136:136 + nb]
print(f"miMATRIX {nb:,} bytes", flush=True)


def sub(buf, p):
    """Read one sub-element at p: returns (type, nb, data_off, data_end, adv) or None."""
    if p + 8 > len(buf):
        return None
    dt, nnb = struct.unpack("<II", buf[p:p + 8])
    if dt & 0xFFFF0000:
        dt2, nb2 = dt >> 16, dt & 0xFFFF
        return (dt2, nb2, p + 4, p + 4 + nb2, 8)
    dt2, nb2 = dt, nnb
    adv = 8 + nb2 + ((8 - nb2 % 8) % 8 if nb2 % 8 else 0)
    return (dt2, nb2, p + 8, p + 8 + nb2, adv)


# top miMATRIX sub-elements: flags, dims, fnlen, fieldnames, then field values
e = sub(buf, 0)
assert e[0] == 6, f"flags type {e[0]}"
p = e[4]
e = sub(buf, p)                       # dims
print("dims:", struct.unpack(f"<{e[1]//4}i", buf[e[2]:e[3]]), flush=True)
p = e[4]
e = sub(buf, p)                       # field name length (miINT32)
fnlen = struct.unpack("<i", buf[e[2]:e[2] + 4])[0]
print("field name length:", fnlen, flush=True)
p = e[4]
e = sub(buf, p)                       # field names (miINT8, fixed width)
names_blob = buf[e[2]:e[3]]
nfields = e[1] // fnlen
names = [names_blob[i * fnlen:(i + 1) * fnlen].split(b"\x00")[0].decode("latin1")
         for i in range(nfields)]
print(f"{nfields} fields:", names, flush=True)
p = e[4]

out = {}
for name in names:
    try:
        e = sub(buf, p)
        if e is None:
            print(f"  {name}: <no room for element>", flush=True)
            break
        dt2, nb2, d0, d1, adv = e
        if d1 > len(buf):
            print(f"  {name}: <oversized element type={dt2} nb={nb2} "
                  f"avail={len(buf)-d0}> -- corrupted char, stopping here", flush=True)
            break
        if dt2 == 14:                 # miMATRIX value
            # parse its inner: flags, dims, name, data
            q = 0
            e1 = sub(buf, d0) or (0, 0, 0, 0, 0)
            q = e1[4]
            e2 = sub(buf, d0 + q)     # dims
            dims = struct.unpack(f"<{e2[1]//4}i", buf[e2[2]:e2[3]]) if e2[0] in (5, 6) else ()
            q = d0 + e2[4]
            e3 = sub(buf, q)          # name
            q += e3[4]
            e4 = sub(buf, q)          # data
            if e4 and e4[0] == 9 and e4[1] == 8:      # miDOUBLE scalar
                out[name] = struct.unpack("<d", buf[e4[2]:e4[2] + 8])[0]
                print(f"  {name} = {out[name]} (dims={dims})", flush=True)
            elif e4 and e4[0] in (1, 16):             # char
                s = buf[e4[2]:min(e4[3], len(buf))].split(b"\x00")[0].decode("latin1", "ignore")
                out[name] = s
                print(f"  {name} = '{s}' (char, dims={dims})", flush=True)
            else:
                print(f"  {name}: <skipped type {e4[0] if e4 else '?'} dims={dims}>", flush=True)
        p += adv if dt2 != 14 else (d1 - p) + ((8 - (d1 - p) % 8) % 8 if (d1 - p) % 8 else 0)
        # for miMATRIX values the element size is exactly (adv from its own tag)
        if dt2 == 14:
            p = d1 + ((8 - nb2 % 8) % 8 if nb2 % 8 else 0)
    except Exception as ex:
        print(f"  {name}: err {ex}", flush=True)
        break

# fallback for pnts/trials from fdt size + subject conventions
import os, json
fdt_bytes = os.path.getsize(FDT)
per_trial = 62 * 2000 * 4
out.setdefault("nbchan", 62)
out.setdefault("srate", 250.0)
out.setdefault("pnts", 2000)
out.setdefault("trials", fdt_bytes // per_trial)
out["_fdt_bytes"] = fdt_bytes
out["_derived_trials"] = fdt_bytes // per_trial
out["_note"] = ("set char-element corruption tolerated; fields read manually; "
                "trials derived from sha256-verified .fdt size / (62*2000*4)")
print("FINAL:", out, flush=True)
json.dump(out, open(DST, "w"), indent=1)
print("written", DST)
