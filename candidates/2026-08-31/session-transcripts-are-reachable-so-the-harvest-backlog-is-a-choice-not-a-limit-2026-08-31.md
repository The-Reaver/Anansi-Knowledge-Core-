---
id: session-transcripts-are-reachable-so-the-harvest-backlog-is-a-choice-not-a-limit-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — verified by recovering session_01Q1wJW3McyXVkdvLjvLVKmy after Remote Control restarts failed, and against the official Remote Control documentation"
project: fleet
tags: [knowledge-core, harvesting, transcripts, teleport, capture-gap, raw-archive]
supersedes: []
superseded_by: null
---

# Cloud sessions are not structurally invisible — teleport pulls their full history to disk

## Body

The fleet's standing position has been that cloud sessions are structurally invisible to
capture, and that undistilled transcripts are therefore unreachable. **Both halves are
wrong**, and the correction matters because it turns a stated impossibility into a task.

Two routes exist, one per environment kind:

- **Bridge sessions** — the transcript is already JSONL on the host's own disk, under
  `~/.claude/projects/<escaped-cwd>/`. Any session on that machine can read it directly.
- **Cloud sessions** — `claude --teleport <session-id>` *"loads the full conversation
  history into your terminal"*. Reopening the session at claude.ai also restores its
  conversation history onto a fresh VM.

`environment_deleted` kills the live session, not the transcript. For a bridge session the
local JSONL survives regardless.

Scale as measured 2026-08-31: **88 sessions, ,649.99 of spend.** 13 sessions over $50, 9
between $5 and $50, 66 under $5. The largest single session — $1,965 and 787k output
tokens — is a **cloud** session, so it is reachable only by teleport or reopening. Inventory:
`docs/session-harvest-worklist-2026-08-31.md`.

This also gives `raw/` its first real path to being populated. ADR-0005 warned that "an
ephemeral chat that closes without an archive write is gone for good" and recorded `raw/` as
scaffolded but empty because historical transcripts were not reachable turn-by-turn. For
bridge sessions at least, they are.

**Teleport's constraints:** clean git state, a checkout of the same repository, the branch
pushed, and the same claude.ai account.

## Links

- relates-to: a-remote-control-session-reconnects-by-recorded-session-id-not-by-machine-identity-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
