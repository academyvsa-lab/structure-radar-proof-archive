# Weekly System Performance Report
Week: 2026-W25
Window: 2026-06-15 00:00:00 to 2026-06-22 00:00:00 (UTC)
Generated: 2026-06-22 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 340
- Stop Hits: 103
- Expired: 6
- Open: 77
- Ambiguous: 0

Resolved (target or stop): 443
Terminal (target/stop/expired): 449

## 2. Realized Trade Performance (resolved only)
Wins: 340
Losses: 103
Win rate: 0.767 (340/443)

T1 reached: 340
T2 reached: 0

Avg RR to T1: 3.092299349240781 (n=461)
Avg RR to T2: 5.8229284164859 (n=461)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 2.8h
- Fastest resolution: 4m
- Slowest resolution: 3.2d
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 8
- Max consecutive wins: 31
- Unmapped status events (debug): 6791

## 4. Market Breakdown
- crypto: total 443 | target_hits 288 | stop_hits 76 | expired 3 | open 76
- equities: total 83 | target_hits 52 | stop_hits 27 | expired 3 | open 1

## 5. Tier Distribution
- starter: total 42 | target_hits 32 | stop_hits 10 | expired 0 | open 0
- pro: total 484 | target_hits 308 | stop_hits 93 | expired 6 | open 77

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 307 | 293 | 79.9% | 0.0% |
| Liquidity Sweep + Reclaim | 219 | 150 | 70.7% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 414 | 353 | 75.1% |
| H4 | 112 | 90 | 83.3% |

## Integrity
- ledger_slice_sha256: `fc96c9b73d0bb1be61b935a419937e28b69dcab0584a8be5448eac560fa642ae`
- engine_version: `v2`
