#!/usr/bin/env python3
"""Surgical correction of the 2nd-Ed PDF, page 13:
   'cold has no thermodynamics'  ->  'cold has no subject study in physics'
Reflows the affected 3-line justified paragraph, preserving line count and
computing word-spacing (Tw) from real FreeSerif metrics so justification stays exact.
"""
import pikepdf
from fontTools.ttLib import TTFont

PDF = "/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation_2nd-Ed.pdf"
FONT = "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"

# ---- font metrics ----
tt = TTFont(FONT)
cmap = tt.getBestCmap()
hmtx = tt["hmtx"]
upm = tt["head"].unitsPerEm

def natural_width(text, size=10.0):
    total = 0
    for ch in text:
        gname = cmap.get(ord(ch))
        if gname is None:
            raise ValueError(f"no glyph for {ch!r}")
        total += hmtx[gname][0]
    return total / upm * size

def n_spaces(s):
    return s.count(" ")

EMDASH = "\u2014"

# original lines (from the content stream; \003 -> em-dash)
L2 = "physics; cold has no thermodynamics; the equations of radiative transfer and of heat flow contain only the"
L3 = "positive quantities. What the privative terms mark is real " + EMDASH + " a hole is not a thing, but you can fall in it " + EMDASH
L4 = "but its reality is the reality of an absence, not of an ingredient."
TW2, TW3 = -0.111057, 0.165981

col_from_L2 = natural_width(L2) + TW2 * n_spaces(L2)
col_from_L3 = natural_width(L3) + TW3 * n_spaces(L3)
col = (col_from_L2 + col_from_L3) / 2
print(f"column width from L2: {col_from_L2:.3f}, from L3: {col_from_L3:.3f}, mean: {col:.3f}")

# new lines (same count = 3)
NL2 = "physics; cold has no subject study in physics; the equations of radiative transfer and of heat flow"
NL3 = "contain only the positive quantities. What the privative terms mark is real " + EMDASH + " a hole is not a thing,"
NL4 = "but you can fall in it " + EMDASH + " but its reality is the reality of an absence, not of an ingredient."

tw2 = (col - natural_width(NL2)) / n_spaces(NL2)
tw3 = (col - natural_width(NL3)) / n_spaces(NL3)
print(f"NL2 width {natural_width(NL2):.3f} spaces {n_spaces(NL2)} -> Tw {tw2:.6f}")
print(f"NL3 width {natural_width(NL3):.3f} spaces {n_spaces(NL3)} -> Tw {tw3:.6f}")
print(f"NL4 width {natural_width(NL4):.3f} (last line, Tw 0, must be < {col:.1f})")
assert natural_width(NL4) < col, "last line overflows!"

def fmt_tw(v):
    s = f"{v:.6f}".rstrip("0").rstrip(".")
    return s if s else "0"

# ---- build the replacement stream block ----
def esc(s):
    out = []
    for ch in s:
        if ch == EMDASH:
            out.append("\\003")
        else:
            out.append(ch)
    return "".join(out)

old_block = (
    b"0 Tw -0.111057 Tw (physics; cold has no thermodynamics; the equations of radiative transfer and of heat flow contain only the) Tj T* "
    b"0 Tw .165981 Tw (positive quantities. What the privative terms mark is real \\003 a hole is not a thing, but you can fall in it \\003) Tj T* "
    b"0 Tw (but its reality is the reality of an absence, not of an ingredient.) Tj T* "
)
new_block = (
    f"0 Tw {fmt_tw(tw2)} Tw ({esc(NL2)}) Tj T* ".encode("latin-1")
    + f"0 Tw {fmt_tw(tw3)} Tw ({esc(NL3)}) Tj T* ".encode("latin-1")
    + f"0 Tw ({esc(NL4)}) Tj T* ".encode("latin-1")
)

pdf = pikepdf.open(PDF, allow_overwriting_input=True)
page = pdf.pages[12]
stream = page.obj["/Contents"]
raw = stream.read_bytes()
assert old_block in raw, "old block not found in page 13 stream!"
raw2 = raw.replace(old_block, new_block, 1)
stream.write(raw2)
pdf.save(PDF)
print("page 13 stream patched and saved.")

# ---- verification ----
pdf = pikepdf.open(PDF)
raw3 = pdf.pages[12].obj["/Contents"].read_bytes()
assert b"cold has no subject study in physics" in raw3
assert b"cold has no thermodynamics" not in raw3
print("verification: new phrase present, old phrase gone.")
pdf.close()

import pdfplumber
with pdfplumber.open(PDF) as pp:
    p13 = pp.pages[12]
    txt = p13.extract_text()
    assert "cold has no subject study in physics" in txt
    # check right margin: max x1 of words in the affected region
    words = p13.extract_words()
    max_x1 = max(w["x1"] for w in words)
    print(f"page 13 max word x1 = {max_x1:.1f} (page width {p13.width:.1f}); text check ok")
    print("\n--- affected paragraph ---")
    i = txt.find("Darkness has no")
    print(txt[i:i+520])
