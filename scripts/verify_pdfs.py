#!/usr/bin/env python3
"""Verify the two PDFs uploaded after Round 21 (user challenge: read or hallucinated?).

Extracts text page-by-page from both files, writes full text cores to
research/r21b/ for archival, prints identification fingerprints (title,
authors, DOI, key numbers) so the main agent can compare them against the
claims actually made in previous rounds.
"""
import hashlib
import os
import re

import pdfplumber

BASE = "/home/z/my-project"
SRC = [
    (f"{BASE}/upload/level 2 decombiniation/20141982.pdf", f"{BASE}/glm agent 2/research/r21b/pdf_20141982"),
    (f"{BASE}/upload/level 2 decombiniation/pone.0242056.pdf", f"{BASE}/glm agent 2/research/r21b/pdf_pone0242056"),
]
os.makedirs(f"{BASE}/glm agent 2/research/r21b", exist_ok=True)

for path, stem in SRC:
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    with pdfplumber.open(path) as pdf:
        n = len(pdf.pages)
        texts = []
        for i, page in enumerate(pdf.pages):
            t = page.extract_text() or ""
            texts.append(f"\n===== PAGE {i+1}/{n} =====\n{t}")
        full = "".join(texts)
    out = stem + "_full.txt"
    open(out, "w").write(full)
    print(f"\n########## {path}")
    print(f"sha256={h[:16]}...  pages={n}  chars={len(full)}  -> {out}")
    # fingerprint: first 2 pages condensed
    head = full[:2600]
    print("---- head ----")
    print(head)
    # DOI / identifiers
    dois = sorted(set(re.findall(r"10\.\d{4,9}/[^\s\"'<>,;)]+", full)))[:8]
    print("---- DOIs found:", dois)
