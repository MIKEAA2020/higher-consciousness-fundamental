#!/usr/bin/env python3
"""Round 16: build readable transcript from ds4 share payload JSON (fragments schema)."""
import json

SRC = "/home/z/my-project/glm agent 2/research/ds4_share_content.json"
DST = "/home/z/my-project/glm agent 2/research/ds4_exchange.md"

with open(SRC, encoding="utf-8") as f:
    payload = json.load(f)

biz = payload["data"]["biz_data"]
messages = biz["messages"]
print(f"messages: {len(messages)}")

out = ["# DeepSeek Exchange ds4 (share l81hpm4u2de69jpeut)", ""]
turn = 0
for i, m in enumerate(messages):
    role = m.get("role", "?")
    frags = m.get("fragments") or []
    if isinstance(frags, str):
        try:
            frags = json.loads(frags)
        except Exception:
            frags = []
    req = "\n\n".join(f.get("content", "") for f in frags if f.get("type") == "REQUEST")
    think = "\n".join(f.get("content", "") for f in frags if f.get("type") == "THINK")
    resp = "\n\n".join(f.get("content", "") for f in frags if f.get("type") in ("RESPONSE", "ANSWER", "OUTPUT"))
    other = [f for f in frags if f.get("type") not in ("REQUEST", "THINK", "RESPONSE", "ANSWER", "OUTPUT")]
    if role == "USER":
        turn += 1
        out.append(f"\n<!-- msg[{i}] turn {turn} USER -->")
        out.append(f"\n## [U{turn}] User\n")
        out.append(req.strip())
        if other:
            for f in other:
                fc = f.get("content", "")
                if fc:
                    out.append(f"\n[FRAGMENT type={f.get('type')}]: {fc[:2000]}")
    elif role == "ASSISTANT":
        out.append(f"\n<!-- msg[{i}] turn {turn} ASSISTANT -->")
        out.append(f"\n### [A{turn}] DeepSeek\n")
        if think:
            out.append(f"*<reasoning trace: {len(think)} chars — elided from body; key quotes extracted separately>*\n")
        out.append(resp.strip() if resp else "")
        if other:
            for f in other:
                fc = f.get("content", "")
                if fc:
                    out.append(f"\n[FRAGMENT type={f.get('type')}]: {fc[:2000]}")

text = "\n".join(out) + "\n"
with open(DST, "w", encoding="utf-8") as f:
    f.write(text)
lines = text.count("\n") + 1
print(f"wrote {DST}: {len(text)} chars, {lines} lines, {turn} turns")

# stats: how many messages have empty RESPONSE fragments
empty_resp = sum(1 for m in messages if m.get("role") == "ASSISTANT" and not any(
    (f.get("type") in ("RESPONSE", "ANSWER", "OUTPUT")) for f in (json.loads(m["fragments"]) if isinstance(m.get("fragments"), str) else (m.get("fragments") or []))))
print(f"assistant messages with no RESPONSE fragment: {empty_resp}")

# verify ending: last assistant RESPONSE
last_resp = ""
for m in reversed(messages):
    if m.get("role") == "ASSISTANT":
        frags = m.get("fragments") or []
        if isinstance(frags, str):
            frags = json.loads(frags)
        for f in frags:
            if f.get("type") in ("RESPONSE", "ANSWER", "OUTPUT") and f.get("content"):
                last_resp = f["content"]
                break
        if last_resp:
            break
print("LAST RESPONSE tail 500 chars:")
print(last_resp[-500:])
