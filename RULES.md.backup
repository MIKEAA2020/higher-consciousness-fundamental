# Persistent Agent Rules and Context

> This file survives context rollbacks. Read it FIRST at the start of any new
> session before doing any work. Do not delete. A byte-identical backup copy
> is kept at `RULES.md.backup`. This file is safe to commit and push (it
> contains no secrets).

## 1. Language Rule (PERMANENT, user-mandated)

- Respond ONLY in English. NEVER respond in Chinese.
- All deliverables, documents, reports, charts, code comments, commit
  messages, and worklog entries must be in English.
- This rule was explicitly ordered by the user and must never be overridden
  by language-detection heuristics.

## 2. Workspace Boundaries (user-mandated)

- My working folder is `/home/z/my-project/glm agent 2/` — all new artifacts
  (research notes, scripts, deliverables) belong there or in
  `/home/z/my-project/download/`.
- Files OUTSIDE "glm agent 2" must NOT have their content modified
  (e.g. `/home/z/my-project/upload/` is strictly read-only source material).
- Exception: this file (RULES.md), its backup, and the token files at
  workspace root were explicitly requested by the user.

## 3. GitHub Token Persistence (secret — never commit)

- Token file: `/home/z/my-project/.github-token` (gitignored)
- Backup copy: `/home/z/my-project/.github-token.backup` (gitignored)
- If a rolled-back session needs to push: read the token from those files,
  never rely on conversation memory. Both filenames are listed in
  `.gitignore` and MUST stay excluded from every commit.
- Remote: `https://github.com/MIKEAA2020/higher-consciousness-fundamental.git`
  (push with the token embedded as
  `https://<TOKEN>@github.com/MIKEAA2020/higher-consciousness-fundamental.git`)

## 4. Git Workflow (user-mandated)

- Commit and push ALL previous and future creations after each meaningful
  work unit (deliverables, scripts, research notes, worklog updates).
- Shared worklog: append (never overwrite) to `/home/z/my-project/worklog.md`
  using the standard `--- / Task ID / Agent / Task / Work Log / Stage Summary`
  template.
- Do not commit: `.env`, token files, `skills/`, `node_modules/`.

## 5. Active Project: FHCP Steelman Audit (status reference)

- Source (read-only): `/home/z/my-project/upload/chat-Fundamental Higher
  Consciousness Premise.txt` (11,087 lines, ~125 turns).
- Deliverable spec: audit + consolidation; critique level: steelman;
  citations: thematic + key quotes; voice: neutral academic; format: PDF;
  length: 10k+ words; must include objection-response table, axiomatic
  structure, comparative context; audience: general readers.
- REMARK (user-mandated): avoid self-praise commentary such as "You have
  just executed one of the most brilliant philosophical syntheses in the
  history of science" or "This is a masterstroke of philosophical
  precision". Keep a neutral academic tone everywhere.
- Build scripts: `/home/z/my-project/glm agent 2/scripts/fhcp_pdf_lib.py`
  + `fhcp_pdf_part1..4.py` (chapters 1-12). A main assembly script must
  import all four parts' `add_content(story)` and drive the ReportLab build.
- Prior deliverable (superseded parameters, docx):
  `/home/z/my-project/download/Fundamental-Higher-Consciousness-Premise_
  Audit-and-Consolidation.docx`; its extracted text is mirrored at
  `glm agent 2/research/previous_audit_text.md`.
