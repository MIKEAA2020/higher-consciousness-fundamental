#!/usr/bin/env python3
"""Extract conversation with clean flowing text (collapse inline breaks)."""
import re
from bs4 import BeautifulSoup

HTML_PATH = '/home/z/my-project/qwen_chat.html'
OUT_PATH = '/home/z/my-project/qwen_conversation_clean.md'

def clean_text(el):
    """Extract text where block elements produce paragraph breaks but inline text flows."""
    # Use get_text with no separator, but first mark block boundaries
    for tag in el.find_all(['p', 'div', 'li', 'h1', 'h2', 'h3', 'h4', 'br', 'tr']):
        if tag.name == 'br':
            tag.replace_with('\n')
        else:
            tag.append('\n')  # mark end of block
    text = el.get_text()
    # Collapse: single newlines from inline wrapping -> space; double+ -> paragraph break
    lines = text.split('\n')
    # Join fragments: lines that don't end a sentence/paragraph get merged
    out = []
    buf = []
    for line in lines:
        line = line.strip()
        if not line:
            if buf:
                out.append(' '.join(buf))
                buf = []
        else:
            buf.append(line)
    if buf:
        out.append(' '.join(buf))
    # Merge very short fragments (math rendering artifacts) into previous paragraph
    merged = []
    for para in out:
        if merged and (len(para) < 4 or (len(para) < 30 and not para[0].isupper() and not para[0].isdigit())):
            merged[-1] += ' ' + para
        else:
            merged.append(para)
    return '\n\n'.join(merged)

def main():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        raw = f.read()

    soup = BeautifulSoup(raw, 'html.parser')
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()

    messages = []
    for container in soup.find_all('div', class_=re.compile(r'qwen-chat-message-(user|assistant)')):
        cls = container.get('class', [])
        if 'qwen-chat-message-user' in cls:
            role = 'USER'
            content_divs = container.find_all(class_=re.compile(r'user-message-content'))
            if not content_divs:
                content_divs = container.find_all('div', class_='chat-user-message')
        elif 'qwen-chat-message-assistant' in cls:
            role = 'ASSISTANT'
            content_divs = container.find_all('div', class_=re.compile(r'response-message-content'))
        else:
            continue

        texts = []
        for cd in content_divs:
            t = clean_text(cd)
            if t.strip():
                texts.append(t.strip())
        text = '\n\n'.join(texts)
        if text.strip():
            messages.append((role, text.strip()))

    print(f'Extracted {len(messages)} messages, total {sum(len(t) for _, t in messages)} chars')
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        for i, (role, text) in enumerate(messages, 1):
            f.write(f"### [{i}] {role}\n\n{text}\n\n---\n\n")
    print(f'Saved to {OUT_PATH}')

if __name__ == '__main__':
    main()
