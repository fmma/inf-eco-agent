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
  echo "Scoring papers with Claude Code in batches of 100..."
  batch_size=100
  # Split papers into batches and score each
  python -c "
import json, math
papers = json.load(open('/tmp/inf-eco-papers.json'))
n = math.ceil(len(papers) / $batch_size)
for i in range(n):
    batch = papers[i*$batch_size:(i+1)*$batch_size]
    json.dump(batch, open(f'/tmp/inf-eco-papers-batch-{i}.json', 'w'), indent=2)
print(n)
" > /tmp/inf-eco-batch-count

  num_batches=$(cat /tmp/inf-eco-batch-count)
  rm -f /tmp/inf-eco-scores.json

  # Score all batches in parallel
  pids=()
  for ((i=0; i<num_batches; i++)); do
    batch_file="/tmp/inf-eco-papers-batch-${i}.json"
    batch_count=$(python -c "import json; print(len(json.load(open('$batch_file'))))")
    echo "  Scoring batch $((i+1))/$num_batches ($batch_count papers)..."
    {
      cat prompt.md
      echo ""
      echo "## Papers JSON"
      echo '```json'
      cat "$batch_file"
      echo '```'
    } | claude --print > "/tmp/inf-eco-scores-batch-${i}.json" &
    pids+=($!)
  done

  # Wait for all batches and fail if any failed
  for pid in "${pids[@]}"; do
    wait "$pid"
  done

  # Combine all batch scores
  python -c "
import json, glob, re
all_scores = []
for f in sorted(glob.glob('/tmp/inf-eco-scores-batch-*.json'),
                key=lambda x: int(re.search(r'(\d+)', x.rsplit('-',1)[1]).group())):
    raw = open(f).read().strip()
    if raw.startswith('\`\`\`'): raw = raw.split('\n', 1)[1]
    if raw.endswith('\`\`\`'): raw = raw.rsplit('\`\`\`', 1)[0].strip()
    all_scores.extend(json.loads(raw))
json.dump(all_scores, open('/tmp/inf-eco-scores.json', 'w'), indent=2)
"
  echo "Merging scores..."
  python src/merge_papers.py /tmp/inf-eco-papers.json /tmp/inf-eco-scores.json
else
  # Clear stale scores so news doesn't re-report old papers
  rm -f /tmp/inf-eco-scores.json
fi

# --- Hype signals: update from external sources ---

echo "Fetching hype signals..."
python src/fetch_hype_signals.py

echo "Updating hype signals..."
python src/rescore_hype.py

# --- Generate hype watch (Claude decides what's notable) ---

HAS_HYPE=0
if python src/build_hype_prompt.py > /tmp/inf-eco-hype-prompt.md 2>/dev/null; then
  echo "Generating hype watch..."
  claude --print < /tmp/inf-eco-hype-prompt.md > /tmp/inf-eco-hype-watch.md
  # Persist for next run's prompt context
  cp /tmp/inf-eco-hype-watch.md data/last-hype-watch.md
  if ! grep -q "NO_HYPE" /tmp/inf-eco-hype-watch.md; then
    HAS_HYPE=1
  else
    echo "Claude found nothing noteworthy in signal trends."
  fi
else
  echo "No papers with signal history to analyze."
fi

# --- Rescore + News (single Claude call, only for new papers) ---

HAS_NEWS=0
if [ "$new_count" -gt 0 ]; then
  echo "Generating rescore + news..."
  python src/generate_news.py
  HAS_NEWS=1
fi

# --- Append hype watch to news.md ---

if [ "$HAS_HYPE" = "1" ]; then
  if [ "$HAS_NEWS" = "1" ]; then
    # Append hype watch section to existing news
    {
      echo ""
      echo "---"
      echo ""
      echo "## Hype Watch"
      cat /tmp/inf-eco-hype-watch.md
    } >> news.md
  else
    # Only hype activity, no new papers — create news.md with just hype watch
    {
      echo "# Inference Ecosystem — Flash News"
      echo "**$(date +%Y-%m-%d)** — No new papers today."
      echo ""
      echo "---"
      echo ""
      echo "## Hype Watch"
      cat /tmp/inf-eco-hype-watch.md
    } > news.md
    HAS_NEWS=1
  fi
fi

echo "Rendering papers.md..."
python src/render.py

if [ "$HAS_NEWS" = "1" ]; then
  git add data/papers.json papers.md news.md
else
  echo "Nothing newsworthy, skipping news generation."
  git add data/papers.json papers.md
fi

# Always stage persisted hype watch (even if NO_HYPE — next run needs it)
[ -f data/last-hype-watch.md ] && git add data/last-hype-watch.md

# --- Commit and push ---

if git diff --cached --quiet; then
  echo "Nothing changed, skipping commit."
else
  msg="scan: $(date +%Y-%m-%d)"
  parts=()
  [ "$new_count" -gt 0 ] && parts+=("$new_count new papers scored")
  [ "$HAS_HYPE" = "1" ] && parts+=("hype watch")
  [ ${#parts[@]} -eq 0 ] && parts+=("hype updated from external signals")
  msg="$msg — $(IFS=', '; echo "${parts[*]}")"
  echo "Committing..."
  git commit -m "$msg"
  git push

  # --- Notify via Discord ---
  if [ "$HAS_NEWS" = "1" ] && [ -n "$DISCORD_TARGET" ] && command -v openclaw &>/dev/null; then
    echo "Posting news to Discord..."
    openclaw message send --channel discord --target "$DISCORD_TARGET" --message "<@231463543449321474>
$(cat news.md)" || echo "Warning: Discord notification failed." >&2
  fi
fi
