// fhcp_lib.js — shared builders for the audit & consolidation document
// English formal report, Profile A (Times New Roman), DS-1 Deep Sea palette, R1 cover.
"use strict";

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, PageNumber, NumberFormat, AlignmentType, HeadingLevel,
  WidthType, BorderStyle, ShadingType, TableLayoutType, SectionType,
  PageBreak, TableOfContents,
} = require("docx");

// ── Palette: DS-1 Deep Sea (annual report / general business) ──
const PAL = {
  bg: "0B1C2C", accent: "529286",
  cover: { titleColor: "FFFFFF", subtitleColor: "B0B8C0", metaColor: "90989F", footerColor: "687078" },
  table: { headerBg: "529286", headerText: "FFFFFF", accentLine: "529286", innerLine: "BECFCC", surface: "E8ECEB" },
};
const PRIMARY = "0B1C2C";   // heading color on white body pages
const BODYCOL = "000000";   // Profile A pure black body

// ── Border constants (cover wrapper MUST be allNoBorders) ──
const NB = { style: BorderStyle.NONE, size: 0, color: "auto" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const allNoBorders = { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB };

// ── Fonts (English document) ──
const F_BODY = { ascii: "Times New Roman", eastAsia: "SimSun" };
const F_HEAD = { ascii: "Times New Roman", eastAsia: "SimHei" };

// ── English-aware title layout (common-rules Rule 3: non-CJK width ~ half) ──
function splitTitleLinesEN(title, charsPerLine) {
  if (title.length <= charsPerLine) return [title];
  const words = title.split(/\s+/);
  const lines = [];
  let cur = "";
  for (const w of words) {
    if ((cur + (cur ? " " : "") + w).length <= charsPerLine) {
      cur = cur ? cur + " " + w : w;
    } else {
      if (cur) lines.push(cur);
      cur = w;
    }
  }
  if (cur) lines.push(cur);
  // orphan prevention: merge tiny last line
  if (lines.length > 1 && lines[lines.length - 1].length <= 8) {
    const last = lines.pop();
    lines[lines.length - 1] += " " + last;
  }
  return lines;
}

function calcTitleLayoutEN(title, maxWidthTwips, preferredPt = 40, minPt = 24) {
  // English char width ~ pt * 10.5 twips (Times New Roman average incl. spaces)
  const charWidth = (pt) => pt * 10.5;
  const charsPerLine = (pt) => Math.floor(maxWidthTwips / charWidth(pt));
  let titlePt = preferredPt, lines;
  while (titlePt >= minPt) {
    const cpl = charsPerLine(titlePt);
    if (cpl < 4) { titlePt -= 2; continue; }
    lines = splitTitleLinesEN(title, cpl);
    if (lines.length <= 3) break;
    titlePt -= 2;
  }
  if (!lines || lines.length > 3) {
    lines = splitTitleLinesEN(title, charsPerLine(minPt));
    titlePt = minPt;
  }
  return { titlePt, titleLines: lines };
}

// ── calcCoverSpacing (from design-system.md, verbatim logic) ──
function calcCoverSpacing(params) {
  const {
    titleLineCount = 1, titlePt = 36, hasSubtitle = false,
    hasEnglishLabel = false, metaLineCount = 0,
    fixedHeight = 800, pageHeight = 16838,
    marginTop = 0, marginBottom = 0,
  } = params;
  const SAFETY = 1200;
  const usableHeight = pageHeight - marginTop - marginBottom - SAFETY;
  const titleHeight = titleLineCount * (titlePt * 23 + 200);
  const subtitleHeight = hasSubtitle ? (12 * 23 + 600) : 0;
  const englishLabelHeight = hasEnglishLabel ? (9 * 23 + 600) : 0;
  const metaHeight = metaLineCount * (10 * 23 + 100);
  const implicitParaHeight = 3 * 300;
  const contentHeight = titleHeight + subtitleHeight + englishLabelHeight +
    metaHeight + fixedHeight + implicitParaHeight;
  const remainingSpace = usableHeight - contentHeight;
  const safeRemaining = Math.max(remainingSpace, 400);
  const FOOTER_MIN = 800;
  const rawTop = Math.floor(safeRemaining * 0.45);
  const rawBottom = Math.floor(safeRemaining * 0.45);
  const bottomSpacing = Math.max(rawBottom, FOOTER_MIN);
  const topSpacing = Math.max(rawTop - Math.max(0, FOOTER_MIN - rawBottom), 400);
  const midSpacing = Math.max(safeRemaining - topSpacing - bottomSpacing, 0);
  return { topSpacing, midSpacing, bottomSpacing };
}

// ── Recipe R1: Pure Paragraph Cover (left-aligned), English title variant ──
function buildCoverR1(config) {
  const P = config.palette;
  const padL = 1200, padR = 800;
  const availableWidth = 11906 - padL - padR - 300;
  const { titlePt, titleLines } = calcTitleLayoutEN(config.title, availableWidth, 40, 24);
  const titleSize = titlePt * 2;
  const spacing = calcCoverSpacing({
    titleLineCount: titleLines.length, titlePt,
    hasSubtitle: !!config.subtitle, hasEnglishLabel: !!config.englishLabel,
    metaLineCount: (config.metaLines || []).length,
    fixedHeight: 400,
  });
  const accentLeft = { style: BorderStyle.SINGLE, size: 8, color: P.accent, space: 12 };
  const children = [];

  // 1. dynamic top whitespace
  children.push(new Paragraph({ spacing: { before: spacing.topSpacing } }));

  // 2. English label with accent bottom border
  if (config.englishLabel) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR }, spacing: { after: 500 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: P.accent, space: 8 } },
      children: [new TextRun({
        text: config.englishLabel.split("").join("  "),
        size: 18, color: P.accent, font: { ascii: "Calibri", eastAsia: "SimHei" }, characterSpacing: 40,
      })],
    }));
  }

  // 3. main title (dynamic size + explicit line spacing, Rule 8)
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      indent: { left: padL },
      spacing: {
        after: i < titleLines.length - 1 ? 100 : 300,
        line: Math.ceil(titlePt * 23), lineRule: "atLeast",
      },
      children: [new TextRun({
        text: titleLines[i], size: titleSize, bold: true,
        color: P.cover.titleColor, font: { eastAsia: "SimHei", ascii: "Arial" },
      })],
    }));
  }

  // 4. subtitle
  if (config.subtitle) {
    children.push(new Paragraph({
      indent: { left: padL }, spacing: { after: 800 },
      children: [new TextRun({
        text: config.subtitle, size: 24, color: P.cover.subtitleColor,
        font: { eastAsia: "Microsoft YaHei", ascii: "Arial" },
      })],
    }));
  }

  // 5. meta lines with left accent border
  for (const line of (config.metaLines || [])) {
    children.push(new Paragraph({
      indent: { left: padL + 200 }, spacing: { after: 80 },
      border: { left: accentLeft },
      children: [new TextRun({
        text: line, size: 22, color: P.cover.metaColor,
        font: { eastAsia: "Microsoft YaHei", ascii: "Arial" },
      })],
    }));
  }

  // 6. dynamic bottom whitespace
  children.push(new Paragraph({ spacing: { before: spacing.bottomSpacing } }));

  // 7. footer with top accent separator
  children.push(new Paragraph({
    indent: { left: padL, right: padR },
    border: { top: { style: BorderStyle.SINGLE, size: 2, color: P.accent, space: 8 } },
    spacing: { before: 200 },
    children: [
      new TextRun({ text: config.footerLeft || "", size: 16, color: P.cover.footerColor, font: { ascii: "Arial" } }),
      new TextRun({ text: "                                        " }),
      new TextRun({ text: config.footerRight || "", size: 16, color: P.cover.footerColor, font: { ascii: "Arial" } }),
    ],
  }));

  // single 16838 wrapper table — the ONLY table, allNoBorders
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.bg }, borders: noBorders,
        children,
      })],
    })],
  })];
}

