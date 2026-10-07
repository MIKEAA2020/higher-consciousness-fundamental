#!/usr/bin/env python3
"""Extract text from the two new DID PDFs (round 13) into glm agent 2/research/new_uploads/."""
import os
from pypdf import PdfReader

OUT_DIR = "/home/z/my-project/glm agent 2/research/new_uploads"
os.makedirs(OUT_DIR, exist_ok=True)

SOURCES = [
    ("/home/z/my-project/upload/Schlumpf-2013-Dissociative-part-dependent-biop.pdf",
     os.path.join(OUT_DIR, "schlumpf-2013.txt")),
    ("/home/z/my-project/upload/aiding-the-diagnosis-of-dissociative-identity-disorder-pattern-recognition-study-of-brain-biomarkers.pdf",
     os.path.join(OUT_DIR, "aiding-diagnosis-2019.txt")),
]

for src, dst in SOURCES:
    reader = PdfReader(src)
    parts = []
    for i, page in enumerate(reader.pages):
        try:
            txt = page.extract_text() or ""
        except Exception as e:  # noqa: BLE001
            txt = f"[EXTRACTION ERROR page {i+1}: {e}]"
        parts.append(f"\n===== PAGE {i+1} =====\n{txt}")
    full = "".join(parts)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(full)
    n_lines = full.count("\n") + 1
    print(f"{os.path.basename(src)} -> {os.path.basename(dst)}: {len(reader.pages)} pages, "
          f"{len(full)} chars, {n_lines} lines")
