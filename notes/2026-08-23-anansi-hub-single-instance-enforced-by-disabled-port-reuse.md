---
id: 2026-08-23-anansi-hub-single-instance-enforced-by-disabled-port-reuse
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering all 7 (all read in full, all 6 unique cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, architecture, multi-session, operations]
sources:
  - ref: "Operator asks how to instruct other chats to run the Hub (line 1289); assistant answers that anansi_hub.py explicitly disables port-reuse (a 2026-08-17 fix after two Hub processes once shared port 8787), so a second start attempt fails loudly rather than splitting traffic (line 1290)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1289, 1290]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Anansi Hub deliberately refuses to let a second instance bind its port, so a second start attempt fails loudly instead of silently splitting traffic

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1238-1324
- confidence: high, confirmed by reading the actual `anansi_hub.py` source (SingleInstanceServer class, port-reuse explicitly disabled)
- verified: 2026-08-23

When the operator asked how to instruct other chat sessions to run the Hub, the assistant checked the actual `anansi_hub.py` source rather than answering from memory and confirmed: the Hub server deliberately disables socket port-reuse (a `SingleInstanceServer` class with reuse-address turned off). This was a fix put in after an earlier incident where two Hub processes both ended up listening on port 8787 at once and silently split traffic between them.

The practical consequence: only one Hub instance can run at a time. If a second session tries to start it while one is already running, that second attempt fails immediately with a clear bind error, rather than starting anyway and creating a second process that shares the port ambiguously. This is correct, intended behavior, not a bug to route around — the guidance for multi-session use is to check whether the Hub is already up (e.g. `curl http://localhost:8787/api/health`) before starting it, not to start it from every session that might need it.

## Links
- related, 2026-08-21-anansi-hub-and-mcp-server-confirmed-live-2026-08-21.md, general Hub liveness verification; this note adds the specific single-instance enforcement mechanism.
