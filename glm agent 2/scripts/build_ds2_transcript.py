#!/usr/bin/env python3
"""Round 9: build a lean transcript from a recovered DeepSeek share payload
(clean JSON form). Usage: python build_ds2_transcript.py <payload.json> <out.md> <share_id>"""
import json
import sys

SRC, DST, SHARE = sys.argv[1], sys.argv[2], sys.argv[3]

raw = open(SRC, encoding="utf-8").read()
obj, end = json.JSONDecoder().raw_decode(raw)
extra = raw[end:]
msgs = obj["data"]["biz_data"]["messages"]
by_id = {m["message_id"]: m for m in msgs}
all_ids = sorted(by_id)
missing = [i for i in range(all_ids[0], all_ids[-1] + 1) if i not in by_id]

problems = []
for mid in all_ids:
    m = by_id[mid]
    frags = m.get("fragments", [])
    if m["role"] == "ASSISTANT" and not any(f["type"] == "RESPONSE" for f in frags):
        problems.append((mid, "assistant missing RESPONSE"))
    if m["role"] == "USER" and not any(f["type"] == "REQUEST" for f in frags):
        problems.append((mid, "user missing REQUEST"))
    for f in frags:
        if f["type"] == "RESPONSE":
            c = (f.get("content") or "").rstrip()
            if c and c[-1] not in ".!?\"')]}:;":
                problems.append((mid, f"response ends abruptly: ...{c[-60:]!r}"))

print(f"messages: {len(by_id)} (ids {all_ids[0]}..{all_ids[-1]}), missing: {missing}")
print(f"extra raw tail: {len(extra)} chars")
print("problems:", problems if problems else "none")

out = [f"# DeepSeek Exchange (share {SHARE}) — full transcript, {sum(1 for m in by_id.values() if m['role']=='USER')} turns\n"]
turn = 0
files = 0
for mid in all_ids:
    m = by_id[mid]
    if m["role"] == "USER":
        turn += 1
        out.append(f"\n\n### USER [T{turn} | msg {mid}]\n")
        for f in m.get("fragments", []):
            if f["type"] == "REQUEST":
                out.append((f.get("content") or "").strip() + "\n")
            elif f["type"] == "FILE":
                files += 1
                out.append(f"\n[ATTACHED FILE: {f.get('file_name', '?')} — {len(f.get('content') or '')} chars, omitted]\n")
    else:
        out.append(f"\n\n### ASSISTANT [T{turn} | msg {mid}]\n")
        for f in m.get("fragments", []):
            if f["type"] == "RESPONSE":
                out.append((f.get("content") or "").strip() + "\n")
            elif f["type"] == "THINK":
                out.append(f"[reasoning trace: {len(f.get('content') or '')} chars, omitted]\n")

text = "".join(out)
open(DST, "w", encoding="utf-8").write(text)
lines = text.count("\n")
print(f"wrote {DST}: {len(text)} chars, {lines} lines, {turn} turns, {files} attached files")
