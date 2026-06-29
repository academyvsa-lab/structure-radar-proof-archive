# Weekly System Performance Report
Week: 2026-W26
Window: 2026-06-22 00:00:00 to 2026-06-29 00:00:00 (UTC)
Generated: 2026-06-29 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 264
- Stop Hits: 140
- Expired: 19
- Open: 61
- Ambiguous: 0

Resolved (target or stop): 404
Terminal (target/stop/expired): 423

## 2. Realized Trade Performance (resolved only)
Wins: 264
Losses: 140
Win rate: 0.653 (264/404)

T1 reached: 264
T2 reached: 0

Avg RR to T1: 5.328747099767981 (n=431)
Avg RR to T2: 10.022969837587006 (n=431)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 59m
- Average time to resolution: 4.0h
- Fastest resolution: 4m
- Slowest resolution: 35.9h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 12
- Max consecutive wins: 15
- Unmapped status events (debug): 7251

## 4. Market Breakdown
- crypto: total 370 | target_hits 186 | stop_hits 122 | expired 1 | open 61
- equities: total 114 | target_hits 78 | stop_hits 18 | expired 18 | open 0

## 5. Tier Distribution
- pro: total 442 | target_hits 234 | stop_hits 130 | expired 18 | open 60
- starter: total 42 | target_hits 30 | stop_hits 10 | expired 1 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 281 | 263 | 64.3% | 0.0% |
| Liquidity Sweep + Reclaim | 203 | 141 | 67.4% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 403 | 341 | 64.5% |
| H4 | 81 | 63 | 69.8% |

## Integrity
- ledger_slice_sha256: `490cdd38bd5c0425f311843ae87e816d07014625b761b782d3814aae831d580e`
- engine_version: `v2`
