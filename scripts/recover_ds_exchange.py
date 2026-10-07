#!/usr/bin/env python3
"""Recover the full 53-turn DeepSeek exchange from the mangled share API response.

Body structure discovered:
  JSON1 (valid): messages with ids 1-12 and 65-106 (54 objects)
  Extra (raw slice, starts mid-string): ...duplicate-tail of an earlier message object,
  then message objects 13..64, trailing cut mid-string.

Recovery: regex-locate every `"message_id":N` in the extra, brace-match each object,
tolerant-parse, merge with JSON1 by message_id, emit a full ordered transcript.
"""
import json
import re

SRC = "/home/z/my-project/glm agent 2/research/ds_chunks/ds_share_content.json"
DST_FULL = "/home/z/my-project/glm agent 2/research/deepseek_exchange_full.json"
DST_MD = "/home/z/my-project/glm agent 2/research/deepseek_exchange_transcript.md"

raw = open(SRC, encoding="utf-8").read()
obj, end = json.JSONDecoder().raw_decode(raw)
base_msgs = {m["message_id"]: m for m in obj["data"]["biz_data"]["messages"]}
extra = raw[end:]

# --- locate message objects in the extra ---
id_matches = list(re.finditer(r'"message_id":(\d+)', extra))
objects = {}
orphan_prefix = None
for i, m in enumerate(id_matches):
    mid = int(m.group(1))
    # find the opening brace of this object: nearest '{' before the match
    brace = extra.rfind("{", 0, m.start())
    if brace < 0:
        continue
    if i == 0:
        orphan_prefix = extra[:brace]  # content before the first object
    # span end: opening brace of next object, or end of extra
    if i + 1 < len(id_matches):
        next_brace = extra.rfind("{", 0, id_matches[i + 1].start())
        span = extra[brace:next_brace]
    else:
        span = extra[brace:]
    # tolerant parse: trim trailing ',' and unmatched braces
    text = span.rstrip()
    if text.endswith(","):
        text = text[:-1]
    parsed = None
    for trim in range(0, 4):
        candidate = text
        # ensure balanced braces: append missing closers
        opens = candidate.count("{") - candidate.count("}")
        if opens > 0:
            candidate = candidate + "}" * opens
        try:
            parsed = json.loads(candidate)
            break
        except json.JSONDecodeError:
            # try cutting back to the last complete '}' and closing
            cut = candidate.rfind("}")
            if cut < 0:
                break
            candidate = candidate[: cut + 1] + "}" * max(0, opens)
            try:
                parsed = json.loads(candidate)
                break
            except json.JSONDecodeError:
                continue
    if parsed and "message_id" in parsed:
        objects[mid] = parsed

print(f"Recovered {len(objects)} message objects from extra: ids {sorted(objects)[:5]}..{sorted(objects)[-5:]}")
if orphan_prefix is not None:
    print(f"Orphan prefix before first object: {len(orphan_prefix)} chars; head: {orphan_prefix[:120]!r}")

# --- merge ---
merged = dict(base_msgs)
dups = []
for mid, m in objects.items():
    if mid in merged:
        dups.append(mid)
    merged[mid] = m
all_ids = sorted(merged)
print(f"Merged message count: {len(merged)} (ids {all_ids[0]}..{all_ids[-1]})")
missing = [i for i in range(all_ids[0], all_ids[-1] + 1) if i not in merged]
print(f"Missing ids in sequence: {missing}")
print(f"Duplicate ids overwritten from extra: {dups}")

# --- completeness check ---
def frag_summary(m):
    out = []
    for f in m.get("fragments", []):
        c = f.get("content") or ""
        out.append((f["type"], len(c)))
    return out

problems = []
for mid in all_ids:
    m = merged[mid]
    role = m["role"]
    frags = m.get("fragments", [])
    has_resp = any(f["type"] == "RESPONSE" for f in frags)
    has_req = any(f["type"] == "REQUEST" for f in frags)
    if role == "ASSISTANT" and not has_resp:
        problems.append((mid, "assistant missing RESPONSE"))
    if role == "USER" and not has_req:
        problems.append((mid, "user missing REQUEST"))
    # check response ends with sentence-final punctuation
    for f in frags:
        if f["type"] == "RESPONSE":
            c = (f.get("content") or "").rstrip()
            if c and c[-1] not in ".!?\"')]}:;":
                problems.append((mid, f"response ends abruptly: ...{c[-60:]!r}"))
print("Problems:", problems if problems else "none")

json.dump({"messages": [merged[i] for i in all_ids]}, open(DST_FULL, "w", encoding="utf-8"), ensure_ascii=False)
print(f"Wrote {DST_FULL}")

# --- transcript ---
out = ["# DeepSeek Exchange (share ei9y81lsr98ujftn91) — full reconstruction\n"]
turn = 0
for mid in all_ids:
    m = merged[mid]
    role = m["role"]
    if role == "USER":
        turn += 1
        out.append(f"\n\n### USER [T{turn} | msg {mid}]\n")
        for f in m.get("fragments", []):
            if f["type"] == "REQUEST":
                out.append((f.get("content") or "").strip() + "\n")
            elif f["type"] == "FILE":
                out.append(f"\n[ATTACHED FILE: {f.get('file_name', '?')} — {len(f.get('content') or '')} chars]\n")
    else:
        out.append(f"\n\n### ASSISTANT [T{turn} | msg {mid}]\n")
        for f in m.get("fragments", []):
            if f["type"] == "THINK":
                out.append(f"<reasoning {len(f.get('content') or '')} chars>\n{(f.get('content') or '').strip()}\n</reasoning>\n")
            elif f["type"] == "RESPONSE":
                out.append((f.get("content") or "").strip() + "\n")

text = "".join(out)
open(DST_MD, "w", encoding="utf-8").write(text)
print(f"Wrote {DST_MD}: {len(text)} chars, {text.count(chr(10))} lines, {turn} turns")
print("Ends with scaffold phrase:", "That is the most honest and useful answer I can give." in text)
print("Contains privation directive:", "darkness is absence of light" in text)
