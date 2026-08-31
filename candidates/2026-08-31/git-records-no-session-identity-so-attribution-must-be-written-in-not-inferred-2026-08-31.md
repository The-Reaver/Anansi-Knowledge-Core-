---
id: git-records-no-session-identity-so-attribution-must-be-written-in-not-inferred-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [git, attribution, provenance, multi-session, trailers]
supersedes: []
superseded_by: null
---

# Three commits were misattributed in one night because git records no session identity at all

## Body

Three separate wrong attributions occurred in a single night's multi-session work. The
root cause is not carelessness: **git has no concept of which session authored a commit.**
It records author and committer identity, both of which are the same human or machine
across every concurrent session. With several sessions committing into related repos, the
only way to tell who did what is inference from timing and content — and inference was
wrong three times out of three.

This nearly cost a working control: a safeguard was judged ineffective because the commits
proving it ran were attributed to the wrong session.

The fix is to write identity in explicitly at commit time — a session trailer — rather
than reconstruct it afterwards. Attribution that has to be inferred is attribution that
will be wrong under exactly the concurrency that makes it matter.

**Check next time a fleet runs concurrent sessions against shared repos:** a session
trailer must be installed in *every* repo, not the one where the work started. Attribution
with a blind half is worse than none, because the covered half reads as complete.

## Links

- relates-to: concurrent-sessions-on-shared-base-branch-race-2026-08-31
- relates-to: concurrent-session-pointer-drift-lesson-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
