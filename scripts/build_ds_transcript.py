#!/usr/bin/env python3
"""Parse the DeepSeek share JSON into a readable markdown transcript."""
import json

SRC = "/home/z/my-project/glm agent 2/research/ds_chunks/ds_share_content.json"
DST = "/home/z/my-project/glm agent 2/research/deepseek_exchange_transcript.md"

data = json.load(open(SRC, encoding="utf-8"))
msgs = data["data"]["biz_data"]["messages"]
print(f"Total messages: {len(msgs)}")
roles = {}
for m in msgs:
    roles[m["role"]] = roles.get(m["role"], 0) + 1
print("Roles:", roles)

out = ["# DeepSeek Exchange: Fundamental Higher Consciousness Premise (share ei9y81lsr98ujftn91)\n"]
turn = 0
for m in msgs:
    role = m["role"]
    content = m.get("content") or ""
    thinking = m.get("thinking_content") or ""
    if role == "USER":
        turn += 1
        out.append(f"\n\n### USER [T{turn}]\n")
        out.append(content.strip() + "\n")
        if thinking:
            out.append(f"\n[USER THINKING OMITTED: {len(thinking)} chars]\n")
    else:
        out.append(f"\n\n### ASSISTANT [T{turn}a]\n")
        if thinking:
            out.append(f"<reasoning trace: {len(thinking)} chars>\n")
            out.append(thinking.strip() + "\n</reasoning trace>\n")
        out.append(content.strip() + "\n")

text = "".join(out)
open(DST, "w", encoding="utf-8").write(text)
nlines = text.count("\n")
print(f"Wrote {DST}: {len(text)} chars, {nlines} lines, {turn} turns")
# quick sanity: check ending phrase
print("Has ending phrase:", "scaffold, not the building" in text)
print("Has privation directive:", "darkness" in text.lower() and "absence of light" in text.lower())
