---
id: 2026-08-06-broken-code-scenarios-ds-domain-complete-50-of-50
type: artifact
status: candidate
source: "this chat, 2026-08-06, Abad asked to run five batches; DS-025 through DS-050 built by parallel subagents and each runner re-verified by the main session, completing the DS domain (source status: active)"
project: fleet
tags: [augustin, curriculum, broken-code-scenarios, distributed-systems, go, build-outcome, verified, domain-complete]
supersedes: []
superseded_by: null
---

# Broken Code Scenarios, DS Domain COMPLETE: 50 of 50 Built and Verified as Go In-Process Models

## Body

The DS domain (Distributed Systems) is complete: all 50 scenarios, DS-001 through DS-050, are built and verified. This note supersedes the 24/50 note. Every scenario is a real Go standard-library in-process model that reproduces the bug deterministically, fixes it, and guards the fix; the main session re-ran each run_tests.sh (not only the building subagent) and committed only on exit 0. None of DS-025 through DS-050 required real external infrastructure — each is an algorithmic, protocol, or logic defect faithfully modelable on CPU, so nothing in this domain was faked or blocked.

The final 26 (DS-025..050), each an in-process reframe of the named technology with its fix: 025 Vault seal-wrap key rotation partial failure (versioned keyring; retire the old key only after every secret is re-wrapped, plus a resume step). 026 Istio/Envoy config push timeout (xDS ACK before advancing version; retry and keep last-good on timeout). 027 Linkerd mTLS renewal race (renew early with overlapping validity and a both-cert trust bundle). 028 OTel batch processor memory leak (flush on size OR a max-age timer). 029 Prometheus remote-write backpressure deadlock (non-blocking bounded enqueue with drop-oldest, decoupled from scrape; deadlock proven by bounded no-progress, not a wall-clock timeout). 030 Loki cardinality explosion (per-tenant stream/cardinality limit; shed only the offending high-card label). 031 Tempo compaction corrupting index (two-phase staging + atomic index swap; crash keeps old consistent index). 032 Thanos metadata cache poisoning (validate checksum + invariants before caching). 033 Cortex ring token collision (detect on join, reassign to a unique token). 034 Mimir compactor shard imbalance (balanced high-entropy sharding vs a low-entropy label). 035 Pyroscope symbolization failure (subtract the module load base before symbol lookup). 036 Parca debuginfo upload race (staged upload + atomic finalize + completeness flag; symbolization reports missing rather than silently wrong). 037 Polar eBPF counter overflow (uint64 saturating counter; a 32-bit counter wrapped a 6.5e9 count negative). 038 Pixie agent eviction data loss (flush on shutdown + periodic checkpoint). 039 Cilium Hubble buffer overflow (ring buffer + accurate drop counter + retain newest). 040 Tetragon filter inversion (corrected allow/deny predicate). 041 Falco false negative on syscall (broaden the rule to the syscall family and write-intent flags without over-matching benign). 042 Kyverno webhook timeout (fail-closed on timeout for security policies). 043 OPA Gatekeeper template compile error (validate on load; fail-closed instead of silent bypass). 044 Crossplane composition loop (cycle detection via topological sort). 045 ArgoCD sync-wave deadlock (topological check + progress deadline, fail fast). 046 Flux HelmRelease semver no-match (surface a degraded/drift status instead of silent no-op). 047 Tekton result propagation failure (wire the result into the downstream param; error on an unmet reference). 048 Knative revision GC premature (skip any revision with active traffic and the latest-ready). 049 KEDA scaler metric auth failure (treat a fetch/auth error as unknown, hold last-known-good/min replicas, never false scale-to-zero). 050 Velero snapshot inconsistent (fsfreeze/quiesce to a consistent transaction boundary before snapshot).

Program status after this: 77 of 500 verified (CM 27, DS 50), 23 blocked-registered (all CM, GPU/ML-framework), 400 not started. Next domain is CT (not yet read from the manual), then ST, NT, SC, RT, AI, FE, BD.

## Links

- supersedes: 2026-08-06-broken-code-scenarios-ds-domain-24-of-50-verified
- affects: 2026-08-06-broken-code-scenarios-program-status-and-dashboard
