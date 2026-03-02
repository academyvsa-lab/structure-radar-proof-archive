# System Performance Proof Archive

This repository contains the public weekly performance archive of a rules-based trading system.

All reports are generated automatically from the production alert ledger and published in Coordinated Universal Time (UTC).

---

## Methodology Overview

- Alerts are emitted by a deterministic rule engine.
- Status transitions are recorded in an immutable ledger.
- Weekly reports are generated exclusively from ledger data.
- No manual performance adjustments are applied.

---

## Definitions

- **Resolved trades:** Target Hits + Stop Hits  
- **Terminal events:** Target Hits + Stop Hits + Expired  
- **Open:** Alerts without terminal status  

Win rate is calculated on resolved trades only.

---

## Data Integrity

Each weekly snapshot includes:

- SHA256 hash of the processed ledger slice  
- Generation timestamp (UTC)  
- Engine version identifier  

Snapshot files are machine-readable and preserved in version history.

---

## Purpose

This archive exists for transparency, documentation, and longitudinal performance tracking.

Educational and decision-support purposes only.
