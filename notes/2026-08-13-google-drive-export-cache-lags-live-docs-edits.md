---
id: 2026-08-13-google-drive-export-cache-lags-live-docs-edits
type: lesson
status: ratified
ratified: "2026-08-14, same-session light pass (Mandate 8 / stag-closeout Step 4) -- a low-risk tooling lesson confirmed by direct md5sum comparison, no build/security/compliance weight requiring full Brain Trust seats"
project: fleet
tags: [google-drive, google-docs, mcp, verification, caching, race-condition, tooling]
sources:
  - ref: "Two consecutive mcp__Google_Drive__download_file_content calls on the same fileId (1NLOAu4Qh_ICV30Yd9tKVoBpX2GNBRiBb), roughly 70 seconds apart, immediately after a live Docs edit"
    reliability: high
    origin: direct observation, this session — md5sum of both decoded payloads matched byte-for-byte
  - ref: "mcp__Google_Drive__get_file_metadata modifiedTime and fileSize fields, checked before and after the stale reads"
    reliability: high
    origin: direct observation, this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-lords-of-cian-room-intake.jsonl
  turns: [43, 44]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A Google Drive download right after a live Docs edit can silently return stale, cached content — check get_file_metadata's modifiedTime first

## What happened

While verifying a browser-driven edit to a Google Doc (typing a new section, confirming it landed
correctly), `mcp__Google_Drive__download_file_content` was called twice on the same file, about a
minute apart, right after the edit. Both calls returned byte-identical output — confirmed by
`md5sum` on the decoded payloads. The second call was expected to reflect the edit; it didn't. The
content was stale by roughly one editing pass' worth of text (missing a paragraph fix made in
between the two calls).

This is easy to misread as document corruption, a failed edit, or a race condition in the editing
tool itself. It's actually simpler: Drive's file-export pipeline (the step that converts a live
Google Doc's internal state into a downloadable `.docx`/plain-text blob) has its own lag, separate
from the Doc's live editing state. The live document (visible in the browser, or read via a
Docs-native API) can be fully correct while the exported file blob a Drive API call returns is
still serving a slightly older snapshot.

## The fix

Before trusting a `download_file_content` (or similarly, `read_file_content`) result as "the
current state of the document," call `mcp__Google_Drive__get_file_metadata` first and check
`modifiedTime` and `fileSize`. If `modifiedTime` isn't at or after the timestamp of the edit being
verified, the export cache hasn't caught up — wait and re-check metadata before re-downloading,
rather than re-downloading immediately and trusting the result. In this session, waiting roughly
10 seconds and re-checking metadata was enough for `modifiedTime` to advance and the next download
to reflect the true state.

## Why this matters beyond this one document

Any fleet workflow that edits a Google Doc (or Sheet, or Slide) via browser automation and then
verifies the result via a Drive API read — rather than re-reading the live page — is exposed to
this. The failure mode is quiet: no error, no warning, just a plausible-looking but stale read. A
verification step that doesn't check `modifiedTime` first can report "edit failed" on a successful
edit, or worse, silently accept a stale read as ground truth and paper over an edit that actually
did fail.

## What this does not mean

This is not a claim that `download_file_content` or `read_file_content` are unreliable in general —
both returned correct data once the cache had caught up. It's specifically about the window
immediately following a live edit, before Drive's export pipeline has processed it.

## Links

- surfaced during, [[2026-08-13-meridian-naming-lock-finalized-and-session-handoff]], the Lords of
  Cian session where this was found and worked around.
- relevant to any future STAG work that edits Google Workspace files via browser automation and
  verifies via a Drive MCP read rather than the live page.
