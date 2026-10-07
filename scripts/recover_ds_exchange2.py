#!/usr/bin/env python3
"""Finalize the recovered DeepSeek exchange: include msg 64 partial, emit lean + full transcripts."""
import json
import re

SRC = "/home/z/my-project/glm agent 2/research/ds_chunks/ds_share_content.json"
DST_FULL = "/home/z/my-project/glm agent 2/research/deepseek_exchange_full.json"
DST_MD = "/home/z/my-project/glm agent 2/research/deepseek_exchange_transcript.md"
DST_LEAN = "/home/z/my-project/glm agent 2/research/deepseek_exchange_lean.md"

raw = open(SRC, encoding="utf-8").read()
obj, end = json.JSONDecoder().raw_decode(raw)
base_msgs = {m["message_id"]: m for m in obj["data"]["biz_data"]["messages"]}
extra = raw[end:]

id_matches = list(re.finditer(r'"message_id":(\d+)', extra))
objects = {}
for i, m in enumerate(id_matches):
    mid = int(m.group(1))
    brace = extra.rfind("{", 0, m.start())
    if brace < 0:
        continue
    nxt = extra.rfind("{", 0, id_matches[i + 1].start()) if i + 1 < len(id_matches) else len(extra)
    span = extra[brace:nxt].rstrip().rstrip(",")
    parsed = None
    for _ in range(3):
        opens = span.count("{") - span.count("}")
        cand = span + "}" * max(0, opens)
        try:
            parsed = json.loads(cand)
            break
        except json.JSONDecodeError:
            cut = span.rfind("}")
            if cut < 0:
                break
            span = span[: cut + 1]
    if parsed and "message_id" in parsed:
        objects[mid] = parsed

# --- msg 64: manual recovery (object cut mid-THINK; RESPONSE deleted from share) ---
pos64 = extra.find('"message_id":64')
if pos64 >= 0 and 64 not in objects:
    tail = extra[pos64 - 1:]
    head = tail[: tail.find('"fragments"')]
    think_txt = ""
    fm = re.search(r'"type":"THINK","content":"(.*?)"\}?$', tail, re.S)
    if fm:
        think_txt = fm.group(1)
    # decode JSON string escapes for the think text
    try:
        think_dec = json.loads('"' + think_txt + '"')
    except Exception:
        think_dec = think_txt
    msg64 = {
        "message_id": 64, "parent_id": 63, "role": "ASSISTANT",
        "thinking_enabled": True, "status": "FINISHED",
        "fragments": [{"id": 1, "type": "THINK", "content": think_dec, "partial": True}],
        "_note": "RESPONSE fragment deleted from the share server-side; only the thinking trace (cut mid-sentence) survives in the raw API payload.",
    }
    objects[64] = msg64
    print(f"msg64 manual recovery: THINK {len(think_dec)} chars (partial)")

merged = dict(base_msgs)
merged.update(objects)
all_ids = sorted(merged)
print(f"Final merged: {len(merged)} messages, ids {all_ids[0]}..{all_ids[-1]}, missing: {[i for i in range(1,107) if i not in merged]}")

json.dump({"messages": [merged[i] for i in all_ids]}, open(DST_FULL, "w", encoding="utf-8"), ensure_ascii=False)

def render(include_think: bool):
    out = []
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
                    out.append(f"\n[ATTACHED FILE: {f.get('file_name', '?')} — {len(f.get('content') or '')} chars, omitted]\n")
        else:
            out.append(f"\n\n### ASSISTANT [T{turn} | msg {mid}]\n")
            if mid == 64:
                out.append("[NOTE: this reply's visible response was deleted from the share; only its reasoning trace survives, cut mid-sentence.]\n")
            for f in m.get("fragments", []):
                if f["type"] == "THINK" and include_think:
                    out.append(f"<reasoning {len(f.get('content') or '')} chars{' PARTIAL' if f.get('partial') else ''}>\n{(f.get('content') or '').strip()}\n</reasoning>\n")
                elif f["type"] == "RESPONSE":
                    out.append((f.get("content") or "").strip() + "\n")
    return "".join(out), turn

full, turns = render(True)
lean, _ = render(False)
open(DST_MD, "w", encoding="utf-8").write("# DeepSeek Exchange (share ei9y81lsr98ujftn91) — full reconstruction, 53 turns\n" + full)
open(DST_LEAN, "w", encoding="utf-8").write("# DeepSeek Exchange (share ei9y81lsr98ujftn91) — conversation text (reasoning traces omitted)\n" + lean)
print(f"FULL: {len(full)} chars, {turns} turns -> {DST_MD}")
print(f"LEAN: {len(lean)} chars -> {DST_LEAN}")
print("Ends with scaffold phrase:", "That is the most honest and useful answer I can give." in lean)
print("Privation directive present:", "darkness is absence of light" in lean)
