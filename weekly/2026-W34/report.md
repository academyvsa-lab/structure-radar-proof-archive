# Weekly System Performance Report
Week: 2026-W34
Window: 2026-08-17 00:00:00 to 2026-08-24 00:00:00 (UTC)
Generated: 2026-08-24 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 493
- Stop Hits: 85
- Expired: 22
- Open: 93
- Ambiguous: 0

Resolved (target or stop): 578
Terminal (target/stop/expired): 600

## 2. Realized Trade Performance (resolved only)
Wins: 493
Losses: 85
Win rate: 0.853 (493/578)

T1 reached: 493
T2 reached: 0

Avg RR to T1: 2.998806451612903 (n=620)
Avg RR to T2: 5.643983870967742 (n=620)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 2.5h
- Fastest resolution: 4m
- Slowest resolution: 27.9h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 9
- Max consecutive wins: 47
- Unmapped status events (debug): 11232

## 4. Market Breakdown
- crypto: total 614 | target_hits 454 | stop_hits 58 | expired 10 | open 92
- equities: total 79 | target_hits 39 | stop_hits 27 | expired 12 | open 1

## 5. Tier Distribution
- pro: total 638 | target_hits 441 | stop_hits 82 | expired 22 | open 93
- starter: total 55 | target_hits 52 | stop_hits 3 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 501 | 469 | 89.8% | 0.0% |
| Liquidity Sweep + Reclaim | 192 | 109 | 66.1% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 553 | 456 | 83.6% |
| H4 | 140 | 122 | 91.8% |

## Integrity
- ledger_slice_sha256: `d9a9671c1c31a96126122ceda5310d08baa7add234520e1850ad540e6203edea`
- engine_version: `v2`
