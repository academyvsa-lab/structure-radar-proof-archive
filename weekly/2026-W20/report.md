# Weekly System Performance Report
Week: 2026-W20
Window: 2026-05-11 00:00:00 to 2026-05-18 00:00:00 (UTC)
Generated: 2026-05-18 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 264
- Stop Hits: 108
- Expired: 13
- Open: 63
- Ambiguous: 0

Resolved (target or stop): 372
Terminal (target/stop/expired): 385

## 2. Realized Trade Performance (resolved only)
Wins: 264
Losses: 108
Win rate: 0.710 (264/372)

T1 reached: 264
T2 reached: 0

Avg RR to T1: 3.774597989949749 (n=398)
Avg RR to T2: 7.0847738693467335 (n=398)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 14m
- Average time to resolution: 4.9h
- Fastest resolution: 3m
- Slowest resolution: 3.8d
- Longest open age: 6.9d

Stability:
- Max consecutive losses: 14
- Max consecutive wins: 26
- Unmapped status events (debug): 4727

## 4. Market Breakdown
- crypto: total 315 | target_hits 181 | stop_hits 77 | expired 3 | open 54
- equities: total 133 | target_hits 83 | stop_hits 31 | expired 10 | open 9

## 5. Tier Distribution
- starter: total 41 | target_hits 30 | stop_hits 6 | expired 0 | open 5
- pro: total 407 | target_hits 234 | stop_hits 102 | expired 13 | open 58

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 297 | 278 | 70.9% | 0.0% |
| Liquidity Sweep + Reclaim | 151 | 94 | 71.3% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 338 | 284 | 73.6% |
| H4 | 110 | 88 | 62.5% |

## Integrity
- ledger_slice_sha256: `b61c3fce938bbe6d2deb5cb7ad41fb3b1442d45a7e54fbea98aa3a4001ef2704`
- engine_version: `v2`
