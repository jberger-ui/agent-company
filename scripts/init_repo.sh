#!/usr/bin/env bash
set -euo pipefail

git init

git add .
git commit -m "Initial Agent Company package"

echo "Repository initialized. Add your remote and push when ready."
