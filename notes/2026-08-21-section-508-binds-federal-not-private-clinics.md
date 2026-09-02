---
id: 2026-08-21-section-508-scope
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [ada, section-508, wcag, accessibility, compliance-citations]
sources:
  - ref: "Live-verification turn after operator flagged the URLs came from knowledge not live fetch: 'section508.gov resolves...Section 508 binds federal only, cite ADA Title III+WCAG for private clinics.'"
    reliability: high
    origin: "2026-08-21 Amadeus fleet audit / CI reconcile session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl
  turns: [32, 33]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Section 508 binds federal agencies, not private clinics; a private HBOT clinic's binding accessibility path is ADA Title III plus WCAG 2.1 AA
- id: 2026-08-21-section-508-scope
- type: finding
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, confirmed by live fetch of section508.gov)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — section508.gov states it covers federal ICT under the Rehabilitation Act
- verified: 2026-08-21
- tags: ada, section-508, wcag, accessibility, compliance-citations
## Body
Section 508 of the Rehabilitation Act (section508.gov, resolves) legally binds federal agencies and their vendors, not private businesses. For a private HBOT clinic, cite the binding authority — ADA Title III (ada.gov/resources/web-guidance) plus WCAG 2.1 AA (w3.org/TR/WCAG21) — and reference Section 508 only as the recognized technical benchmark, never as a law the clinic "violates."
## Links
- instance-of, ci-cite-or-omit-law.md, accessibility KB atom framing
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
