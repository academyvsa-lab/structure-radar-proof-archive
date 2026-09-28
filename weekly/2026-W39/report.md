# Weekly System Performance Report
Week: 2026-W39
Window: 2026-09-21 00:00:00 to 2026-09-28 00:00:00 (UTC)
Generated: 2026-09-28 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 473
- Stop Hits: 133
- Expired: 16
- Open: 70
- Ambiguous: 0

Resolved (target or stop): 606
Terminal (target/stop/expired): 622

## 2. Realized Trade Performance (resolved only)
Wins: 473
Losses: 133
Win rate: 0.781 (473/606)

T1 reached: 473
T2 reached: 0

Avg RR to T1: 3.4871987480438187 (n=639)
Avg RR to T2: 6.550704225352112 (n=639)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 44m
- Average time to resolution: 3.5h
- Fastest resolution: 4m
- Slowest resolution: 2.2d
- Longest open age: 6.9d

Stability:
- Max consecutive losses: 14
- Max consecutive wins: 32
- Unmapped status events (debug): 13942

## 4. Market Breakdown
- crypto: total 569 | target_hits 399 | stop_hits 100 | expired 4 | open 66
- equities: total 123 | target_hits 74 | stop_hits 33 | expired 12 | open 4

## 5. Tier Distribution
- pro: total 668 | target_hits 449 | stop_hits 133 | expired 16 | open 70
- starter: total 24 | target_hits 24 | stop_hits 0 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 492 | 469 | 80.4% | 0.0% |
| Liquidity Sweep + Reclaim | 200 | 137 | 70.1% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 557 | 493 | 76.7% |
| H4 | 135 | 113 | 84.1% |

## Integrity
- ledger_slice_sha256: `1ff78f7906800293d96d8740faa54a5c1278c9189e42b6b7cb6fc9e14d85df1c`
- engine_version: `v2`
