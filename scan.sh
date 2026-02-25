#!/bin/bash
set -eo pipefail
cd "$(dirname "$0")"

# Activate venv if it exists
if [ -d .venv ]; then
  source .venv/bin/activate
fi

# Allow running from within a Claude Code session or hook
unset CLAUDECODE

DISCORD_TARGET="${DISCORD_CHANNEL:-}"

# --- Error handling ---

notify_error() {
  local msg="$1"
  if [ -n "$DISCORD_TARGET" ] && command -v openclaw &>/dev/null; then
    openclaw message send --channel discord --target "$DISCORD_TARGET" \
      --message "<@231463543449321474> **inf-eco-agent failed:**
\`\`\`
$msg
\`\`\`" 2>/dev/null || true
  fi
}

has_internet() {
  curl -sf --max-time 5 https://arxiv.org > /dev/null 2>&1
}

on_error() {
  local exit_code=$?
  local failed_line=$1
  # If no internet, exit silently and let systemd retry
  if ! has_internet; then
    echo "No internet connectivity, exiting for systemd retry." >&2
    exit 1
  fi
  # Real error — notify
  local msg="Exit code $exit_code at line $failed_line. Check: journalctl --user -u inf-eco-scan.service -n 50"
  echo "Error: $msg" >&2
  notify_error "$msg"
  exit "$exit_code"
}

trap 'on_error $LINENO' ERR

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

  # --- Notify via Discord ---
  if [ -f news.md ] && [ -n "$DISCORD_TARGET" ] && command -v openclaw &>/dev/null; then
    echo "Posting news to Discord..."
    openclaw message send --channel discord --target "$DISCORD_TARGET" --message "<@231463543449321474>
$(cat news.md)" || echo "Warning: Discord notification failed." >&2
  fi
fi
