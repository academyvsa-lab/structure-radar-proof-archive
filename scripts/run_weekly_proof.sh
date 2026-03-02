#!/usr/bin/env bash
set -euo pipefail

# Weekly job wrapper (uses flock to prevent overlaps)
# Usage:
#   ./scripts/run_weekly_proof.sh /home/ubuntu/structure-radar-oracle/output/alerts_ledger.jsonl /home/ubuntu/proof-archive
#
# Expected output:
# - "OK" block from build_weekly_proof.py
# - Then either "No changes to push." or push output.

LEDGER="${1:?ledger path required}"
PROOF_DIR="${2:?proof repo dir required}"

LOCK="/tmp/proof_archive.lock"

exec /usr/bin/flock -n "$LOCK" bash -lc "
  python3 \"$PROOF_DIR/scripts/build_weekly_proof.py\" --ledger \"$LEDGER\" --out-dir \"$PROOF_DIR\" --rebuild-manifest --engine-version v1
  \"$PROOF_DIR/scripts/push_proof.sh\" \"$PROOF_DIR\"
"