// ── Body builders ──
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER,
    spacing: { before: 400, after: 200, line: 312 },
    children: [new TextRun({ text, bold: true, size: 32, color: PRIMARY, font: F_HEAD })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 140, line: 312 },
    children: [new TextRun({ text, bold: true, size: 28, color: PRIMARY, font: F_HEAD })],
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 220, after: 100, line: 312 },
    children: [new TextRun({ text, bold: true, size: 24, color: PRIMARY, font: F_HEAD })],
  });
}
// body paragraph — justified, 1.3x; supports [{t, b, i}] rich runs or plain string
function para(content, opts = {}) {
  const runs = (typeof content === "string")
    ? [new TextRun({ text: content, size: 24, color: BODYCOL, font: F_BODY })]
    : content.map(r => new TextRun({
        text: r.t, bold: !!r.b, italics: !!r.i,
        size: r.s || 24, color: r.c || BODYCOL, font: F_BODY,
      }));
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { after: opts.after != null ? opts.after : 120, line: 312 },
    children: runs,
  });
}
// quotation block — indented, italic, left accent border
function quote(text, src) {
  const runs = [new TextRun({ text, italics: true, size: 22, color: "333333", font: F_BODY })];
  if (src) runs.push(new TextRun({ text: "  " + src, size: 20, color: "666666", font: F_BODY }));
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 480, right: 360 },
    spacing: { before: 60, after: 140, line: 312 },
    border: { left: { style: BorderStyle.SINGLE, size: 10, color: PAL.table.accentLine, space: 10 } },
    children: runs,
  });
}
// bullet item — LEFT aligned per rules (lists never justified)
function bullet(content, level = 0) {
  const runs = (typeof content === "string")
    ? [new TextRun({ text: content, size: 24, color: BODYCOL, font: F_BODY })]
    : content.map(r => new TextRun({
        text: r.t, bold: !!r.b, italics: !!r.i, size: r.s || 24, color: r.c || BODYCOL, font: F_BODY,
      }));
  return new Paragraph({
    bullet: { level },
    alignment: AlignmentType.LEFT,
    spacing: { after: 80, line: 312 },
    children: runs,
  });
}
// table caption (keepNext keeps it with the table)
function tableTitle(text) {
  return new Paragraph({
    keepNext: true,
    alignment: AlignmentType.LEFT,
    spacing: { before: 160, after: 80, line: 312 },
    children: [new TextRun({ text, bold: true, size: 21, color: PRIMARY, font: F_BODY })],
  });
}
// generic table builder — percentage widths, margins, CLEAR shading, tableHeader/cantSplit
function makeTable(headers, rows, colWidths, opts = {}) {
  const cellSize = opts.size || 20;
  const headerRow = new TableRow({
    tableHeader: true, cantSplit: true,
    children: headers.map((text, i) => new TableCell({
      children: [new Paragraph({
        alignment: AlignmentType.LEFT, spacing: { line: 312 },
        children: [new TextRun({ text, bold: true, size: cellSize, color: PAL.table.headerText, font: F_BODY })],
      })],
      shading: { type: ShadingType.CLEAR, fill: PAL.table.headerBg },
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      width: { size: colWidths[i], type: WidthType.PERCENTAGE },
    })),
  });
  const dataRows = rows.map((cells, ri) => new TableRow({
    cantSplit: true,
    children: cells.map((cell, i) => {
      const spec = (typeof cell === "string") ? { t: cell } : cell;
      return new TableCell({
        children: [new Paragraph({
          alignment: AlignmentType.LEFT, spacing: { line: 312 },
          children: [new TextRun({
            text: spec.t, bold: !!spec.b, italics: !!spec.i,
            size: cellSize, color: spec.c || BODYCOL, font: F_BODY,
          })],
        })],
        shading: (opts.zebra && ri % 2 === 1)
          ? { type: ShadingType.CLEAR, fill: PAL.table.surface } : undefined,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        width: { size: colWidths[i], type: WidthType.PERCENTAGE },
      });
    }),
  }));
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: PAL.table.accentLine },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: PAL.table.accentLine },
      left: NB, right: NB,
      insideHorizontal: { style: BorderStyle.SINGLE, size: 1, color: PAL.table.innerLine },
      insideVertical: { style: BorderStyle.SINGLE, size: 1, color: "D8E2DF" },
    },
    rows: [headerRow, ...dataRows],
  });
}

module.exports = {
  PAL, PRIMARY, BODYCOL, NB, noBorders, allNoBorders, F_BODY, F_HEAD,
  calcTitleLayoutEN, splitTitleLinesEN, calcCoverSpacing, buildCoverR1,
  h1, h2, h3, para, quote, bullet, tableTitle, makeTable,
  docx: {
    Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
    Header, Footer, PageNumber, NumberFormat, AlignmentType, HeadingLevel,
    WidthType, BorderStyle, ShadingType, TableLayoutType, SectionType,
    PageBreak, TableOfContents,
  },
};
