---
id: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [git, silent-failure, heartbeat, monitoring, lock]
supersedes: []
superseded_by: null
---

# A 29-day-old git lock silently froze a repo, and the only symptom was a commit that never got pushed

## Body

A lock file left behind by an interrupted operation sat in a repository for 29 days. It
did not error, warn, or surface anywhere. The single visible consequence was an unpushed
commit that was a month old — noticed only because someone happened to look at it and
wonder why a month-old commit was still local.

This is the shape of the most expensive class of failure in this fleet: not a loud break,
but a loop that quietly stopped turning while everything downstream continued to assume it
was running. The elapsed time is the damage. A broken thing found in an hour is an
incident; the same thing found in 29 days has silently invalidated a month of assumptions
built on top of it.

**Check next time a recurring loop is built:** give it a heartbeat — something that fires
when the loop *stops*, not only when it fails. Staleness must be an alertable condition in
its own right. "No news" from an automated process is not good news; it is no news, and the
two are indistinguishable without a liveness check.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
