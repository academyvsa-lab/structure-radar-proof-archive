# Weekly System Performance Report
Week: 2026-W17
Window: 2026-04-20 00:00:00 to 2026-04-27 00:00:00 (UTC)
Generated: 2026-04-27 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 348
- Stop Hits: 96
- Expired: 20
- Open: 100
- Ambiguous: 0

Resolved (target or stop): 444
Terminal (target/stop/expired): 464

## 2. Realized Trade Performance (resolved only)
Wins: 348
Losses: 96
Win rate: 0.784 (348/444)

T1 reached: 348
T2 reached: 0

Avg RR to T1: 4.005365853658537 (n=492)
Avg RR to T2: 7.525264227642276 (n=492)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 4.2h
- Fastest resolution: 4m
- Slowest resolution: 48.0h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 6
- Max consecutive wins: 32
- Unmapped status events (debug): 3166

## 4. Market Breakdown
- crypto: total 426 | target_hits 251 | stop_hits 71 | expired 14 | open 90
- equities: total 138 | target_hits 97 | stop_hits 25 | expired 6 | open 10

## 5. Tier Distribution
- starter: total 47 | target_hits 35 | stop_hits 10 | expired 0 | open 2
- pro: total 517 | target_hits 313 | stop_hits 86 | expired 20 | open 98

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 333 | 287 | 80.5% | 0.0% |
| Liquidity Sweep + Reclaim | 231 | 157 | 74.5% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 438 | 359 | 77.7% |
| H4 | 126 | 85 | 81.2% |

## Integrity
- ledger_slice_sha256: `b6262a29bf589ac11f4757e69be9b4c73634dca39b68e7a328614b15451a1715`
- engine_version: `v2`
