#!/bin/sh
# Push workspace creations to GitHub (standing protocol, RULES.md).
# Target: MIKEAA2020/higher-consciousness-fundamental (writable by the current PAT).
# Note: MIKEAA2020/master is READ-ONLY for the current PAT (Contents:write denied,
# 403). If a future token grants master write access, the PREFERENCES.md master
# protocol can be resumed with a worktree-based additive merge.
# Token: /home/z/my-project/.github_pat (never printed, never committed).
set -e

WS=/home/z/my-project
export GIT_ASKPASS=$WS/scripts/git-askpass.sh
export GIT_TERMINAL_PROMPT=0
TOKEN=$(cat "$WS/.github_pat")
cd "$WS"

echo "[1/4] Verifying token..."
LOGIN=$(curl -s -m 20 -H "Authorization: Bearer $TOKEN" https://api.github.com/user \
        | python3 -c "import json,sys; print(json.load(sys.stdin).get('login',''))")
if [ "$LOGIN" != "MIKEAA2020" ]; then
  echo "ERROR: token rejected (login='$LOGIN'). Replace $WS/.github_pat with a valid PAT."
  exit 1
fi
echo "    authenticated as: $LOGIN"

echo "[2/4] Credential sweep..."
if git ls-files | grep -qE '^\.(github_pat|env)' || grep -rE "github_pat_1[A-Za-z0-9]{20,}" --include="*.md" --include="*.py" --include="*.sh" --include="*.html" -l . --exclude-dir=.git --exclude-dir=skills 2>/dev/null | grep -q .; then
  echo "ERROR: credential leakage detected. Aborting."
  exit 1
fi

echo "[3/4] Committing workspace state..."
git add -A
if git diff --cached --quiet; then
  echo "    nothing to commit"
else
  git commit -m "Round update: workspace creations"
fi

echo "[4/4] Pushing to higher-consciousness-fundamental..."
git push hcf main
echo "DONE: https://github.com/MIKEAA2020/higher-consciousness-fundamental"
