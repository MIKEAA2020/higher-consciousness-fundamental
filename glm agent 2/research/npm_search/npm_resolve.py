#!/usr/bin/env python3
"""npm_resolve.py — resolve canonical URLs (DOI, PMC, publisher) for the
load-bearing neural-parameter-map papers via the OpenAlex API.
Outputs npm_resolved.json with per-paper landing URLs, then fetch-probes each.
"""
import json, subprocess, urllib.request, urllib.parse, time

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) research/1.0"}

papers = [
    ("Bojak & Liley 2005 — Modeling the effects of anesthesia on the EEG (Phys Rev E)",
     'Modeling the effects of anesthesia on the electroencephalogram'),
    ("Bojak et al. 2013 — Ketamine, Propofol, and the EEG: neural field analysis (Front Comput Neurosci)",
     'Ketamine, propofol, and the EEG: a neural field analysis of HCN1-mediated interactions'),
    ("Deco et al. 2018 — Whole-brain multimodal model using 5HT2A receptor density (Cell Rep)",
     'Whole-Brain Multimodal Neuroimaging Model Using 5HT2A Receptor Density'),
    ("Jirsa et al. 2017 — Individualized whole-brain models of epilepsy spread (NeuroImage)",
     'Individualized whole-brain models of epilepsy spread'),
    ("Penas et al. 2024 — Parameter estimation whole-brain network model epilepsy (PLOS Comput Biol)",
     'Parameter estimation in a whole-brain network model of intractable epilepsy'),
    ("Odor 2019 — Critical synchronization dynamics Kuramoto human connectome",
     'Critical synchronization dynamics of the Kuramoto model on the human connectome'),
    ("Luppi et al. 2022 — Whole-brain modelling effects of anaesthesia (Nat Commun)",
     'Whole-brain modelling identifies distinct but convergent effects of anaesthesia and disorders of consciousness'),
    ("Herzog et al. 2023 — Whole-brain model neural entropy increase psychedelics",
     'A whole-brain model of the neural entropy increase elicited by psychedelic drugs'),
    ("Preller et al. 2019 — Effective connectivity changes in LSD (PNAS)",
     'Effective connectivity changes in LSD-induced altered states of consciousness'),
    ("Eisen et al. 2024 — Propofol anesthesia destabilizes neural dynamics (Neuron)",
     'Propofol anesthesia destabilizes neural dynamics across behavioral states'),
    ("Haldeman & Beggs 2005 — Critical branching neural networks",
     'Critical branching captures activity in living neural networks and a new class of Percolation models'),
    ("Robinson et al. 2001 — Prediction and quantification of spatiotemporal EEG dynamics",
     'Prediction and quantification of spatiotemporal EEG dynamics'),
]

def oa(query, tries=3):
    url = ("https://api.openalex.org/works?search="
           + urllib.parse.quote(query) + "&per-page=1&mailto=r@example.org")
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                d = json.load(r)
            if d.get("results"):
                w = d["results"][0]
                best = w.get("best_oa_location") or {}
                locs = [l for l in (w.get("locations") or []) if l.get("landing_page_url")]
                return {
                    "title": w.get("display_name", "")[:120],
                    "doi": w.get("doi"),
                    "year": w.get("publication_year"),
                    "cited": w.get("cited_by_count"),
                    "oa_pdf": best.get("pdf_url"),
                    "oa_landing": best.get("landing_page_url"),
                    "publisher_landing": (w.get("primary_location") or {}).get("landing_page_url"),
                    "all_landings": sorted({l["landing_page_url"] for l in locs}),
                }
            return {"error": "no result"}
        except Exception as e:
            if attempt < tries - 1:
                time.sleep(6 * (attempt + 1))  # backoff for 429 rate limits
                continue
            return {"error": str(e)}
    return {"error": "no result"}

def probe(u):
    try:
        r = subprocess.run(["curl", "-sL", "-o", "/dev/null", "-w", "%{http_code}",
                            "--max-time", "12", "-A", UA["User-Agent"], u],
                           capture_output=True, text=True, timeout=15)
        return r.stdout.strip() or "ERR"
    except Exception:
        return "TIMEOUT"

out = []
for label, q in papers:
    info = oa(q)
    time.sleep(3)  # pacing between OpenAlex calls
    entry = {"label": label, **info}
    if "error" not in info:
        cands = [info.get("oa_landing"), info.get("publisher_landing"),
                 *(info.get("all_landings") or [])]
        cands = [c for c in cands if c]
        probes = {}
        for c in sorted(set(cands))[:4]:
            probes[c] = probe(c)
        entry["fetch_probes"] = probes
    out.append(entry)
    print(f"\n### {label}")
    if "error" in info:
        print(f"    OpenAlex error: {info['error']}")
    else:
        print(f"    {info['title']} ({info.get('year')}, cited {info.get('cited')})")
        print(f"    doi: {info.get('doi')}")
        print(f"    oa_pdf: {info.get('oa_pdf')}")
        for u, c in (entry.get("fetch_probes") or {}).items():
            print(f"    [{c}] {u[:110]}")

json.dump(out, open("npm_resolved.json", "w"), indent=1)
print("\nsaved npm_resolved.json")
