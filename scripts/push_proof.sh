#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/push_proof.sh /home/ubuntu/proof-archive
#
# Expected output:
# - If no changes: "No changes to push."
# - If changes:
#   - "Pushing to origin..."
#   - "OK - pushed."

REPO_DIR="${1:?repo dir required}"

cd "$REPO_DIR"

git add -A

if git diff --cached --quiet; then
  echo "No changes to push."
  exit 0
fi

WEEK="$(date -u +%G-W%V)"
git commit -m "Weekly proof update: ${WEEK}"

echo "Pushing to origin..."
git push origin main

echo "OK - pushed."
