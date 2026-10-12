# Weekly System Performance Report
Week: 2026-W41
Window: 2026-10-05 00:00:00 to 2026-10-12 00:00:00 (UTC)
Generated: 2026-10-12 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 324
- Stop Hits: 84
- Expired: 26
- Open: 46
- Ambiguous: 0

Resolved (target or stop): 408
Terminal (target/stop/expired): 434

## 2. Realized Trade Performance (resolved only)
Wins: 324
Losses: 84
Win rate: 0.794 (324/408)

T1 reached: 324
T2 reached: 0

Avg RR to T1: 2.8217954545454544 (n=440)
Avg RR to T2: 5.317931818181818 (n=440)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 3.0h
- Fastest resolution: 4m
- Slowest resolution: 36.0h
- Longest open age: 6.9d

Stability:
- Max consecutive losses: 8
- Max consecutive wins: 42
- Unmapped status events (debug): 15066

## 4. Market Breakdown
- crypto: total 345 | target_hits 227 | stop_hits 69 | expired 3 | open 46
- equities: total 135 | target_hits 97 | stop_hits 15 | expired 23 | open 0

## 5. Tier Distribution
- starter: total 48 | target_hits 39 | stop_hits 9 | expired 0 | open 0
- pro: total 432 | target_hits 285 | stop_hits 75 | expired 26 | open 46

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 308 | 289 | 82.0% | 0.0% |
| Liquidity Sweep + Reclaim | 172 | 119 | 73.1% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 417 | 352 | 77.8% |
| H4 | 63 | 56 | 89.3% |

## Integrity
- ledger_slice_sha256: `8fbf3de3f4d1c095537ea5d2d4029385837bb76ada3401e907f8f56fdd44af23`
- engine_version: `v2`
