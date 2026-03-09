# Weekly System Performance Report
Week: 2026-W10
Window: 2026-03-02 00:00:00 to 2026-03-09 00:00:00 (UTC)
Generated: 2026-03-09 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 232
- Stop Hits: 106
- Expired: 14
- Open: 44
- Ambiguous: 0

Resolved (target or stop): 338
Terminal (target/stop/expired): 352

## 2. Realized Trade Performance (resolved only)
Wins: 232
Losses: 106
Win rate: 0.686 (232/338)

T1 reached: 232
T2 reached: 0

Avg RR to T1: 4.6143732590529245 (n=359)
Avg RR to T2: 8.68590529247911 (n=359)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 52m
- Average time to resolution: 4.8h
- Fastest resolution: 2m
- Slowest resolution: 2.5d
- Longest open age: 5.6d

Stability:
- Max consecutive losses: 9
- Max consecutive wins: 21
- Unmapped status events (debug): 126

## 4. Market Breakdown
- crypto: total 281 | target_hits 167 | stop_hits 75 | expired 3 | open 36
- equities: total 115 | target_hits 65 | stop_hits 31 | expired 11 | open 8

## 5. Tier Distribution
- starter: total 31 | target_hits 22 | stop_hits 4 | expired 0 | open 5
- pro: total 365 | target_hits 210 | stop_hits 102 | expired 14 | open 39

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 212 | 197 | 63.5% | 0.0% |
| Liquidity Sweep + Reclaim | 184 | 141 | 75.9% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 289 | 247 | 70.0% |
| H4 | 107 | 91 | 64.8% |

## Integrity
- ledger_slice_sha256: `720287077fb6f5c8610653048d8c1d51e92734bbe42dece2afb2b7b0a721bc0b`
- engine_version: `v2`
