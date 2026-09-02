---
id: 2026-08-30-design-brief-2026-08-01-core-pointer
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "references/design/briefs/design-brief-2026-08-01.md (Oluwole, Vanguard Researcher, 2026-08-01), harvested retroactively 2026-08-30 per the ratified vanguard-research-harvest-and-review-cadence rule"
project: fleet
tags: [oluwole, design, design-principles, knowledge-core, harvest-backlog, amaya, tables, navigation, responsive, ai-surfaces]
sources:
  - ref: "references/design/briefs/design-brief-2026-08-01.md, 12 findings, 11 cited URLs (theosoti, Pencil & Paper x2, Datafloq x2, Molly Hellmuth/Medium, Vercel changelog x2, artofstyleframe, Setproduct, UXPin, Framer, BrowserStack, groovyweb x3)"
    reliability: high
    origin: "Oluwole's original web research, 2026-08-01"
provenance:
  archive: research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl
  turns: [28, 29]
risk_class: C
evidence_state: SUPPORTED
next_review: 2026-11-30
classified: 2026-08-30
---

- class: confirmed
- confidence: high — pointer/summary of an existing, already-published, already-cited brief, not a new judgment
- verified: 2026-08-30

# Design brief 2026-08-01 (data tables, navigation shell, responsive priority, AI-native surfaces) — retroactive Core pointer

## Body

Third of six weekly briefs; predates the "Recommended next steps for Amaya" convention. Findings:
turn on `tabular-nums` for aligned numeric columns, proportional digits for body copy; right-align
numbers and left-align text with consistent US formatting; default the navigation shell to a
resizable, hideable left sidebar over horizontal tabs (citing Vercel's Feb 2026 dashboard
redesign); ship a row-density toggle plus virtual scrolling for long tables; sticky headers always,
inline editing for single-field changes vs. modal for multi-field/high-weight changes; on mobile,
make HTML source order equal priority order (inverted pyramid, critical info in the first ~100px);
set breakpoints where content actually breaks, not at fixed device pixels; add a floating
bottom bar for primary mobile actions; stream AI output token-by-token, never a blocking
all-at-once reply; pair AI output with source chips, a reasoning toggle, and honest status cues
("searching", "generating"); seed AI input fields with suggested prompts rather than leaving them
blank; and run data tables at 13–14px with attention to numeral legibility. None applied to
`DESIGN_PRINCIPLES.md` as of 2026-08-30. Full findings, each independently cited:
`references/design/briefs/design-brief-2026-08-01.md`.

## Links
- relates-to: `2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles` — the parent finding this pointer note satisfies.
- relates-to: `research/knowledge-home/structure-notes/vanguard-research-harvest-and-review-cadence.md` — the rule this note is retroactively harvested under.
