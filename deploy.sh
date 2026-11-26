#!/bin/bash
set -eo pipefail

# The host's SSH alias stays out of the repository; keep it in the local, gitignored .env
if [ -f .env ]; then
  # shellcheck source=/dev/null
  source .env
fi
: "${DEPLOY_HOST:?DEPLOY_HOST is not set, put export DEPLOY_HOST=<ssh alias> in .env}"

if ! git diff --quiet || ! git diff --cached --quiet || [ "$(git rev-parse HEAD)" != "$(git rev-parse '@{u}')" ]; then
  echo "Error: local repo has uncommitted or unpushed changes." >&2
  exit 1
fi

ssh "$DEPLOY_HOST" 'cd ~/inf-eco-agent && git pull --ff-only'
