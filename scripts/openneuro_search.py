#!/usr/bin/env python3
"""Query OpenNeuro GraphQL search for consciousness-domain dataset keywords."""
import json
import subprocess

KEYWORDS = [
    "psilocybin", "LSD", "DMT", "psychedelic", "ayahuasca",
    "ketamine", "propofol", "anesthesia", "anaesthesia", "sevoflurane",
    "dexmedetomidine", "xenon", "sedation",
    "dissociative identity", "dissociation", "split-brain", "callosotomy",
    "commissurotomy", "corpus callosum", "consciousness",
]

QUERY = """query Search($q: String!) {
  search(q: $q, first: 20) {
    edges { node { id name } }
  }
}"""

def gql(query, variables):
    payload = json.dumps({"query": query, "variables": variables})
    r = subprocess.run(
        ["curl", "-sS", "-m", "45", "-X", "POST", "https://openneuro.org/crn/graphql",
         "-H", "content-type: application/json", "-d", payload],
        capture_output=True, text=True, timeout=60,
    )
    return json.loads(r.stdout)

seen = {}
for kw in KEYWORDS:
    try:
        d = gql(QUERY, {"q": kw})
        edges = (d.get("data") or {}).get("search", {}).get("edges", [])
        print(f"### {kw!r} -> {len(edges)} results")
        for e in edges:
            n = e["node"]
            print(f"  {n['id']}  {n['name'][:80]}")
            seen.setdefault(n["id"], n["name"])
    except Exception as ex:
        print(f"### {kw!r} -> ERROR: {ex}")

print("\n=== UNIQUE DATASETS ===")
for i in sorted(seen):
    print(f"{i}  {seen[i][:80]}")
with open("/home/z/my-project/glm agent 2/research/dataset_search/openneuro_datasets.json", "w") as f:
    json.dump(seen, f, indent=1)
