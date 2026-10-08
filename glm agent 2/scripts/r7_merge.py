#!/usr/bin/env python3
"""Merge the Seventh Edition (Parameter-Map Edition): cover + body ->
final PDF in download/."""
import os

from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
COVER = os.path.join(HERE, 'r7_cover.pdf')
BODY = os.path.join(HERE, 'r7_body.pdf')
OUT = ('/home/z/my-project/download/'
       'Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation_'
       'Parameter-Map-Ed.pdf')

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
                  'Consolidation, Seventh Edition (Parameter-Map Edition)',
        '/Author': 'Z.ai',
        '/Creator': 'Z.ai',
        '/Subject': 'The neural parameter map verdict corrected and the '
                    'assembly specified: five newly-read sources, the '
                    'fragments-and-assembly statement, and the concrete '
                    'seven-phase Level-2 decombination protocol',
    })
    with open(OUT, 'wb') as f:
        writer.write(f)
    size = os.path.getsize(OUT)
    print('MERGED:', OUT, '(%.1f KB, %d pages)' % (size / 1024.0,
                                                   len(writer.pages)))


if __name__ == '__main__':
    main()
