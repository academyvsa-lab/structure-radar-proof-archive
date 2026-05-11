# Weekly System Performance Report
Week: 2026-W19
Window: 2026-05-04 00:00:00 to 2026-05-11 00:00:00 (UTC)
Generated: 2026-05-11 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 493
- Stop Hits: 85
- Expired: 27
- Open: 53
- Ambiguous: 0

Resolved (target or stop): 578
Terminal (target/stop/expired): 605

## 2. Realized Trade Performance (resolved only)
Wins: 493
Losses: 85
Win rate: 0.853 (493/578)

T1 reached: 493
T2 reached: 0

Avg RR to T1: 2.5249427168576104 (n=611)
Avg RR to T2: 4.746153846153846 (n=611)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 3.2h
- Fastest resolution: 4m
- Slowest resolution: 48.0h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 6
- Max consecutive wins: 48
- Unmapped status events (debug): 4116

## 4. Market Breakdown
- crypto: total 545 | target_hits 429 | stop_hits 57 | expired 11 | open 48
- equities: total 113 | target_hits 64 | stop_hits 28 | expired 16 | open 5

## 5. Tier Distribution
- starter: total 84 | target_hits 73 | stop_hits 9 | expired 0 | open 2
- pro: total 574 | target_hits 420 | stop_hits 76 | expired 27 | open 51

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 495 | 465 | 88.8% | 0.0% |
| Liquidity Sweep + Reclaim | 163 | 113 | 70.8% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 496 | 435 | 84.1% |
| H4 | 162 | 143 | 88.8% |

## Integrity
- ledger_slice_sha256: `b2593a1758f538ffb63d85b0c55b251c3162d3b5b2f5499cf8b6d836e328be06`
- engine_version: `v2`
