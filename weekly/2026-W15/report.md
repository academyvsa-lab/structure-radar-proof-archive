# Weekly System Performance Report
Week: 2026-W15
Window: 2026-04-06 00:00:00 to 2026-04-13 00:00:00 (UTC)
Generated: 2026-04-13 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 335
- Stop Hits: 65
- Expired: 23
- Open: 43
- Ambiguous: 0

Resolved (target or stop): 400
Terminal (target/stop/expired): 423

## 2. Realized Trade Performance (resolved only)
Wins: 335
Losses: 65
Win rate: 0.838 (335/400)

T1 reached: 335
T2 reached: 0

Avg RR to T1: 2.487511415525114 (n=438)
Avg RR to T2: 4.678949771689498 (n=438)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 4.2h
- Fastest resolution: 3m
- Slowest resolution: 4.5d
- Longest open age: 6.9d

Stability:
- Max consecutive losses: 6
- Max consecutive wins: 41
- Unmapped status events (debug): 2263

## 4. Market Breakdown
- crypto: total 345 | target_hits 257 | stop_hits 52 | expired 0 | open 36
- equities: total 121 | target_hits 78 | stop_hits 13 | expired 23 | open 7

## 5. Tier Distribution
- pro: total 445 | target_hits 316 | stop_hits 63 | expired 23 | open 43
- starter: total 21 | target_hits 19 | stop_hits 2 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 332 | 302 | 87.4% | 0.0% |
| Liquidity Sweep + Reclaim | 134 | 98 | 72.4% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 357 | 310 | 83.5% |
| H4 | 109 | 90 | 84.4% |

## Integrity
- ledger_slice_sha256: `676c66577a5ce82c1a0e5e4faf0e45e4e8a88041b92e73a371b6893947e884ff`
- engine_version: `v2`
