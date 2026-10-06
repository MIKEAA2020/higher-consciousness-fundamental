#!/usr/bin/env python3
"""Build the full markdown transcript of Qwen share 68292366 from qwen2_messages.jsonl.

Handles the double-encoded JSON that agent-browser eval returns
(each line is a JSON-string containing the message object).
Output: /home/z/my-project/qwen2_chat_transcript.md
"""
import json
import sys

IN_PATH = sys.argv[1] if len(sys.argv) > 1 else '/home/z/my-project/qwen2_messages.jsonl'
OUT_PATH = sys.argv[2] if len(sys.argv) > 2 else '/home/z/my-project/qwen2_chat_transcript.md'
TITLE = sys.argv[3] if len(sys.argv) > 3 else 'Fundamental Higher Consciousness Premise (share 68292366, October 05 2026)'

def decode_line(line):
    line = line.strip()
    if not line:
        return None
    obj = json.loads(line)          # outer JSON string (or object)
    if isinstance(obj, str):
        obj = json.loads(obj)       # inner JSON object
    return obj

def main():
    messages = []
    bad = 0
    with open(IN_PATH, encoding='utf-8') as f:
        for line in f:
            try:
                obj = decode_line(line)
            except Exception:
                bad += 1
                continue
            if isinstance(obj, dict) and 'err' not in obj and 'text' in obj:
                messages.append(obj)
            elif isinstance(obj, dict) and 'err' in obj:
                bad += 1

    # sort by original index in case of ordering surprises
    messages.sort(key=lambda m: m['i'])

    total_chars = sum(len(m['text']) for m in messages)
    with open(OUT_PATH, 'w', encoding='utf-8') as out:
        out.write(f'# {TITLE}\n\n')
        out.write(f'Extracted {len(messages)} messages '
                  f'({sum(1 for m in messages if m["role"]=="USER")} user, '
                  f'{sum(1 for m in messages if m["role"]=="ASSISTANT")} assistant), '
                  f'{total_chars:,} characters total.\n\n')
        out.write('---\n\n')
        for m in messages:
            role = 'USER' if m['role'] == 'USER' else 'ASSISTANT'
            n = m['i'] + 1
            out.write(f'## [{n}] {role}\n\n')
            text = m['text'].strip()
            out.write(text + '\n\n')
        # line count for the reading pass
    with open(OUT_PATH, encoding='utf-8') as f:
        lines = sum(1 for _ in f)
    print(f'messages: {len(messages)} (bad lines: {bad}), chars: {total_chars:,}, lines: {lines}')
    print(f'transcript: {OUT_PATH}')

if __name__ == '__main__':
    main()
