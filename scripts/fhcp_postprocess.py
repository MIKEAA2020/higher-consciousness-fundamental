#!/usr/bin/env python3
"""fhcp_postprocess.py — patch footer PAGE fields and strip empty pgNumType.

Steps (per docx skill toc.md):
  1. Remove empty <w:pgNumType/> elements (cover section emits them).
  2. Patch footer instrText: front-matter footer -> PAGE \\* ROMAN \\* MERGEFORMAT,
     body footer -> PAGE \\* arabic \\* MERGEFORMAT. WPS ignores pgNumType fmt otherwise.
  3. Convert to PDF via LibreOffice for visual verification (optional, --pdf).
"""
import sys, zipfile, shutil, re, os, subprocess, tempfile

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def read(z, name):
    return z.read(name).decode("utf-8")

def patch(path):
    tmp = path + ".tmp"
    zin = zipfile.ZipFile(path, "r")
    names = zin.namelist()

    # Map footer files to their section usage by scanning document.xml order.
    docxml = read(zin, "word/document.xml")
    # strip empty pgNumType (cover section)
    docxml2 = docxml.replace("<w:pgNumType/>", "")

    # find sectPr blocks in order; associate footer rIds
    # section order: cover (no footer), front (roman), body (arabic)
    sect_footers = []  # list of footer rIds per section in order
    for sect in re.findall(r"<w:sectPr[ >].*?</w:sectPr>", docxml2, re.S):
        rids = re.findall(r'<w:footerReference[^>]*r:id="([^"]+)"', sect)
        fmt = re.search(r'<w:pgNumType[^>]*w:fmt="([^"]+)"', sect)
        sect_footers.append((rids, fmt.group(1) if fmt else None))

    # resolve rIds -> footer files via document.xml.rels
    rels = read(zin, "word/_rels/document.xml.rels")
    rid2file = dict(re.findall(r'<Relationship[^>]*Id="([^"]+)"[^>]*Target="([^"]+)"', rels))

    # decide format per section: upperRoman -> ROMAN, decimal/none -> arabic
    plan = {}  # footer file -> fmt word
    for rids, fmt in sect_footers:
        if not rids:
            continue
        word = "ROMAN" if (fmt and "oman" in fmt) else "arabic"
        for rid in rids:
            f = rid2file.get(rid)
            if f:
                plan["word/" + f.lstrip("/")] = word

    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for item in names:
        data = zin.read(item)
        if item == "word/document.xml":
            data = docxml2.encode("utf-8")
        elif item in plan:
            xml = data.decode("utf-8")
            word = plan[item]
            xml = re.sub(
                r"(<w:instrText[^>]*>)\s*PAGE\s*(</w:instrText>)",
                r"\g<1> PAGE \\* " + word + r" \\* MERGEFORMAT \g<2>",
                xml)
            data = xml.encode("utf-8")
            print(f"patched {item} -> {word}")
        zout.writestr(item, data)
    zout.close()
    zin.close()
    shutil.move(tmp, path)
    print("postprocessed", path)

if __name__ == "__main__":
    patch(sys.argv[1])
