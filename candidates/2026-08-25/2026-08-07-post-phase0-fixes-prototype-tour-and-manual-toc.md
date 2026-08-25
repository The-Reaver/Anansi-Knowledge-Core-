---
id: 2026-08-07-post-phase0-fixes-prototype-tour-and-manual-toc
type: finding
status: candidate
source: Cowork session 2026-08-07; operator tested the drivable prototype tour and the manual; pinned these to fix after Phase 0. (source status: pinned)
project: fleet
tags: [prototype, tour, accessibility, adhd, manual, docx, toc, fix, post-phase0]
---

# Post-Phase-0 fix list, prototype tour highlight drift and manual table of contents

## Body

## 1. Prototype tour highlight drifts on scroll (priority, accessibility)
- Symptom: the dim/highlight spotlight box does not stay locked to the section it describes. Scrolling moves the content but the spotlight stays put, so it detaches and points at the wrong place. Operator had to zoom the browser to 50% to see the whole screen. Confusing, and specifically hard for an ADD/ADHD user.
- Fix approach: when a step starts, scroll the target to center; lock page scroll (disable body scroll) while the step is shown so nothing can drift; recompute spotlight and tip on resize; keep the tip fully in the viewport; re-anchor if layout changes. The highlight must be rock-solid stable. This is a neurodivergent-UX must-fix, not cosmetic.

## 2. Manual table of contents appears missing
- Cause: the docx TableOfContents is a Word field that only populates when the document is opened and the field is updated (right-click -> Update Field, or F9). It can look blank until then.
- Fix: ship the manual with the contents pre-populated, or deliver a PDF with the TOC rendered, so it is never blank on open.

## Timing
- Address both after the Phase 0 implementation, per operator.

## Links

- relates-to: the drivable prototype (privacy_copilot_prototype.html) and STAG_Operating_Manual.docx delivered 2026-08-07.
