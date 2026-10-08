#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover (page 0) + body -> final v2 PDF, normalized to A4."""
import os
from pypdf import PdfReader, PdfWriter

BASE = '/home/z/my-project'
COVER = os.path.join(BASE, 'scripts', '_cover_v2.pdf')
BODY  = os.path.join(BASE, 'scripts', '_body_v2.pdf')
OUT   = os.path.join(BASE, 'download',
                     'The_Dream_That_Must_Be_v2_Trilogy_Edition.pdf')

A4_W, A4_H = 595.28, 841.89

def normalize_page_to_a4(page):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.1 or abs(h - A4_H) > 0.1:
        page.scale_to(A4_W, A4_H)
    return page

writer = PdfWriter()
writer.add_page(normalize_page_to_a4(PdfReader(COVER).pages[0]))
for page in PdfReader(BODY).pages:
    writer.add_page(normalize_page_to_a4(page))
writer.add_metadata({
    '/Title': 'The Dream That Must Be - Trilogy Edition (Critique, Steelman, Survival Test)',
    '/Author': 'Z.ai',
    '/Creator': 'Z.ai',
    '/Subject': ('Consolidated second edition: the superdeterminism/free-will critique, the '
                 'arc-test with corrected verdicts, the FEP inversion audit, the constitutive '
                 'self-othering steelman, and the survival tests re-run across the three Qwen '
                 'conversations of the Fundamental Higher Consciousness Premise.'),
})
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'wb') as f:
    writer.write(f)
print('final pdf:', OUT, '| pages:', len(writer.pages))
