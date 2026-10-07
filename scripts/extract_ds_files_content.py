#!/usr/bin/env python3
"""Extract the two DeepSeek attached files (window.__decomb, window.__elev)
from the headless browser page into local files, in slices."""
import json
import subprocess
import sys

OUT = {
    "__decomb": "/home/z/my-project/glm agent 2/research/decombination.txt",
    "__elev": "/home/z/my-project/glm agent 2/research/elevation_cost.txt",
}
SLICE = 100_000

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

for var, target in OUT.items():
    total = int(ev(f"{var}.length"))
    print(f"{var}: length {total}")
    parts = []
    pos = 0
    while pos < total:
        end = min(pos + SLICE, total)
        chunk = ev(f"{var}.slice({pos},{end})")
        if not isinstance(chunk, str):
            raise RuntimeError(f"slice {pos}:{end} returned {type(chunk)}")
        parts.append(chunk)
        pos = end
        print(f"  slice {pos}/{total}", flush=True)
    text = "".join(parts)
    if len(text) > total or total - len(text) > 200:
        raise AssertionError(f"length mismatch: {len(text)} vs {total}")
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  wrote {target}: {len(text)} chars")
print("DONE")
