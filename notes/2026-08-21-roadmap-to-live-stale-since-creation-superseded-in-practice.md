---
id: 2026-08-21-roadmap-to-live-stale-since-creation-superseded-in-practice
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [geo-suite, geo-platform, roadmap, documentation-drift]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn establishing ROADMAP_TO_LIVE.md's single-commit history against GEO_STATUS_AND_ROADMAP_2026-08-17.md as the roadmap actually being worked from."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"GEO Suite\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: medium — file contents and git log read directly; "superseded in practice" is an inference from content overlap, not a stated supersession in ROADMAP_TO_LIVE.md itself
- verified: 2026-08-21

# ROADMAP_TO_LIVE.md, the doc the 2026-08-03 checklist points to for GEO go-live tracking, has had exactly one commit since it was written and is superseded in practice (not formally) by GEO_STATUS_AND_ROADMAP_2026-08-17.md

## Body
The 2026-08-03 checklist said go-live tracking lives in `ROADMAP_TO_LIVE.md`. That file still exists at the
stag repo root, but `git log` shows it has had exactly one commit (its creation, "v1 2026-07-24") — no
updates since. Its content is a Phase A-E structure (Verify what exists → owner product → billing plumbing →
first paying client → standing) with generic, dateless exit gates.

Inside `projects/geo_platform/`, a materially different and far more current roadmap now exists:
`GEO_STATUS_AND_ROADMAP_2026-08-17.md`, which opens by stating it "Supersedes
`GEO_STATUS_AND_ROADMAP_2026-08-16.md`" (a same-project predecessor, not `ROADMAP_TO_LIVE.md`) and contains
a concrete, dated §5 "Full remaining roadmap" and §6 "Queue" with specific numbered items (get an API key
into Railway, build the bulk-upload pipeline, fix a site-generator auth-header bug, etc.), each tagged with
who owns it. This doc's content and `ROADMAP_TO_LIVE.md`'s Phase A-E structure do not cross-reference each
other, and `ROADMAP_TO_LIVE.md` is not marked superseded, deprecated, or archived anywhere found in this
sweep.

This is a documentation-drift finding, not a claim that either roadmap is wrong: the *operational* roadmap
that's actually being worked from (per the 2026-08-17 doc's own "Queue" section and the real commit history
showing frontend/auth/deploy fixes through 2026-08-19) is the one inside `projects/geo_platform/`, not the
one the checklist named. Anyone following the checklist's pointer to `ROADMAP_TO_LIVE.md` for current
go-live status would land on an 18-day-untouched, generically-worded doc instead of the one that reflects
what's actually happened.

## Links
- related-to, research/knowledge-home/candidates/2026-08-21/2026-08-21-geo-platform-now-has-own-github-repo-and-ci-but-local-checkout-26-commits-behind.md, the same GEO Suite go-live tracking claim from the 2026-08-03 checklist.
