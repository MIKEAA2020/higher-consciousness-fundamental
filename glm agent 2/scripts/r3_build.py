#!/usr/bin/env python3
"""Main assembly: builds the Revised Edition (Third Edition) audit body PDF
(chapters 1-14 + Appendix A).

Pipeline position: body PDF only (no cover in story). Cover is rendered
separately via html2poster.js and merged by r3_merge.py.

Usage: python3 r3_build.py
Output: r3_body.pdf (next to this script)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fhcp_pdf_lib as L
import r3_part1
import r3_part2
import r3_part3
import r3_part4
import r3_part5

from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r3_body.pdf')


def build():
    story = []

    # -- Front matter: Table of Contents --------------------------------
    story.append(Paragraph('<b>Table of Contents</b>', L.S['toc_title']))
    toc = TableOfContents()
    toc.levelStyles = [L.S['toc0'], L.S['toc1']]
    toc.dotsMinLevel = 0
    story.append(toc)
    story.append(PageBreak())

    # -- Body start marker: switches footer to arabic numbering ---------
    story.append(L.BodyStartMarker())

    # -- Chapters 1-14 + Appendix A from the five part modules ----------
    for mod in (r3_part1, r3_part2, r3_part3, r3_part4, r3_part5):
        mod.add_content(story)

    doc = L.TocDocTemplate(
        OUT,
        pagesize=(L.PAGE_W, L.PAGE_H),
        leftMargin=L.MARGIN, rightMargin=L.MARGIN,
        topMargin=L.MARGIN, bottomMargin=L.MARGIN,
        title='The Fundamental Higher Consciousness Premise: Audit and '
              'Consolidation, Revised Edition',
        author=L.DOC_AUTHOR,
        creator='Z.ai',
        subject='Adjudicated steelman audit and consolidation of a '
                'consciousness-first corpus: 130-turn dialogue, 53-turn '
                'DeepSeek exchange, consolidation treatise, and two '
                'external audits',
    )
    doc.multiBuild(story, onFirstPage=L.paint_page, onLaterPages=L.paint_page)

    size = os.path.getsize(OUT)
    print('BUILT:', OUT, '(%.1f KB)' % (size / 1024.0))


if __name__ == '__main__':
    build()
