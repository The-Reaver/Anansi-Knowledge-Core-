---
id: 2026-08-21-cj-dropshipping-disabled-token-interceptor-bean
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, cj-dropshipping, coupling-cohesion, technical-debt, refactor-opportunity]
sources:
  - ref: "Archive turn 39 (background-agent Coupling/Cohesion audit of CJ-dropshipping's service layer): confirms the token-fetch-and-header pattern duplicated 30+ times across all 9 domain services, and a commented-out RestClient interceptor bean in RestClientConfig.java (lines 49-60) that would fix it via an interceptor."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [39, 39]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, confirmed by direct read of RestClientConfig.java and the repeated pattern across service classes
- verified: 2026-08-21

# CJ-dropshipping has a commented-out RestClient interceptor bean that would eliminate 30+ duplicated manual token-attachment code blocks

## Body
Nearly every method across all 9 domain services in CJ-dropshipping manually repeats the same pattern: fetch a token via `authService.getValidToken()`, then attach it as a `CJ-Access-Token` header on the outgoing request. This appears 30+ times across the service layer. `RestClientConfig.java` already contains a commented-out `RestClient` bean (lines 49-60 at the time of the audit) that would attach the auth header automatically via an interceptor, which — if uncommented/enabled — would eliminate all of that duplicated per-method plumbing and turn token attachment into cross-cutting infrastructure instead of copy-pasted service code. This is a low-risk, high-leverage cleanup: the fix already exists in the codebase, just disabled.

## Links
- relates-to, 2026-08-21-cj-dropshipping-two-god-object-services.md, same repo, same coupling/cohesion audit.
