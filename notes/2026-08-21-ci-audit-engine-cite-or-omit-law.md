---
id: 2026-08-21-ci-cite-or-omit-law
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [compliance-intelligence, crawler, citations, sales, hipaa, ada]
sources:
  - ref: "Operator's ask for 'a real crawlable engine catching HIPAA/ADA/HBOT compliances with governmental citations' and the resulting plan turn: 'wrote CI_AUDIT_ENGINE_EXCELLENCE_PLAN (crawler->extract->deterministic rules->GPT interprets only->cited report; cite-or-omit; candidate-not-verdict; evidence-class honesty; 0.70 floor; determinism).'"
    reliability: high
    origin: "2026-08-21 Amadeus fleet audit / CI reconcile session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl
  turns: [28, 29]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The CI audit engine's core law is cite-or-omit: no finding without crawl evidence plus a resolvable governmental citation
- id: 2026-08-21-ci-cite-or-omit-law
- type: decision
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, grounded in CI VISION architecture)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — codifies the VISION doc's rules-plus-AI-hybrid architecture
- verified: 2026-08-21
- tags: compliance-intelligence, crawler, citations, sales, hipaa, ada
## Body
REVIEW: high-impact
The Compliance Intelligence audit engine crawls a clinic's public web presence and emits candidate compliance risks under five laws: (1) cite-or-omit — every client-facing finding carries crawl evidence (URL + exact snippet) AND a resolvable authoritative citation from the KB; (2) candidate-not-verdict framing ("may present elevated regulatory risk under [authority]", never "violates"); (3) evidence-class honesty (PUBLIC / DOC-REQUESTED / ON-SITE, never faked); (4) 0.70 confidence floor for client delivery; (5) deterministic — snapshot the crawl so audits re-run identically. Deterministic rules own gateable truth; GPT interprets only, never invents findings.
## Links
- enables, ci-three-version-compliance-suite.md, this is how the suite produces sales audits
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
