---
id: 2026-08-30-design-brief-2026-08-22-core-pointer
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "references/design/briefs/design-brief-2026-08-22.md (Oluwole, Vanguard Researcher, 2026-08-22), harvested retroactively 2026-08-30 per the ratified vanguard-research-harvest-and-review-cadence rule"
project: fleet
tags: [oluwole, design, design-principles, knowledge-core, harvest-backlog, amaya, typography, grid, spacing, REVIEW-high-impact]
sources:
  - ref: "references/design/briefs/design-brief-2026-08-22.md, 9 findings + an explicit 'Recommended next steps for Amaya' section, 8 cited URLs"
    reliability: high
    origin: "Oluwole's original web research, 2026-08-22"
provenance:
  archive: research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl
  turns: [28, 29]
risk_class: B
evidence_state: SUPPORTED
next_review: 2026-11-30
classified: 2026-08-30
---

- class: confirmed
- confidence: high — pointer/summary of an existing, already-published, already-cited brief, not a new judgment
- verified: 2026-08-30

REVIEW: high-impact — one of the three briefs the 2026-08-30 Brain Trust ruling identified by
line-by-line check as having concrete, still-unapplied recommendations.

# Design brief 2026-08-22 (type weight discipline, layout grid math, section rhythm) — retroactive Core pointer

## Body

Fifth of six weekly briefs. Findings: turn on Inter's `cv01`/`ss03` OpenType features globally;
shift UI weight from the current 400/600 toward Linear's actual 300/510/590 band; add a dedicated
`section-gap` token (proposed ~96px) distinct from card-level spacing, since the current 4–64px
scale has no answer for "how far apart do major sections sit"; adopt exactly three radii by role
(6px controls, 12px containers, 9999px pills) rather than one-off values; standardize the
dashboard shell at a 240–280px sidebar, 12-column grid, 16–24px gutters; size KPI cards by role
(hero 4–6 columns, secondary 2–3 columns); split card padding (~24px) from card-to-card gap
(16–24px) into separate tokens instead of reusing one spacing value for both; restrict the
`surface` token to elevated cards only, never whole-section backgrounds; and flagged, not
recommended, a possible exception to the one-accent rule for workflow-scoped accents (Vercel's
deploy/preview/develop color pattern) — explicitly left for Amaya's call, not auto-adopted.

**The brief's own "Recommended next steps for Amaya" list, verbatim in source, still unapplied as
of 2026-08-30:** add the `cv01`/`ss03` font-feature-settings; evaluate the 510/590 weight shift;
introduce the `section-gap` token; add pill radius and formalize the three-radius rule; standardize
the dashboard shell numbers; split card-padding and card-gap tokens; restrict `surface` to cards
only; decide the workflow-accent exception question. None of these appear in the current
`DESIGN_PRINCIPLES.md` as of 2026-08-30. Full findings, each independently cited:
`references/design/briefs/design-brief-2026-08-22.md`.

## Links
- relates-to: `2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles` — the parent finding this pointer note satisfies.
- relates-to: `reports/DESIGN_BRIEF_PIPELINE_BRAIN_TRUST_RESULTS_2026-08-30.md` — independent verification that this brief's recommendations are unapplied.
- relates-to: `research/knowledge-home/structure-notes/vanguard-research-harvest-and-review-cadence.md` — the rule this note is retroactively harvested under.
