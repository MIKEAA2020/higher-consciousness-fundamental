#!/usr/bin/env python3
"""Probe OpenNeuro GraphQL for the four anesthesia corpora: metadata + EEG file listing."""
import json
import subprocess

DS = ["ds006623", "ds005620", "ds003171", "ds004541"]

def gql(query, variables):
    payload = json.dumps({"query": query, "variables": variables})
    r = subprocess.run(
        ["curl", "-sS", "-m", "60", "-X", "POST",
         "https://openneuro.org/crn/graphql",
         "-H", "content-type: application/json", "-d", payload],
        capture_output=True, text=True, timeout=90)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"raw": r.stdout[:400]}

Q1 = """query D($id: ID!) {
  dataset(id: $id) {
    id name public publishDate
    latestSnapshot { id tag }
  }
}"""

out = {}
for dsid in DS:
    d = gql(Q1, {"id": dsid})
    out[dsid] = d
    ds = (d.get("data") or {}).get("dataset") or {}
    print("=", dsid, "->", json.dumps({k: ds.get(k) for k in ("name", "public", "publishDate")})[:300])

# file listing for each: try snapshot files query
Q2 = """query S($datasetId: ID!, $tag: String!) {
  snapshot(datasetId: $datasetId, tag: $tag) {
    id tag
    files { id filename size }
  }
}"""
for dsid in DS:
    ds = (out[dsid].get("data") or {}).get("dataset") or {}
    tag = (ds.get("latestSnapshot") or {}).get("tag")
    if not tag:
        print(dsid, "no tag"); continue
    d = gql(Q2, {"datasetId": dsid, "tag": tag})
    files = ((d.get("data") or {}).get("snapshot") or {}).get("files") or []
    print(f"== {dsid} tag={tag}: {len(files)} root entries")
    for f in files[:25]:
        print(f"   {f.get('size', 0)/1e6:9.2f} MB  {f.get('filename')}")
    # save full listing
    with open(f"/home/z/my-project/glm agent 2/research/phase2/{dsid}_files.json", "w") as fh:
        json.dump(d, fh, indent=1)
