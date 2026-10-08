#!/usr/bin/env python3
"""npm_resolve2.py — canonical-URL resolver via CrossRef + Europe PMC REST.
OpenAlex is 429-limited from this IP, so this pivot uses:
  1. api.crossref.org -> DOI + title + publisher URL
  2. europepmc REST (ebi.ac.uk) -> PMC landing page when it exists
  3. curl probe of each candidate landing URL
Outputs npm_resolved.json (overwrites failed attempt).
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

def get_json(url, tries=2):
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                return json.load(r)
        except Exception as e:
            if attempt == tries - 1:
                return {"_error": str(e)}
            time.sleep(4)

def crossref(q):
    url = ("https://api.crossref.org/works?query.bibliographic="
           + urllib.parse.quote(q) + "&rows=1&select=DOI,title,container-title,published,URL,is-referenced-by-count")
    d = get_json(url)
    items = (d or {}).get("message", {}).get("items", [])
    if items:
        it = items[0]
        return {
            "title": (it.get("title") or [""])[0][:130],
            "doi": it.get("DOI"),
            "journal": (it.get("container-title") or [""])[0][:70],
            "year": ((it.get("published") or {}).get("date-parts") or [[None]])[0][0],
            "cited": it.get("is-referenced-by-count"),
        }
    return {"_error": "crossref no result"}

def epmc(doi):
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
           + urllib.parse.quote(f'DOI:"{doi}"') + "&format=json&pageSize=1")
    d = get_json(url)
    res = (d or {}).get("resultList", {}).get("result", [])
    if res:
        r = res[0]
        pmcid = r.get("pmcid") or ""
        if pmcid:
            return f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", r.get("inEPMC") == "Y"
    return None, False

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
    cr = crossref(q)
    time.sleep(1.2)
    entry = {"label": label, **({k: v for k, v in cr.items() if not k.startswith("_")})}
    if "error" not in cr and cr.get("doi"):
        pmc_url, in_epmc = epmc(cr["doi"])
        cands = {"doi_landing": f"https://doi.org/{cr['doi']}"}
        if pmc_url:
            cands["pmc"] = pmc_url
        entry["fetch_probes"] = {k: probe(v) for k, v in cands.items()}
        entry["in_epmc"] = in_epmc
    else:
        entry["error"] = cr.get("_error", "no doi")
    out.append(entry)
    print(f"\n### {label}")
    if entry.get("error"):
        print(f"    error: {entry['error']}")
    else:
        print(f"    {entry.get('title')} ({entry.get('journal')}, {entry.get('year')}, cited {entry.get('cited')})")
        print(f"    doi: {entry.get('doi')}  inEPMC={entry.get('in_epmc')}")
        for k, c in (entry.get("fetch_probes") or {}).items():
            print(f"    [{c}] {k}")

json.dump(out, open("npm_resolved.json", "w"), indent=1)
print("\nsaved npm_resolved.json")
