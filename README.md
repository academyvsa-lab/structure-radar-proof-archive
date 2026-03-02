# QueryIQ Proof Archive Pack (Cloudflare Pages, premium index)

This pack builds a public Proof Archive:
- One premium index page (dashboard style)
- Weekly archived reports (report.md) + machine snapshots (snapshot.json)
- Automatic index table via manifest.json
- Safe weekly push to GitHub -> Cloudflare Pages auto-deploy

## Your definitions (locked)
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

## Expected output rule
Whenever you run a terminal command from this guide, you will see an "Expected output" block.


## Branding (Proof Archive optimized)
- assets/q-proof.svg is a subtle monochrome Q mark designed for audit pages.
