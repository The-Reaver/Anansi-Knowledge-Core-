---
id: 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally
type: finding
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: anansi
tags: [anansi, harvesting, cloud-sessions, tooling-limit, provenance]
sources:
  - ref: "Verified directly by the harvesting session, 2026-08-27: WebFetch on the session URL returned HTTP 403; `claude --help` exposes no session-export subcommand (only `--cloud` to attach interactively); the cloud session's own ~/.claude/projects/*.jsonl lives in its sandbox at /workspace/the-geo-suite-, not on local disk; a grep of local transcripts found only commit-trailer references to the session URL"
    reliability: high
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [1, 1]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A claude.ai/code cloud session's raw transcript cannot be retrieved from the local machine, so anything worth harvesting must be exported from inside that session while it is open

## Body
When asked to harvest a cloud session (`https://claude.ai/code/session_<id>`) into the Core
from a local machine, the raw transcript is **not reachable**. Checked directly rather than
assumed:

- `WebFetch` on the session URL returns **HTTP 403** -- it is an authenticated SPA, not a
  fetchable document.
- The Claude Code CLI has **no session-export subcommand**. `claude --cloud <url>` attaches to the
  session *interactively*; it does not dump history, and attaching would append turns to the
  operator's session as a side effect.
- The session's own native transcript (`~/.claude/projects/<cwd>/<session_id>.jsonl`, the file
  `scripts/knowledge_home/backfill_import.py` is built to ingest) lives **in the cloud sandbox**,
  not on local disk. For this session that sandbox was `/workspace/the-geo-suite-`.
- A local search found the session ID only inside **commit trailers**
  (`Claude-Session: https://claude.ai/code/session_...`) captured in another session's transcript
  -- enough to correlate commits to a session, not to reconstruct it.

**Consequence for harvesting:** the best available input is whatever that session **exported
before it closed** -- a development log, a handoff, a summary. That is second-hand by
construction, and if the session was compacted, parts of it are second-hand twice over. Ingest
should say so in the archive header rather than presenting a summary as a transcript.

**What to do differently:** when a cloud session is doing work worth keeping, have it write the
export *itself*, while it still has its own full context -- and prefer a dense, quote-preserving
development log over a tidy summary, since verbatim operator wording is the first thing a summary
discards and the last thing a note can reconstruct.

(The commit-trailer convention is quietly valuable here and worth keeping: it is the only durable
local link between shipped code and the cloud session that produced it.)

**As of 2026-08-27.** This describes the tooling available on that date, not a permanent
property. If Anthropic ships a session-export command or a transcript API, the whole finding
changes. Re-check `claude --help` for an export subcommand before relying on this; the
workaround (have the cloud session export itself, or commit its transcript) stays useful
either way.

## Links
- relates-to: candidates/2026-08-25/2026-08-25-stag-closeout-skill-remote-session-gap.md
- relates-to: 2026-08-27-the-24-page-audit-report-is-a-compounding-narrative-not-a-build-spec
