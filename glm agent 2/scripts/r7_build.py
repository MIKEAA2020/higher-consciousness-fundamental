#!/usr/bin/env python3
"""Main assembly: builds the Seventh Edition (Parameter-Map Edition)
body PDF (chapters 1-8).

Pipeline position: body PDF only (no cover in story). Cover is rendered
separately via html2poster.js and merged by r7_merge.py.

Usage: python3 r7_build.py
Output: r7_body.pdf (next to this script)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fhcp_pdf_lib as L
import r7_part1
import r7_part2
import r7_part3
import r7_part4
import r7_part5

from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r7_body.pdf')


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

    # -- Chapters 1-8 from the five part modules -------------------------
    for mod in (r7_part1, r7_part2, r7_part3, r7_part4, r7_part5):
        mod.add_content(story)

    doc = L.TocDocTemplate(
        OUT,
        pagesize=(L.PAGE_W, L.PAGE_H),
        leftMargin=L.MARGIN, rightMargin=L.MARGIN,
        topMargin=L.MARGIN, bottomMargin=L.MARGIN,
        title='The Fundamental Higher Consciousness Premise: Audit and '
              'Consolidation, Seventh Edition (Parameter-Map Edition)',
        author=L.DOC_AUTHOR,
        creator='Z.ai',
        subject='The neural parameter map verdict corrected and the '
                'assembly specified: five newly-read sources (the Virtual '
                'Epileptic Patient, hierarchical critical synchronization, '
                'serotonin receptor parameterization, ketanserin blockade, '
                'metabolic connectivity mapping), the fragments-and-'
                'assembly statement for requirement 4, and the concrete '
                'seven-phase Level-2 decombination protocol with named '
                'methods, data, nulls, and failure conditions',
    )
    doc.multiBuild(story, onFirstPage=L.paint_page, onLaterPages=L.paint_page)

    size = os.path.getsize(OUT)
    print('BUILT:', OUT, '(%.1f KB)' % (size / 1024.0))


if __name__ == '__main__':
    build()
