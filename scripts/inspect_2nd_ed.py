#!/usr/bin/env python3
"""Inspect 2nd-Ed PDF: fonts, page 13 content stream structure, and the target phrase."""
import pikepdf
import pdfplumber
import re

PDF = "/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation_2nd-Ed.pdf"

pdf = pikepdf.open(PDF)
print(f"Pages: {len(pdf.pages)}")

# Fonts across doc
fonts = set()
for i, page in enumerate(pdf.pages):
    res = page.get("/Resources", {})
    fdict = res.get("/Font", {})
    for name, ref in fdict.items():
        try:
            f = ref
            bf = str(f.get("/BaseFont", "?"))
            sub = str(f.get("/Subtype", "?"))
            enc = str(f.get("/Encoding", "none"))
            fonts.add((bf, sub, enc))
        except Exception as e:
            fonts.add(("ERR", str(e), ""))
print("Fonts (BaseFont, Subtype, Encoding):")
for f in sorted(fonts):
    print("  ", f)

# Page 13 content stream
p13 = pdf.pages[12]
data = p13.obj.get("/Contents")
print("\nPage 13 contents type:", type(data))
try:
    raw = p13.obj["/Contents"].read_bytes()
except Exception:
    raw = b"".join(pikepdf.Page(p13).contents_coalesce() if False else x.read_bytes() for x in (data if isinstance(data, pikepdf.Array) else [data]))
print(f"Page 13 stream bytes: {len(raw)}")
# Find the target phrase fragments in the stream
for frag in [b"thermodynamics", b"cold has no", b"Darkness has no"]:
    idxs = [m.start() for m in re.finditer(re.escape(frag), raw)]
    print(f"  {frag!r}: {len(idxs)} occurrences at {idxs[:5]}")
# Show a window around first 'thermodynamics' occurrence
i = raw.find(b"thermodynamics")
if i >= 0:
    print("\nContext around 'thermodynamics':")
    print(raw[max(0,i-400):i+200].decode("latin-1"))
pdf.close()
