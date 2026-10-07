#!/usr/bin/env python3
"""Verify OpenNeuro dataset IDs exist (curl only gets the SPA shell)."""
import json
import subprocess

IDS = ["ds006072", "ds006110", "ds003059", "ds006644", "ds007768",
       "ds005917", "ds006623", "ds005620", "ds003171", "ds004541",
       "ds005602", "ds007401"]

Q = """query D($id: ID!) {
  dataset(id: $id) {
    id
    name
    public
    publishDate
    latestSnapshot { id tag }
  }
}"""

def gql(var):
    payload = json.dumps({"query": Q, "variables": var})
    r = subprocess.run(
        ["curl", "-sS", "-m", "45", "-X", "POST",
         "https://openneuro.org/crn/graphql",
         "-H", "content-type: application/json", "-d", payload],
        capture_output=True, text=True, timeout=60)
    return r.stdout

results = {}
for i in IDS:
    try:
        out = gql({"id": i})
        d = json.loads(out)
        ds = (d.get("data") or {}).get("dataset")
        if ds is None:
            errs = d.get("errors") or []
            msg = errs[0].get("message", "?") if errs else "null dataset"
            results[i] = {"exists": False, "note": msg[:90]}
        else:
            vers = [ds.get("latestSnapshot", {}).get("tag", "")]
            results[i] = {"exists": True, "name": ds.get("name", "")[:95],
                          "public": ds.get("public"), "snapshot": vers}
    except Exception as e:
        results[i] = {"exists": None, "note": str(e)[:90]}
    print(i, "->", json.dumps(results[i])[:160])

with open("/home/z/my-project/glm agent 2/research/dataset_search/openneuro_verify.json", "w") as f:
    json.dump(results, f, indent=1)
