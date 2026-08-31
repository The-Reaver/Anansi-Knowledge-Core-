---
id: large-draft-pr-description-can-go-stale-vs-head-2026-08-31
type: finding
status: candidate
source: "This session, 2026-08-31 — reviewing The-Reaver/Stag-Fleet#1"
project: fleet
tags: [pr-review, staleness, verification, draft-pr]
supersedes: []
superseded_by: null
---

# A long-lived draft PR's description reflects whatever slice existed when it opened, with nothing forcing it to track the actual head

## Body

Found a draft PR whose description named three specific, verifiable claims about a small
feature slice — all confirmed true against the code. But the description was written on
the PR's opening day, while its actual head was 110 commits and 2,423 changed files later,
bundling entirely unrelated work (a dashboard bridge, new governance mandates, curriculum
exercises) never mentioned anywhere in the description. The specific claims being true
didn't make the PR, as a whole, an accurate or reviewable unit — the description simply
stopped being updated while the branch kept growing.

**Check next time a PR's claims are being taken at face value, especially a long-lived or
draft one:** compare `created_at` against `updated_at` and the current `commits`/
`changed_files` count from a plain PR-metadata fetch. A large gap between when the
description was written and how much the branch has since grown is itself a signal —
verify claims against the actual current diff, not just against what the description
says, and say so explicitly if the description no longer represents the head.

## Links

- relates-to: verify-full-diff-against-pr-changed-files-stat-2026-08-31
