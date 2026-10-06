#!/usr/bin/env python3
"""Merge cover + body into the final FHCP steelman audit PDF.

Normalizes all pages to A4, inserts the cover as page 0, sets metadata.
"""
import os

from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
COVER = os.path.join(HERE, 'fhcp_cover.pdf')
BODY = os.path.join(HERE, 'fhcp_body.pdf')
OUT = '/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_Steelman-Audit-and-Consolidation.pdf'

A4_W, A4_H = 595.28, 841.89  # A4 in points


def normalize_page_to_a4(page):
    """Scale a page to A4 if its dimensions do not match."""
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
        '/Title': 'The Fundamental Higher Consciousness Premise: '
                  'A Steelman Audit and Consolidation',
        '/Author': 'Z.ai',
        '/Creator': 'Z.ai',
        '/Subject': 'Steelman audit and consolidation of a consciousness-first '
                    'metaphysical dialogue (11,087-line transcript)',
    })

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'wb') as f:
        writer.write(f)

    size = os.path.getsize(OUT)
    n = len(PdfReader(OUT).pages)
    print('MERGED:', OUT, '(%d pages, %.1f KB)' % (n, size / 1024.0))


if __name__ == '__main__':
    main()
