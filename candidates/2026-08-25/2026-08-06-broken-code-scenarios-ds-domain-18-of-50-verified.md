---
id: 2026-08-06-broken-code-scenarios-ds-domain-18-of-50-verified
type: artifact
status: candidate
source: "this chat, 2026-08-05 to 2026-08-06, Augustin curriculum work on the 500 Broken Code Scenarios manual, DS domain (Distributed Systems) (source status: active)"
project: fleet
tags: [augustin, curriculum, broken-code-scenarios, distributed-systems, go, build-outcome, verified]
---

# Broken Code Scenarios, DS Domain: 18 of 50 Built and Verified as Go In-Process Models

## Body

The DS domain (Distributed Systems, 50 scenarios) stands at 18 built and verified, DS-001 through DS-018. Each is a real Go in-process model that reproduces a protocol or data bug deterministically, fixes it, and guards the fix, with the main session re-running every run_tests.sh and committing only on exit 0. Go in-process models are faithful here because these are algorithm-level and ordering-level defects, not infrastructure-specific ones.

The 18 built, each with its fix: DS-001 Raft election livelock (pre-vote plus randomized timeout), DS-002 Paxos ballot wraparound (wide round-plus-node ballot so two values cannot both be chosen), DS-003 CRDT non-commutative last-writer-wins merge (timestamp-plus-replica-id total order), DS-004 vector-clock aggressive pruning dropping a causal ancestor (prune only below the global lower bound), DS-005 HLC backward NTP skew (l = max(prev, physical) with a logical tiebreak), DS-006 gossip amplification storm (dedup by id plus TTL plus anti-entropy), DS-007 SWIM false-positive cascade (indirect probe plus suspicion plus incarnation numbers), DS-008 consistent-hashing reshard data loss (ring plus vnodes plus migration), DS-009 quorum stale read after leader change (ReadIndex plus heartbeat quorum), DS-010 2PC coordinator crash blocking participants (prepare timeout plus durable-log recovery; 2PC is inherently blocking, so 3PC or Paxos-commit is noted as the next tightening), DS-011 saga compensation out of order (committed-only, strict reverse, idempotent), DS-012 outbox duplicate publish (idempotency key plus dedup consumer), DS-013 CDC WAL applied-LSN failover (checkpointed LSN), DS-014 replication slot retention explosion (slot cap plus invalidate), DS-015 watermark late events (bounded lateness plus dead-letter queue), DS-016 idempotency key collision (full-identity key), DS-017 Kafka rebalance storm (cooperative rebalance), DS-018 Pulsar cursor mark-delete lag (mark-delete coalesce).

DS-019 through DS-050 are not yet done. The next wave is DS-019 through DS-024 (RabbitMQ mirror-queue sync hang on promotion, NATS JetStream ack-floor reset, Redis cluster slot migration stuck importing, Memcached consistent-hash weight mismatch, and DS-023/024 still to be read from the manual), all expected to reframe faithfully into Go in-process models.

## Links

- affects: 2026-08-06-broken-code-scenarios-program-status-and-dashboard
