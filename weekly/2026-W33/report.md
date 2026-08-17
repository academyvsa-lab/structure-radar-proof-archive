# Weekly System Performance Report
Week: 2026-W33
Window: 2026-08-10 00:00:00 to 2026-08-17 00:00:00 (UTC)
Generated: 2026-08-17 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 279
- Stop Hits: 103
- Expired: 22
- Open: 63
- Ambiguous: 0

Resolved (target or stop): 382
Terminal (target/stop/expired): 404

## 2. Realized Trade Performance (resolved only)
Wins: 279
Losses: 103
Win rate: 0.730 (279/382)

T1 reached: 279
T2 reached: 0

Avg RR to T1: 4.663106796116505 (n=412)
Avg RR to T2: 8.759441747572815 (n=412)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 42m
- Average time to resolution: 3.1h
- Fastest resolution: 4m
- Slowest resolution: 2.2d
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 8
- Max consecutive wins: 18
- Unmapped status events (debug): 10820

## 4. Market Breakdown
- crypto: total 358 | target_hits 205 | stop_hits 82 | expired 8 | open 63
- equities: total 109 | target_hits 74 | stop_hits 21 | expired 14 | open 0

## 5. Tier Distribution
- pro: total 450 | target_hits 266 | stop_hits 99 | expired 22 | open 63
- starter: total 17 | target_hits 13 | stop_hits 4 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 294 | 267 | 71.9% | 0.0% |
| Liquidity Sweep + Reclaim | 173 | 115 | 75.7% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 395 | 328 | 73.5% |
| H4 | 72 | 54 | 70.4% |

## Integrity
- ledger_slice_sha256: `4e3afe8eab00aeeab83cdd366f8d684cd5a09ce6b876fb9b59330b5b4086549f`
- engine_version: `v2`
