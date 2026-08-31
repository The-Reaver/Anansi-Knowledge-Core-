---
id: the-teachable-language-library-has-been-queued-and-unscoped-since-2026-08-03-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) dormant-area audit, 2026-08-31 — relayed by the operator into a recovery session; the audit itself ran against the local Knowledge Home and could not be re-run here"
project: fleet
tags: [language-library, dormant-area, unscoped, backlog, heartbeat]
supersedes: []
superseded_by: null
---

# The teachable language library has sat queued and unscoped for 28 days with zero commits, and nothing ever flagged it

## Body

Audited 2026-08-31. The teachable language workstream was queued **2026-08-03**. As of the
audit it remained unscoped, with **zero commits and no related content** anywhere. A note
recorded the same state at the 18-day mark; the audit found it unchanged at 23 days, and it
stands at 28 days from queueing to today.

The work is real and recorded. Nothing is lost. What is absent is any mechanism that treats
"queued and unscoped for four weeks" as a condition worth raising. The item's status was
only ever discovered by someone deliberately going to look, twice.

This is the same shape as the 29-day stale git lock: a thing that stopped, in a system with
no liveness check, found by inspection rather than by alert. The difference is only that a
backlog item stalling looks normal, which makes it harder to notice and easier to accept.

**Action this implies:** either scope it or explicitly park it with a date. An item that is
neither scoped nor parked consumes attention at every audit while producing nothing, and its
age keeps being rediscovered as if it were news.

## Links

- relates-to: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
