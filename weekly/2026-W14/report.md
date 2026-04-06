# Weekly System Performance Report
Week: 2026-W14
Window: 2026-03-30 00:00:00 to 2026-04-06 00:00:00 (UTC)
Generated: 2026-04-06 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 381
- Stop Hits: 74
- Expired: 7
- Open: 66
- Ambiguous: 0

Resolved (target or stop): 455
Terminal (target/stop/expired): 462

## 2. Realized Trade Performance (resolved only)
Wins: 381
Losses: 74
Win rate: 0.837 (381/455)

T1 reached: 381
T2 reached: 0

Avg RR to T1: 8.831057082452432 (n=473)
Avg RR to T2: 16.598012684989428 (n=473)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 24m
- Average time to resolution: 4.2h
- Fastest resolution: 4m
- Slowest resolution: 3.2d
- Longest open age: 6.9d

Stability:
- Max consecutive losses: 4
- Max consecutive wins: 30
- Unmapped status events (debug): 1790

## 4. Market Breakdown
- crypto: total 426 | target_hits 302 | stop_hits 61 | expired 2 | open 61
- equities: total 102 | target_hits 79 | stop_hits 13 | expired 5 | open 5

## 5. Tier Distribution
- pro: total 482 | target_hits 341 | stop_hits 69 | expired 7 | open 65
- starter: total 46 | target_hits 40 | stop_hits 5 | expired 0 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 325 | 311 | 85.5% | 0.0% |
| Liquidity Sweep + Reclaim | 203 | 144 | 79.9% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 398 | 352 | 86.6% |
| H4 | 130 | 103 | 73.8% |

## Integrity
- ledger_slice_sha256: `1870cf986e08149ac41a68146b778b1f85a7c1e4db8d8ad71baae0369c7904be`
- engine_version: `v2`
