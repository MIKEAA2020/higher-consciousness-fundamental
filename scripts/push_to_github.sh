#!/bin/sh
# Push the workspace repo to GitHub.
# Requires a valid PAT in /home/z/my-project/.github_pat
# (fine-grained PAT needs: Administration:write (repo creation),
#  Contents:write (push)). The token is never printed or committed.
set -e
PAT_FILE=/home/z/my-project/.github_pat
REPO_NAME=workspace-creations

TOKEN=$(cat "$PAT_FILE")
cd /home/z/my-project

echo "[1/4] Verifying token..."
LOGIN=$(curl -s -m 20 -H "Authorization: Bearer $TOKEN" https://api.github.com/user \
        | python3 -c "import json,sys; print(json.load(sys.stdin).get('login',''))")
if [ -z "$LOGIN" ]; then
  echo "ERROR: token rejected by GitHub (401). Replace $PAT_FILE with a valid PAT."
  exit 1
fi
echo "    authenticated as: $LOGIN"

echo "[2/4] Ensuring repo $REPO_NAME exists (private)..."
CODE=$(curl -s -o /tmp/_repo.json -w "%{http_code}" -m 20 \
       -H "Authorization: Bearer $TOKEN" \
       -d "{\"name\":\"$REPO_NAME\",\"private\":true,\"description\":\"Workspace creations: Grand Dream framework analyses, transcripts, scripts\"}" \
       https://api.github.com/user/repos)
if [ "$CODE" = "201" ] || [ "$CODE" = "422" ]; then
  echo "    repo ready (HTTP $CODE)"
else
  echo "    WARNING: repo creation returned HTTP $CODE"; cat /tmp/_repo.json; echo
fi

echo "[3/4] Configuring remote..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$LOGIN/$REPO_NAME.git"

echo "[4/4] Pushing..."
export GIT_ASKPASS=/home/z/my-project/scripts/git-askpass.sh
export GIT_TERMINAL_PROMPT=0
git push -u origin main
echo "DONE: https://github.com/$LOGIN/$REPO_NAME"
