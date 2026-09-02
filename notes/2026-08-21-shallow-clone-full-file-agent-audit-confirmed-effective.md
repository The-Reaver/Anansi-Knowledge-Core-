---
id: 2026-08-21-shallow-clone-full-file-agent-audit-confirmed-effective
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, technique, usage-efficiency, background-agents, code-audit]
sources:
  - ref: "Archive turns 14-41 span two background-agent delegations against shallow-cloned SONNY repos: the endpoint audit (turn 17, full directory walk, 30 controller files / 128 endpoints in SonnyBackEndRepo alone) and the coupling/cohesion audit (turns 39 and 41, full reads of CJ-dropshipping's 10 service classes/1,257 LOC and SonnyBackEndRepo's 27 service classes/~4,600+ LOC)."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [14, 41]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, this is the technique actually used and the results it produced in this session, across two separate multi-repo audits
- verified: 2026-08-21

# Shallow-cloning + delegating full-file reads to background agents let a 4-repo, 192-endpoint SONNY audit run without sampling or blowing up context

## Body
In this session, four SONNY/ShopOnlineNewYork repos (SonnyBackEndRepo, CJ-dropshipping, sonny-admin-dashboard, sonny-nextjs) were shallow-cloned locally, and the endpoint/controller scan and, separately, the coupling-and-cohesion service-layer scan were each delegated to background agents rather than done in the main conversation thread. The agents explicitly located every controller/route and every service file by directory walk (not sampled) and read each one in full — one pass covered 30 controller files (128 endpoints) in SonnyBackEndRepo alone, another read all 27 of SonnyBackEndRepo's service classes (roughly 4,600+ LOC) in full, and a separate pass covered CJ-dropshipping's 10 service classes (1,257 LOC) in full. This confirms, in a real run, the earlier untested hypothesis from a 2026-08-01 SONNY session that a shallow clone excluding build artifacts keeps deep code review cheap even for a large/bloated repo: the approach worked, produced a complete (not sampled) audit, and kept the raw file dumps out of the main agent's context.

## Links
- confirms, 2026-08-21-shallow-clone-decouples-repo-size-from-diagnostic-cost.md, the earlier session's untested claim about shallow clones, now exercised and holding up in this session.
