---
id: hardcoded-count-assertion-anti-pattern-2026-08-31
type: lesson
status: candidate
source: this chat, 2026-08-31, fixing red CI in The-Reaver/The-Geo-Suite- (PR #7), directly caused by tests/test_knowledge_core_feeds_import.py
project: fleet
tags: [testing, brittle-assertions, geosuite, ci]
supersedes: []
superseded_by: null
---

# A test that asserts an exact count of externally-added files will go stale every time — that's not bad luck, it's the design

## Body

GeoSuite's `test_regulatory_raw_law_data_is_untouched_by_the_import_fix` asserts
`len(md_files) == N` for a directory of numbered legal-citation source files that different
sessions add to over time. Its own comment history shows the literal has been corrected five
times across three days as files were added: 20 → 34 → 39 → 40 → 43. This session's own
`geosuite-raw-law-count-fix-2026-08-31` fixed the fifth instance (a real red-CI break on `main`,
caused by a different session's commit adding 3 files without touching this assertion).

**Why this isn't "someone keeps forgetting" — it's the test shape itself:** an exact-count
assertion against a directory that legitimately grows encodes today's snapshot as if it were an
invariant. Every single future addition to that directory is *by construction* a breaking change
to this test, regardless of how careful the session adding files is, unless updating this one
unrelated test file is part of that session's own mental checklist for "add a source file." Five
occurrences in three days is not a discipline failure to fix with a reminder — it is the expected
failure rate of this test shape under this fleet's actual concurrent-session-authorship pattern.

**What the test actually needs to protect, and a shape that would:** the comment states the real
intent — confirm the `feeds/` import-safety fix didn't silently delete or corrupt the `raw_law/`
corpus. An exact count is one way to detect deletion, but it also alarms on the common, wanted case
(addition) exactly as loudly as the rare, bad case (deletion) or corruption. A shape that separates
those: assert a **minimum** count (`>=` the last known-good number, never silently lowered) rather
than an exact one — catches deletion/corruption without ever going red just because the corpus
grew. This wasn't applied in this pass (out of scope for a CI-unblock fix), but is recorded here
as the concrete alternative for whoever next touches this test.

**The general pattern, beyond this one file:** any assertion of the form "exactly N items exist"
against a collection that legitimate future work is expected to add to is a maintenance trap with
a predictable failure rate, not a one-time bug. Related to but distinct from
`concurrent-session-pointer-drift-lesson-2026-08-31` (hand-maintained "next free" pointers) — that
lesson is about a counter going stale because nobody updates it; this one is about a test
*designed* to break every time the counted thing correctly grows, independent of concurrency. Worth
checking for the same shape (`assert len(x) == <hardcoded literal>` against directories/collections
other sessions are expected to keep adding to) elsewhere in this fleet's test suites.

## Links

- concurrent-session-pointer-drift-lesson-2026-08-31 (this candidates folder) — a related but
  distinct staleness pattern (hand-maintained counters vs. exact-count test assertions)
- geosuite-s14-fix-2026-08-31, geosuite-s48-fix-2026-08-31 (this candidates folder) — this
  session's other GeoSuite mutation-testing/CI-discipline work from the same day
