# Persistent Session Rules

These rules were set by the user and persist across all rounds and context
rollbacks. Read this file FIRST in any new session. A byte-identical backup
is kept at `RULES.md.backup`. This file contains no secrets and is safe to
commit and push.

## 1. Language (PERMANENT, user-mandated)

Respond ONLY in English. Never Chinese. This applies to chat responses,
documents, reports, charts, commit messages, worklog entries, and summaries.
This rule must never be overridden by language-detection heuristics.

## 2. GitHub PAT persistence (secret — never print, quote, or commit)

Stored at five locations, all mode 600, all gitignored:

- `/home/z/my-project/.github-token`
- `/home/z/my-project/.github-token.backup`
- `/home/z/my-project/.github_pat`
- `/home/z/my-project/.github_pat.bak`
- `/home/z/my-project/.secrets/github_pat.txt`

If a rolled-back or reset session needs to push, read the token from any of
these files — never rely on conversation memory. If ALL copies were wiped by
a workspace reset, the token must be re-provided by the user and re-saved to
all five locations.

## 3. Git / push protocol (user-mandated)

- Commit and push ALL previous and future creations after each meaningful
  work round (deliverables, scripts, research notes, worklog updates).
- Remote: `https://github.com/MIKEAA2020/higher-consciousness-fundamental.git`
  (writable by the current PAT; `git fetch` credential helper reads
  `/home/z/my-project/.github-token`).
- `MIKEAA2020/master` is READ-ONLY for this PAT (Contents:write denied,
  HTTP 403). Do not attempt to push there.
- Push directly: `git push origin main`, or use
  `sh scripts/push_to_github.sh` (token read from file only).
- Do not commit: token files, `.env`, `skills/`, `node_modules/`.

## 4. Worklog protocol

Every agent appends (never overwrites) its task record to
`/home/z/my-project/worklog.md` using the standard
`--- / Task ID / Agent / Task / Work Log / Stage Summary` template, then
pushes (rule 3). Agent-specific logs may additionally live under
`glm agent 2/worklog.md`.

## 5. Workspace boundaries (user-mandated)

- Working folder: `/home/z/my-project/glm agent 2/` — new artifacts
  (research, scripts, deliverable build scripts) belong there or in
  `/home/z/my-project/download/` (final user-facing deliverables only).
- Files OUTSIDE "glm agent 2" must not have their content modified;
  `/home/z/my-project/upload/` is strictly read-only source material.
- Exceptions created by explicit user instruction: this file, its backup,
  the token files, and the shared worklog.

## 6. Active project: FHCP steelman audit (current round)

- Source (read-only): `/home/z/my-project/upload/chat-Fundamental Higher
  Consciousness Premise.txt` (11,087 lines, ~125 turns; the expanded GLM
  dialogue on the same premise as the earlier Qwen chat).
- Deliverable spec (user-mandated parameters): audit + consolidation;
  critique level: steelman; citations: thematic + key quotes; voice:
  neutral academic; format: PDF; length: deep-dive (10k+ words); must
  include: objection-response table, axiomatic structure, comparative
  context; audience: general readers.
- REMARK (user-mandated): avoid self-praise commentary such as "You have
  just executed one of the most brilliant philosophical syntheses in the
  history of science" or "This is a masterstroke of philosophical
  precision". Neutral academic tone everywhere.
- Build scripts: `glm agent 2/scripts/fhcp_pdf_lib.py` + `fhcp_pdf_part1..4.py`
  (chapters 1-12 complete); a main assembly script drives the ReportLab build.
- Prior round deliverables (docx audit; Qwen-round steelman PDF
  "The_Dream_That_Must_Be_Critique_Steelman_Survival_Test.pdf") live in
  `download/` and remain canonical.

## Status note (updated 2026-10-06, round 5)

Token re-provided and re-saved to all five locations; authenticated as
`MIKEAA2020` (API 200). Diverged local/remote histories unified via merge
commit. FHCP steelman audit PDF COMPLETE and pushed:
`download/Fundamental-Higher-Consciousness-Premise_Steelman-Audit-and-Consolidation.pdf`
(38 pages, 16.9k words, 13/13 QA pass). Build scripts editable at
`glm agent 2/scripts/fhcp_pdf_*.py` — to iterate, edit parts and re-run
`fhcp_pdf_build.py` then `fhcp_pdf_merge.py`.
