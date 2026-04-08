#!/bin/bash
set -eo pipefail

ssh foadell 'cd ~/inf-eco-agent && git pull --rebase'
