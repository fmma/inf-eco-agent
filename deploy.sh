#!/bin/bash
set -eo pipefail

ssh foadell 'cd ~/inf-eco-agent && git diff --quiet && git diff --cached --quiet && test "$(git rev-parse HEAD)" = "$(git rev-parse @{u})" || { echo "Error: foadell has unpushed local changes." >&2; exit 1; }; git pull --ff-only'
