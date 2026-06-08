# Weekly System Performance Report
Week: 2026-W23
Window: 2026-06-01 00:00:00 to 2026-06-08 00:00:00 (UTC)
Generated: 2026-06-08 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 215
- Stop Hits: 145
- Expired: 16
- Open: 79
- Ambiguous: 0

Resolved (target or stop): 360
Terminal (target/stop/expired): 376

## 2. Realized Trade Performance (resolved only)
Wins: 215
Losses: 145
Win rate: 0.597 (215/360)

T1 reached: 215
T2 reached: 0

Avg RR to T1: 4.2038903394255875 (n=383)
Avg RR to T2: 7.9822193211488255 (n=383)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 4.7h
- Fastest resolution: 4m
- Slowest resolution: 44.6h
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 10
- Max consecutive wins: 25
- Unmapped status events (debug): 5955

## 4. Market Breakdown
- crypto: total 307 | target_hits 136 | stop_hits 90 | expired 2 | open 79
- equities: total 148 | target_hits 79 | stop_hits 55 | expired 14 | open 0

## 5. Tier Distribution
- starter: total 40 | target_hits 28 | stop_hits 11 | expired 0 | open 1
- pro: total 415 | target_hits 187 | stop_hits 134 | expired 16 | open 78

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Liquidity Sweep + Reclaim | 233 | 154 | 57.8% | 0.0% |
| Break + Retest | 222 | 206 | 61.2% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 400 | 325 | 61.2% |
| H4 | 55 | 35 | 45.7% |

## Integrity
- ledger_slice_sha256: `8f1ea0aa334ae6903e621d291f15fa756e7be77142f72d9aae6370c43dbd2463`
- engine_version: `v2`
