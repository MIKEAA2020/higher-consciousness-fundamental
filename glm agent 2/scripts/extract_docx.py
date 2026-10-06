#!/usr/bin/env python3
"""Extract full text from the previous audit .docx into a markdown research file.

Handles paragraphs (with heading detection), tables (pipe rows), and preserves
order. No external dependencies (zipfile + ElementTree only).
"""
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
}

def w(tag):
    return '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}' + tag

def para_text(p):
    parts = []
    for node in p.iter():
        if node.tag == w('t'):
            parts.append(node.text or '')
        elif node.tag == w('tab'):
            parts.append('\t')
        elif node.tag == w('br'):
            parts.append(' ')
    return ''.join(parts).strip()

def para_style(p):
    ppr = p.find(w('pPr'))
    if ppr is None:
        return ''
    st = ppr.find(w('pStyle'))
    if st is None:
        return ''
    return st.get(w('val'), '')

def walk_body(body, out):
    for child in body:
        if child.tag == w('p'):
            text = para_text(child)
            if not text:
                continue
            style = para_style(child)
            if 'Heading' in style or 'Title' in style:
                try:
                    level = int(''.join(c for c in style if c.isdigit()) or '1')
                except ValueError:
                    level = 1
                out.append('#' * min(level + 1, 6) + ' ' + text)
            else:
                out.append(text)
            out.append('')
        elif child.tag == w('tbl'):
            rows = []
            for tr in child.findall(w('tr')):
                cells = []
                for tc in tr.findall(w('tc')):
                    cell_parts = []
                    for p in tc.iter(w('p')):
                        t = para_text(p)
                        if t:
                            cell_parts.append(t)
                    cells.append(' / '.join(cell_parts))
                rows.append('| ' + ' | '.join(cells) + ' |')
            if rows:
                sep = '| ' + ' | '.join(['---'] * (rows[0].count('|') - 1)) + ' |'
                out.append(rows[0])
                out.append(sep)
                out.extend(rows[1:])
                out.append('')

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    with zipfile.ZipFile(src) as z:
        xml = z.read('word/document.xml')
    root = ET.fromstring(xml)
    body = root.find(w('body'))
    out = []
    walk_body(body, out)
    text = '\n'.join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(text)
    words = len(text.split())
    print(f'extracted {words} words -> {dst}')

if __name__ == '__main__':
    main()
