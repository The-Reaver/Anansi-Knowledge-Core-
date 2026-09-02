---
id: 2026-08-23-anansi-hub-semantic-search-first-call-blocked-by-synchronous-full-corpus-embedding
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify this\"), given after reviewing an operator-facing review report covering all 6 (all read in full, all 6 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, semantic-search, embeddings, ollama, bug-fix, production, sdlc]
sources:
  - ref: "Assistant root-causes the hang: Ollama itself is fine (~0.34s/call) but ensure_embeddings() synchronously embeds all 945 notes on the first /api/semantic request, ~5+ minutes (line 1207); fixes it via a background-thread warmup flag and verifies live (0.42s first call, no duplicate warmup threads, other endpoints stay responsive) (lines 1209-1224)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1207, 1224]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Anansi Hub's /api/semantic appeared to hang because ensure_embeddings() synchronously embedded the entire 945-note corpus inside the very first request instead of returning immediately

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1085-1237
- confidence: high, directly measured Ollama per-call latency and corpus size, and verified before/after response times live
- verified: 2026-08-23
- REVIEW: high-impact

A robustness gap in Anansi Hub's `/api/semantic` endpoint — first surfaced as a reported request error by the `agent_breakers` harness run, and independently confirmed with a raw `curl` call that itself timed out after 15+ seconds with zero response — was root-caused precisely rather than assumed. Ollama itself was running fine: a single embedding call, tested directly, took about 0.34 seconds. The actual problem was in `ensure_embeddings()`, which ran synchronously inside the very first call to the `/api/semantic` request handler and embedded the *entire* Knowledge Core corpus (945 notes at the time) one HTTP call at a time before returning anything at all — roughly 945 x 0.34s, over 5 minutes of true first-call latency, far past any normal client's or curl's timeout. That is why it presented as a hang rather than as merely slow.

This is a meaningfully worse failure mode than two much earlier (2026-08-08) Knowledge Core notes describing the same underlying mechanism as a stated, accepted limit ("first semantic search after a restart re-embeds the whole corpus, wait about a minute for ~300 notes, then it's instant"). At the corpus's current size, the identical mechanism now exceeds ordinary client timeouts entirely, turning an accepted one-time wait into an effective outage on first use.

Fixed by moving the one-time corpus embedding into a background thread: a new `_EMB_WARMING` flag guarded by the existing `_EMB_LOCK` for thread safety, `reload_data()` updated to reset the new flag too, and `semantic_search()` changed to raise a fast, honest "still warming up" error that the existing `/api/semantic` handler already turned into a graceful keyword-search fallback — so the request now returns immediately either way instead of blocking on the corpus embed. Verified live: the first call after restart responded in about 0.4 seconds with real keyword-fallback results, subsequent calls did not spawn duplicate warmup threads, other endpoints stayed fully responsive while warmup ran in the background, and no errors appeared after about 68 seconds of background runtime. Full corpus warmup still takes a few minutes to complete on its own; `/api/health`'s `semantic_ready` flag flips to true once it finishes, with no action required.

## Links
- relates, 2026-08-08-terminal-glossary-first-semantic-search-slow-after-restart.md, the earlier, smaller-corpus version of this same mechanism, documented then as an accepted limit rather than a bug — this note records the point at which corpus growth turned that accepted limit into an effective outage, and the fix that resolved it
- relates, 2026-08-21-lifespan-background-services-must-be-exception-and-timeout-guarded.md, the same general architectural pattern (a slow warmup/background task must never block the primary request path) applied in a different codebase
- relates, 2026-08-23-agent-breakers-context-request-lacked-timeout-exception-handling.md, the harness fix that first turned this bug's symptom into a visible, reportable finding instead of a silent timeout
- relates, 2026-08-23-dashboard-ratify-page-and-graph-color-sliders-committed-after-hub-restart.md, unrelated pending work that got committed alongside this fix because fixing it required the Hub restart that had been unavailable for the rest of the session
