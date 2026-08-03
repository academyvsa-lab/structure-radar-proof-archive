# Weekly System Performance Report
Week: 2026-W31
Window: 2026-07-27 00:00:00 to 2026-08-03 00:00:00 (UTC)
Generated: 2026-08-03 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 368
- Stop Hits: 87
- Expired: 16
- Open: 66
- Ambiguous: 0

Resolved (target or stop): 455
Terminal (target/stop/expired): 471

## 2. Realized Trade Performance (resolved only)
Wins: 368
Losses: 87
Win rate: 0.809 (368/455)

T1 reached: 368
T2 reached: 0

Avg RR to T1: 3.314149377593361 (n=482)
Avg RR to T2: 6.214004149377594 (n=482)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 2.9h
- Fastest resolution: 4m
- Slowest resolution: 2.2d
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 3
- Max consecutive wins: 57
- Unmapped status events (debug): 9819

## 4. Market Breakdown
- crypto: total 398 | target_hits 277 | stop_hits 57 | expired 3 | open 61
- equities: total 139 | target_hits 91 | stop_hits 30 | expired 13 | open 5

## 5. Tier Distribution
- pro: total 485 | target_hits 324 | stop_hits 80 | expired 16 | open 65
- starter: total 52 | target_hits 44 | stop_hits 7 | expired 0 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 302 | 282 | 82.3% | 0.0% |
| Liquidity Sweep + Reclaim | 235 | 173 | 78.6% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 464 | 397 | 81.4% |
| H4 | 73 | 58 | 77.6% |

## Integrity
- ledger_slice_sha256: `7cdd70956c4d6d32d669e8e1a8699f8dc1b6f770d26c5f785c91f3b375f5c215`
- engine_version: `v2`
