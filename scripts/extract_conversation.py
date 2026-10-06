#!/usr/bin/env python3
"""Extract full conversation from Qwen share page HTML using BeautifulSoup."""
import re
import html as htmllib
from bs4 import BeautifulSoup

HTML_PATH = '/home/z/my-project/qwen_chat.html'
OUT_PATH = '/home/z/my-project/qwen_conversation.md'

def get_text_safe(el):
    """Get text preserving paragraph breaks."""
    return el.get_text('\n', strip=True)

def main():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Conversation region only (before it is app shell/JS)
    soup = BeautifulSoup(raw, 'html.parser')

    # Remove script and style tags entirely
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()

    # Find all message containers in order: qwen-chat-message-user / qwen-chat-message-assistant
    messages = []
    for container in soup.find_all('div', class_=re.compile(r'qwen-chat-message-(user|assistant)')):
        cls = container.get('class', [])
        if 'qwen-chat-message-user' in cls:
            role = 'USER'
        elif 'qwen-chat-message-assistant' in cls:
            role = 'ASSISTANT'
        else:
            continue

        # User message content
        if role == 'USER':
            # May be multiple paragraphs; find the user-message-content or chat-user-message
            content_divs = container.find_all(class_=re.compile(r'user-message-content'))
            if not content_divs:
                content_divs = container.find_all('div', class_='chat-user-message')
            texts = []
            for cd in content_divs:
                t = cd.get_text('\n', strip=True)
                if t:
                    texts.append(t)
            text = '\n'.join(texts)
        else:
            # Assistant message: response-message-content divs (may exclude thinking cards)
            content_divs = container.find_all('div', class_=re.compile(r'response-message-content'))
            texts = []
            for cd in content_divs:
                t = cd.get_text('\n', strip=True)
                if t:
                    texts.append(t)
            text = '\n'.join(texts)

        if text.strip():
            messages.append((role, text.strip()))

    print(f'Extracted {len(messages)} messages')
    total_chars = sum(len(t) for _, t in messages)
    print(f'Total text chars: {total_chars}')

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        for i, (role, text) in enumerate(messages, 1):
            f.write(f"{'='*80}\n[{i}] {role}\n{'='*80}\n")
            f.write(text)
            f.write('\n\n')
    print(f'Saved to {OUT_PATH}')

    # Print summary of each message (first 150 chars)
    for i, (role, text) in enumerate(messages, 1):
        preview = text[:150].replace('\n', ' | ')
        print(f'[{i:2d}] {role:9s} ({len(text):6d} chars): {preview}')

if __name__ == '__main__':
    main()
