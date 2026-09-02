---
id: 2026-08-25-never-guess-conflicting-real-facts
type: decision
status: ratified
ratified: "2026-08-25 — Brain Trust + AJ ratification pass (seats: Celestina, Jasiah, Oluwole, Omar, Sentinel; AJ independent audit). Vote and conditions recorded in reports/STAG_BRAIN_TRUST_LEDGER.md. Operator ruling per Mandate 1."
project: agame-sports-rebuild
tags: [content-accuracy, editorial-judgment, real-business-data, guardrail]
sources:
  - ref: "Content-sweep queue fix, turn 51: contradictions resolvable from page context were fixed; birthday-party guest-cap numbers were deliberately left for the business owner, A-Game Sports rebuild, 2026-08-25"
    reliability: medium
    origin: "A-Game Sports rebuild remote session, 2026-08-25; transcript reconstructed manually and ingested into the Core by the bridge-cse session the same day"
provenance:
  archive: research/knowledge-home/raw/2026-08-25-agame-remote-diagnostics-and-content-sweep.jsonl
  turns: [59, 60]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

> **Provenance added 2026-08-25 on ingest.** This note was authored in a remote container with no
> access to the Core, so it originally carried no ADR-0005 provenance pointer. The session
> transcript has since been ingested (96 records) and the turn range above was read off that
> archive, not estimated. Ratified 2026-08-25 by the Brain Trust + AJ pass; the
> conditions that ruling attached have been applied to this note.

# When independent sources on a real business disagree on a fact, flag it for a human decision instead of picking one
- id: 2026-08-25-never-guess-conflicting-real-facts
- type: decision
- status: ratified
- ratified: 2026-08-25 Brain Trust+AJ
- class: confirmed
- source: A-Game Sports rebuild diagnostics session, 2026-08-25
- confidence: high — applied consistently across two rounds of fixes on this session
- verified: 2026-08-25
- tags: content-accuracy, editorial-judgment, real-business-data, guardrail

## Body
During a content-accuracy sweep of a real business's marketing site, some contradictions are safe to fix unilaterally (an internally impossible staffing rule, a tiebreaker rule stated two ways in the same file, a stale date reference) because there is one obviously-correct resolution derivable from the page's own logic. Others are not safe to guess — e.g. two different guest-cap numbers on a birthday-party pricing page (a "15 kid" base vs. a "22+" overage threshold) where either number could be the real business rule and picking wrong publishes incorrect pricing/capacity policy for real paying customers. The workable rule applied this session: fix contradictions where the correct resolution is derivable from context already on the page or corroborated by multiple independent pages (e.g. reconciling a staff bio's years-of-experience by trusting the most detailed, dated bio over two vaguer restatements); leave contradictions alone and flag them explicitly when resolving them requires knowledge only the business owner has (real pricing, real capacity limits, real staff assignments) — never fabricate a resolution to a real commercial fact.

## Links
- related, 2026-08-25-multi-agent-diagnostic-sweep-pattern.md, this guardrail is what the sweep's synthesis report needs to encode per finding
