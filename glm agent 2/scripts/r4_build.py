#!/usr/bin/env python3
"""Main assembly: builds the Fourth Edition (Strengthened Edition) audit
body PDF (chapters 1-14 + Appendix A).

Pipeline position: body PDF only (no cover in story). Cover is rendered
separately via html2poster.js and merged by r4_merge.py.

Usage: python3 r4_build.py
Output: r4_body.pdf (next to this script)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fhcp_pdf_lib as L
import r4_part1
import r4_part2
import r4_part3
import r4_part4
import r4_part5
import r4_part6

from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r4_body.pdf')


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

    # -- Chapters 1-14 + Appendix A from the six part modules -----------
    for mod in (r4_part1, r4_part2, r4_part3, r4_part4, r4_part5, r4_part6):
        mod.add_content(story)

    doc = L.TocDocTemplate(
        OUT,
        pagesize=(L.PAGE_W, L.PAGE_H),
        leftMargin=L.MARGIN, rightMargin=L.MARGIN,
        topMargin=L.MARGIN, bottomMargin=L.MARGIN,
        title='The Fundamental Higher Consciousness Premise: Audit and '
              'Consolidation, Fourth Edition (Strengthened Edition)',
        author=L.DOC_AUTHOR,
        creator='Z.ai',
        subject='Strengthened steelman audit and consolidation of a '
                'consciousness-first corpus across two dialogue lines and '
                'four DeepSeek exchanges: ten auditing parties, the '
                'convergence record, the eliminative program, the '
                'privation register, and the formal decombination program',
    )
    doc.multiBuild(story, onFirstPage=L.paint_page, onLaterPages=L.paint_page)

    size = os.path.getsize(OUT)
    print('BUILT:', OUT, '(%.1f KB)' % (size / 1024.0))


if __name__ == '__main__':
    build()
