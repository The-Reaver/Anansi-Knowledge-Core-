---
id: 2026-08-27-automated-lead-engine-declined-in-full-two-refinements-banked
type: decision
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [brain-trust, lead-scoring, architecture, decision-record, geo]
sources:
  - ref: "GEO Suite commit 9c0d318, 2026-08-27: backend/app/services/sales/prospect_source.py's module docstring extended with the declining verdict plus two salvaged refinements; the proposal was reviewed against the real lead_scorer.py / prospect_source.py rather than its own description of them"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [7, 8]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The Automated Lead Engine proposal was declined in full, with two refinements salvaged and written into the docstring of the module they govern

## Body
The "Automated Lead Engine Plan" -- an enterprise-stack architecture (the same pattern as
the rejected Federal Litigation Tracking documents) applied to lead scoring -- was **declined in
full** after Brain Trust review. A fifth document, a praise-piece reinforcing the same rejected
architecture, was reviewed too; its review is what surfaced the material worth keeping.

**Two refinements survived and were banked:**
1. Name `SELECT ... FOR UPDATE SKIP LOCKED`, `claimed_by` and `claimed_at` explicitly in the
   claim path, rather than leaving the concurrency mechanism implicit.
2. Bank an outbox-lite pattern for a future outreach-approval feature.

Two things about *how* this was decided are the durable part:

**The review was run against the real code.** The proposal was evaluated by reading the actual
`lead_scorer.py` and `prospect_source.py`, not the proposal's own account of what they do. A
document arguing for a rewrite is not a reliable narrator of the thing it wants rewritten.

**The verdict was written into the code it governs**, as an extended module docstring on
`prospect_source.py`, not into a separate decision document. That puts the reasoning in front of
the next person who opens the file to change it -- which is precisely when "should we replace
this with an enterprise pipeline?" gets asked again. A rejection recorded somewhere else gets
re-litigated; a rejection in the docstring gets read.

**Evidence is second-hand, twice over.** This is drawn from Part 1 of the source development
log, which is itself a platform-compaction summary of the earlier part of that session rather
than first-hand record. The commit hash (`9c0d318`) and the docstring it points at are
checkable; the reasoning attributed to the review is not, from here. Verify against the repo
before treating the detail as settled.

## Links
- relates-to: 2026-08-27-source-verifies-on-terminology-and-fails-on-numeric-hero-claims
