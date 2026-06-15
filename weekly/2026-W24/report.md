# Weekly System Performance Report
Week: 2026-W24
Window: 2026-06-08 00:00:00 to 2026-06-15 00:00:00 (UTC)
Generated: 2026-06-15 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 362
- Stop Hits: 78
- Expired: 6
- Open: 51
- Ambiguous: 0

Resolved (target or stop): 440
Terminal (target/stop/expired): 446

## 2. Realized Trade Performance (resolved only)
Wins: 362
Losses: 78
Win rate: 0.823 (362/440)

T1 reached: 362
T2 reached: 0

Avg RR to T1: 3.3479955947136566 (n=454)
Avg RR to T2: 6.290484581497798 (n=454)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 6.6h
- Fastest resolution: 4m
- Slowest resolution: 6.0d
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 12
- Max consecutive wins: 36
- Unmapped status events (debug): 6338

## 4. Market Breakdown
- crypto: total 368 | target_hits 259 | stop_hits 61 | expired 0 | open 48
- equities: total 129 | target_hits 103 | stop_hits 17 | expired 6 | open 3

## 5. Tier Distribution
- pro: total 470 | target_hits 337 | stop_hits 77 | expired 6 | open 50
- starter: total 27 | target_hits 25 | stop_hits 1 | expired 0 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 336 | 325 | 84.3% | 0.0% |
| Liquidity Sweep + Reclaim | 161 | 115 | 76.5% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 415 | 371 | 83.8% |
| H4 | 82 | 69 | 73.9% |

## Integrity
- ledger_slice_sha256: `dc964ccde2d298665b5df7b6e88a6484519be6151676c614ee5abc232c69e90a`
- engine_version: `v2`
