---
id: egress-control-and-behavioural-isolation-are-different-control-classes-2026-09-01
type: ruling
status: candidate
source: "Hestia (privacy-domain challenger), 2026-09-01, adversarial panel against the security-arsenal plan; reasoning relayed, the workflow facts it rests on re-verified here"
project: fleet
tags: [egress, isolation, containment, fail-closed, control-design, r7]
supersedes: []
superseded_by: null
---

# Deferring behavioural isolation is defensible; deferring egress control is not, and conflating them hides that

## Body

A security plan refused to build automated isolation on anomalous behaviour, arguing there was no
staging to exercise it, no baseline defining "anomalous", and no on-call — and that a false
isolation would train operators to disable the control before the real event. **For behavioural
isolation that argument holds.**

It does not transfer to egress control, and the plan deferred both by never distinguishing them:

| | Behavioural isolation | Default-deny egress |
|---|---|---|
| Needs a learned baseline | Yes | **No** — the allowlist is declared |
| Needs staging to exercise | Yes | **No** — deterministic, testable offline |
| False-positive mode | A 03:00 production outage | A **build-time** failure on an undeclared destination |
| Acts in time | Needs a human | In-path, at line rate |

The asymmetry that decides it: **an outage is recoverable and bounded by duration; a disclosure is
monotonic and irreversible.** Once data reaches an external host, no confirmation, runbook or
subsequent isolation retrieves it. A control whose value is measured in seconds, gated behind a
human who is admittedly not on call, will reliably arrive after the event it exists to prevent.

By the Core's own standard — *an unperformed check is not a clean check* — a containment action
that cannot run without an absent human **has not run**.

**The rule:** integrity scanning may ship report-only and graduate. Containment ships blocking on day
one. They are different control classes and a plan that treats them as one will defer the wrong half.

## Links

- relates-to: hosted-ci-is-itself-an-r7-violation-for-a-patient-data-system-2026-09-01
- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
- relates-to: a-hunting-team-closes-the-adversarial-loop-2026-09-01
