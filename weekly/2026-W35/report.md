# Weekly System Performance Report
Week: 2026-W35
Window: 2026-08-24 00:00:00 to 2026-08-31 00:00:00 (UTC)
Generated: 2026-08-31 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 366
- Stop Hits: 101
- Expired: 29
- Open: 50
- Ambiguous: 0

Resolved (target or stop): 467
Terminal (target/stop/expired): 496

## 2. Realized Trade Performance (resolved only)
Wins: 366
Losses: 101
Win rate: 0.784 (366/467)

T1 reached: 366
T2 reached: 0

Avg RR to T1: 5.350555555555555 (n=504)
Avg RR to T2: 10.068194444444444 (n=504)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 4.2h
- Fastest resolution: 4m
- Slowest resolution: 2.8d
- Longest open age: 6.6d

Stability:
- Max consecutive losses: 6
- Max consecutive wins: 49
- Unmapped status events (debug): 11852

## 4. Market Breakdown
- crypto: total 427 | target_hits 292 | stop_hits 79 | expired 8 | open 48
- equities: total 119 | target_hits 74 | stop_hits 22 | expired 21 | open 2

## 5. Tier Distribution
- pro: total 510 | target_hits 339 | stop_hits 95 | expired 27 | open 49
- starter: total 36 | target_hits 27 | stop_hits 6 | expired 2 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 329 | 304 | 81.6% | 0.0% |
| Liquidity Sweep + Reclaim | 217 | 163 | 72.4% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 471 | 408 | 78.9% |
| H4 | 75 | 59 | 74.6% |

## Integrity
- ledger_slice_sha256: `4828e197bcaaa11e9c72b3a8cfa819d532269c421597b2fcf2fbde74c59c7b67`
- engine_version: `v2`
