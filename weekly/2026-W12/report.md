# Weekly System Performance Report
Week: 2026-W12
Window: 2026-03-16 00:00:00 to 2026-03-23 00:00:00 (UTC)
Generated: 2026-03-23 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 284
- Stop Hits: 104
- Expired: 11
- Open: 43
- Ambiguous: 0

Resolved (target or stop): 388
Terminal (target/stop/expired): 399

## 2. Realized Trade Performance (resolved only)
Wins: 284
Losses: 104
Win rate: 0.732 (284/388)

T1 reached: 284
T2 reached: 0

Avg RR to T1: 4.1725062034739455 (n=403)
Avg RR to T2: 7.850818858560794 (n=403)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 4.3h
- Fastest resolution: 4m
- Slowest resolution: 2.2d
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 9
- Max consecutive wins: 96
- Unmapped status events (debug): 1022

## 4. Market Breakdown
- crypto: total 326 | target_hits 209 | stop_hits 73 | expired 2 | open 42
- equities: total 116 | target_hits 75 | stop_hits 31 | expired 9 | open 1

## 5. Tier Distribution
- pro: total 408 | target_hits 256 | stop_hits 99 | expired 11 | open 42
- starter: total 34 | target_hits 28 | stop_hits 5 | expired 0 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 277 | 266 | 75.2% | 0.0% |
| Liquidity Sweep + Reclaim | 165 | 122 | 68.9% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 352 | 306 | 70.9% |
| H4 | 90 | 82 | 81.7% |

## Integrity
- ledger_slice_sha256: `36b532a450cf3cd899a1dab77b2f2cef1583b509a272a574124c7a9cd1ade34f`
- engine_version: `v2`
