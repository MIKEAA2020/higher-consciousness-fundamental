#!/usr/bin/env python3
"""Convert pdf.py extract.text JSON output (2nd_ed_extracted.txt) to plain pages text."""
import json, re, sys

SRC = "/home/z/my-project/glm agent 2/research/2nd_ed_extracted.txt"
DST = "/home/z/my-project/glm agent 2/research/2nd_ed_pages.txt"

raw = open(SRC, encoding="utf-8").read()
# Strip warning lines before the JSON object
start = raw.find("{")
data = json.loads(raw[start:])
out = []
for p in data["data"]["pages"]:
    out.append(f"\n===== PAGE {p['page']} ({p['chars']} chars) =====\n")
    out.append(p["text"])
open(DST, "w", encoding="utf-8").write("".join(out))
print(f"Wrote {DST}: {sum(p['chars'] for p in data['data']['pages'])} chars across {data['data']['total_pages']} pages")
