---
id: 2026-08-06-broken-code-scenarios-ds-domain-24-of-50-verified
type: artifact
status: candidate
source: "this chat, 2026-08-06, Augustin curriculum DS wave DS-019 through DS-024 built by parallel subagents and re-verified by the main session (source status: active)"
project: fleet
tags: [augustin, curriculum, broken-code-scenarios, distributed-systems, go, build-outcome, verified]
---

# Broken Code Scenarios, DS Domain: 24 of 50 Built and Verified (DS-019..024 Wave Added)

## Body

The DS domain (Distributed Systems, 50 scenarios) now stands at 24 built and verified, DS-001 through DS-024. This note supersedes the earlier 18/50 note; it adds the DS-019 through DS-024 wave. Each scenario is a real Go standard-library in-process model that reproduces the bug deterministically, fixes it, and guards the fix. Every runner was re-run by the main session (not only the building subagent) and committed only on exit 0, which is the guard against fabricated results.

The six added this wave, each an in-process reframe of the named technology with its fix: DS-019 RabbitMQ mirror-queue sync hang on promotion (broken promotes an unsynced mirror and loses the un-backfilled messages; fix gates promotion on a fully in-sync mirror, delivered 10 of 10 with zero loss). DS-020 NATS JetStream consumer ack-floor reset (broken keeps the ack floor in memory only, resets to 0 on restart, reprocesses the already-acked 1..K; fix persists and restores the floor, redelivers only K+1..N, zero duplicates). DS-021 Redis cluster slot migration stuck IMPORTING (broken crashes mid-migration leaving the slot with no definitive owner and keys in limbo; fix adds an atomic finalize plus a recovery routine that completes-forward to a single owner with all keys retrievable). DS-022 Memcached consistent-hash weight mismatch (broken changes a node weight without re-sorting the ring, so clockwise lookups mis-route and a ~70 percent miss storm forms; fix rebuilds the sorted weighted ring on any weight change, zero spurious misses and bounded key movement). DS-023 etcd watch stream silent disconnect (broken resumes the watch from the latest revision and misses gap events, leaving the client view stale; fix resumes from last-observed-revision+1 and falls back to a full snapshot re-list on ErrCompacted, converging to the authoritative state). DS-024 Consul health-check flapping (broken flips status on every sample so transient blips cause spurious deregisters and dropped traffic; fix adds failure-count and success-count hysteresis thresholds, absorbing transient noise so only a sustained outage flips the service once).

DS-025 through DS-050 are not yet done. The next wave is DS-025 through DS-030 (Vault seal-wrap key rotation partial failure, Istio sidecar Envoy config push timeout, Linkerd mTLS certificate renewal race, and DS-028/029/030 still to be read from the manual), all expected to reframe faithfully into Go in-process models.

## Links

- supersedes: 2026-08-06-broken-code-scenarios-ds-domain-18-of-50-verified
- affects: 2026-08-06-broken-code-scenarios-program-status-and-dashboard
