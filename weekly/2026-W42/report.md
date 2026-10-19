# Weekly System Performance Report
Week: 2026-W42
Window: 2026-10-12 00:00:00 to 2026-10-19 00:00:00 (UTC)
Generated: 2026-10-19 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 261
- Stop Hits: 139
- Expired: 20
- Open: 61
- Ambiguous: 0

Resolved (target or stop): 400
Terminal (target/stop/expired): 420

## 2. Realized Trade Performance (resolved only)
Wins: 261
Losses: 139
Win rate: 0.652 (261/400)

T1 reached: 261
T2 reached: 0

Avg RR to T1: 3.3730281690140846 (n=426)
Avg RR to T2: 6.366150234741784 (n=426)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 3.8h
- Fastest resolution: 4m
- Slowest resolution: 2.3d
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 12
- Max consecutive wins: 29
- Unmapped status events (debug): 15505

## 4. Market Breakdown
- crypto: total 370 | target_hits 198 | stop_hits 106 | expired 7 | open 59
- equities: total 111 | target_hits 63 | stop_hits 33 | expired 13 | open 2

## 5. Tier Distribution
- pro: total 447 | target_hits 237 | stop_hits 130 | expired 20 | open 60
- starter: total 34 | target_hits 24 | stop_hits 9 | expired 0 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 250 | 232 | 59.9% | 0.0% |
| Liquidity Sweep + Reclaim | 231 | 168 | 72.6% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 418 | 347 | 66.9% |
| H4 | 63 | 53 | 54.7% |

## Integrity
- ledger_slice_sha256: `31ebf390276c3ffba0682e7cec9630edf3461e7444df3f7c2e2fc5c28568950b`
- engine_version: `v2`
