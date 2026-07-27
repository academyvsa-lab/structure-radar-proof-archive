# Weekly System Performance Report
Week: 2026-W30
Window: 2026-07-20 00:00:00 to 2026-07-27 00:00:00 (UTC)
Generated: 2026-07-27 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 380
- Stop Hits: 110
- Expired: 15
- Open: 86
- Ambiguous: 0

Resolved (target or stop): 490
Terminal (target/stop/expired): 505

## 2. Realized Trade Performance (resolved only)
Wins: 380
Losses: 110
Win rate: 0.776 (380/490)

T1 reached: 380
T2 reached: 0

Avg RR to T1: 4.154145383104126 (n=509)
Avg RR to T2: 7.799037328094303 (n=509)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 3.6h
- Fastest resolution: 4m
- Slowest resolution: 3.0d
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 8
- Max consecutive wins: 46
- Unmapped status events (debug): 9310

## 4. Market Breakdown
- crypto: total 493 | target_hits 325 | stop_hits 80 | expired 2 | open 86
- equities: total 98 | target_hits 55 | stop_hits 30 | expired 13 | open 0

## 5. Tier Distribution
- pro: total 548 | target_hits 347 | stop_hits 100 | expired 15 | open 86
- starter: total 43 | target_hits 33 | stop_hits 10 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 356 | 333 | 84.4% | 0.0% |
| Liquidity Sweep + Reclaim | 235 | 157 | 63.1% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 489 | 412 | 77.2% |
| H4 | 102 | 78 | 79.5% |

## Integrity
- ledger_slice_sha256: `1348abb81f3fa4d93cf85a55d1eeb591818168a111e9900e51d18198c37c3e76`
- engine_version: `v2`
