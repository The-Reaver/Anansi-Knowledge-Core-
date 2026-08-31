---
id: verify-full-diff-against-pr-changed-files-stat-2026-08-31
type: lesson
status: ratified
source: "This session, 2026-08-31 — reviewing The-Reaver/Stag-Fleet#1, a subagent's first pass treated a 162,782-character fetched file list as the complete diff"
project: fleet
tags: [pr-review, tooling, pagination, verification]
supersedes: []
superseded_by: null
---

# A "full diff" fetched for a large PR can be silently paginated with nothing in the response saying so

## Body

Fetched what looked like the complete file list/diff for a GitHub PR — a single large
result, 162,782 characters, no truncation notice, no error. It turned out to be page 1 of
a paginated response covering only 30 of the PR's actual 2,423 changed files. Nothing
about the tool result signaled incompleteness; the only way to catch it was to separately
call a plain PR-metadata fetch and notice the `changed_files`/`additions`/`deletions`
counts didn't match what had just been reviewed.

**Check next time a large PR's diff or file list is fetched for review:** cross-check the
result's file count against the PR's own metadata (`changed_files`, `additions`,
`deletions` from a plain `pull_request_read: get` call) before treating the fetch as
complete. A mismatch means more pages exist and haven't been seen yet. Skipping this check
risks reviewing a small fraction of a change while believing the whole thing was covered.

## Links

- relates-to: large-draft-pr-description-can-go-stale-vs-head-2026-08-31
