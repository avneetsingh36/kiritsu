#!/usr/bin/env bash
# clean.sh – trim Python + CDK build junk
set -euo pipefail

DEEP=false
if [[ "${1:-}" == "--deep" ]]; then
  DEEP=true
fi

echo "➤ Removing __pycache__ folders..."
find . -type d -name '__pycache__' -exec rm -rf {} +

echo "➤ Removing *.py[cod] files..."
find . -type f \( -name '*.pyc' -o -name '*.pyo' -o -name '*.pyd' \) -delete

echo "➤ Removing CDK output..."
rm -rf cdk.out

echo "➤ Removing other build artefacts..."
find . -type d -name '.pytest_cache' -exec rm -rf {} +
find . -type d -name '.mypy_cache'  -exec rm -rf {} +
find . -type d -name '*.egg-info'   -exec rm -rf {} +

if $DEEP; then
  echo "➤ Deep clean: removing .venv and node_modules..."
  rm -rf .venv node_modules
fi

echo "✓ Clean complete."

