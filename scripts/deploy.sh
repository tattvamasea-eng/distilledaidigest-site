#!/usr/bin/env bash
# deploy.sh — D·A·D deterministic deploy spine.
# Assumes Claude has already: written issues/issue-N.html, placed the thumbnail,
# and run update_site.py to edit index.html + archive.html.
# This script does the git mechanics + live verification only.
#
# Usage: ./scripts/deploy.sh <NUM> "<TITLE>"
set -euo pipefail
N="${1:?usage: deploy.sh <num> <title>}"
TITLE="${2:?missing title}"
cd "$(dirname "$0")/.."

# Preconditions
[ -f "issues/issue-${N}.html" ] || { echo "❌ issues/issue-${N}.html missing"; exit 1; }
[ -f "assets/thumbnail_issue${N}.png" ] || { echo "❌ thumbnail missing"; exit 1; }
grep -q "issue-${N}" index.html   || { echo "❌ index.html does not link issue-${N}"; exit 1; }
grep -q "issue-${N}" archive.html || { echo "❌ archive.html does not link issue-${N}"; exit 1; }

# Guardrails
grep -q "— Ram\b" "issues/issue-${N}.html" && { echo "❌ personal byline 'Ram' present"; exit 1; } || true
grep -qi "organis" "issues/issue-${N}.html" && echo "⚠️  British spelling 'organis…' found" || true

# Keep .DS_Store out
grep -q "^.DS_Store$" .gitignore 2>/dev/null || echo ".DS_Store" >> .gitignore
find . -name .DS_Store -print -exec git rm --cached --ignore-unmatch {} \; >/dev/null 2>&1 || true

git add -A
echo "----- staged -----"; git status --short
git diff --cached --name-only | grep -q "issue-${N}.html" || { echo "❌ issue not staged"; exit 1; }

git commit -m "Add Issue #${N}: ${TITLE}"
git push origin main
echo "✅ Pushed. Netlify deploying…"

URL="https://distilledaidigest.com/issues/issue-${N}.html"
for i in $(seq 1 12); do
  sleep 10
  CODE=$(curl -sI "$URL" | head -1 | awk '{print $2}')
  echo "  check $i: $CODE"
  [ "$CODE" = "200" ] && { echo "✅ LIVE: $URL"; exit 0; }
done
echo "⚠️  Not 200 yet — check Netlify dashboard."
