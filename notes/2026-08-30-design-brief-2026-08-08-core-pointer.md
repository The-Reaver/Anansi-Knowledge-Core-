---
id: 2026-08-30-design-brief-2026-08-08-core-pointer
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "references/design/briefs/design-brief-2026-08-08.md (Oluwole, Vanguard Researcher, 2026-08-08), harvested retroactively 2026-08-30 per the ratified vanguard-research-harvest-and-review-cadence rule"
project: fleet
tags: [oluwole, design, design-principles, knowledge-core, harvest-backlog, amaya, oklch, dark-mode, forms, charts, wcag, REVIEW-high-impact]
sources:
  - ref: "references/design/briefs/design-brief-2026-08-08.md, 14 findings + an explicit 'Recommended next steps for Amaya' section, 22 cited URLs"
    reliability: high
    origin: "Oluwole's original web research, 2026-08-08"
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

REVIEW: high-impact — this is one of the three briefs the 2026-08-30 Brain Trust ruling identified
by line-by-line check as having concrete, still-unapplied recommendations.

# Design brief 2026-08-08 (color authoring, dark mode, interaction feedback, forms, chart restraint) — retroactive Core pointer

## Body

Fourth of six weekly briefs; the first to carry an explicit "Recommended next steps for Amaya"
section. Findings: author color in OKLCH, export hex for compatibility (Tailwind v4 already ships
OKLCH tokens); dark theme base should sit near-black (`#0E`–`#1A` range), never pure `#000`;
express dark-mode elevation via surface lightness, not shadow; prefer an undo toast over a
confirmation dialog for single reversible actions, but keep explicit confirmation (with the count
in the copy) for bulk destructive actions; use skeletons for content-shaped 1–10s waits, spinners
only for atomic 300ms–1s waits; forms go single-column with visible above-field labels; validate
inline on blur, debounced ~500ms, never keystroke-by-keystroke; strip charts to the data-ink
(faint/absent gridlines, no 3D, no redundant axis labels); treat the empty state as the real
onboarding surface, with distinct copy for first-use vs. user-cleared; ship a Cmd+K command
palette built correctly (input keeps DOM focus, listbox shows a virtual highlight, trap focus,
close on Escape); and gave concrete numbers for "Linear's look" (near-black `#08090a`, `-0.022em`
tracking, 400–510 weight band, 0.5px hairline borders, 6px/12px radii) plus four specific WCAG 2.2
AA gaps (24×24px target size, focus-not-obscured, 3:1 focus contrast, `prefers-reduced-motion`).

**The brief's own "Recommended next steps for Amaya" list, verbatim in source, still unapplied as
of 2026-08-30:** reauthor tokens in OKLCH with hex fallback; add a dark token set with near-black
base and surface-lightness elevation ramp; define the undo-toast/bulk-confirm/skeleton feedback
trio as components; add form and chart defaults to the rules section; extend the conformance gate
with target-size, focus-not-obscured, focus-contrast, and reduced-motion checks. None of these
five items appear in the current `DESIGN_PRINCIPLES.md` as of 2026-08-30 — independently verified
by both the original candidate note and a 4-seat Brain Trust panel, not just this brief's own
claim. Full findings, each independently cited: `references/design/briefs/design-brief-2026-08-08.md`.

## Links
- relates-to: `2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles` — the parent finding this pointer note satisfies.
- relates-to: `reports/DESIGN_BRIEF_PIPELINE_BRAIN_TRUST_RESULTS_2026-08-30.md` — independent verification that this brief's recommendations are unapplied.
- relates-to: `research/knowledge-home/structure-notes/vanguard-research-harvest-and-review-cadence.md` — the rule this note is retroactively harvested under.
