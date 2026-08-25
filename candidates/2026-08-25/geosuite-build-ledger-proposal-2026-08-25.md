---
id: geosuite-build-ledger-proposal-2026-08-25
type: finding
status: candidate
source: Architecture, Redlined — Rev. 3, Part V; this session's own GeoSuite roadmap-gaps slices; captured via GeoSuite session handoff, 2026-08-25
project: geo
tags: [geosuite, build-ledger, site-generator]
---

# One atomic note per non-obvious build decision, not a commentary on every line

## Body

Proposal: one atomic note per real, non-obvious decision a GeoSuite build surfaces — not a
running commentary on every line changed (git history already is that). Two real entries
already exist from the session that drafted this proposal, proving the format before
scaling it:

1. `site_pipeline.py`'s `_persist()` globs every `*.html` file unconditionally, so a new
   page type can't ship its rendering half without its persistence half in the same commit
   (discovered landing the Terms of Service page — see The-Geo-Suite- commit 01340f5).
2. A 10th hero-bearing theme file, `trust_panel.py`, hardcoded the same
   `background-image:url('assets/hero-bg.svg')` reference the first theme-sweep pass
   missed — only 9 of 10 were caught initially (see commit d575ff1 / d7ff8da).

Purpose: not making any single generated site more creative — GeoSuite's own
`compute_seed()`/`select_theme()` mechanism already owns that job (proven by a passing
test, `test_hero_bg_actually_differs_between_two_real_generated_businesses`). This is
about not making the next agent re-derive a decision that's already been paid for once.

This is a finding, not yet ratified — whether and how to build this is a decision for the
operator, not something to silently treat as decided.

## Links

- Architecture, Redlined Rev. 3, Part V
- The-Reaver/The-Geo-Suite- commits 01340f5, d575ff1, d7ff8da
