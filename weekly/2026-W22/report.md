# Weekly System Performance Report
Week: 2026-W22
Window: 2026-05-25 00:00:00 to 2026-06-01 00:00:00 (UTC)
Generated: 2026-06-01 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 294
- Stop Hits: 76
- Expired: 21
- Open: 61
- Ambiguous: 0

Resolved (target or stop): 370
Terminal (target/stop/expired): 391

## 2. Realized Trade Performance (resolved only)
Wins: 294
Losses: 76
Win rate: 0.795 (294/370)

T1 reached: 294
T2 reached: 0

Avg RR to T1: 4.758255528255528 (n=407)
Avg RR to T2: 8.945552825552825 (n=407)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 3.5h
- Fastest resolution: 4m
- Slowest resolution: 3.0d
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 7
- Max consecutive wins: 23
- Unmapped status events (debug): 5548

## 4. Market Breakdown
- crypto: total 330 | target_hits 202 | stop_hits 63 | expired 6 | open 59
- equities: total 122 | target_hits 92 | stop_hits 13 | expired 15 | open 2

## 5. Tier Distribution
- starter: total 51 | target_hits 40 | stop_hits 8 | expired 0 | open 3
- pro: total 401 | target_hits 254 | stop_hits 68 | expired 21 | open 58

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 281 | 244 | 82.0% | 0.0% |
| Liquidity Sweep + Reclaim | 171 | 126 | 74.6% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 348 | 294 | 81.3% |
| H4 | 104 | 76 | 72.4% |

## Integrity
- ledger_slice_sha256: `cdf7efa9664ac1f71c026447d64383c85f9f8ee467525d79eae0abc5f55e2e0e`
- engine_version: `v2`
