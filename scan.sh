#!/bin/bash
set -e
cd "$(dirname "$0")"

# Activate venv if it exists
if [ -d .venv ]; then
  source .venv/bin/activate
fi

if [ "$1" = "--post" ]; then
  echo "Skipping fetch and score, reusing /tmp/inf-eco-{papers,scores}.json..."
  if [ ! -f /tmp/inf-eco-papers.json ] || [ ! -f /tmp/inf-eco-scores.json ]; then
    echo "Error: temp files from previous run not found." >&2
    exit 1
  fi
else
  # Fetch papers from arXiv (skips already-scored IDs)
  echo "Fetching papers from arXiv..."
  python src/fetch_papers.py > /tmp/inf-eco-papers.json

  # Count results
  count=$(python -c "import json; print(len(json.load(open('/tmp/inf-eco-papers.json'))))")
  echo "Fetched $count new papers from arXiv"

  if [ "$count" -eq 0 ]; then
    echo "No new papers, skipping."
    exit 0
  fi

  # Invoke Claude Code non-interactively to score papers (JSON output only)
  # Unset to allow running from within a Claude Code session or hook
  unset CLAUDECODE
  echo "Scoring papers with Claude Code..."
  {
    cat prompt.md
    echo ""
    echo "## Papers JSON"
    echo '```json'
    cat /tmp/inf-eco-papers.json
    echo '```'
  } | claude --print > /tmp/inf-eco-scores.json
fi

# Count papers (needed for commit message, and when --post skips the fetch step)
count=$(python -c "import json; print(len(json.load(open('/tmp/inf-eco-papers.json'))))")

# Merge scores into data/papers.json
echo "Merging scores..."
python src/merge_papers.py /tmp/inf-eco-papers.json /tmp/inf-eco-scores.json

# Render the living paper list
echo "Rendering papers.md..."
python src/render.py

# Generate news.md — flash news for noteworthy new papers
echo "Generating news.md..."
{
  cat news-prompt.md
  echo ""
  echo "## New Papers"
  echo '```json'
  python -c "
import json, sys; sys.path.insert(0, 'src')
from parse_scores import parse_scores
papers = {p['id']: p for p in json.load(open('/tmp/inf-eco-papers.json'))}
scores = {s['id']: s for s in parse_scores('/tmp/inf-eco-scores.json')}
merged = []
for pid, p in papers.items():
    s = scores.get(pid, {})
    merged.append({
        **p,
        'score': s.get('score', 0),
        'justification': s.get('justification', ''),
        'hype': s.get('hype', 0),
        'hype_justification': s.get('hype_justification', ''),
    })
print(json.dumps(merged, indent=2))
"
  echo '```'
} | claude --print > news.md

# Commit and push
echo "Committing..."
git add data/papers.json papers.md news.md
git commit -m "scan: $(date +%Y-%m-%d) — $count new papers scored"
git push
