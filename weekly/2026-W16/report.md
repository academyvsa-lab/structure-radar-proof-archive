# Weekly System Performance Report
Week: 2026-W16
Window: 2026-04-13 00:00:00 to 2026-04-20 00:00:00 (UTC)
Generated: 2026-04-20 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 380
- Stop Hits: 65
- Expired: 16
- Open: 42
- Ambiguous: 0

Resolved (target or stop): 445
Terminal (target/stop/expired): 461

## 2. Realized Trade Performance (resolved only)
Wins: 380
Losses: 65
Win rate: 0.854 (380/445)

T1 reached: 380
T2 reached: 0

Avg RR to T1: 3.099123931623932 (n=468)
Avg RR to T2: 5.839145299145299 (n=468)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 3.3h
- Fastest resolution: 4m
- Slowest resolution: 3.0d
- Longest open age: 6.2d

Stability:
- Max consecutive losses: 9
- Max consecutive wins: 39
- Unmapped status events (debug): 2700

## 4. Market Breakdown
- crypto: total 368 | target_hits 274 | stop_hits 52 | expired 5 | open 37
- equities: total 135 | target_hits 106 | stop_hits 13 | expired 11 | open 5

## 5. Tier Distribution
- pro: total 454 | target_hits 340 | stop_hits 58 | expired 16 | open 40
- starter: total 49 | target_hits 40 | stop_hits 7 | expired 0 | open 2

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 391 | 367 | 87.2% | 0.0% |
| Liquidity Sweep + Reclaim | 112 | 78 | 76.9% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 365 | 321 | 86.0% |
| H4 | 138 | 124 | 83.9% |

## Integrity
- ledger_slice_sha256: `a1173b5b496f57f311325d1971967f300f443f9ce78bd59375f8d5219538fb2c`
- engine_version: `v2`
