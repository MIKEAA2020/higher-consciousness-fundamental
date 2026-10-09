#!/usr/bin/env python3
"""Drill into OpenNeuro subject folders for the four anesthesia corpora."""
import json
import subprocess

def gql(query, variables):
    payload = json.dumps({"query": query, "variables": variables})
    r = subprocess.run(
        ["curl", "-sS", "-m", "90", "-X", "POST",
         "https://openneuro.org/crn/graphql",
         "-H", "content-type: application/json", "-d", payload],
        capture_output=True, text=True, timeout=120)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"raw": r.stdout[:400]}

Q = """query S($datasetId: ID!, $tag: String!, $prefix: String!) {
  snapshot(datasetId: $datasetId, tag: $tag) {
    id
    files(prefix: $prefix) { id filename size }
  }
}"""

READMEQ = """query R($datasetId: ID!, $tag: String!) {
  snapshot(datasetId: $datasetId, tag: $tag) {
    id
    files(prefix: "README") { id filename size }
  }
}"""

targets = [
    ("ds003171", "2.0.1", ["sub-02CB/", "sub-02CB/eeg/"]),
    ("ds005620", "1.0.0", ["sub-1010/", "sub-1010/eeg/"]),
    ("ds006623", "1.0.0", ["sub-02/", "sub-02/func/"]),
    ("ds004541", "1.0.0", ["sub-02/", "sub-02/eeg/"]),
]

for dsid, tag, prefixes in targets:
    for p in prefixes:
        d = gql(Q, {"datasetId": dsid, "tag": tag, "prefix": p})
        files = ((d.get("data") or {}).get("snapshot") or {}).get("files") or []
        print(f"== {dsid} :: {p} -> {len(files)} entries")
        for f in files[:30]:
            print(f"   {f.get('size', 0)/1e6:9.2f} MB  {f.get('filename')}")
        if "raw" in d:
            print("   RAW-ERR:", d["raw"][:200])
