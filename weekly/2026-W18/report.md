# Weekly System Performance Report
Week: 2026-W18
Window: 2026-04-27 00:00:00 to 2026-05-04 00:00:00 (UTC)
Generated: 2026-05-04 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 324
- Stop Hits: 94
- Expired: 23
- Open: 70
- Ambiguous: 0

Resolved (target or stop): 418
Terminal (target/stop/expired): 441

## 2. Realized Trade Performance (resolved only)
Wins: 324
Losses: 94
Win rate: 0.775 (324/418)

T1 reached: 324
T2 reached: 0

Avg RR to T1: 4.811804347826087 (n=460)
Avg RR to T2: 9.193478260869565 (n=460)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 3.6h
- Fastest resolution: 4m
- Slowest resolution: 3.0d
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 15
- Max consecutive wins: 16
- Unmapped status events (debug): 3657

## 4. Market Breakdown
- crypto: total 367 | target_hits 226 | stop_hits 66 | expired 11 | open 64
- equities: total 144 | target_hits 98 | stop_hits 28 | expired 12 | open 6

## 5. Tier Distribution
- pro: total 473 | target_hits 291 | stop_hits 91 | expired 23 | open 68
- starter: total 38 | target_hits 33 | stop_hits 3 | expired 0 | open 2

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 340 | 302 | 76.2% | 0.0% |
| Liquidity Sweep + Reclaim | 171 | 116 | 81.0% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 407 | 349 | 75.9% |
| H4 | 104 | 69 | 85.5% |

## Integrity
- ledger_slice_sha256: `2840ecd1aea2a9cff51dcb7707955cad1112ef256b18932e73f75a2c024537df`
- engine_version: `v2`
