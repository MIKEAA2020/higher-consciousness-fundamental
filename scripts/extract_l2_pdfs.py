#!/usr/bin/env python3
"""extract_l2_pdfs.py — extract text from the 5 user-uploaded Level-2 PDFs.
Outputs to glm agent 2/research/new_uploads/ as .txt files with page markers.
"""
import fitz  # PyMuPDF
import os

SRC = "/home/z/my-project/upload/level 2 decombiniation"
DST = "/home/z/my-project/glm agent 2/research/new_uploads"
os.makedirs(DST, exist_ok=True)

pdfs = [
    ("1-s2.0-S1053811916300891-main.pdf", "jirsa2017_vep.txt"),
    ("2024.05.08.593146v4.full.pdf", "biorxiv_2024_05_08_593146.txt"),
    ("The_Dream_That_Must_Be_Critique_Steelman_Survival_Test.pdf", "survival_test_ref.txt"),
    ("elife-35082-v3.pdf", "preller2018_elife_lsd.txt"),
    ("riedl-et-al-2015-metabolic-connectivity-mapping-reveals-effective-connectivity-in-the-resting-human-brain.pdf", "riedl2015_metabolic.txt"),
]

for src_name, out_name in pdfs:
    path = os.path.join(SRC, src_name)
    doc = fitz.open(path)
    parts = []
    for i, page in enumerate(doc):
        t = page.get_text("text")
        parts.append(f"\n===== PAGE {i+1}/{len(doc)} =====\n{t}")
    full = "".join(parts)
    out = os.path.join(DST, out_name)
    with open(out, "w", encoding="utf-8") as f:
        f.write(full)
    # First 300 chars of page 1 for identification
    first_page = doc[0].get_text("text")[:600].replace("\n", " | ")
    print(f"{src_name[:60]} -> {out_name} ({len(doc)} pages, {len(full)} chars)")
    print(f"    ID: {first_page[:350]}")
    doc.close()
