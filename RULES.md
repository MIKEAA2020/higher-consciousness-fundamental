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

## Status note (2026-10-06)

The PAT provided on 2026-10-06 was rejected by the GitHub API with
`401 Bad credentials` (tried both `Bearer` and `token` schemes; stored length
86 chars vs. the 93 expected of a well-formed fine-grained PAT — it appears
truncated, expired, or auto-revoked by GitHub secret scanning). The local repo
is initialized and committed; `scripts/push_to_github.sh` will complete the
push as soon as `.github_pat` holds a valid token (fine-grained, with
Administration:write + Contents:write permissions).
