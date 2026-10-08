#!/usr/bin/env python3
"""Revised Edition, Part 5: Appendix A - The Complete Turn Index.

Rows are computed at build time directly from the read-only source
transcript, so the coverage record cannot drift from the file it records.
"""
import html
import re

import fhcp_pdf_lib as L

SRC = '/home/z/my-project/upload/chat-Fundamental Higher Consciousness Premise.txt'


def _clean(text):
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
    text = re.sub(r'[\u200b-\u200f\u2028-\u202f\u2060\ufeff]', '', text)
    return text


def _load_turns():
    """Return [(turn, user_range, asst_range, opening)] from the transcript."""
    lines = [None] + _clean(open(SRC, encoding='utf-8').read()).split('\n')
    markers = []
    for i, line in enumerate(lines[1:], start=1):
        if line == '### USER':
            markers.append(('USER', i))
        elif line == '### ASSISTANT':
            markers.append(('ASSISTANT', i))
    turns = []
    idx = 0
    n = len(markers)
    while idx + 1 < n:
        role, uline = markers[idx]
        role2, aline = markers[idx + 1]
        if role != 'USER' or role2 != 'ASSISTANT':
            idx += 1
            continue
        # user message text: lines after the marker until the assistant marker
        nxt = aline - 1
        text_lines = [lines[j].strip() for j in range(uline + 1, min(nxt, uline + 12) + 1) if lines[j].strip()]
        opening = ' '.join(text_lines)[:64]
        # assistant range ends where the next USER marker begins (or EOF)
        end = markers[idx + 2][1] - 1 if idx + 2 < n else len(lines) - 1
        turns.append((len(turns) + 1, (uline, nxt), (aline, end), opening))
        idx += 2
    return turns


def add_content(story):
    L.h1(story, 'Appendix A. The Complete Turn Index')

    L.body(story,
           'This appendix is the coverage record for the dialogue source. '
           'The transcript contains exactly 130 user\u2013assistant turn '
           'pairs in strict alternation; every line of the 11,088-line '
           'file falls inside an indexed message. Each row gives the turn '
           'number, the line range of the user message, the line range of '
           'the assistant reply, and the verbatim opening of the user '
           'message (truncated where long; spelling as in the source). '
           'The audit\u2019s claims in chapters 3 through 11 cite lines '
           'within these ranges; the index is the instrument that makes '
           'every citation checkable against the whole. The companion '
           'record for the DeepSeek exchange is the message-space index '
           'of \u00a72.2: 106 messages, 53 turns, 52 of them recovered '
           'from the displaced fragment, with the three source-critical '
           'notes attached.')

    turns = _load_turns()
    assert len(turns) == 130, f'expected 130 turns, found {len(turns)}'
    last_end = turns[-1][2][1]
    assert last_end <= 11088, f'last line {last_end} exceeds file length'

    rows = []
    for t, (u0, u1), (a0, a1), opening in turns:
        rows.append([
            str(t),
            f'{u0}\u2013{u1}',
            f'{a0}\u2013{a1}',
            html.escape(opening),
        ])

    L.data_table(
        story,
        f'Table A1. The 130 turns of chat-Fundamental Higher Consciousness '
        f'Premise.txt (verbatim openings; coverage = all '
        f'{last_end} of 11,088 lines).',
        ['Turn', 'User lines', 'Assistant lines',
         'Opening of user message (verbatim, truncated)'],
        rows,
        [0.06, 0.13, 0.14, 0.67], font_size=7.6, header_font=8.2)

    L.body(story,
           'The exchange\u2019s turn map, for reference: T1\u2013T5 '
           'phenomenal concepts and the entry; T4\u2013T13 the ascent '
           '(self-sufficiency, mathematics tested, brute fact and regress '
           'eliminated, ipsum esse); T14\u2013T22 external critiques and '
           'the steelmanned contingency proof; T23\u2013T33 the quest, the '
           'eliminative program, and the privation turn (T32\u2013T33, '
           'with the message-64 reply lost); T34\u2013T43 the maze and '
           'the successive deletion of process vocabulary; T44\u2013T49 '
           'the impasse; T50\u2013T51 the G\u00f6del analysis and the '
           'two-truth synthesis; T52\u2013T53 the lighthouse and scaffold '
           'verdicts. The consolidation treatise contributes its four '
           'turns; the external audits, their two registers; the prior '
           'editions, the lineage that this revised edition adjudicates '
           'and completes.')
