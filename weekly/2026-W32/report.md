# Weekly System Performance Report
Week: 2026-W32
Window: 2026-08-03 00:00:00 to 2026-08-10 00:00:00 (UTC)
Generated: 2026-08-10 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 434
- Stop Hits: 61
- Expired: 15
- Open: 117
- Ambiguous: 0

Resolved (target or stop): 495
Terminal (target/stop/expired): 510

## 2. Realized Trade Performance (resolved only)
Wins: 434
Losses: 61
Win rate: 0.877 (434/495)

T1 reached: 434
T2 reached: 0

Avg RR to T1: 3.171577946768061 (n=526)
Avg RR to T2: 5.956863117870722 (n=526)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 4.3h
- Fastest resolution: 4m
- Slowest resolution: 5.5d
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 3
- Max consecutive wins: 25
- Unmapped status events (debug): 10297

## 4. Market Breakdown
- crypto: total 511 | target_hits 348 | stop_hits 44 | expired 7 | open 112
- equities: total 116 | target_hits 86 | stop_hits 17 | expired 8 | open 5

## 5. Tier Distribution
- pro: total 590 | target_hits 399 | stop_hits 59 | expired 15 | open 117
- starter: total 37 | target_hits 35 | stop_hits 2 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 384 | 363 | 89.8% | 0.0% |
| Liquidity Sweep + Reclaim | 243 | 132 | 81.8% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 521 | 419 | 87.6% |
| H4 | 106 | 76 | 88.2% |

## Integrity
- ledger_slice_sha256: `7fa527d85766342a8df4b741beebf2409efc2d695e6d73883a4864679e57229d`
- engine_version: `v2`
