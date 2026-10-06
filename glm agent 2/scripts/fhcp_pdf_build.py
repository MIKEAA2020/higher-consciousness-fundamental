#!/usr/bin/env python3
"""Main assembly: builds the FHCP steelman audit body PDF (chapters 1-12).

Pipeline position: body PDF only (no cover in story). Cover is rendered
separately via html2poster.js and merged by fhcp_pdf_merge.py.

Usage: python3 fhcp_pdf_build.py
Output: fhcp_body.pdf (next to this script)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fhcp_pdf_lib as L
import fhcp_pdf_part1
import fhcp_pdf_part2
import fhcp_pdf_part3
import fhcp_pdf_part4

from reportlab.platypus import Paragraph, PageBreak, Spacer
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fhcp_body.pdf')


def build():
    story = []

    # ── Front matter: Table of Contents ────────────────────────────────
    story.append(Paragraph('<b>Table of Contents</b>', L.S['toc_title']))
    toc = TableOfContents()
    toc.levelStyles = [L.S['toc0'], L.S['toc1']]
    toc.dotsMinLevel = 0            # dot leaders on all levels
    story.append(toc)
    story.append(PageBreak())

    # ── Body start marker: switches footer to arabic numbering ────────
    story.append(L.BodyStartMarker())

    # ── Chapters 1-12 from the four part modules ──────────────────────
    for mod in (fhcp_pdf_part1, fhcp_pdf_part2,
                fhcp_pdf_part3, fhcp_pdf_part4):
        mod.add_content(story)

    doc = L.TocDocTemplate(
        OUT,
        pagesize=(L.PAGE_W, L.PAGE_H),
        leftMargin=L.MARGIN, rightMargin=L.MARGIN,
        topMargin=L.MARGIN, bottomMargin=L.MARGIN,
        title=L.DOC_TITLE,
        author=L.DOC_AUTHOR,
        creator='Z.ai',
        subject='Steelman audit and consolidation of a consciousness-first '
                'metaphysical dialogue (11,087-line transcript)',
    )
    doc.multiBuild(story, onFirstPage=L.paint_page, onLaterPages=L.paint_page)

    size = os.path.getsize(OUT)
    print('BUILT:', OUT, '(%.1f KB)' % (size / 1024.0))


if __name__ == '__main__':
    build()
