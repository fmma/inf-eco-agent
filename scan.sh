#!/bin/bash
set -e
cd "$(dirname "$0")"

# Activate venv if it exists
if [ -d .venv ]; then
  source .venv/bin/activate
fi

# Fetch papers from arXiv
echo "Fetching papers from arXiv..."
python src/fetch_papers.py > /tmp/inf-eco-papers.json

# Count results
count=$(python -c "import json; print(len(json.load(open('/tmp/inf-eco-papers.json'))))")
echo "Fetched $count papers from arXiv"

if [ "$count" -eq 0 ]; then
  echo "No papers found, skipping."
  exit 0
fi

# Invoke Claude Code non-interactively to score and report
echo "Scoring papers with Claude Code..."
{
  cat prompt.md
  echo ""
  echo "## Papers JSON"
  echo '```json'
  cat /tmp/inf-eco-papers.json
  echo '```'
} | claude --print \
  --allowedTools "Read,Write,Edit,Bash(git *)"
