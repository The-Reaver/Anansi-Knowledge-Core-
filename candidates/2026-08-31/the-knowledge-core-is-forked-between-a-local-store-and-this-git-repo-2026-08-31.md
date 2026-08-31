---
id: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — verified directly against this git repo while the originating Architecture session was offline"
project: fleet
tags: [knowledge-core, capture-gap, divergence, retrieval, anansi, provenance]
supersedes: []
superseded_by: null
---

# "The Core" names two different stores with different contents, so a retrieval claim is only true of whichever one was searched

## Body

A dormant-area audit cited five note ids. Checked against this git-tracked repo, **four of
the five do not exist here**:

- `2026-08-02-fleet-dashboard-spec-approved-pending-release` — absent
- `2026-08-08-fleet-dev-dashboard-assigned-to-antigravity` — absent
- `2026-08-21-teachable-language-workstream-still-queued-unscoped-18-days-later` — absent
- `2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles` — absent
- `2026-08-06-cross-agent-stars-dreams-curriculum-design` — present, but only as an
  unratified candidate in `candidates/2026-08-25/`

The audit was not wrong. It searched the operator's **local Knowledge Home** at
`C:\Users\abadm\stag\research\knowledge-home\`. ADR-0005 names that store explicitly
and says this git repo "had only ever carried the Core half of it". The STARS/DREAMS
candidate independently confirms the convention: "every finished task becomes an atomic
note in `research/knowledge-home/notes/`". The local store is where notes are written; this
repo holds 125 ratified and 71 candidates, a **partial mirror**.

The consequence is that "I searched the Core and it isn't there" is an ambiguous
statement. A cloud session can only reach the git repo, and will truthfully report absence
for notes that exist locally. A local session reports presence. Both are right about
different stores, and neither says which one it means.

**Measured evidence, added after a full graph audit.** Seven links in the git store point at
note ids that do not exist here — broken edges whose targets are, on the naming evidence,
notes that live only in the local Knowledge Home:

- `2026-08-06-does-training-translate-to-building-complex-apps`
- `2026-08-06-master-todo-and-offline-guide-established`
- `2026-08-06-read-first-rulebook-and-dev-process`
- `2026-08-07-cippe-local-build-brief-for-antigravity`
- `2026-08-07-mandate-1-fleet-first-decisions`
- `2026-08-07-agent-naming-split-resolved-alias-kept`
- `2026-08-07-user-originated-zettelkasten-application-to-anansi`

`2026-08-07-mandate-1-fleet-first-decisions` is the sharpest of these: a **mandate** — the
Core's highest-authority content — is cited by a ratified note and is not in the git store.
The fork is not a backlog of unsynced extras; it is load-bearing governance the reachable
half of the Core cannot see.

This is a sharper version of the BEDROCK/Jicome gap: there the fact lived outside the Core
entirely; here it lives in *a* Core, just not the reachable one.

**Check next time a session reports the Core does not hold something:** name the store
searched. And treat reconciling the two stores as a prerequisite for trusting any
absence-based conclusion — an unsynced mirror makes every "not found" unfalsifiable.

## Links

- relates-to: bedrock-was-renamed-jicome-a-childrens-learning-platform-and-the-core-never-recorded-it-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: 2026-08-06-cross-agent-stars-dreams-curriculum-design
