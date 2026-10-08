#!/usr/bin/env python3
"""npm_resolve3.py — Europe PMC title-search resolver for the papers CrossRef
mis-matched (preprints/comments/siblings). Prints PMCID + DOI + journal + probe.
"""
import json, subprocess, urllib.request, urllib.parse, time

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) research/1.0"}

queries = [
    ("Preller 2019 PNAS — Effective connectivity changes in LSD",
     'TITLE:"Effective connectivity changes in LSD-induced altered states of consciousness"'),
    ("Penas 2024 PLOS Comput Biol — Parameter estimation whole-brain epilepsy",
     'TITLE:"Parameter estimation in a whole-brain network model of epilepsy"'),
    ("Eisen 2024 Neuron — Propofol destabilizes neural dynamics",
     'TITLE:"Propofol anesthesia destabilizes neural dynamics across cortex"'),
    ("Haldeman & Beggs 2005 — Critical branching",
     'TITLE:"Critical branching captures activity in living neural networks"'),
    ("Robinson et al. 2001 — Prediction and quantification of spatiotemporal EEG dynamics",
     'TITLE:"Prediction and quantification of spatiotemporal EEG dynamics"'),
    ("Deco 2018 Current Biology — serotonin receptor maps LSD (verify)",
     'TITLE:"Whole-Brain Multimodal Neuroimaging Model Using Serotonin Receptor Maps"'),
]

def epmc(q, tries=2):
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
           + urllib.parse.quote(q) + "&format=json&pageSize=3&resultType=core")
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                return json.load(r)
        except Exception as e:
            if attempt == tries - 1:
                return {"_error": str(e)}
            time.sleep(4)

def probe(u):
    try:
        r = subprocess.run(["curl", "-sL", "-o", "/dev/null", "-w", "%{http_code}",
                            "--max-time", "12", "-A", UA["User-Agent"], u],
                           capture_output=True, text=True, timeout=15)
        return r.stdout.strip() or "ERR"
    except Exception:
        return "TIMEOUT"

out = []
for label, q in queries:
    d = epmc(q)
    time.sleep(1.5)
    print(f"\n### {label}")
    if "_error" in d:
        print(f"    error: {d['_error']}")
        out.append({"label": label, "error": d["_error"]})
        continue
    res = d.get("resultList", {}).get("result", [])
    hits = []
    for r in res[:3]:
        pmcid = r.get("pmcid") or ""
        doi = r.get("doi") or ""
        pmc_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/" if pmcid else ""
        doi_url = f"https://doi.org/{doi}" if doi else ""
        hits.append({
            "title": r.get("title", "")[:130],
            "journal": r.get("journalTitle", ""),
            "year": r.get("pubYear"),
            "doi": doi, "pmcid": pmcid,
            "pmc_url": pmc_url, "doi_url": doi_url,
            "probe_pmc": probe(pmc_url) if pmc_url else "-",
            "probe_doi": probe(doi_url) if doi_url else "-",
        })
    out.append({"label": label, "hits": hits})
    for h in hits:
        print(f"    {h['title']} | {h['journal']} {h['year']} | doi={h['doi']} pmcid={h['pmcid']}")
        if h["pmc_url"]:
            print(f"      [{h['probe_pmc']}] {h['pmc_url']}")
        if h["doi_url"]:
            print(f"      [{h['probe_doi']}] {h['doi_url']}")

json.dump(out, open("npm_resolved3.json", "w"), indent=1)
print("\nsaved npm_resolved3.json")
