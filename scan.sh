#!/usr/bin/env bash
set -eo pipefail
cd "$(dirname "$0")"

# Discard uncommitted changes from crashed runs, then sync with remote.
# Unpushed commits (scored data) are preserved via rebase.
git checkout -- .
git pull --rebase

# Activate venv if it exists
if [ -d .venv ]; then
  # shellcheck source=/dev/null
  source .venv/bin/activate
fi

# Allow running from within a Claude Code session or hook
unset CLAUDECODE
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1

DISCORD_TARGET="${DISCORD_CHANNEL:-}"

# --- Error handling ---

notify_error() {
  local msg="$1"
  if [ -n "$DISCORD_TARGET" ] && command -v openclaw &> /dev/null; then
    openclaw message send --channel discord --target "$DISCORD_TARGET" \
      --message "<@231463543449321474> **inf-eco-agent failed:**
\`\`\`
$msg
\`\`\`" 2> /dev/null || true
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

# --- Scan: fetch → enqueue → drain queue ---
#
# The scoring step is rate-limited by claude's daily/per-minute quota, so we
# decouple discovery from scoring. fetch_papers.py finds new papers (deduping
# against papers.json and the queue); they get split into 100-paper batches
# under data/queue/. Each run drains up to MAX_DRAIN of the oldest batches
# sequentially; whatever doesn't fit waits until tomorrow.

MAX_DRAIN=10

mkdir -p data/queue

echo "Fetching papers from arXiv..."
python src/fetch_papers.py > /tmp/inf-eco-papers.json

new_count=$(python -c "import json; print(len(json.load(open('/tmp/inf-eco-papers.json'))))")
echo "Fetched $new_count new papers from arXiv"

if [ "$new_count" -gt 0 ]; then
  python -c "
import json, math, time
papers = json.load(open('/tmp/inf-eco-papers.json'))
ts = int(time.time())
n = math.ceil(len(papers) / 100)
for i in range(n):
    batch = papers[i*100:(i+1)*100]
    json.dump(batch, open(f'data/queue/batch_{ts}_{i:03d}.json', 'w'), indent=2)
print(f'Enqueued {len(papers)} papers as {n} batch(es).')
"
fi

# Drain the oldest MAX_DRAIN queue files. Batch filenames embed a unix
# timestamp prefix, so sorting by name is chronological.
mapfile -t queue_batches < <(find data/queue -maxdepth 1 -name 'batch_*.json' | sort | head -n "$MAX_DRAIN")
num_batches=${#queue_batches[@]}
total_queued=$(find data/queue -maxdepth 1 -name 'batch_*.json' | wc -l)
processed=()
rm -f /tmp/inf-eco-scores-out-*.json /tmp/inf-eco-scores.json

if [ "$num_batches" -gt 0 ]; then
  echo "Draining $num_batches of $total_queued queued batch(es) sequentially..."

  for batch in "${queue_batches[@]}"; do
    name=$(basename "$batch" .json)
    out="/tmp/inf-eco-scores-out-${name}.json"
    echo "  $name..."
    {
      cat score-prompt.md
      echo ""
      echo "## Papers JSON"
      echo '```json'
      cat "$batch"
      echo '```'
    } | claude --print --effort max > "$out" || true

    if python -c "
