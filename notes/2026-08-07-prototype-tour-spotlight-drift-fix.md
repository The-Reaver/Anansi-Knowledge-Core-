---
id: 2026-08-07-prototype-tour-spotlight-drift-fix
type: lesson
status: ratified
source: Cowork session 2026-08-07; operator tested the drivable prototype tour and the manual, pinned to fix after Phase 0 (source status: pinned); mined from candidates/2026-08-25/2026-08-07-post-phase0-fixes-prototype-tour-and-manual-toc.md
project: cippe
tags: [prototype, tour, accessibility, adhd, ui-bug]
---

# Prototype guided-tour spotlight drifts from its target on scroll — lock scroll and re-anchor on step start, it's a neurodivergent-UX must-fix, not cosmetic

## Body

Symptom: the dim/highlight spotlight box does not stay locked to the section it describes; scrolling moves the content but the spotlight stays put, so it detaches and points at the wrong place. The operator had to zoom the browser to 50% to see the whole screen — confusing, and specifically hard for an ADD/ADHD user. Fix approach: when a step starts, scroll the target to center; lock page scroll (disable body scroll) while the step is shown so nothing can drift; recompute spotlight and tip on resize; keep the tip fully in the viewport; re-anchor if layout changes. The highlight must be rock-solid stable.

## Links

- relates: 2026-08-07-docx-toc-blank-until-field-updated-ship-prerendered
- relates: 2026-08-07-cippe-cognitive-load-design-rules
