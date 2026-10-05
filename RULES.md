# Persistent Session Rules

These rules were set by the user and persist across all future rounds.

1. **Language**: Respond ONLY in English. Never Chinese. This applies to chat
   responses, documents, charts, commit messages, and summaries.

2. **GitHub PAT**: Stored at `/home/z/my-project/.github_pat`
   (backup: `/home/z/my-project/.github_pat.bak`, mode 600).
   - NEVER print, quote, echo, or log the token.
   - NEVER commit it (it is listed in `.gitignore`).
   - Use it only via `scripts/git-askpass.sh` (export GIT_ASKPASS=...) for
     git push, or by reading it from the file into a shell variable for
     GitHub API calls.

3. **Push protocol**: At the end of every work round, commit all creations
   (documents, scripts, transcript artifacts) and push to the GitHub repo
   `workspace-creations` (private, created for this purpose):
   ```
   cd /home/z/my-project
   export GIT_ASKPASS=/home/z/my-project/scripts/git-askpass.sh
   git add -A && git commit -m "<round summary>" && git push origin main
   ```
   Or simply run `scripts/push_to_github.sh` (verifies the token, creates
   the repo if needed, pushes).

4. **Worklog**: Every agent appends its task record to `/home/z/my-project/worklog.md`
   per the shared protocol, then pushes (rule 3).

## Status note (updated 2026-10-06, round 4)

New PAT provided in round 4 (93 chars, well-formed fine-grained PAT) — verified
valid, authenticated as `MIKEAA2020`. Push protocol is operational.

NOTE: workspace resets between rounds can wipe gitignored files (including
`.github_pat`). If the push script reports a missing/rejected token after a
reset, the token must be re-provided and re-saved. The canonical push command:
`scripts/push_to_github.sh` (verifies token, ensures the private repo
`workspace-creations` exists, pushes main).
