---
id: 2026-08-30-design-brief-2026-08-29-core-pointer
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "references/design/briefs/design-brief-2026-08-29.md (Oluwole, Vanguard Researcher, 2026-08-29), harvested same-day 2026-08-30 per the ratified vanguard-research-harvest-and-review-cadence rule"
project: fleet
tags: [oluwole, design, design-principles, knowledge-core, harvest-backlog, amaya, icons, settings, notifications, loading, dark-mode, REVIEW-high-impact]
sources:
  - ref: "references/design/briefs/design-brief-2026-08-29.md, 11 findings + an explicit 'Recommended next steps for Amaya' section, 11 cited URLs"
    reliability: high
    origin: "Oluwole's original web research, 2026-08-29 (this session)"
provenance:
  archive: research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl
  turns: [1, 6]
risk_class: B
evidence_state: SUPPORTED
next_review: 2026-11-30
classified: 2026-08-30
---

- class: confirmed
- confidence: high — pointer/summary of an existing, already-published, already-cited brief, not a new judgment
- verified: 2026-08-30

REVIEW: high-impact — one of the three briefs the 2026-08-30 Brain Trust ruling identified by
line-by-line check as having concrete, still-unapplied recommendations. This is the first brief to
get a same-day Core pointer note under the new rule rather than a retroactive one.

# Design brief 2026-08-29 (icon systems, settings pages, notifications, skeleton loading, dark-mode-first) — retroactive/same-day Core pointer

## Body

Sixth of six weekly briefs, the one that triggered this session's Knowledge-Core investigation.
Findings: pick one icon stroke width (1.5–2px) on a 24×24px grid; group settings by function with
progressive disclosure on desktop, full-screen drill-down rows with sticky bottom actions on
mobile; split toasts (transient) from a persistent notification center, cap stacked toasts at
three with summary consolidation, fixed corner placement; adopt Carbon's progressive skeleton
sequence (primary numbers before charts before tables/logs), skeleton dimensions must match final
content exactly; flag for Amaya, not decided here, that Linear/Vercel/Supabase-class references are
trending dark-mode-first rather than light-first, which cuts against the current `bg #FFFFFF`
default; adopt Notion's workspace-switcher pattern (full navigation reset, not a header-only
badge) if a multi-workspace surface is ever built; and standardize multi-widget dashboards on one
global filter driving all widgets plus a saved-views mechanism.

**The brief's own "Recommended next steps for Amaya" list, verbatim in source, still unapplied as
of 2026-08-30 (same day it was written):** adopt a single icon stroke width and 24×24px grid; add
the settings-page pattern; define toast-vs-notification-center split, 3-toast cap, fixed placement;
adopt Carbon's progressive-loading sequence and exact-dimension skeleton rule; decide, deliberately,
the light-first-vs-dark-first question (flagged, not resolved); adopt the workspace-switcher pattern
if/when relevant; standardize global-filter-plus-saved-views for multi-widget dashboards.

## Links
- relates-to: `2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles` — the parent finding this pointer note satisfies, and the brief whose own investigation produced this entire harvest.
- relates-to: `reports/DESIGN_BRIEF_PIPELINE_BRAIN_TRUST_RESULTS_2026-08-30.md` — independent verification that this brief's recommendations are unapplied.
- relates-to: `research/knowledge-home/structure-notes/vanguard-research-harvest-and-review-cadence.md` — the rule this note satisfies, same-day rather than retroactively, for the first time.
