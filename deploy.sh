#!/bin/bash
set -eo pipefail

rsync -av --exclude .venv --exclude .git --exclude __pycache__ \
  "$(dirname "$0")/" foadell:~/inf-eco-agent/
