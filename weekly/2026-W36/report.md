# Weekly System Performance Report
Week: 2026-W36
Window: 2026-08-31 00:00:00 to 2026-09-07 00:00:00 (UTC)
Generated: 2026-09-07 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 425
- Stop Hits: 123
- Expired: 20
- Open: 54
- Ambiguous: 0

Resolved (target or stop): 548
Terminal (target/stop/expired): 568

## 2. Realized Trade Performance (resolved only)
Wins: 425
Losses: 123
Win rate: 0.776 (425/548)

T1 reached: 425
T2 reached: 0

Avg RR to T1: 3.427247386759582 (n=574)
Avg RR to T2: 6.443449477351916 (n=574)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 3.2h
- Fastest resolution: 4m
- Slowest resolution: 2.5d
- Longest open age: 6.6d

Stability:
- Max consecutive losses: 10
- Max consecutive wins: 37
- Unmapped status events (debug): 12355

## 4. Market Breakdown
- crypto: total 526 | target_hits 368 | stop_hits 101 | expired 3 | open 54
- equities: total 96 | target_hits 57 | stop_hits 22 | expired 17 | open 0

## 5. Tier Distribution
- pro: total 583 | target_hits 389 | stop_hits 120 | expired 20 | open 54
- starter: total 39 | target_hits 36 | stop_hits 3 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 429 | 411 | 80.8% | 0.0% |
| Liquidity Sweep + Reclaim | 193 | 137 | 67.9% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 516 | 451 | 77.4% |
| H4 | 106 | 97 | 78.4% |

## Integrity
- ledger_slice_sha256: `13d4192d1e64e3fd7b0f9a0c8bb0a243112576de834bc2e5b84b26768ab55e75`
- engine_version: `v2`
