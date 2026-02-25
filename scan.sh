#!/bin/bash
set -eo pipefail
cd "$(dirname "$0")"

# Activate venv if it exists
if [ -d .venv ]; then
  source .venv/bin/activate
fi

# Allow running from within a Claude Code session or hook
unset CLAUDECODE

# --- Scan: discover and score new papers ---

echo "Fetching papers from arXiv..."
python src/fetch_papers.py > /tmp/inf-eco-papers.json

new_count=$(python -c "import json; print(len(json.load(open('/tmp/inf-eco-papers.json'))))")
echo "Fetched $new_count new papers from arXiv"

if [ "$new_count" -gt 0 ]; then
  echo "Scoring papers with Claude Code..."
  {
    cat prompt.md
    echo ""
    echo "## Papers JSON"
    echo '```json'
    cat /tmp/inf-eco-papers.json
    echo '```'
  } | claude --print > /tmp/inf-eco-scores.json

  echo "Merging scores..."
  python src/merge_papers.py /tmp/inf-eco-papers.json /tmp/inf-eco-scores.json
else
  # Clear stale scores so news doesn't re-report old papers
  rm -f /tmp/inf-eco-scores.json
fi

# --- Rescore: update hype from external signals ---

echo "Fetching hype signals..."
python src/fetch_hype_signals.py

echo "Re-scoring hype..."
python src/rescore_hype.py

surge_count=$(python -c "import json; print(len(json.load(open('/tmp/inf-eco-hype-surges.json'))))")
echo "Found $surge_count hype surges"

# --- Render + News ---

echo "Rendering papers.md..."
python src/render.py

if [ "$new_count" -gt 0 ] || [ "$surge_count" -gt 0 ]; then
  echo "Generating news.md..."
  python src/build_news_prompt.py | claude --print > news.md
  git add data/papers.json papers.md news.md
else
  echo "Nothing newsworthy, skipping news generation."
  git add data/papers.json papers.md
fi

# --- Commit and push ---

if git diff --cached --quiet; then
  echo "Nothing changed, skipping commit."
else
  msg="scan: $(date +%Y-%m-%d)"
  parts=()
  [ "$new_count" -gt 0 ] && parts+=("$new_count new papers scored")
  [ "$surge_count" -gt 0 ] && parts+=("$surge_count hype surges")
  [ ${#parts[@]} -eq 0 ] && parts+=("hype updated from external signals")
  msg="$msg — $(IFS=', '; echo "${parts[*]}")"
  echo "Committing..."
  git commit -m "$msg"
  git push
fi
