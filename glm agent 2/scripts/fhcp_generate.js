// fhcp_generate.js — main assembly for the audit & consolidation document
// 3-section architecture: Cover (no page#) / Front matter (TOC, Roman) / Body (Arabic from 1)
"use strict";
const fs = require("fs");
const {
  PAL, PRIMARY, BODYCOL, F_BODY, F_HEAD, buildCoverR1,
} = require("./fhcp_lib.js");
const D = require("./fhcp_lib.js").docx;
const { buildAudit } = require("./fhcp_audit.js");
const { buildFinal } = require("./fhcp_final.js");

const OUT = "/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation.docx";

// ── Page geometry ──
const pgSize = { width: 11906, height: 16838 };
const pgMargin = { top: 1440, bottom: 1440, left: 1701, right: 1417 };

// ── Cover config ──
const coverConfig = {
  title: "The Fundamental Higher Consciousness Premise",
  subtitle: "A Line-Level Audit and Consolidation of the Dialogue",
  englishLabel: "PHILOSOPHICAL AUDIT REPORT",
  metaLines: [
    "Source: chat-Fundamental Higher Consciousness Premise.txt (11,087 lines, ~125 turns)",
    "Method: adversarial line-level review with line-number citations",
    "Contents: surviving points, weaknesses, repairs, objection ledger, consolidated premise",
    "Status: metaphysical interpretation with an empirical annex",
  ],
  footerLeft: "Consciousness-First Monism - Audit and Consolidation",
  footerRight: "October 2026",
  palette: PAL,
};

// ── Shared header/footer ──
function docHeader() {
  return new D.Header({
    children: [new D.Paragraph({
      alignment: D.AlignmentType.CENTER,
      spacing: { after: 60 },
      children: [new D.TextRun({
        text: "The Fundamental Higher Consciousness Premise - Audit and Consolidation",
        size: 18, color: "808080", font: F_BODY,
      })],
    })],
  });
}
function pageNumFooter() {
  return new D.Footer({
    children: [new D.Paragraph({
      alignment: D.AlignmentType.CENTER,
      children: [new D.TextRun({ children: [D.PageNumber.CURRENT], size: 18, color: "808080", font: F_BODY })],
    })],
  });
}

// ── Front matter: TOC page ──
const frontMatter = [
  // TOC title — must NOT use HeadingLevel (would index itself)
  new D.Paragraph({
    alignment: D.AlignmentType.CENTER,
    spacing: { before: 480, after: 360 },
    children: [new D.TextRun({
      text: "Table of Contents", bold: true, size: 32,
      color: PRIMARY, font: F_HEAD,
    })],
  }),
  // TOC field element
  new D.TableOfContents("Table of Contents", {
    hyperlink: true,
    headingStyleRange: "1-3",
  }),
  // refresh hint (mandatory)
  new D.Paragraph({
    spacing: { before: 200 },
    children: [new D.TextRun({
      text: "Note: This Table of Contents is generated via field codes. To ensure page number accuracy after editing, please right-click the TOC and select \"Update Field.\"",
      italics: true, size: 18, color: "888888", font: F_BODY,
    })],
  }),
  // page break after TOC (mandatory)
  new D.Paragraph({ children: [new D.PageBreak()] }),
];

// ── Body ──
const body = [...buildAudit(), ...buildFinal()];

// ── Document ──
const doc = new D.Document({
  creator: "Audit and Consolidation",
  title: "The Fundamental Higher Consciousness Premise - A Line-Level Audit and Consolidation",
  styles: {
    default: {
      document: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimSun" }, size: 24, color: BODYCOL },
        paragraph: { spacing: { line: 312 } },
      },
      heading1: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimHei" }, size: 32, bold: true, color: PRIMARY },
        paragraph: { spacing: { before: 400, after: 200, line: 312 }, outlineLevel: 0 },
      },
      heading2: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimHei" }, size: 28, bold: true, color: PRIMARY },
        paragraph: { spacing: { before: 300, after: 140, line: 312 }, outlineLevel: 1 },
      },
      heading3: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimHei" }, size: 24, bold: true, color: PRIMARY },
        paragraph: { spacing: { before: 220, after: 100, line: 312 }, outlineLevel: 2 },
      },
    },
  },
  sections: [
    // Section 1: Cover — margin 0, no footer, no pageNumbers
    {
      properties: {
        page: { size: pgSize, margin: { top: 0, bottom: 0, left: 0, right: 0 } },
      },
      children: buildCoverR1(coverConfig),
    },
    // Section 2: Front matter — Roman numerals
    {
      properties: {
        type: D.SectionType.NEXT_PAGE,
        page: {
          size: pgSize, margin: pgMargin,
          pageNumbers: { start: 1, formatType: D.NumberFormat.UPPER_ROMAN },
        },
      },
      headers: { default: docHeader() },
      footers: { default: pageNumFooter() },
      children: frontMatter,
    },
    // Section 3: Body — Arabic numerals restarting at 1
    {
      properties: {
        type: D.SectionType.NEXT_PAGE,
        page: {
          size: pgSize, margin: pgMargin,
          pageNumbers: { start: 1, formatType: D.NumberFormat.DECIMAL },
        },
      },
      headers: { default: docHeader() },
      footers: { default: pageNumFooter() },
      children: body,
    },
  ],
});

D.Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log("WROTE", OUT, buf.length, "bytes");
}).catch((e) => { console.error("FAIL", e); process.exit(1); });
