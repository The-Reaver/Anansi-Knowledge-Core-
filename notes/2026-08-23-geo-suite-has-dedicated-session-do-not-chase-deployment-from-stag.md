---
id: 2026-08-23-geo-suite-has-dedicated-session-do-not-chase-deployment-from-stag
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify this\"), given after reviewing an operator-facing review report covering all 6 (all read in full, all 6 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [geo-suite, scoping, advisory, process, standing-rule]
sources:
  - ref: "Right after the assistant's top advisory recommendation was to chase down where the-geo-suite- actually deploys, the operator states 'i have a dedicated GEO Suite session going on for the last few days,' and the assistant acknowledges this reframes advisory scope and stops treating GEO Suite items as things to chase"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1124, 1126]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# GEO Suite has its own dedicated, continuously-running session; a stag-repo session should not proactively chase its deployment or commit status
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1085-1237
- confidence: high, direct operator statement, immediately applied to reshape the assistant's own advisory recommendations in the same session
- verified: 2026-08-23

REVIEW: high-impact

## Body
Moments after the assistant proposed, as its top advisory recommendation, chasing down where the `the-geo-suite-` repo actually deploys (in order to resolve a real unresolved observability gap it had just found — see the linked note), the operator stated: "i have a dedicated GEO Suite session going on for the last few days." The assistant acknowledged this reframes advisory scope: GEO Suite already receives continuous, dedicated attention from its own session, so it is not something sitting unattended that a general/stag-scoped session should proactively investigate, push on, or chase down. GEO Suite's own work — including its own deployment questions, security fixes, and Knowledge Core notes — will land in the Core through that dedicated session's own process, the same way GEO Suite content had already been swept into the Core earlier in this same session.

Standing effect for future sessions: when running a general or stag-repo-scoped advisory pass (of the kind requested earlier in this same stretch — proactively recommend what to do next, grounded in the Knowledge Core, using an SDLC/engineering-plugin lens) GEO Suite items should be excluded from the recommendation list by default and deferred entirely to the dedicated GEO Suite session, unless the operator explicitly asks for a GEO Suite item to be picked up from a different session. This was applied immediately in the same session: the assistant's revised recommendation list right after this correction dropped every GEO Suite item and pivoted to stag-native work instead (the `agent_breakers` harness, later the `/api/semantic` hang).

## Links
- relates, 2026-08-23-railway-deployment-target-unconfirmable-for-geo-suite-commit.md, the observability gap the assistant had just found and was about to chase when this correction landed
- relates, 2026-08-22c-operator-controls-geo-suite-commits-standing-rule.md, a different, narrower GEO Suite process rule from the same GEO Suite session (who runs git commands for that repo), not about which sessions should track it
