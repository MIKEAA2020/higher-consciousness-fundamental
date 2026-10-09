#!/usr/bin/env python3
"""Raw_data_2 release downloader (Round 21).

Downloads release assets per manifest.tsv (name, size, sha256, url), verifies
sha256, resumable across calls. Run: python3 rd2_download.py <start> <end>
(indices into manifest, end-exclusive). Files land in rawdata2/<subdir> where
subdir = evoked/ for .mat, spontaneous/ for .fdt/.set, root for readme.
"""
import hashlib
import os
import subprocess
import sys

BASE = "/home/z/my-project/glm agent 2/research/rawdata2"
MANIFEST = os.path.join(BASE, "manifest.tsv")


def target_path(name):
    if name.endswith(".mat"):
        return os.path.join(BASE, "evoked", name)
    if name.endswith((".fdt", ".set")):
        return os.path.join(BASE, "spontaneous", name)
    return os.path.join(BASE, name)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    rows = [l.rstrip("\n").split("\t") for l in open(MANIFEST) if l.strip()]
    rows = [r for r in rows if len(r) == 4]
    os.makedirs(os.path.join(BASE, "evoked"), exist_ok=True)
    os.makedirs(os.path.join(BASE, "spontaneous"), exist_ok=True)
    ok = skip = fail = 0
    for name, size, dg, url in rows[lo:hi]:
        dst = target_path(name)
        if os.path.exists(dst) and sha256_file(dst) == dg:
            skip += 1
            continue
        r = subprocess.run(
            ["curl", "-sL", "--retry", "3", "--retry-delay", "2",
             "-C", "-", "-o", dst, url],
            timeout=900)
        if r.returncode != 0:
            print(f"FAIL curl rc={r.returncode}: {name}")
            fail += 1
            continue
        got = sha256_file(dst) if os.path.exists(dst) else ""
        if got == dg:
            ok += 1
        else:
            print(f"FAIL sha256 {name}: got {got[:16]} want {dg[:16]}")
            fail += 1
    print(f"slice [{lo}:{hi}) -> ok={ok} skip={skip} fail={fail}")


if __name__ == "__main__":
    main()
