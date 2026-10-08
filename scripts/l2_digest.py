#!/usr/bin/env python3
"""l2_digest.py — strip references + page markers from the 5 Level-2 paper
extractions, producing compact reading files. Measures before/after."""
import re, os

SRC = "/home/z/my-project/glm agent 2/research/new_uploads"
DST = "/home/z/my-project/glm agent 2/research/new_uploads/digests"
os.makedirs(DST, exist_ok=True)

files = [
    "jirsa2017_vep.txt",
    "biorxiv_2024_05_08_593146.txt",
    "deco2018_currbio_lsd.txt",
    "preller2018_elife_lsd.txt",
    "riedl2015_metabolic.txt",
]

for fn in files:
    p = os.path.join(SRC, fn)
    t = open(p, encoding="utf-8").read()
    orig_lines = t.count("\n")
    # find the LAST plausible References/Acknowledgments section start
    cut = len(t)
    for m in re.finditer(r"(?m)^(References|REFERENCE|Acknowledg(e)?ments|Acknowledg(e)?ment)\s*$", t):
        # only cut if less than 45% into the doc remains (refs are at the end)
        if m.start() > len(t) * 0.55:
            cut = min(cut, m.start())
    t = t[:cut]
    # strip bioRxiv draft line-number columns (standalone number lines)
    t = re.sub(r"(?m)^\s*\d{1,4}\s*$", "", t)
    # collapse 3+ blank lines
    t = re.sub(r"\n{3,}", "\n\n", t)
    out = os.path.join(DST, fn)
    open(out, "w", encoding="utf-8").write(t)
    lines = t.count("\n")
    print(f"{fn}: {orig_lines} -> {lines} lines, {len(t)} chars ({len(t)//1024}KB)")
