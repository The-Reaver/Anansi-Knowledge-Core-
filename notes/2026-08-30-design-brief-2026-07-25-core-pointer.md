---
id: 2026-08-30-design-brief-2026-07-25-core-pointer
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "references/design/briefs/design-brief-2026-07-25.md (Oluwole, Vanguard Researcher, 2026-07-25), harvested retroactively 2026-08-30 per the ratified vanguard-research-harvest-and-review-cadence rule"
project: fleet
tags: [oluwole, design, design-principles, knowledge-core, harvest-backlog, amaya, oklch, motion, accessibility]
sources:
  - ref: "references/design/briefs/design-brief-2026-07-25.md, 11 findings, 12 cited URLs (66colorful, Builderius, letdataspeak, IBM Carbon/Medium, chartgen, Carbon Design System x4, techinterview, Mobbin, Pope Tech, MDN, Orbix, SaaSFrame)"
    reliability: high
    origin: "Oluwole's original web research, 2026-07-25"
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

# Design brief 2026-07-25 (Motion, Color Systems, Interaction Patterns) — retroactive Core pointer

## Body

Second of six weekly briefs; predates the "Recommended next steps for Amaya" convention. Core
proposal, echoed again in the later 08-08 brief and still unapplied as of 2026-08-30: author
color in OKLCH instead of hex for predictable neutral/dark-mode ramps. Other findings: in dark
mode use surface elevation instead of shadow; avoid pure black for dark data backgrounds (use a
near-black grey); cap chart palettes near eight colors and grayscale-test them; tokenize motion
durations roughly 70–700ms (IBM Carbon's six-step scale cited as a model); keep micro-interactions
under ~120ms with ease-out on input; adopt a small named set of easing curves, no bounce/stretch;
always honor `prefers-reduced-motion`; ship a Cmd+K command palette (repeated again in 08-08);
design keyboard-only focus rings at 3:1 contrast, 2px minimum, via `:focus-visible`; and consider
bento-style modular grids for data-dense screens, with hierarchy decided before layout. None
applied to `DESIGN_PRINCIPLES.md` as of 2026-08-30. Full findings, each independently cited:
`references/design/briefs/design-brief-2026-07-25.md`.

## Links
- relates-to: `2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles` — the parent finding this pointer note satisfies.
- relates-to: `2026-08-30-design-brief-2026-08-08-core-pointer` — the OKLCH and command-palette recommendations recur there with a fuller "Recommended next steps" treatment.
- relates-to: `research/knowledge-home/structure-notes/vanguard-research-harvest-and-review-cadence.md` — the rule this note is retroactively harvested under.
