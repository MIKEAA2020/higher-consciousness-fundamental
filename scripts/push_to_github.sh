#!/bin/sh
# Push workspace creations to MIKEAA2020/master (standing protocol, PREFERENCES.md).
# Additive merge: never rewrites master history, never clobbers existing files.
# Token: /home/z/my-project/.github_pat (never printed, never committed).
set -e

WS=/home/z/my-project
PAT_FILE=$WS/.github_pat
export GIT_ASKPASS=$WS/scripts/git-askpass.sh
export GIT_TERMINAL_PROMPT=0

TOKEN=$(cat "$PAT_FILE")
cd "$WS"

echo "[1/6] Verifying token..."
LOGIN=$(curl -s -m 20 -H "Authorization: Bearer $TOKEN" https://api.github.com/user \
        | python3 -c "import json,sys; print(json.load(sys.stdin).get('login',''))")
if [ "$LOGIN" != "MIKEAA2020" ]; then
  echo "ERROR: token rejected (login='$LOGIN'). Replace $PAT_FILE with a valid PAT."
  exit 1
fi
echo "    authenticated as: $LOGIN"

echo "[2/6] Preparing worktree of master/main..."
git remote remove master 2>/dev/null || true
git remote add master https://github.com/MIKEAA2020/master.git
git worktree remove .master_wt 2>/dev/null || true
git branch -D deliver/master 2>/dev/null || true
git fetch master main
git worktree add .master_wt -b deliver/master master/main

echo "[3/6] Copying creations (additive only)..."
# Deliverables (skip download/README.md - identical template already in master)
for f in "$WS"/download/*; do
  b=$(basename "$f")
  [ "$b" = "README.md" ] && continue
  cp "$f" .master_wt/download/
done
# Workspace generation scripts (unique names, no collisions with master scripts/)
for s in merge_finalize.py git-askpass.sh push_to_github.sh extract_conversation.py \
         extract_clean.py critique_content.py export_md.py cover.html \
         extract_qwen_chat.py extract_qwen_chat.sh build_pdf.py; do
  [ -f "$WS/scripts/$s" ] && cp "$WS/scripts/$s" .master_wt/scripts/
done
# Standing rules
cp "$WS/RULES.md" .master_wt/RULES.md 2>/dev/null || true

echo "[4/6] Merging worklog (append workspace lineage)..."
if ! grep -q "Grand Dream / Higher Consciousness lineage" .master_wt/worklog.md; then
  printf '\n\n---\n\n# Worklog - Grand Dream / Higher Consciousness lineage\n\n(Parallel zai-web workspace lineage: Qwen chat extractions, Grand Dream framework critique and steelman. Appended by the standing push protocol.)\n' >> .master_wt/worklog.md
fi
sed '1d' "$WS/worklog.md" >> .master_wt/worklog.md

echo "[5/6] Credential sweep + committing..."
if grep -rE "github_pat_1[A-Za-z0-9]{20,}" .master_wt --include="*.md" --include="*.py" --include="*.sh" --include="*.html" -l 2>/dev/null | grep -q .; then
  echo "ERROR: credential leakage detected in staged content. Aborting."
  exit 1
fi
cd .master_wt
git add -A
if git diff --cached --quiet; then
  echo "    nothing new to push"
else
  git commit -m "Grand Dream lineage: Qwen transcript, critique/steelman (PDF+MD+cover), extraction/build scripts, RULES"
fi

echo "[6/6] Pushing to master..."
git push master deliver/master:main

cd "$WS"
git worktree remove .master_wt
echo "DONE: https://github.com/MIKEAA2020/master"
