---
id: 2026-08-21-uuid-not-json-serializable-at-service-boundary
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [python, uuid, json-serialization, type-coercion, fastapi, supabase, backend]
sources:
  - ref: "Archive turns 331-341: a live TypeError 'Object of type UUID is not JSON serializable' traced to the router passing real UUID objects (versus local tests that only used strings), fixed by coercing ids to str at the service entry point, then reproduced and confirmed with UUID inputs returning status active."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [331, 341]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, reproduced live against the deployed backend with a concrete traceback and fixed
- verified: 2026-08-21

# A UUID object survives read-path Supabase filters but crashes write-path JSON encoding, hiding a type bug until the write path runs

## Body
In a FastAPI backend, a router-level dependency (an owner-context object) can hand a `UUID` object down to a service function whose local tests had only ever been exercised with plain strings. The UUID survives read-path calls, such as a Supabase `.eq(...)` filter, because it gets stringified into the request URL — but the exact same UUID passed into a write payload that Supabase JSON-encodes raises `TypeError: Object of type UUID is not JSON serializable` and surfaces as an opaque 500. This class of bug stays invisible until a write path is exercised with production-shaped types: a local test that only passes strings can look clean while the deployed router, which passes real `UUID` objects, 500s on the exact same function. The fix is to coerce ids to `str` at the service entry point so it is robust to both string and UUID callers.

## Links
- relates, origin-check15-backend-mypy-type-gate.md, this is the exact shape of type-boundary drift (`arg-type`) that gate's mypy check is designed to catch at generation time.
