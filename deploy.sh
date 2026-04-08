#!/bin/bash
set -eo pipefail

if ! git diff --quiet || ! git diff --cached --quiet || [ "$(git rev-parse HEAD)" != "$(git rev-parse @{u})" ]; then
  echo "Error: local repo has uncommitted or unpushed changes." >&2
  exit 1
fi

ssh foadell 'cd ~/inf-eco-agent && git pull --ff-only'
