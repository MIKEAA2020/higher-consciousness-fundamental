#!/usr/bin/env python3
"""Main assembly: builds the Eighth Edition (Computed Edition)
body PDF (chapters 1-8).

Pipeline position: body PDF only (no cover in story). Cover is rendered
separately via html2poster.js and merged by r8_merge.py.

Usage: python3 r8_build.py
Output: r8_body.pdf (next to this script)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fhcp_pdf_lib as L
import r8_part1
import r8_part2
import r8_part3
import r8_part4
import r8_part5

from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r8_body.pdf')


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
    for mod in (r8_part1, r8_part2, r8_part3, r8_part4, r8_part5):
        mod.add_content(story)

    doc = L.TocDocTemplate(
        OUT,
        pagesize=(L.PAGE_W, L.PAGE_H),
        leftMargin=L.MARGIN, rightMargin=L.MARGIN,
        topMargin=L.MARGIN, bottomMargin=L.MARGIN,
        title='The Fundamental Higher Consciousness Premise: Audit and '
              'Consolidation, Eighth Edition (Computed Edition)',
        author=L.DOC_AUTHOR,
        creator='Z.ai',
        subject='The Level-2 protocol\u2019s first two phases executed '
                'on open data \u2014 coupling and criticality estimation '
                'on seven connectomes with the honest structure-function '
                'negative, the beta sedation ordering passed in its clean '
                'form \u2014 and the Farnes et al. 2020 corpus resolved '
                'through the Raw_data_2 release: the evoked-LZ contrast '
                'completed with the R32 reshape repair, the three-layer '
                'result reproducing the paper\u2019s spontaneous-yes-'
                'evoked-no dissociation, and the spontaneous LZc '
                'replication',
    )
    doc.multiBuild(story, onFirstPage=L.paint_page, onLaterPages=L.paint_page)

    size = os.path.getsize(OUT)
    print('BUILT:', OUT, '(%.1f KB)' % (size / 1024.0))


if __name__ == '__main__':
    build()
