---
id: 2026-08-22-ci-q2-emergency-security-fix-shipped-auth-signoff-authority-tier-history
type: decision
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [compliance-intelligence, brain-trust, security-fix, decision, authority-tier]
sources:
  - ref: "Archive lines 373-398: assistant reports all four Q2 fixes built and tested (19/19 including 9 new tests: X-API-Key auth on the KB endpoints, the atoms sign-off gate, authority_tier plus the report.py render gate, and kb/history.py real git-log history), then confirms commit 77b647e landed cleanly."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [373, 398]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# CI's Q2 emergency security fix (unauthenticated KB endpoints, atoms active-by-default) shipped, 13 days after being ruled "not blocked, proceed immediately"

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — code changes directly made and tested in-session (19/19 test battery green, including 9 new tests), commit 77b647e confirmed landed
- verified: 2026-08-22

REVIEW: high-impact

## Body
A 2026-08-08 Brain Trust ruling (Q2, CARRIED 4-0-2, "not blocked, proceed immediately") found a live security exposure in Compliance Intelligence: three KB endpoints (`/api/kb/search`, `/api/kb/atoms`, `/api/kb/atoms/{id}`) had no authentication, and atoms defaulted to `active` status with no sign-off gate before affecting output. A separate re-verification earlier this same session confirmed the fix was still unfixed 13 days later — zero commits to the project since 2026-08-04. Two operator-uploaded AI-generated architecture documents ("Architecting for Accountability" and a "Verifiable Legal Ingestion Pipeline" draft) were evaluated against the real codebase per explicit instruction (does each proposed piece solve a confirmed real gap, is it appropriately scoped, is it buildable now) rather than trusted at face value — most of both documents' proposals (blockchain/DID provenance, multi-jurisdiction ingestion, workflow orchestration engines) were discarded as solving problems the system doesn't actually have, but two ideas were adopted in radically descoped form.

Four concrete fixes were built and shipped in `projects/compliance_intelligence` (a separate nested git repo) at commit `77b647e`: (1) `X-API-Key` header auth on the three KB endpoints, fail-closed with no hardcoded fallback key; (2) a sign-off gate in `kb/atoms.py` — atoms with no explicit `status` are now excluded instead of defaulting to `active` (verified beforehand that all 11 existing atoms already had explicit `status: active`, so no regression); (3) an `authority_tier` field (statutory/regulatory/judicial/municipal/advisory) per atom plus a `report.py` render gate visually separating binding citations from advisory ones — the real, descoped version of the documents' "Verifiable Citation Engine"/"5-Tier Classification" ideas; (4) a real atom version-history viewer (`kb/history.py`, reading actual `git log` per atom file) that honestly flags atoms whose history is a single squashed commit as a commit-discipline gap rather than a complete record — the descoped version of the documents' "Temporal Diffing Engine." All four were tested (19/19 including 9 new tests) before shipping.

`CI_API_KEY` was generated and verified working end-to-end locally (403/403/200 for no-key/wrong-key/correct-key). Deploying the fix live was explicitly left open: no hosting exists anywhere for this project (checked Railway directly — no matching project), and deploying the current codebase would put CI's legal-retrieval mechanism into production while its Q1 ship/hold question sits on HOLD — a tension flagged to the operator rather than resolved unilaterally.

## Links
- resolves, 2026-08-21-ci-brain-trust-emergency-security-fix-still-unfixed-13-days-later.md — the note this fix directly closes out (that note was separately flagged as stale by a later review pass in this same session, since it was overtaken by this work).
- relates, 2026-08-22-ci-q1-tie-break-ruled-hold-pending-operator-redesign-input.md — the separate, still-open Q1 ruling this Q2 fix is explicitly independent of.
- relates, 2026-08-22-evaluate-ai-generated-architecture-docs-against-confirmed-gaps-not-own-claims.md — the evaluation method used to scope these four fixes down from the two uploaded documents' much larger proposals.
