#!/usr/bin/env python3
import argparse
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median

TERMINAL_TO_STATUS = {"HIT_TARGET", "HIT_STOP", "EXPIRED"}

def parse_ts(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)

def iso_week_id(dt: datetime) -> str:
    y, w, _ = dt.isocalendar()
    return f"{y}-W{w:02d}"

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def window_bounds(now_utc: datetime, days: int) -> tuple[datetime, datetime]:
    start = now_utc - timedelta(days=days)
    return start, now_utc

def safe_avg(nums):
    nums = [x for x in nums if isinstance(x, (int, float))]
    return (sum(nums) / len(nums)) if nums else None

def human_dur(seconds):
    if seconds is None:
        return "-"
    seconds = float(seconds)
    if seconds < 60:
        return f"{int(seconds)}s"
    minutes = seconds / 60
    if minutes < 60:
        return f"{int(round(minutes))}m"
    hours = seconds / 3600
    if hours < 48:
        return f"{hours:.1f}h"
    days = hours / 24
    return f"{days:.1f}d"

def build_report_md(snapshot: dict) -> str:
    w = snapshot["week"]
    win = snapshot["window"]
    totals = snapshot["totals"]
    resolved = snapshot["resolved"]
    targets = snapshot["targets"]
    rr = snapshot["rr"]
    v2 = snapshot["validation_v2"]
    by_market = snapshot["by_market"]
    by_tier = snapshot["by_tier"]
    by_setup = snapshot["by_setup_type"]
    by_tf = snapshot["by_timeframe"]

    lines = []
    lines.append("# Weekly System Performance Report")
    lines.append(f"Week: {w}")
    lines.append(f"Window: {win['start_utc']} to {win['end_utc']} (UTC)")
    lines.append(f"Generated: {snapshot['integrity']['generated_at_utc']} (UTC)")
    lines.append("")
    lines.append("## 1. Execution Status")
    lines.append(f"- Target Hits: {totals['hit_target']}")
    lines.append(f"- Stop Hits: {totals['hit_stop']}")
    lines.append(f"- Expired: {totals['expired']}")
    lines.append(f"- Open: {totals['open']}")
    lines.append(f"- Ambiguous: {totals['ambiguous']}")
    lines.append("")
    lines.append(f"Resolved (target or stop): {resolved['count']}")
    lines.append(f"Terminal (target/stop/expired): {totals['hit_target'] + totals['hit_stop'] + totals['expired']}")
    lines.append("")
    lines.append("## 2. Realized Trade Performance (resolved only)")
    lines.append(f"Wins: {resolved['wins']}")
    lines.append(f"Losses: {resolved['losses']}")
    lines.append(f"Win rate: {resolved['win_rate']:.3f} ({resolved['wins']}/{resolved['count']})" if resolved["count"] else "Win rate: -")
    lines.append("")
    lines.append(f"T1 reached: {targets['t1_reached']}")
    lines.append(f"T2 reached: {targets['t2_reached']}")
    lines.append("")
    lines.append(f"Avg RR to T1: {rr['avg_t1'] if rr['avg_t1'] is not None else '-'} (n={rr['n_t1']})")
    lines.append(f"Avg RR to T2: {rr['avg_t2'] if rr['avg_t2'] is not None else '-'} (n={rr['n_t2']})")
    lines.append("")
    lines.append("## 3. Validation Performance Block v2")
    lines.append("Resolution timing:")
    lines.append(f"- Median time to resolution: {human_dur(v2.get('median_resolution_seconds'))}")
    lines.append(f"- Average time to resolution: {human_dur(v2.get('avg_resolution_seconds'))}")
    lines.append(f"- Fastest resolution: {human_dur(v2.get('fastest_resolution_seconds'))}")
    lines.append(f"- Slowest resolution: {human_dur(v2.get('slowest_resolution_seconds'))}")
    lines.append(f"- Longest open age: {human_dur(v2.get('longest_open_seconds'))}")
    lines.append("")
    lines.append("Stability:")
    lines.append(f"- Max consecutive losses: {v2.get('max_consecutive_losses') if v2.get('max_consecutive_losses') is not None else '-'}")
    lines.append(f"- Max consecutive wins: {v2.get('max_consecutive_wins') if v2.get('max_consecutive_wins') is not None else '-'}")
    lines.append(f"- Unmapped status events (debug): {v2.get('unmapped_status_events')}")
    lines.append("")
    lines.append("## 4. Market Breakdown")
    for m, d in by_market.items():
        lines.append(f"- {m}: total {d['total']} | target_hits {d['hit_target']} | stop_hits {d['hit_stop']} | expired {d['expired']} | open {d['open']}")
    lines.append("")
    lines.append("## 5. Tier Distribution")
    for t, d in by_tier.items():
        lines.append(f"- {t}: total {d['total']} | target_hits {d['hit_target']} | stop_hits {d['hit_stop']} | expired {d['expired']} | open {d['open']}")
    lines.append("")
    lines.append("## 6. Setup-Type Performance")
    lines.append("| setup_type | total | resolved | win_rate | t2_rate |")
    lines.append("|---|---:|---:|---:|---:|")
    for st, d in sorted(by_setup.items(), key=lambda x: x[1]["total"], reverse=True):
        wr = (d["wins"] / d["resolved"]) if d["resolved"] else None
        t2r = (d["t2"] / d["resolved"]) if d["resolved"] else None
        if wr is None:
            lines.append(f"| {st} | {d['total']} | {d['resolved']} | - | - |")
        else:
            lines.append(f"| {st} | {d['total']} | {d['resolved']} | {(wr*100):.1f}% | {(t2r*100):.1f}% |")
    lines.append("")
    lines.append("## 7. Timeframe Performance")
    lines.append("| timeframe | total | resolved | win_rate |")
    lines.append("|---|---:|---:|---:|")
    for tf, d in sorted(by_tf.items(), key=lambda x: x[1]["total"], reverse=True):
        wr = (d["wins"] / d["resolved"]) if d["resolved"] else None
        if wr is None:
            lines.append(f"| {tf} | {d['total']} | {d['resolved']} | - |")
        else:
            lines.append(f"| {tf} | {d['total']} | {d['resolved']} | {(wr*100):.1f}% |")
    lines.append("")
    lines.append("## Integrity")
    lines.append(f"- ledger_slice_sha256: `{snapshot['integrity']['ledger_slice_sha256']}`")
    lines.append(f"- engine_version: `{snapshot['integrity']['engine_version']}`")
    return "\n".join(lines) + "\n"

