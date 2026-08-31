---
id: 2026-08-05-app-layer-ledger-write-never-run-end-to-end
type: finding
status: candidate
source: "this chat, 2026-08-05, Abad asked for a thorough announcement of Knowledge Core's real state and business benefit (source status: active); mined from candidates/2026-08-25/2026-08-05-knowledge-core-benefits-and-honest-risk-reference.md"
project: fleet
tags: [knowledge-core, limitation, network-egress, terminal]
supersedes: []
superseded_by: null
---

# The application layer reading/writing the capability ledger had, as of 2026-08-05, never run end to end — it needs the operator's own terminal

## Body

Neither the Cowork session nor the device bridge holds a network path to Supabase or OpenAI, so the first true end-to-end write through the application layer (as opposed to a direct database test) has to happen from the operator's own terminal. This is a point-in-time status report rather than a durable rule — it should be re-verified against the current state of the ledger before anyone relies on it, which is why it is held as a candidate rather than ratified.

## Links

- relates: 2026-08-05-capability-ledger-live-tested-on-supabase
- relates: 2026-08-04-sandbox-network-egress-blocks-real-deploy
