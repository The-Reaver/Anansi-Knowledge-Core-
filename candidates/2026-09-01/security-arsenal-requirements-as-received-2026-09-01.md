---
id: security-arsenal-requirements-as-received-2026-09-01
type: spec
status: candidate
source: "Relayed prompt, received 2026-09-01 — drafted by another AI assistant FOR the operator to forward (its closing line reads 'before you hand it off to Claude'), pasted twice in one message alongside the Hestia/Bayamanaco naming ruling; recorded here verbatim in substance so future sessions can search rather than recall"
project: fleet
tags: [security, hestia, bayamanaco, requirements, spec, relayed-prompt, provenance, arsenal]
supersedes: []
superseded_by: null
---

# The seven security-arsenal requirements, as received — searchable so nobody has to remember whether they were already sent

## Body

**Why this note exists.** The operator asked, twice in one session, whether a block of security
requirements "rang a bell." It had been sent 90 minutes earlier and already acted on. The answer to
*"did we already send this?"* should be a search, not a memory. This note is that search target.

**Provenance, stated exactly.** The text opens "Hey Claude" and closes *"Let me know if you want to
tweak any of the specific technical requirements before you hand it off to Claude!"* — so it was
**not written to a Claude session**. It was drafted by another AI assistant *for the operator to
forward*. Under the standing order of 2026-08-21, a relayed prompt from another agent is a
**proposal to scrutinise**, not an instruction to execute. That distinction earned its keep on first
contact: requirement 3 would have taken down production if implemented literally (see §Refusal).

**The stated intent**, in the operator's forwarded words: *"I don't want static security policies or
compliance checklists just sitting in a markdown file... If it's a security rule, it needs to be code
— automated guardrails, active pipeline triggers, and event-driven mechanisms that enforce the rules
systematically."* Plus an explicit delegation: *"If a specific implementation is going to bottleneck,
harm, or break what we already have running, I trust you to pivot and find a safer, smarter way to
enforce the intent of the rule."*

### 1. Automated "Fire Drills" — testing and validation

- **Vulnerability scanning.** Automated pipeline triggers scanning code and dependencies for known
  vulnerabilities on every push, **physically blocking the deployment** if a critical flaw is found.
- **Automated boundary testing.** Scheduled scripts acting as an automated pen-test / red team,
  actively pinging endpoints and testing authentication boundaries.

### 2. Active defence mechanisms — blue-team guardrails

- **Network segmentation.** Infrastructure-as-code (Terraform, Docker configs) strictly isolating
  services and environments, with hard barriers preventing lateral movement after a compromise.
- **System hardening.** Configurations that automatically strip or disable unused services, ports and
  default permissions across servers and containers.
- **Privilege-escalation and access monitoring.** Active event monitoring flagging unauthorised
  attempts to gain admin access or move laterally.

### 3. Event-driven incident response

- **Automated isolation.** Event-driven triggers that automatically isolate a container, service or
  endpoint on highly anomalous behaviour, acting as an automated first responder.

### Verbatim labels, preserved for exact-match search

Reproduced with the original capitalisation, spelling and punctuation, because the rest of this
note paraphrases and a paste of the original text would otherwise miss it:

```
1. Automated "Fire Drills" (Testing & Validation)
   Vulnerability Scanning
   Automated Boundary Testing
2. Active Defense Mechanisms (Blue Team Guardrails)
   Network Segmentation
   System Hardening
   Privilege Escalation & Access Monitoring
3. Event-Driven Incident Response
   Automated Isolation
```

Two sentences from the original, verbatim, as further search anchors:

> "I need to integrate a comprehensive arsenal of cybersecurity strategies directly into our
> governance architecture."

> "Analyze the current workspace, tell me how you plan to weave these into our existing governance
> structure without breaking it, and let's get to work implementing them."

### Where the response lives

`docs/specs/2026-09-01-security-arsenal-integration-plan.md` — the requirements mapped onto the
verified stack, sequenced wiring-first because 27 of 34 gates are unwired, with CI rather than git
hooks as the enforcement floor since a fresh clone has an empty `.git/hooks`.

### Refusal, recorded so it is not silently reversed

**Requirement 3 (automated isolation) was deliberately not implemented as written.** There is no
staging environment to exercise it, no baseline defining "anomalous", and no on-call. The ratified
precedent is that a false block trains people to override a control; a false *isolation* trains them
to disable it, and then it is absent for the real event. Replaced with: detect → alert → human, the
isolation action written and tested one command away, shadow-mode logging to produce the
false-positive rate as a number, and automatic action gated on staging existing plus that number
being acceptable. **Anyone reversing this should read that reasoning first.**

## Links

- relates-to: hestia-and-bayamanaco-enforce-security-as-code-not-policy-2026-09-01
- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
- relates-to: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
- relates-to: geo-pushes-straight-to-main-with-no-staging-environment-2026-08-31
- relates-to: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
