# Weekly System Performance Report
Week: 2026-W13
Window: 2026-03-23 00:00:00 to 2026-03-30 00:00:00 (UTC)
Generated: 2026-03-30 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 249
- Stop Hits: 90
- Expired: 18
- Open: 48
- Ambiguous: 0

Resolved (target or stop): 339
Terminal (target/stop/expired): 357

## 2. Realized Trade Performance (resolved only)
Wins: 249
Losses: 90
Win rate: 0.735 (249/339)

T1 reached: 249
T2 reached: 0

Avg RR to T1: 5.574289617486339 (n=366)
Avg RR to T2: 10.4748087431694 (n=366)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 4.4h
- Fastest resolution: 4m
- Slowest resolution: 44.9h
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 12
- Max consecutive wins: 27
- Unmapped status events (debug): 1424

## 4. Market Breakdown
- crypto: total 280 | target_hits 173 | stop_hits 67 | expired 0 | open 40
- equities: total 125 | target_hits 76 | stop_hits 23 | expired 18 | open 8

## 5. Tier Distribution
- starter: total 39 | target_hits 30 | stop_hits 5 | expired 0 | open 4
- pro: total 366 | target_hits 219 | stop_hits 85 | expired 18 | open 44

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 239 | 218 | 72.9% | 0.0% |
| Liquidity Sweep + Reclaim | 166 | 121 | 74.4% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 315 | 269 | 76.2% |
| H4 | 90 | 70 | 62.9% |

## Integrity
- ledger_slice_sha256: `71b8913d4277756b1ecaaa02f50278cde3171e300787827793ed7adaaa726b21`
- engine_version: `v2`
