# Weekly System Performance Report
Week: 2026-W38
Window: 2026-09-14 00:00:00 to 2026-09-21 00:00:00 (UTC)
Generated: 2026-09-21 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 485
- Stop Hits: 102
- Expired: 27
- Open: 75
- Ambiguous: 0

Resolved (target or stop): 587
Terminal (target/stop/expired): 614

## 2. Realized Trade Performance (resolved only)
Wins: 485
Losses: 102
Win rate: 0.826 (485/587)

T1 reached: 485
T2 reached: 0

Avg RR to T1: 3.6805617977528087 (n=623)
Avg RR to T2: 6.914478330658106 (n=623)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 2.3h
- Fastest resolution: 4m
- Slowest resolution: 23.9h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 5
- Max consecutive wins: 30
- Unmapped status events (debug): 13321

## 4. Market Breakdown
- crypto: total 584 | target_hits 422 | stop_hits 86 | expired 2 | open 74
- equities: total 105 | target_hits 63 | stop_hits 16 | expired 25 | open 1

## 5. Tier Distribution
- pro: total 635 | target_hits 441 | stop_hits 94 | expired 25 | open 75
- starter: total 54 | target_hits 44 | stop_hits 8 | expired 2 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 461 | 431 | 87.2% | 0.0% |
| Liquidity Sweep + Reclaim | 228 | 156 | 69.9% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 581 | 499 | 82.6% |
| H4 | 108 | 88 | 83.0% |

## Integrity
- ledger_slice_sha256: `640f87acb247b3abf1fdcbc4e5783de642fce80412d7ab19bc0618d8461135e8`
- engine_version: `v2`
