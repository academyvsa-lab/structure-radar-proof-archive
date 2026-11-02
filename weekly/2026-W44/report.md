# Weekly System Performance Report
Week: 2026-W44
Window: 2026-10-26 00:00:00 to 2026-11-02 00:00:00 (UTC)
Generated: 2026-11-02 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 358
- Stop Hits: 115
- Expired: 18
- Open: 79
- Ambiguous: 0

Resolved (target or stop): 473
Terminal (target/stop/expired): 491

## 2. Realized Trade Performance (resolved only)
Wins: 358
Losses: 115
Win rate: 0.757 (358/473)

T1 reached: 358
T2 reached: 0

Avg RR to T1: 3.3426892430278885 (n=502)
Avg RR to T2: 6.289641434262949 (n=502)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 3.4h
- Fastest resolution: 4m
- Slowest resolution: 32.0h
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 9
- Max consecutive wins: 27
- Unmapped status events (debug): 16405

## 4. Market Breakdown
- crypto: total 442 | target_hits 268 | stop_hits 89 | expired 9 | open 76
- equities: total 128 | target_hits 90 | stop_hits 26 | expired 9 | open 3

## 5. Tier Distribution
- pro: total 538 | target_hits 333 | stop_hits 109 | expired 18 | open 78
- starter: total 32 | target_hits 25 | stop_hits 6 | expired 0 | open 1

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 352 | 328 | 77.4% | 0.0% |
| Liquidity Sweep + Reclaim | 218 | 145 | 71.7% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 512 | 433 | 75.1% |
| H4 | 58 | 40 | 82.5% |

## Integrity
- ledger_slice_sha256: `ba13faa6df1b4855dfff1a65f4ea0710ebc162bc47657f2f9a84b6885909e4d0`
- engine_version: `v2`
