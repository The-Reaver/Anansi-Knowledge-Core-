---
id: 2026-08-21-hhs-tracking-bulletin-vacated
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [hipaa, tracking-pixels, phi, compliance-citations, hbot]
sources:
  - ref: "Live-verification turn after operator flagged the URLs came from knowledge not live fetch: 'HHS tracking URL resolves BUT portion vacated by federal court June 20 2024 -> cite HIPAA Privacy Rule as durable authority + bulletin w/ vacatur caveat.'"
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

# HHS's online-tracking HIPAA bulletin was partially vacated in June 2024, so cite the Privacy Rule itself as the durable authority
- id: 2026-08-21-hhs-tracking-bulletin-vacated
- type: finding
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, confirmed by live web search)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — HHS URL resolves; court vacatur reported by AHA and multiple firms
- verified: 2026-08-21
- tags: hipaa, tracking-pixels, phi, compliance-citations, hbot
## Body
REVIEW: high-impact
HHS OCR's "Use of Online Tracking Technologies by HIPAA Covered Entities" guidance (hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) resolves and is canonical, but a U.S. District Court vacated a portion on 2026-06-20 (the "unauthenticated public webpage visit = PHI" reading). A client audit must cite the durable authority — the HIPAA Privacy Rule, 45 CFR 164.502/514 (vendor disclosures, marketing) — with the bulletin as interpretive guidance plus a one-line vacatur caveat. The core obligation (no PHI to Meta/Google pixels without authorization or a BAA) still stands. This is the highest-value, crawl-detectable HBOT-clinic web risk.
## Links
- instance-of, ci-cite-or-omit-law.md, a KB atom must carry this nuance
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
