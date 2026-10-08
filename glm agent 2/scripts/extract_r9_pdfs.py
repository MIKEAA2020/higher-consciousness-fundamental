#!/usr/bin/env python3
"""Round 9: extract page-by-page text from the two additional audit PDFs
identified by the user, into line-readable research files."""
from pypdf import PdfReader

JOBS = [
    (
        "/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_Steelman-Audit-and-Consolidation.pdf",
        "/home/z/my-project/glm agent 2/research/steelman_1st_ed_pages.txt",
    ),
    (
        "/home/z/my-project/download/The_Dream_That_Must_Be_v2_Trilogy_Edition.pdf",
        "/home/z/my-project/glm agent 2/research/dream_v2_trilogy_pages.txt",
    ),
]

for src, dst in JOBS:
    reader = PdfReader(src)
    out = []
    total = 0
    for i, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as e:
            text = f"[extraction error: {e}]"
        total += len(text)
        out.append(f"\n===== PAGE {i} =====\n")
        out.append(text)
    with open(dst, "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"{src}\n  -> {dst}\n  {len(reader.pages)} pages, {total} chars\n")
