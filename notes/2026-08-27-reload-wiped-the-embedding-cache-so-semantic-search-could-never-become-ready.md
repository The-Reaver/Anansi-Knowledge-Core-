---
id: 2026-08-27-reload-wiped-the-embedding-cache-so-semantic-search-could-never-become-ready
type: finding
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: anansi
tags: [anansi, semantic-search, cache-invalidation, embeddings, benchmarking, silent-failure]
sources:
  - ref: "anansi_hub.py reported semantic_ready=false after 25h uptime with Ollama running. Root-caused 2026-08-27: reload_data() reset _EMB={} and _EMB_READY=False on every call, and _warm_embeddings() swallowed exceptions. Fixed with content-hashed incremental vectors, an atomic on-disk cache and an 8-way parallel warm; verified by full warm (998 notes, ~16 min, 0 errors), instant-ready restart, reload-preserves-ready, and a mutation test proving an edited note re-embeds in ~4s"
    reliability: high
    origin: "bridge-cse stag session, 2026-08-27, on the operator's instruction to resolve semantic_ready"
provenance:
  archive: research/knowledge-home/raw/2026-08-27-audit-report-standard-mandate.jsonl
  turns: [3, 3]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Anansi's meaning-search could never become ready, because every reload silently discarded the whole embedding index

## Body
`anansi_hub.py` reported `semantic_ready: false` after 25 hours of uptime with Ollama running
and the model present. Not slowness — **two defects that made readiness structurally
unreachable.**

1. **`reload_data()` wiped the index.** It set `_EMB = {}` and `_EMB_READY = False` on every
   call, and warming only restarted on the *next* semantic query. A full warm took ~16 minutes;
   `POST /api/reload` is what you call after writing notes. So the exact workflow the Core exists
   to support — write notes, reload, search — reset the index every time. Three reloads in one
   session destroyed three partial warms. **Meaning-search could not have become ready in any
   note-writing workflow, ever.**
2. **The warm thread swallowed its own exceptions.** `_warm_embeddings()` had `try/finally` and no
   `except`, so a single Ollama failure aborted the run, left `_EMB_READY` false, and wrote
   nothing anywhere. That is why this looked like "still warming" for weeks instead of "broken."

**The fix**, all in `anansi_hub.py`:
- **Content-hashed vectors** (`_EMB_HASH`, sha256 over model + embedded text). Reload now *prunes*
  rather than wipes: entries whose note is gone or edited are dropped, every still-valid vector is
  kept, and `_EMB_READY` is true only when every current note is covered.
- **An atomic on-disk cache** (`.anansi_embeddings.json`, written via `os.replace`), so a restart
  no longer throws away the warm. This matters more now that the hub autostarts at logon.
- **8-way parallel warm** and an `except` that prints and persists partial progress, so a failure
  resumes instead of restarting.

**Verified, not assumed:** full warm 998 notes in ~16 min with 0 errors; restart → `semantic_ready`
true immediately from cache; `/api/reload` → still true (the original bug, now a regression test);
mutation test — edit a note's embedded text, reload → correctly flips false, re-warms in **~4s for
that one note** rather than 16 minutes.

**The cross-cutting lesson, and it is the third time in this repo:
benchmarking on synthetic inputs produced a confidently wrong number.** The old code comment
assumed 0.3s per note; my own first measurement said 0.362s at 8 workers and I told the operator
"~6 minutes." Both were measured on *short test strings*. Real note bodies run to `MAX_CHARS`
(4000) and embed roughly 3x slower — the true figure is 0.96s/note, ~16 minutes. The same failure
shape as the 2026-08-26 secret-scan regex, which was tuned against synthetic fixtures and silently
stopped matching 7 of 7 real keys. **Benchmark and test against the real corpus, at real sizes, or
do not quote the number.** The code now carries `SEC_PER_NOTE = 0.96` labelled as measured, with
an instruction to re-measure if the model or `MAX_CHARS` changes.

**A methodology note on the mutation test.** The first attempt appended a marker to the end of the
file and readiness did *not* flip — which looked like broken invalidation. It was not: the hub
embeds only the parsed `## Body` section, so the appended text was never part of the hash. The
test was wrong, not the code. Checking *why* a mutation test fails to fire is as important as
running it; a mutation test that silently tests nothing is the same class of defect as the
`setup_function` no-op found earlier the same day.

## Links
- same-class-as: 2026-08-27-pytest-setup-function-is-a-no-op-for-tests-inside-a-class — machinery
  that appears to run, does nothing, and leaves everything green.
- relates-to: 2026-08-27-knowledge-core-connectivity-hardened-three-fixes — the disk cache is what
  makes the new logon autostart cheap instead of a 16-minute re-warm every boot.
- relates-to: 2026-08-27-note-id-slugs-self-propagate-secret-scanner-false-positives — the other
  live consequence of the 2026-08-26 synthetic-fixture regex incident.