def rebuild_manifest(out_root: Path):
    weekly_root = out_root / "weekly"
    weeks = []
    if weekly_root.exists():
        for p in weekly_root.iterdir():
            if p.is_dir():
                snap = p / "snapshot.json"
                if snap.exists():
                    obj = json.loads(snap.read_text(encoding="utf-8"))
                    weeks.append({
                        "week": obj.get("week"),
                        "totals": obj.get("totals"),
                        "resolved": obj.get("resolved"),
                        "validation_v2": obj.get("validation_v2"),
                        "targets": obj.get("targets"),
                        "rr": obj.get("rr")
                    })
    weeks.sort(key=lambda x: x["week"], reverse=True)
    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "weeks": weeks
    }
    (out_root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest

def compute_streaks(resolved_events):
    resolved_events = sorted(resolved_events, key=lambda x: x["created_at_utc"])
    max_loss = max_win = 0
    cur_loss = cur_win = 0
    for e in resolved_events:
        t = e["terminal_to"]
        if t == "HIT_STOP":
            cur_loss += 1
            cur_win = 0
        elif t == "HIT_TARGET":
            cur_win += 1
            cur_loss = 0
        else:
            cur_loss = 0
            cur_win = 0
        max_loss = max(max_loss, cur_loss)
        max_win = max(max_win, cur_win)
    return max_loss, max_win

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True, help="Path to alerts_ledger.jsonl")
    ap.add_argument("--out-dir", required=True, help="Path to proof archive repo root")
    ap.add_argument("--days", type=int, default=7, help="Rolling window size in days (default 7)")
    ap.add_argument("--engine-version", default="v1", help="Engine version string written into snapshots")
    ap.add_argument("--now-utc", default=None, help="Override now UTC (ISO, e.g. 2026-03-02T21:30:00Z)")
    ap.add_argument("--rebuild-manifest", action="store_true", help="Rebuild manifest after writing")
    args = ap.parse_args()

    ledger_path = Path(args.ledger)
    out_root = Path(args.out_dir)
    (out_root / "weekly").mkdir(parents=True, exist_ok=True)

    now = parse_ts(args.now_utc) if args.now_utc else datetime.now(timezone.utc)
    start_utc, end_utc = window_bounds(now, args.days)
    week = iso_week_id(end_utc)

    alerts = []
    statuses = []
    raw_bytes_for_hash = bytearray()

    with ledger_path.open("rb") as f:
        for line in f:
            if not line.strip():
                continue
            raw_bytes_for_hash.extend(line)
            obj = json.loads(line.decode("utf-8"))
            kind = obj.get("kind")
            if kind == "ALERT":
                alerts.append(obj)
            elif kind == "STATUS":
                statuses.append(obj)

    ledger_hash = sha256_hex(bytes(raw_bytes_for_hash))

    # Filter alerts by created_at_utc within window
    alerts_w = []
    for a in alerts:
        created = parse_ts(a["created_at_utc"])
        if start_utc <= created <= end_utc:
            a["_created_dt"] = created
            alerts_w.append(a)

    # Prep status rows (terminal only), with parsed time
    terminal_statuses = []
    for s in statuses:
        to = s.get("to")
        if to in TERMINAL_TO_STATUS:
            s["_event_dt"] = parse_ts(s["event_ts_utc"])
            terminal_statuses.append(s)

    # Build index of alert instances by alert_id (collision-safe)
    by_id = defaultdict(list)
    for a in alerts_w:
        by_id[a["alert_id"]].append(a)
    for aid in by_id:
        by_id[aid].sort(key=lambda x: x["_created_dt"])

    # Map status to best alert instance: latest created <= event_ts
    mapped = []
    unmapped = []
    for s in terminal_statuses:
        candidates = by_id.get(s["alert_id"], [])
        best = None
        for a in candidates:
            if a["_created_dt"] <= s["_event_dt"]:
                best = a
            else:
                break
        if best is None:
            unmapped.append(s)
        else:
            mapped.append((s, best))

    # Earliest terminal event per alert instance
    terminal_by_instance = {}
    for s, a in sorted(mapped, key=lambda x: x[0]["_event_dt"]):
        key = (a["alert_id"], a["_created_dt"].isoformat())
        if key not in terminal_by_instance:
            terminal_by_instance[key] = (s.get("to"), s["_event_dt"])

    totals = {"alerts": len(alerts_w), "hit_target": 0, "hit_stop": 0, "expired": 0, "open": 0, "ambiguous": 0}
    resolved_count = 0
    wins = losses = 0
    t1_reached = t2_reached = 0

    rr_t1_vals = []
    rr_t2_vals = []

    resolution_times = []
    open_ages = []
    resolved_for_streak = []

    by_market = defaultdict(lambda: {"total": 0, "hit_target": 0, "hit_stop": 0, "expired": 0, "open": 0})
    by_tier = defaultdict(lambda: {"total": 0, "hit_target": 0, "hit_stop": 0, "expired": 0, "open": 0})
    by_setup = defaultdict(lambda: {"total": 0, "resolved": 0, "wins": 0, "t2": 0})
    by_tf = defaultdict(lambda: {"total": 0, "resolved": 0, "wins": 0})

    for a in alerts_w:
        created = a["_created_dt"]
        market = a.get("market", "UNKNOWN")
        tier = a.get("tier", "UNKNOWN")
        setup_type = a.get("setup_type", "UNKNOWN")
        timeframe = a.get("timeframe", "UNKNOWN")

        by_market[market]["total"] += 1
        by_tier[tier]["total"] += 1
        by_setup[setup_type]["total"] += 1
        by_tf[timeframe]["total"] += 1

        rr1 = a.get("rr_t1")
        rr2 = a.get("rr_t2")
        if isinstance(rr1, (int, float)):
            rr_t1_vals.append(float(rr1))
        if isinstance(rr2, (int, float)):
            rr_t2_vals.append(float(rr2))

        key = (a["alert_id"], created.isoformat())
        if key in terminal_by_instance:
            terminal_to, terminal_ts = terminal_by_instance[key]
            if terminal_to == "HIT_TARGET":
                totals["hit_target"] += 1
                wins += 1
                by_market[market]["hit_target"] += 1
                by_tier[tier]["hit_target"] += 1
                by_setup[setup_type]["wins"] += 1
                by_tf[timeframe]["wins"] += 1
                t1_reached += 1
                bth = a.get("best_target_hit")
                if isinstance(bth, int) and bth >= 2:
                    t2_reached += 1
            elif terminal_to == "HIT_STOP":
                totals["hit_stop"] += 1
                losses += 1
                by_market[market]["hit_stop"] += 1
                by_tier[tier]["hit_stop"] += 1
            elif terminal_to == "EXPIRED":
                totals["expired"] += 1
                by_market[market]["expired"] += 1
                by_tier[tier]["expired"] += 1

            if terminal_to in {"HIT_TARGET", "HIT_STOP"}:
                resolved_count += 1
                by_setup[setup_type]["resolved"] += 1
                by_tf[timeframe]["resolved"] += 1
                resolution_times.append((terminal_ts - created).total_seconds())
                resolved_for_streak.append({"created_at_utc": created, "terminal_to": terminal_to})
            else:
                resolved_for_streak.append({"created_at_utc": created, "terminal_to": "EXPIRED"})
        else:
            totals["open"] += 1
            by_market[market]["open"] += 1
            by_tier[tier]["open"] += 1
            open_ages.append((end_utc - created).total_seconds())

    max_loss, max_win = compute_streaks(resolved_for_streak) if resolved_for_streak else (0, 0)

    v2 = {
        "median_resolution_seconds": median(resolution_times) if resolution_times else None,
        "avg_resolution_seconds": (sum(resolution_times) / len(resolution_times)) if resolution_times else None,
        "fastest_resolution_seconds": min(resolution_times) if resolution_times else None,
        "slowest_resolution_seconds": max(resolution_times) if resolution_times else None,
        "longest_open_seconds": max(open_ages) if open_ages else None,
        "max_consecutive_losses": max_loss,
        "max_consecutive_wins": max_win,
        "unmapped_status_events": len(unmapped)
    }

    resolved = {
        "count": resolved_count,
        "wins": wins,
        "losses": losses,
        "win_rate": (wins / resolved_count) if resolved_count else 0.0
    }

    rr = {
        "avg_t1": safe_avg(rr_t1_vals),
        "avg_t2": safe_avg(rr_t2_vals),
        "n_t1": len(rr_t1_vals),
        "n_t2": len(rr_t2_vals)
    }

    snapshot = {
        "week": week,
        "window": {
            "start_utc": start_utc.strftime("%Y-%m-%d %H:%M:%S"),
            "end_utc": end_utc.strftime("%Y-%m-%d %H:%M:%S")
        },
        "totals": totals,
        "resolved": resolved,
        "targets": {"t1_reached": t1_reached, "t2_reached": t2_reached},
        "rr": rr,
        "by_market": dict(by_market),
        "by_tier": dict(by_tier),
        "by_setup_type": dict(by_setup),
        "by_timeframe": dict(by_tf),
        "validation_v2": v2,
        "integrity": {
            "ledger_slice_sha256": ledger_hash,
            "generated_at_utc": end_utc.strftime("%Y-%m-%d %H:%M:%S"),
            "engine_version": args.engine_version
        }
    }

    week_dir = out_root / "weekly" / week
    week_dir.mkdir(parents=True, exist_ok=True)
    (week_dir / "snapshot.json").write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    (week_dir / "report.md").write_text(build_report_md(snapshot), encoding="utf-8")

    if args.rebuild_manifest:
        m = rebuild_manifest(out_root)
    else:
        m = None

    print("OK")
    print(f"week: {week}")
    print(f"window_start_utc: {start_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"window_end_utc: {end_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"alerts_in_window: {len(alerts_w)}")
    print(f"terminal_status_events_mapped: {len(mapped)}")
    print(f"terminal_status_events_unmapped: {len(unmapped)}")
    if m is not None:
        print(f"manifest_weeks: {len(m['weeks'])}")
        print(f"written: {out_root/'manifest.json'}")
    print(f"written: {week_dir/'snapshot.json'}")
    print(f"written: {week_dir/'report.md'}")

if __name__ == "__main__":
    main()
