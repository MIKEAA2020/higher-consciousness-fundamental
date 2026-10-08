#!/usr/bin/env python3
"""npm_fetch_test.py — fetch-test every URL discovered in the neural-parameter-map searches.

Reads q*.json from this directory, dedupes URLs, probes each with curl
(4s timeout, browser-ish UA, allow redirects), and writes npm_fetch_results.json
with status code + title (when parseable). Never mutates the search JSONs.
"""
import json, glob, subprocess, html, re

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

urls = []
for f in sorted(glob.glob("q*.json")):
    try:
        data = json.load(open(f))
    except Exception:
        continue
    items = data if isinstance(data, list) else data.get("results", [])
    for it in items:
        u = (it.get("url") or "").strip()
        if u.startswith("http"):
            urls.append((u, f))

# dedupe, keep first source
seen, probes = set(), []
for u, src in urls:
    if u not in seen:
        seen.add(u)
        probes.append((u, src))

def probe(u):
    try:
        r = subprocess.run(
            ["curl", "-sL", "-o", "/dev/null", "-w", "%{http_code}",
             "--max-time", "12", "-A", UA, u],
            capture_output=True, text=True, timeout=15)
        code = r.stdout.strip()
    except Exception:
        code = "TIMEOUT"
    return code or "ERR"

def get_title(u):
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "12", "-A", UA, u],
            capture_output=True, text=True, timeout=15)
        m = re.search(r"<title[^>]*>(.*?)</title>", r.stdout[:200000],
                      re.I | re.S)
        if m:
            t = html.unescape(m.group(1)).strip()
            return re.sub(r"\s+", " ", t)[:110]
    except Exception:
        pass
    return ""

results = []
for u, src in probes:
    code = probe(u)
    title = get_title(u) if code in ("200", "403", "406") else ""
    results.append({"url": u, "source": src, "code": code, "title": title})
    print(f"{code:>7}  {u[:95]}")

json.dump(results, open("npm_fetch_results.json", "w"), indent=1)
ok = sum(1 for r in results if r["code"] == "200")
print(f"\nTOTAL: {len(results)} unique URLs | fetchable(200): {ok} | "
      f"blocked/failed: {len(results)-ok}")
