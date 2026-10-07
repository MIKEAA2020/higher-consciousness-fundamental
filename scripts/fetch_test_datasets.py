#!/usr/bin/env python3
"""Fetch-test all candidate dataset/resource links for the four
Level-2 protocol domains (psychedelics / anesthesia / split-brain / DID).
Reports HTTP status, final URL, content type, size, page title."""
import json
import re
import subprocess
import tempfile

LINKS = [
    # --- domain, label, url ---
    # PSYCHEDELICS
    ("psychedelics", "Psilocybin Precision Functional Mapping (OpenNeuro ds006072)",
     "https://openneuro.org/datasets/ds006072/versions/1.2.0"),
    ("psychedelics", "PsiConnect multimodal psilocybin (OpenNeuro ds006110)",
     "https://openneuro.org/datasets/ds006110/versions/1.2.0"),
    ("psychedelics", "LSD MEG - Neural correlates of the LSD experience (OpenNeuro ds003059)",
     "https://openneuro.org/datasets/ds003059/versions/1.0.0"),
    ("psychedelics", "DMT-HAR-MED: DMT + harmine fMRI (OpenNeuro ds006644)",
     "https://openneuro.org/datasets/ds006644/versions/1.0.1"),
    ("psychedelics", "HaD-PET: DMT + harmine FDG-PET (OpenNeuro ds007768)",
     "https://openneuro.org/datasets/ds007768"),
    ("psychedelics", "NIMH Ketamine Mechanism of Action Study (OpenNeuro ds005917)",
     "https://openneuro.org/datasets/ds005917"),
    ("psychedelics", "LSD & psilocybin complexity results (Mendeley zxt5zsfhjr)",
     "https://data.mendeley.com/datasets/zxt5zsfhjr/1"),
    ("psychedelics", "PsiConnect on NEMAR (EEG/MEG mirror)",
     "https://nemar.org/dataset/on006110"),
    # ANESTHESIA
    ("anesthesia", "PhysioNet: propofol-anesthesia-dynamics (behavioral/autonomic/EEG)",
     "https://physionet.org/content/propofol-anesthesia-dynamics/"),
    ("anesthesia", "Michigan Human Anesthesia fMRI Dataset-1 (OpenNeuro ds006623)",
     "https://openneuro.org/datasets/ds006623"),
    ("anesthesia", "Repeated awakening / complexity measures (OpenNeuro ds005620)",
     "https://openneuro.org/datasets/ds005620/versions/1.0.0"),
    ("anesthesia", "Anesthesia-induced LOC biomarkers (OpenNeuro ds003171)",
     "https://openneuro.org/datasets/ds003171"),
    ("anesthesia", "Multimodal EEG-fNIRS general anesthesia (OpenNeuro ds004541)",
     "https://openneuro.org/datasets/ds004541"),
    ("anesthesia", "Cambridge repository: brain connectivity during propofol sedation",
     "https://www.repository.cam.ac.uk/items/b7817912-50b5-423b-882e-978fb39a49df"),
    # SPLIT-BRAIN (adjacent corpora; no dedicated open dataset found)
    ("split-brain", "IDEAS: Imaging Database for Epilepsy and Surgery (OpenNeuro ds005602)",
     "https://openneuro.org/datasets/ds005602"),
    ("split-brain", "IDEAS II open diffusion MRI + connectivity release (OpenNeuro ds007401)",
     "https://openneuro.org/datasets/ds007401"),
    ("split-brain", "EEG signatures of loss and recovery of consciousness (PMC3607036, reference)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC3607036/"),
    # DID
    ("DID", "NFED-fmri (Zenodo 13759829) - VERIFIED UNRELATED: facial-expression fMRI",
     "https://zenodo.org/records/13759829"),
    ("DID", "Schlumpf et al. 2014 PLOS ONE: DID part-dependent resting-state (paper)",
     "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098795"),
    ("DID", "Functional Neuroimaging in Dissociative Disorders review (PMC9502311)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC9502311/"),
    # AGGREGATORS (cross-domain)
    ("aggregator", "FieldTrip FAQ: open access MEG/EEG data list",
     "https://www.fieldtriptoolbox.org/faq/other/open_data/"),
    ("aggregator", "openlists/ElectrophysiologyData (GitHub) - open EEG dataset index",
     "https://github.com/openlists/ElectrophysiologyData"),
    ("aggregator", "Harvard Brain Imaging & Neurophysiology Database (BIND)",
     "https://bdsp.io"),
    ("aggregator", "NITRC-IR neuroimaging tools & data repository",
     "https://www.nitrc.org"),
]

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

def fetch(url):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tf:
        path = tf.name
    try:
        r = subprocess.run(
            ["curl", "-sS", "-L", "-m", "35", "-A", UA,
             "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
             "-H", "Accept-Language: en-US,en;q=0.9",
             "--max-filesize", "8000000",
             "-o", path, "-w",
             "%{http_code}|%{url_effective}|%{content_type}|%{size_download}",
             url],
            capture_output=True, text=True, timeout=50,
        )
        w = (r.stdout or "").strip()
        parts = w.split("|")
        code, final, ctype, size = (parts + ["", "", "", ""])[:4]
        title = ""
        try:
            with open(path, "rb") as f:
                head = f.read(300000).decode("utf-8", "ignore")
            m = re.search(r"<title[^>]*>(.*?)</title>", head, re.S | re.I)
            if m:
                title = re.sub(r"\s+", " ", m.group(1)).strip()[:110]
        except Exception:
            pass
        err = (r.stderr or "").strip()
        return {"code": code or "ERR", "final": final, "ctype": ctype.split(";")[0],
                "size": size, "title": title, "err": err[:120]}
    finally:
        try:
            import os
            os.unlink(path)
        except Exception:
            pass

results = []
for domain, label, url in LINKS:
    print(f"GET {url}", flush=True)
    res = fetch(url)
    rec = {"domain": domain, "label": label, "url": url, **res}
    results.append(rec)
    print(f"   -> {res['code']} | {res['ctype']} | {res['size']}B | {res['title'][:70]}", flush=True)

out_path = "/home/z/my-project/glm agent 2/research/dataset_search/fetch_test_results.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=1)
print(f"\nwrote {out_path}")

ok = [r for r in results if r["code"] in ("200", "304")]
bad = [r for r in results if r["code"] not in ("200", "304")]
print(f"\nFETCHABLE: {len(ok)}/{len(results)}")
print("NOT FETCHABLE / DEGRADED:")
for r in bad:
    print(f"  [{r['code']}] {r['label'][:70]} -> {r['url']}")
    if r["err"]:
        print(f"        err: {r['err'][:100]}")
