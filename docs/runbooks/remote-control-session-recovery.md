# Runbook — recovering a Remote Control session that says "Can't reach your computer"

Written 2026-08-31 after recovering `session_01Q1wJW3McyXVkdvLjvLVKmy`. Everything here was
verified in that recovery or quoted from the official docs; guesses are marked as such.

## The symptom

> **Can't reach your computer.** It may be asleep or offline. This session will reconnect
> when it's back. — `Remote Control host unreachable (computer_unreachable)`

## What is and isn't lost

**Nothing is lost.** Three separate stores are involved and none of them is the offline
machine:

| What | Where it lives | Survives the host going offline? |
| --- | --- | --- |
| Conversation transcript | Anthropic servers (and locally as JSONL) | Yes |
| Pending question / tool call | Anthropic servers | Yes |
| Files the session wrote | your own disk | Yes — a bridge host is not an ephemeral container |
| The live *binding* to the host | the session record | **No — this is the only thing that breaks** |

The docs are explicit that the transcript is server-side: *"While Remote Control is
connected, the session transcript... is stored on Anthropic servers. The stored transcript
keeps the conversation in sync across your devices and lets the session reconnect after a
network drop."*

So the failure is a **stale binding**, not data loss. Treat it that way.

## The trap: restarting Remote Control does not fix it

This is the part that costs hours.

A bridge environment is registered as `HOSTNAME:WORKING_DIRECTORY:TOKEN` — for example
`DESKTOP-4UC2LTP:C:\Users\abadm\stag:5229`. **That trailing token is a random per-host-instance
id, not a port.** Restarting Remote Control mints a *new* environment with a *new* token
(`…stag:d218`) rather than re-registering the old one. The session stays pinned to the old
environment id, nothing answers for it, and it never reconnects — no matter how many times
you restart.

**How to confirm you are in this state:** list your environments. If you see two bridge
entries for the same hostname and the same directory with different trailing tokens, and the
newer one's `created_at` matches when you restarted, that is exactly this. A second tell is
that the session's `last_init_error` timestamp stays **frozen** at the original failure — a
genuinely retrying session updates it.

Do not chase the token. It is not a port, there is no flag to set it, and Remote Control
*"makes outbound HTTPS requests only and never opens inbound ports on your machine."*

## The fix

Reconnection is keyed to the **session id recorded in the conversation**, not to the machine
or network identity. From the docs: *"When you resume a conversation with `claude --resume`
or `claude --continue`, Claude Code reconnects to the Remote Control session recorded in that
conversation."*

So, on the host machine, in the session's original working directory:

```
cd C:\Users\abadm\stag
claude --resume
```

Pick the conversation by title. This is what worked.

Alternatives, in order of preference:

```
claude --continue                                   # the last session started in this directory
claude remote-control --session-id <session_id>     # server mode, one specific session by id
```

`--session-id` and `--continue` need Claude Code v2.1.200 or later; earlier versions reject
them as unknown arguments.

### Before you run it

- **Use a separate terminal** from any other Remote Control session in the same directory.
  Resuming in a second terminal while the first still holds Remote Control leaves it *off*
  in the second rather than stealing it; run `/remote-control` there to move it.
- **Read the failure reason first.** If it says the session was taken over or ended from
  another device, or that the server can't find it, resuming will not recover it — that is
  the one genuinely terminal case, and the docs deliberately omit the usual "run
  `/remote-control`" advice for it.
- **If compaction rewrote the conversation, or you switched conversations with `/resume`
  in the meantime,** Claude Code archives the old server session instead of restoring it.
  Find it by filtering for archived sessions.

## Do not delegate this to a session on the same host

A session hosted *by* Remote Control must not restart Remote Control. It would sever its own
connection and mint yet another environment, leaving you worse off. Run the recovery from a
terminal, by hand.

## Belt and braces: write a handoff before you need one

Recovery worked here, but it was not guaranteed. The durable insurance is a handoff document
committed to a repo — not to the machine that might be the thing that is offline. See
`docs/handoffs/2026-08-31-architecture-session.md` for the shape: what is blocked, what is
in flight and where, what is verified versus relayed, the still-binding constraints, and a
suggested resume order.

A new session seeded with that document is a working fallback even when the original is
unrecoverable, and it costs nothing when the original comes back.

## Quick reference

| Situation | Action |
| --- | --- |
| Host asleep, session says unreachable | Wake host, then `claude --resume` in the original directory |
| Restarted Remote Control, still won't reconnect | Expected. Restarting mints a new environment. Use `--resume`, not another restart |
| Two bridge environments, same host and directory | Confirms the stale-binding state |
| `last_init_error` timestamp frozen | No reconnect is being attempted; the binding is orphaned |
| Reason says taken over / ended elsewhere / not found | Not recoverable. Seed a new session from a handoff |
| Conversation was compacted since | Old server session is archived; filter for archived sessions |
| Need to keep working meanwhile | Start a new session on the *current* environment, seeded with the handoff |
