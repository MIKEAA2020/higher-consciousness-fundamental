#!/usr/bin/env python3
"""Extract text from the Fourth (Strengthened) Edition PDF for Fifth-Edition continuity."""
import os
from pypdf import PdfReader

SRC = "/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation_Strengthened-Ed.pdf"
DST = "/home/z/my-project/glm agent 2/research/strengthened_ed_pages.txt"

reader = PdfReader(SRC)
parts = []
for i, page in enumerate(reader.pages):
    try:
        txt = page.extract_text() or ""
    except Exception as e:  # noqa: BLE001
        txt = f"[EXTRACTION ERROR page {i+1}: {e}]"
    parts.append(f"\n===== PAGE {i+1} =====\n{txt}")
full = "".join(parts)
with open(DST, "w", encoding="utf-8") as f:
    f.write(full)
print(f"{len(reader.pages)} pages, {len(full)} chars, {full.count(chr(10)) + 1} lines -> {DST}")
