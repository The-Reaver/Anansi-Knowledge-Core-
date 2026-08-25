---
id: knowledge-core-confidence-tier-gap-2026-08-25
type: finding
status: candidate
source: Architecture, Redlined — Rev. 3, Part V; captured via GeoSuite session handoff, 2026-08-25
project: fleet
tags: [knowledge-core, zettelkasten, deepening]
---

# Ratified and unverified notes collapse into one undifferentiated truth tier

## Body

GeoSuite's own audit rubric already tags claims `documented` vs. `hypothesis` rather than
asserting everything with equal confidence. The Knowledge Core doesn't appear to have the
same tier: a `ratified` note (human sign-off) and a `finding` note (one agent's unverified
read) can currently collapse into one undifferentiated "truth" tier at retrieval time.

Leaving this open in the system that governs the product is the same bug the rubric was
built to close in the product itself, one level up.

This is a finding, not yet ratified — whether and how to build this is a decision for the
operator, not something to silently treat as decided.

## Links

- Architecture, Redlined Rev. 3, Part V
- GeoSuite rubric.py's documented/hypothesis tagging (backend/app/core/rubric.py, The-Reaver/The-Geo-Suite-)