import sys
sys.path.insert(0, 'src')
from parse_scores import try_parse_scores
sys.exit(0 if try_parse_scores('$out') else 1)
" 2> /dev/null; then
      echo "    ok"
      processed+=("$batch")
    else
      echo "    failed (likely rate-limited); leaving in queue"
      rm -f "$out"
    fi
  done

  if [ ${#processed[@]} -gt 0 ]; then
    printf '%s\n' "${processed[@]}" > /tmp/inf-eco-processed-list.txt
    python src/finalize_score_run.py /tmp/inf-eco-processed-list.txt \
      /tmp/inf-eco-papers-scored.json /tmp/inf-eco-scores.json

    echo "Merging scores..."
    python src/merge_papers.py /tmp/inf-eco-papers-scored.json /tmp/inf-eco-scores.json

    # Drop processed queue files (the scores are now in papers.json).
    for batch in "${processed[@]}"; do
      rm -f "$batch"
    done

    # Commit scoring progress before downstream steps so a hype/news failure
    # doesn't roll back the day's actual work.
    git add data/papers.json data/queue/
    if ! git diff --cached --quiet; then
      git -c commit.gpgsign=false commit -s --quiet \
        -m "[Scan] Score ${#processed[@]} batch(es) — $(date +%Y-%m-%d)"
    fi
  fi
fi

# --- Hype signals: update from external sources ---

echo "Fetching hype signals..."
python src/fetch_hype_signals.py

echo "Updating hype signals..."
python src/rescore_hype.py

# --- Generate hype watch (Claude decides what's notable) ---

HAS_HYPE=0
if python src/build_hype_prompt.py > /tmp/inf-eco-hype-prompt.md 2> /dev/null; then
  echo "Generating hype watch..."
  claude --print --effort max < /tmp/inf-eco-hype-prompt.md > /tmp/inf-eco-hype-watch.md
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

# --- Rescore + News (only when this run actually scored papers) ---

HAS_NEWS=0
if [ -s /tmp/inf-eco-scores.json ]; then
  echo "Generating rescore + news..."
  python src/generate_news.py
  HAS_NEWS=1
fi

# --- Append hype watch to news.md (always shown) ---

# Determine hype watch content
if [ "$HAS_HYPE" = "1" ]; then
  HYPE_CONTENT=$(cat /tmp/inf-eco-hype-watch.md)
else
  HYPE_CONTENT="Nothing noteworthy in signal trends today."
fi

if [ "$HAS_NEWS" = "1" ]; then
  # Append hype watch section to existing news
  {
    echo ""
    echo "---"
    echo ""
    echo "## Surge Watch"
    echo ""
    echo "$HYPE_CONTENT"
  } >> news.md
else
  # No new papers — create news.md with just hype watch
  {
    echo "# Inference Ecosystem — Flash News"
    echo "**$(date +%Y-%m-%d)** — No new papers today."
    echo ""
    echo "---"
    echo ""
    echo "## Surge Watch"
    echo ""
    echo "$HYPE_CONTENT"
  } > news.md
  HAS_NEWS=1
fi

if [ "$HAS_NEWS" = "1" ]; then
  git add data/papers.json news.md
else
  echo "Nothing newsworthy, skipping news generation."
  git add data/papers.json
fi

# Always stage persisted hype watch (even if NO_HYPE — next run needs it)
[ -f data/last-hype-watch.md ] && git add data/last-hype-watch.md

# --- Commit and push ---

if git diff --cached --quiet; then
  echo "Nothing changed, skipping commit."
else
  msg="[Scan] Daily $(date +%Y-%m-%d)"
  remaining=$((total_queued - ${#processed[@]}))
  parts=()
  [ "$new_count" -gt 0 ] && parts+=("$new_count fetched")
  [ ${#processed[@]} -gt 0 ] && parts+=("${#processed[@]} batch(es) scored")
  [ "$remaining" -gt 0 ] && parts+=("$remaining still queued")
  [ "$HAS_HYPE" = "1" ] && parts+=("hype watch")
  [ ${#parts[@]} -eq 0 ] && parts+=("hype updated from external signals")
  msg="$msg — $(
    IFS=', '
    echo "${parts[*]}"
  )"
  echo "Committing..."
  git commit -s -m "$msg"
  git push

  # --- Notify via Discord ---
  if [ "$HAS_NEWS" = "1" ] && [ -n "$DISCORD_TARGET" ] && command -v openclaw &> /dev/null; then
    echo "Posting news to Discord..."
    openclaw message send --channel discord --target "$DISCORD_TARGET" --message "<@231463543449321474>
$(cat news.md)" || echo "Warning: Discord notification failed." >&2
  fi
fi
