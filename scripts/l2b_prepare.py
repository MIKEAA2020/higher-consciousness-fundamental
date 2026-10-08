#!/usr/bin/env python3
"""Round 19 — prepare readable core texts for the 8 newly supplied papers.

Strips pdftotext noise (page-number lines, bioRxiv banners, journal sidebars),
collapses whitespace, cuts reference lists, and writes core_<name>.txt files
whose byte size is small enough for chunked reading.
"""
import re
from pathlib import Path

SRC = Path("/home/z/my-project/glm agent 2/research/new_uploads")
DST = SRC / "cores"
DST.mkdir(exist_ok=True)

NOISE_PATTERNS = [
    r'^\s*\d+\s*$',                      # bare page numbers
    r'^www\.pnas\.org',
    r'^bioRxiv preprint',
    r'^available under a',
    r'^was not certified by peer review',
    r'^The copyright holder for this preprint',
    r'^;?\s*https?://doi\.org/10\.1101',
    r'^doi:\s*$',
    r'^DRAFT$',
    r'^Myrov et al\.',
    r'^\.\s*CC-BY-NC-ND',
    r'^This version posted',
    r'^\(?which',
    r'^perpetuity',
    r'^\d+\s*—\s*$',
]

REF_HEADS = [
    r'^\s*references\s*$',
    r'^\s*references\s*:?\s*$',
    r'^\s*REFERENCES\s*$',
    r'^\s*bibliography\s*$',
    r'^\s*BIBLIOGRAPHY\s*$',
    r'^\s*References\s*\(\d+\)',
]

def clean(text: str, cut_refs: bool = True) -> str:
    lines = text.split('\n')
    out = []
    ref_mode = False
    for ln in lines:
        s = ln.strip()
        if any(re.match(p, s) for p in NOISE_PATTERNS):
            continue
        if cut_refs and any(re.match(p, s) for p in REF_HEADS):
            ref_mode = True
        if ref_mode:
            continue
        out.append(s)
    txt = '\n'.join(out)
    txt = re.sub(r'[ \t]{2,}', ' ', txt)          # collapse wide spacing
    txt = re.sub(r'\n{3,}', '\n\n', txt)          # collapse blank runs
    # re-wrap at 100 cols for readability
    import textwrap
    wrapped = []
    for para in txt.split('\n'):
        if not para.strip():
            wrapped.append('')
            continue
        wrapped.extend(textwrap.wrap(para, width=100) or [''])
    return '\n'.join(wrapped)

FILES = {
    "l2b_1-s2.0-S0165027026001895-main.txt": "butler2026_neurochem_connectivity",   # J Neurosci Methods
    "l2b_1-s2.0-S245190222300191X-main.txt": "avram_cnni_2024",                    # Biol Psychiatry CNNI
    "l2b_Bedfordetal-2023-TheeffectsofLSDonwhole-brainconnectivity.txt": "bedford2023_lsd_rDCM",
    "l2b_Fabus_2023_Spatiotemporal_brain_dynamics.txt": "fabus2023_thesis",         # special: thesis
    "l2b_file.txt": "liang2015_pknmm",
    "l2b_s41593-025-02016-y.txt": "taxidis2025_voltage_imaging",
    "l2b_s41597-025-04832-0.txt": "diosdi2025_spheroids",
    "l2b_s42003-025-07576-0.txt": "piccinini2025_dmt",
}

for src_name, core_name in FILES.items():
    raw = (SRC / src_name).read_text(errors='replace')
    if core_name == "fabus2023_thesis":
        core = clean(raw, cut_refs=False)   # keep whole thesis; refs handled by chunking
    else:
        core = clean(raw, cut_refs=True)
    (DST / f"core_{core_name}.txt").write_text(core)
    print(f"{core_name:38s} {len(core):>8,} bytes  (from {src_name})")
print("DONE")
