---
id: 2026-08-07-note-quality-rubric-and-dedup-threshold
type: spec
status: ratified
source: Google Drive inbox capture, source chat not recorded in original note (source status: pinned Anansi note, answering whether proven formulas exist beyond Wilson); mined from candidates/2026-08-25/2026-08-07-quality-and-performance-formulas.md
project: fleet
tags: [formulas, note-quality, dedup, provenance, rubric]
---

# Note-quality rubric: atomicity, 100% provenance, dedup at cosine similarity < 0.92, self-containedness, calibrated confidence — a note enters the Core only above threshold with full provenance

## Body

Atomicity: exactly one claim per note. Provenance completeness (must be 100%): source, capture date, confidence, at least one typed link. Non-duplication: max cosine similarity to any existing note < 0.92 — at or above, merge instead of adding. Self-containedness: understandable alone, no dangling pronouns. Calibrated confidence (see the calibration bar). Composite note score is a weighted sum of these. BAR: a note enters the Core only above the composite threshold and with provenance at 100%.

## Links

- relates: 2026-08-07-harvest-completeness-bar-capture-recapture-chao1
- relates: 2026-08-07-weighted-consensus-auto-approve-rule
