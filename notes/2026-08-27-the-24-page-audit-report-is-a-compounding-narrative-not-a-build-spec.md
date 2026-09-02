---
id: 2026-08-27-the-24-page-audit-report-is-a-compounding-narrative-not-a-build-spec
type: correction
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [geo, audit-engine, reports, knowledge-core, unblock, partner-docs]
sources:
  - ref: "Verified directly in the Core by the harvesting session on 2026-08-27: notes/2026-08-07-partner-docs-key-message-core-scales-report-depth.md states the 24 pages are explicitly 'not a literal 24 pages' in the demo, and reports/GEO_DEMO_READINESS_QUEUE_2026-08-12.md item B7 records it as 'Already answered this session... not a literal target, by design'"
    reliability: high
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [25, 25]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The '24-page audit benchmark' is not a spec document and never was: it is the partner-facing compounding argument, already answered 2026-08-07 and re-confirmed 2026-08-12

## Body
The GEO cloud session was **blocked** on building the Audit and Reports sidebar features:
the operator referenced "the 24 page audit benchmark" as the spec to build against, believing it
lived in the Knowledge Core, and that session had no `anansi_*` access to check. It correctly
reported the blocker instead of inventing a spec.

Checked directly against the Core from a session that does have access. **There is no 24-page
benchmark document, and there is no methodology spec by that name.** What exists is the opposite
of a build target -- it is a *sales and investment* argument:

- `notes/2026-08-07-partner-docs-key-message-core-scales-report-depth.md` (design-decision,
  status active) states the message the partner documents must carry: report depth is a function
  of how much validated material the Knowledge Core holds. Its own words: *"In the demo the
  sample data is small, so the generated report is real but short, not a literal 24 pages. Once
  the Core is live and full with all the rules and citations the lawyer validated, the same
  button produces the deep, 24-page-caliber document."*
- `reports/GEO_DEMO_READINESS_QUEUE_2026-08-12.md`, item B7 ("The 24-page audit report"), records
  it as already answered and carried only as a pointer: *"not a literal target, by design. Report
  depth scales with Knowledge Core richness (B1)... no new action beyond B1 actually landing."*

**So the blocker dissolves.** "24 pages" is a claim about what a rich Core will eventually
produce, not a page count to engineer toward. Building Audit/Reports does not require the missing
document, because it does not exist.

The one real, actionable spec line the 2026-08-07 note *does* contain for this feature: *"Add
real depth to the Generate report output on the Reports screen (multi-section paginated GEO
report) so the partner sees the real deliverable in the demo."* That -- a multi-section paginated
report whose length follows the available validated content -- is the build target. Related specs
worth reading before starting: `2026-08-07-knowledge-core-partner-report-spec` and
`2026-08-06-geo-suite-demo-spec`.

Meta-lesson: an agent session without Core access reported a blocker that a session *with* Core
access resolved in two lookups. When work stalls on "the operator says this document exists,"
that is a Core-retrieval task, not a dead end -- and the answer may be that the premise itself
needs correcting.

## Links
- corrects: the blocker recorded at 2026-08-27-geo-open-work-still-unstarted
- sources: notes/2026-08-07-partner-docs-key-message-core-scales-report-depth.md
- relates-to: the 2026-08-16 finding "GEO's site generator is built to clear its own audit
  engine's publish gate" (closed-loop calibration risk). Full note id deliberately not spelled
  out contiguously here: the slug contains a literal "sk-" run that trips the repo-wide
  pre-commit secret scanner as a kebab-case false positive. Retrieve via anansi_search
  "closed-loop calibration".
