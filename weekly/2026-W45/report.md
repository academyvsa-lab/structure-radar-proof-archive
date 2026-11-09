# Weekly System Performance Report
Week: 2026-W45
Window: 2026-11-02 00:00:00 to 2026-11-09 00:00:00 (UTC)
Generated: 2026-11-09 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 259
- Stop Hits: 108
- Expired: 16
- Open: 77
- Ambiguous: 0

Resolved (target or stop): 367
Terminal (target/stop/expired): 383

## 2. Realized Trade Performance (resolved only)
Wins: 259
Losses: 108
Win rate: 0.706 (259/367)

T1 reached: 259
T2 reached: 0

Avg RR to T1: 5.2688354430379745 (n=395)
Avg RR to T2: 9.822759493670887 (n=395)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 54m
- Average time to resolution: 4.9h
- Fastest resolution: 4m
- Slowest resolution: 2.8d
- Longest open age: 7.0d

Stability:
- Max consecutive losses: 4
- Max consecutive wins: 24
- Unmapped status events (debug): 16903

## 4. Market Breakdown
- crypto: total 352 | target_hits 192 | stop_hits 81 | expired 8 | open 71
- equities: total 108 | target_hits 67 | stop_hits 27 | expired 8 | open 6

## 5. Tier Distribution
- pro: total 406 | target_hits 222 | stop_hits 94 | expired 15 | open 75
- starter: total 54 | target_hits 37 | stop_hits 14 | expired 1 | open 2

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 254 | 241 | 71.0% | 0.0% |
| Liquidity Sweep + Reclaim | 206 | 126 | 69.8% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 349 | 275 | 73.5% |
| H4 | 111 | 92 | 62.0% |

## Integrity
- ledger_slice_sha256: `f55b03022caa21facb230bdd37201012b63901985247d17173299b4b028405ea`
- engine_version: `v2`
