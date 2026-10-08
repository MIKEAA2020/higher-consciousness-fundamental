#!/usr/bin/env python3
"""Round 9: extract a large payload stored in window.__ds (DeepSeek share API
response) from the headless browser page into a local file, in slices."""
import json
import subprocess
import sys

TARGET = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/glm agent 2/research/ds2_share_content.json"
SLICE = 200_000

def ev(expr):
    r = subprocess.run(
        ["agent-browser", "eval", expr, "--json"],
        capture_output=True, text=True, timeout=180,
    )
    out = r.stdout.strip()
    obj = json.loads(out)
    if not obj.get("success"):
        raise RuntimeError(f"eval failed: {out[:200]}")
    return obj["data"]["result"]

total = int(ev("window.__ds.length"))
print(f"payload length: {total}")
parts = []
pos = 0
while pos < total:
    end = min(pos + SLICE, total)
    chunk = ev(f"window.__ds.slice({pos},{end})")
    if not isinstance(chunk, str):
        raise RuntimeError(f"slice {pos}:{end} returned {type(chunk)}")
    parts.append(chunk)
    pos = end
    print(f"  slice {pos}/{total} ({len(chunk)} chars)", flush=True)

text = "".join(parts)
# JS .length counts UTF-16 code units; Python counts characters — surrogate
# pairs (emoji etc.) produce a small positive slack, never a negative one.
if len(text) > total or total - len(text) > 200:
    raise AssertionError(f"length mismatch: {len(text)} vs {total}")
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(text)
print(f"wrote {TARGET}: {len(text)} chars")
