# -*- coding: utf-8 -*-
"""
Aggregator for "The Dream That Must Be — Trilogy Edition" (v2) content.

Single source of truth: consumed by scripts/build_pdf_v2.py (PDF body) and
scripts/export_md_v2.py (Markdown companion). Content lives in four part
modules (v2a: sections 1-3, v2b: 4-5, v2c: 6-7, v2d: 8-10) for editability.
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import critique_content_v2a as _A
import critique_content_v2b as _B
import critique_content_v2c as _C
import critique_content_v2d as _D
importlib.reload(_A); importlib.reload(_B); importlib.reload(_C); importlib.reload(_D)

DOC_TITLE = "The Dream That Must Be"
DOC_SUBTITLE = ("Trilogy Edition — Necessity and Freedom in the Grand Dream Framework: "
                "the Consolidated Critique, Steelman, and Survival Test Across Three "
                "Conversations")
DOC_DATE = "October 2026"
DOC_AUTHOR = "Z.ai"
BASE_DIR = "/home/z/my-project"

META_NOTE = ("Second edition. Citations use three prefixes: v1L / v2L / v3L are line numbers "
             "of the canonical transcripts of the three Qwen conversations "
             "(qwen_chat_fundamental_higher_consciousness_premise.md, …_v2.md, …_v3.md; shares "
             "f30d7216, 68292366, a6629bde respectively). C1 [n], C2 [n], C3 [n] are message "
             "markers within each conversation. All quotations are verbatim. Citations of "
             "classic works are paraphrase-flagged where wording is uncertain. This edition "
             "retracts one finding of the prior line-level reading and reports the arc-test "
             "that forced the retraction (Sections 1 and 5).")

SECTIONS = (_A.SECTIONS_A + _B.SECTIONS_B + _C.SECTIONS_C + _D.SECTIONS_D)

if __name__ == "__main__":
    n_blocks = sum(len(s["blocks"]) for s in SECTIONS)
    n_tables = sum(1 for s in SECTIONS for b in s["blocks"] if b[0] == "table")
    words = 0
    for s in SECTIONS:
        for kind, payload in s["blocks"]:
            if kind in ("body", "note", "quote"):
                words += len(payload.split())
            elif kind == "table":
                words += sum(len(" ".join(r).split()) for r in payload["rows"])
                words += len(" ".join(payload["header"]).split())
    print("sections:", len(SECTIONS), "| blocks:", n_blocks, "| tables:", n_tables,
          "| approx words:", words)
