# Weekly System Performance Report
Week: 2026-W28
Window: 2026-07-06 00:00:00 to 2026-07-13 00:00:00 (UTC)
Generated: 2026-07-13 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 360
- Stop Hits: 99
- Expired: 16
- Open: 58
- Ambiguous: 0

Resolved (target or stop): 459
Terminal (target/stop/expired): 475

## 2. Realized Trade Performance (resolved only)
Wins: 360
Losses: 99
Win rate: 0.784 (360/459)

T1 reached: 360
T2 reached: 0

Avg RR to T1: 3.5679754601226996 (n=489)
Avg RR to T2: 6.690327198364009 (n=489)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 49m
- Average time to resolution: 3.8h
- Fastest resolution: 4m
- Slowest resolution: 48.0h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 6
- Max consecutive wins: 44
- Unmapped status events (debug): 8319

## 4. Market Breakdown
- crypto: total 412 | target_hits 282 | stop_hits 68 | expired 4 | open 58
- equities: total 121 | target_hits 78 | stop_hits 31 | expired 12 | open 0

## 5. Tier Distribution
- pro: total 508 | target_hits 338 | stop_hits 96 | expired 16 | open 58
- starter: total 25 | target_hits 22 | stop_hits 3 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 354 | 328 | 82.9% | 0.0% |
| Liquidity Sweep + Reclaim | 179 | 131 | 67.2% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 438 | 390 | 77.9% |
| H4 | 95 | 69 | 81.2% |

## Integrity
- ledger_slice_sha256: `ca57a6fa2ca65c3035eb395ee5941174f1da743afbcaf6eb575d4d4ff61cdbdb`
- engine_version: `v2`
