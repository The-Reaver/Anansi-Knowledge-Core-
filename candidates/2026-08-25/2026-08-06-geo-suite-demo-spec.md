---
id: 2026-08-06-geo-suite-demo-spec
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; asked for a tight demo scope to show the partner a real working product within two days. (source status: active)"
project: geo
tags: [geo-suite, demo, spec, partner, prospecting, audit, report, sales, two-day]
---

# GEO Suite two-day demo spec, one real practice end to end

## Body

## Goal
Show one real medical practice go through GEO Suite from start to finish, found, audited, reported, improved, handed to sales, so it feels like a real product, not a plan. One real practice, about five minutes.

## The click-through
1. Dashboard. GEO Suite home showing three pillars: Prospecting, Compliance and Reports, Sales Pipeline.
2. Prospecting. Ranked call list of real California practices, an HBOT one highlighted, from the real lead data. Who to call and why.
3. Audit. Click the practice and run the real audit. Show the seven-category AI-Search Readiness score and the compliance findings, each with a citation. Real engine output.
4. Report. Findings grouped by risk, each with a citation and the score, the prospect-facing report.
5. The fix. Improved AI-ready site preview scoring above the 90 gate. Before and after.
6. Sales kit. Call kit for the practice: issues, citations, score, talking points.
7. Pipeline. The practice moving discovered to called to closed.

## Reuse, build, cut
- Reuse (built): site preview (geo-demo), dashboard mockup, audit engines, report builder, HBOT lead data.
- Build in two days: one clickable flow connecting these on one example with real audit numbers, polished to look like a product.
- Cut for the demo, on purpose: live feeds, atom-versioning schema, real multi-user logins, attorney correction workflow, payments, scaling. Post-demo. Tell the partner it is a guided demo on one example, not final production.

## Two-day slice plan
Day one:
- Pick the example HBOT practice, run the real audit, capture real numbers and findings.
- Dashboard landing and prospecting call list wired to the example.
- Audit and report screen with real findings and score.
Day two:
- Improved-site before and after.
- Sales kit and pipeline view.
- Stitch into one smooth clickable flow, polish, rehearse the five-minute walk-through.
Each slice: build, verify it renders and works, then next. Capture the build as notes (trains the fleet).

## Acceptance
- One smooth click-through: dashboard, prospect, audit, report, improved site, sales kit, pipeline, on one real practice, about five minutes, nothing breaks.
- Audit numbers are real, from the engine, not entered by hand.
- Looks like something a doctor would trust.

## Honesty rule
- Do not fake audit numbers; use the real, already-built engine. Label any not-ready piece as a preview, never as live production. One example done well beats five half-done.

## Links

- extends: 2026-08-06-capstone-ladder-and-build-priority-order
- relates-to: 2026-08-06-brain-trust-verdicts-and-operator-contributions
