---
id: 2026-08-07-geo-suite-demo-build-on-lovable
type: artifact
status: ratified
source: Cowork session 2026-08-06 to 2026-08-07, operator on phone; built the GEO Suite partner demo on Lovable end to end, then produced the partner documents. (source status: active)
project: geo
tags: [geo-suite, demo, lovable, build-outcome, slice-by-slice, lessons, fleet-training]
---

# GEO Suite demo built on Lovable, slice by slice, plus lessons for the fleet

## Body

## What was built
- A working GEO Suite demo on Lovable (project id 0854feac-ea9b-422d-be1c-40b9158565fc), React + Tailwind + shadcn, dark professional theme.
- Nine screens: Home, Compliance Library, Prospecting, Audit, Reports, The Fix, Site Generator, Sales Kit, Pipeline.
- Two generators: Site Generator and Report Generator, both layered and verified slice by slice, score climbing 38 to 93 past a 90 gate.
- Compliance Library as the front door for filing legal documents that become rules.
- A built-in guided tour with three paths (Full, Legal, Sales).
- A deep multi-page generated report (cover, TOC, exec summary, methodology, seven categories, findings by risk with citations, remediation, before/after, appendix).
- One example practice, Pacific Coast Hyperbarics (HBOT, Santa Monica), runs through every screen. Sample data clearly labeled.

## How it was built (method that worked)
- Plan mode first on Lovable to lock structure cheaply (1 credit), then build one screen per message.
- Slice by slice: build, verify it renders, then next. Never overwrite a working base; layered features (for example the site generator's verified layers) added on top.
- The product embodies the method: the generators build in verified, cumulative, logged layers.

## Lessons for the fleet
- Lovable builds exceed the 60-second MCP tool window; the send times out but the build continues. Poll with get_project or list_messages instead of assuming failure.
- get_project screenshots can be stale (showed an old nav order after a reorder that had actually applied). Verify the code or hard-refresh, do not trust one screenshot.
- Plan mode before big builds saves credits by avoiding wrong-direction rework.
- Keep one shared data file as the single source so every screen stays consistent.

## Honest boundary (Mandate 7)
- Demo runs on labeled sample data. Real audit numbers, full report depth, and any-practice generation come once the Knowledge Core is live and the compliance intelligence pipeline runs.

## Links

- extends: 2026-08-06-geo-suite-demo-spec
- relates-to: 2026-08-07-site-generator-mirrors-build-methodology
- relates-to: 2026-08-07-compliance-intelligence-gathering-plan
