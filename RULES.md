# Persistent Session Rules

These rules were set by the user and persist across all future rounds.

1. **Language**: Respond ONLY in English. Never Chinese. This applies to chat
   responses, documents, charts, commit messages, and summaries.

2. **GitHub PAT**: Stored at `/home/z/my-project/.github_pat`
   (backups: `/home/z/my-project/.github_pat.bak` and
   `/home/z/my-project/.secrets/github_pat.txt`, all mode 600).
   - NEVER print, quote, echo, or log the token.
   - NEVER commit it (all three paths are listed in `.gitignore`).
   - Use it only via `scripts/git-askpass.sh` (export GIT_ASKPASS=...) for
     git push, or by reading it from the file into a shell variable for
     GitHub API calls.

3. **Push protocol**: At the end of every work round, commit all creations
   (documents, scripts, transcript artifacts) and push to
   `MIKEAA2020/higher-consciousness-fundamental` (the repo matching this
   project; writable by the current PAT):
   ```
   cd /home/z/my-project
   sh scripts/push_to_github.sh   # verify token, sweep, commit, push
   ```
   Direct equivalent:
   ```
   export GIT_ASKPASS=/home/z/my-project/scripts/git-askpass.sh
   git add -A && git commit -m "<round summary>" && git push hcf main
   ```
   Note: `MIKEAA2020/master` (the PREFERENCES.md target) is READ-ONLY for
   the current PAT (Contents:write denied, HTTP 403). If a future token
   grants master write access, resume the master additive-merge protocol.

4. **Worklog**: Every agent appends its task record to `/home/z/my-project/worklog.md`
   per the shared protocol, then pushes (rule 3).

## Status note (updated 2026-10-06, round 4)

New PAT provided in round 4 (93 chars, well-formed fine-grained PAT) — verified
valid, authenticated as `MIKEAA2020`. ALL PREVIOUS CREATIONS PUSHED to
`MIKEAA2020/higher-consciousness-fundamental` (transcript, critique/steelman
PDF+MD+cover, scripts, RULES, worklog; upstream LICENSE preserved).

Token scope discovered by probes: `master` = read-only (403 on write);
`higher-consciousness-fundamental` = full write. 18 other repos visible.

NOTE: workspace resets between rounds can wipe gitignored files (including
`.github_pat`). If the push script reports a missing/rejected token after a
reset, the token must be re-provided and re-saved to all three locations.
