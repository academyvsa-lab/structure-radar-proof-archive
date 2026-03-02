# QueryIQ Proof Archive Pack

This pack builds a public Proof Archive:
- One premium index page (dashboard style)
- Weekly archived reports (report.md) + machine snapshots (snapshot.json)
- Automatic index table via manifest.json
- Safe weekly push to GitHub -> Cloudflare Pages auto-deploy

## Definitions
- Resolved trades: Target Hits + Stop Hits
- Terminal events: Target Hits + Stop Hits + Expired
- Open pipeline: Open only

## Files
Site:
- index.html
- manifest.json
- assets/style.css
- assets/app.js

Scripts:
- scripts/build_weekly_proof.py
- scripts/push_proof.sh
- scripts/run_weekly_proof.sh
