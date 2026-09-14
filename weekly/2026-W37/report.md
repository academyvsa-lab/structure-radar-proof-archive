# Weekly System Performance Report
Week: 2026-W37
Window: 2026-09-07 00:00:00 to 2026-09-14 00:00:00 (UTC)
Generated: 2026-09-14 00:00:00 (UTC)

## 1. Execution Status
- Target Hits: 257
- Stop Hits: 111
- Expired: 22
- Open: 69
- Ambiguous: 0

Resolved (target or stop): 368
Terminal (target/stop/expired): 390

## 2. Realized Trade Performance (resolved only)
Wins: 257
Losses: 111
Win rate: 0.698 (257/368)

T1 reached: 257
T2 reached: 0

Avg RR to T1: 3.502741116751269 (n=394)
Avg RR to T2: 6.582766497461929 (n=394)

## 3. Validation Performance Block v2
Resolution timing:
- Median time to resolution: 59m
- Average time to resolution: 4.3h
- Fastest resolution: 4m
- Slowest resolution: 2.5d
- Longest open age: 6.8d

Stability:
- Max consecutive losses: 8
- Max consecutive wins: 19
- Unmapped status events (debug): 12927

## 4. Market Breakdown
- crypto: total 402 | target_hits 224 | stop_hits 97 | expired 13 | open 68
- equities: total 57 | target_hits 33 | stop_hits 14 | expired 9 | open 1

## 5. Tier Distribution
- pro: total 424 | target_hits 230 | stop_hits 103 | expired 22 | open 69
- starter: total 35 | target_hits 27 | stop_hits 8 | expired 0 | open 0

## 6. Setup-Type Performance
| setup_type | total | resolved | win_rate | t2_rate |
|---|---:|---:|---:|---:|
| Break + Retest | 238 | 218 | 67.4% | 0.0% |
| Liquidity Sweep + Reclaim | 221 | 150 | 73.3% | 0.0% |

## 7. Timeframe Performance
| timeframe | total | resolved | win_rate |
|---|---:|---:|---:|
| H1 | 384 | 304 | 70.7% |
| H4 | 75 | 64 | 65.6% |

## Integrity
- ledger_slice_sha256: `0498f201ab86aca0ceb76a0ced3dfe0721635a17f9126a9b01008d27252c95d1`
- engine_version: `v2`
