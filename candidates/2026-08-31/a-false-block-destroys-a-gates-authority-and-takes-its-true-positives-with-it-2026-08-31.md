---
id: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [gates, false-positive, governance, override, tier-gate, secret-scanning]
supersedes: []
superseded_by: null
---

# A false block is more dangerous than a missed one, because it trains the override reflex

## Body

A **false block** is a gate stopping a commit that was actually fine. The tier gate
refused a commit because it classified `governance/mandates.json` — a declarative
registry, effectively config — as "implementation code". Nothing was wrong with the
commit; the gate was wrong about the file.

Why this is dangerous rather than merely annoying: every false block teaches the operator
the gate is unreliable. After a few, they stop reading its output and reach for the
override reflexively. Then the day it blocks something real, they override that too —
without looking, because that is the trained response. A false-positive-prone gate does not
just waste time; **it destroys its own authority and takes its true positives down with
it.** An override that becomes routine has stopped being an override.

The same pattern appeared in the secret scanner, where `flask-`, `task-` and `risk-`
matched as API keys — and the Core already records a session reporting "7 keys" when 5
were kebab-case slugs.

The correct response in the moment was taken: `--no-verify` was refused twice and the
commits were split instead. But the durable fix is to repair the classification, not to
build tolerance for overriding.

**Check next time a gate blocks:** if the block was wrong, that is a defect with the same
priority as a miss — file it, don't just work around it. Count overrides; a rising
override rate is the leading indicator that a gate is about to fail silently.

## Links

- relates-to: per-file-verification-caught-a-prune-list-that-would-have-blinded-the-secret-scanner-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
