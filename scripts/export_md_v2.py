#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export the analysis content as the companion Markdown deliverable (GitHub-friendly)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import critique_content_v2 as C

OUT = os.path.join(C.BASE_DIR if hasattr(C, 'BASE_DIR') else '/home/z/my-project',
                   'download', 'the_dream_that_must_be_v2_trilogy_edition.md')

def md_cell(text):
    return text.replace('|', '\\|').replace('\n', ' ')

lines = []
lines.append('# ' + C.DOC_TITLE)
lines.append('')
lines.append('**' + C.DOC_SUBTITLE + '**')
lines.append('')
lines.append('*' + C.DOC_AUTHOR + ' · ' + C.DOC_DATE + '*')
lines.append('')
lines.append('> ' + C.META_NOTE)
lines.append('')
lines.append('## Contents')
for s in C.SECTIONS:
    lines.append('%s. [%s](#%s)' % (s['num'], s['title'],
                                    (s['num'] + '-' + s['title'].lower()
                                     .replace(' ', '-').replace(':', '').replace('/', '')
                                     .replace(',', '').replace('—', '').replace("'", ''))))
lines.append('')
for s in C.SECTIONS:
    lines.append('')
    lines.append('## ' + s['num'] + '. ' + s['title'])
    lines.append('')
    for kind, payload in s['blocks']:
        if kind == 'body':
            lines.append(payload)
            lines.append('')
        elif kind == 'h2':
            lines.append('### ' + payload)
            lines.append('')
        elif kind == 'quote':
            lines.append('> ' + payload.replace('\n', '\n> '))
            lines.append('')
        elif kind == 'table':
            lines.append('| ' + ' | '.join(md_cell(h) for h in payload['header']) + ' |')
            lines.append('|' + '---|' * len(payload['header']))
            for row in payload['rows']:
                lines.append('| ' + ' | '.join(md_cell(c) for c in row) + ' |')
            lines.append('')
            lines.append('*' + payload['caption'] + '*')
            lines.append('')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines).rstrip() + '\n')
print('markdown written:', OUT, '|', len(open(OUT).read().split()), 'words')
