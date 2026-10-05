#!/usr/bin/env python3
"""Extract the full conversation (user + assistant messages) from Qwen share page HTML."""
import re
import html as htmllib

HTML_PATH = '/home/z/my-project/qwen_chat.html'
OUT_PATH = '/home/z/my-project/qwen_conversation.md'

def main():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        raw = f.read()

    # The rendered conversation begins around index 2322000. Find message containers.
    # User message content: <p class="...user-message-content ...">TEXT</p>
    # We need to figure out assistant message container class names.
    conv_start = 2322000
    conv = raw[conv_start:]

    # Find all class names containing 'message'
    classes = set(re.findall(r'class="([^"]*message[^"]*)"', conv))
    print('Message-related classes:')
    for c in sorted(classes):
        print('  -', c)

    print()
    # Find assistant-side classes
    classes2 = set(re.findall(r'class="([^"]*assistant[^"]*)"', conv))
    print('Assistant-related classes:')
    for c in sorted(classes2):
        print('  -', c)

    classes3 = set(re.findall(r'class="([^"]*chat-[^"]*)"', conv))
    print('Chat-related classes (unique, first 30):')
    for c in sorted(classes3)[:30]:
        print('  -', c)

if __name__ == '__main__':
    main()
