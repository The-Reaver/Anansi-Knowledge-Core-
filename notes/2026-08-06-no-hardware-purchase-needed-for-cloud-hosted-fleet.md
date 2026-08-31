---
id: 2026-08-06-no-hardware-purchase-needed-for-cloud-hosted-fleet
type: decision
status: ratified
source: "Cowork session 2026-08-06, operator on phone; asked the Brain Trust to render verdicts on a large set of planning queries (source status: active); mined from candidates/2026-08-25/2026-08-06-brain-trust-verdicts-and-operator-contributions.md"
project: fleet
tags: [hardware, budget, cloud, supabase, memory]
---

# Text and the Knowledge Core database stay tiny for years; no hardware purchase is needed unless running models locally

## Body

Notes, docs, and artifacts are tiny and will never fill the machine; the Knowledge Core database is a few gigabytes for years of notes. Only running models locally needs big RAM and a strong GPU — models currently run in Anthropic's cloud, so no such hardware is needed to operate today. Build the Knowledge Core in the cloud (Supabase, already owned, near-free at this scale); local stays a later option for privacy and control, designed for both so it can switch. Buying a big GPU preemptively is premature spend.

## Links

- relates: 2026-08-06-build-local-capable-system-now-not-later-for-patient-data
