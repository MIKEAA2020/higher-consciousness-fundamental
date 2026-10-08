#!/usr/bin/env python3
"""Merge the Revised Edition: cover + body -> final PDF in download/."""
import os

from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
COVER = os.path.join(HERE, 'r3_cover.pdf')
BODY = os.path.join(HERE, 'r3_body.pdf')
OUT = ('/home/z/my-project/download/'
       'Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation_Revised-Ed.pdf')

A4_W, A4_H = 595.28, 841.89


def normalize_page_to_a4(page):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.1 or abs(h - A4_H) > 0.1:
        page.scale_to(A4_W, A4_H)
    return page


def main():
    writer = PdfWriter()
    cover_page = PdfReader(COVER).pages[0]
    writer.add_page(normalize_page_to_a4(cover_page))
    for page in PdfReader(BODY).pages:
        writer.add_page(normalize_page_to_a4(page))
    writer.add_metadata({
        '/Title': 'The Fundamental Higher Consciousness Premise: Audit and '
                  'Consolidation, Revised Edition',
        '/Author': 'Z.ai',
        '/Creator': 'Z.ai',
        '/Subject': 'Adjudicated steelman audit and consolidation of a '
                    'consciousness-first corpus: 130-turn dialogue, 53-turn '
                    'DeepSeek exchange, consolidation treatise, and two '
                    'external audits',
    })
    with open(OUT, 'wb') as f:
        writer.write(f)
    size = os.path.getsize(OUT)
    print('MERGED:', OUT, '(%.1f KB, %d pages)' % (size / 1024.0, len(writer.pages)))


if __name__ == '__main__':
    main()
