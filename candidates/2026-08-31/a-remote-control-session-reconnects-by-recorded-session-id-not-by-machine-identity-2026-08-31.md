---
id: a-remote-control-session-reconnects-by-recorded-session-id-not-by-machine-identity-2026-08-31
type: lesson
status: candidate
source: "Recovery session, 2026-08-31 — verified by recovering session_01Q1wJW3McyXVkdvLjvLVKmy after Remote Control restarts failed, and against the official Remote Control documentation"
project: fleet
tags: [remote-control, session-recovery, runbook, bridge-environment, tooling]
supersedes: []
superseded_by: null
---

# Restarting Remote Control cannot recover an offline session — it mints a new environment and orphans the old binding

## Body

A session showed *"Can't reach your computer... Remote Control host unreachable
(computer_unreachable)"*. Restarting Remote Control, repeatedly, did not recover it.

The reason: a bridge environment registers as `HOSTNAME:WORKING_DIRECTORY:TOKEN`, e.g.
`DESKTOP-4UC2LTP:C:\Users\abadm\stag:5229`. **That trailing token is a random per-host
instance id, not a port.** Each restart mints a *new* environment (`...stag:d218`) instead
of re-registering the old one, so the session stays pinned to an environment nothing answers
for. Two tells confirm the state: two bridge environments for the same host and directory
with different tokens, and the session's `last_init_error` timestamp staying **frozen** — a
session genuinely retrying updates it.

Chasing the token is a dead end. Remote Control *"makes outbound HTTPS requests only and
never opens inbound ports on your machine"*, so there is no port to bind and no flag to set.

**The fix is that reconnection is keyed to the session id recorded in the conversation:**
run `claude --resume` (or `--continue`, or `claude remote-control --session-id <id>`) from
the session's original working directory on the host. This worked immediately after restarts
had failed for an hour.

Three constraints: run it in a terminal separate from any other Remote Control session in
that directory; if the failure reason says the session was taken over or ended elsewhere, it
is genuinely unrecoverable; and if the conversation was compacted meanwhile, the old server
session is archived rather than restored.

**Never delegate this to a session running on the same host** — restarting Remote Control
from inside a session that Remote Control is hosting severs its own connection and mints yet
another environment.

Full procedure: `docs/runbooks/remote-control-session-recovery.md`.

## Links

- relates-to: session-transcripts-are-reachable-so-the-harvest-backlog-is-a-choice-not-a-limit-2026-08-31
- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
