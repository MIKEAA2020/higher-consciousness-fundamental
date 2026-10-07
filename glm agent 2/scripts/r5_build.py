#!/usr/bin/env python3
"""Main assembly: builds the Fifth Edition (Anchored Edition) audit
body PDF (chapters 1-14 + Appendix A).

Pipeline position: body PDF only (no cover in story). Cover is rendered
separately via html2poster.js and merged by r5_merge.py.

Usage: python3 r5_build.py
Output: r5_body.pdf (next to this script)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fhcp_pdf_lib as L
import r5_part1
import r5_part2
import r5_part3
import r5_part4
import r5_part5
import r5_part6

from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r5_body.pdf')


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
    for mod in (r5_part1, r5_part2, r5_part3, r5_part4, r5_part5, r5_part6):
        mod.add_content(story)

    doc = L.TocDocTemplate(
        OUT,
        pagesize=(L.PAGE_W, L.PAGE_H),
        leftMargin=L.MARGIN, rightMargin=L.MARGIN,
        topMargin=L.MARGIN, bottomMargin=L.MARGIN,
        title='The Fundamental Higher Consciousness Premise: Audit and '
              'Consolidation, Fifth Edition (Anchored Edition)',
        author=L.DOC_AUTHOR,
        creator='Z.ai',
        subject='Anchored steelman audit and consolidation of a '
                'consciousness-first corpus: twelve auditing parties, the '
                'adversarial adjudication of the external Claude audit, the '
                'recorded contingency critiques, and the three empirical '
                'anchors of the decombination program',
    )
    doc.multiBuild(story, onFirstPage=L.paint_page, onLaterPages=L.paint_page)

    size = os.path.getsize(OUT)
    print('BUILT:', OUT, '(%.1f KB)' % (size / 1024.0))


if __name__ == '__main__':
    build()
