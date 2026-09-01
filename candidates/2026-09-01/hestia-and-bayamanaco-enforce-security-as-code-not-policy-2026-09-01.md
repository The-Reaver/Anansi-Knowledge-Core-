---
id: hestia-and-bayamanaco-enforce-security-as-code-not-policy-2026-09-01
type: ruling
status: candidate
source: "Operator directive, 2026-09-01 — Abad named the privacy-domain agent Hestia and its counterpart Bayamanaco, and specified the security arsenal they must enforce as active code rather than policy documents"
project: fleet
tags: [hestia, bayamanaco, privacy-domain, security, agents, guardrails, naming]
supersedes: []
superseded_by: null
---

# The privacy-domain seat is named Hestia, paired with Bayamanaco, and both enforce security as running code rather than policy documents

## Body

Operator ruling, 2026-09-01. The **PrivacyDomain** agent is renamed **Hestia**. A second agent
performing the same duties is code-named **Bayamanaco**. They are paired deliberately, on the same
principle already ratified for the Breakers: two independent enforcers that **fail differently**,
so neither is a single point of trust.

Their remit is stated as a rejection of the fleet's current default: *"I don't want static security
policies or compliance checklists just sitting in a markdown file... If it's a security rule, it
needs to be code — automated guardrails, active pipeline triggers, and event-driven mechanisms."*

**This is the same defect this Core has now recorded four times**, applied to security: a mandate
naming an enforcement mechanism that does not exist, a gate battery 34 built and 7 wired, hooks
that do not survive a fresh clone, and an approved retrofit nobody ran. A security policy in a
markdown file is a safeguard whose existence does not imply invocation. Hestia and Bayamanaco exist
to make security the exception to that pattern rather than its next instance.

**Seven required capabilities**, as specified: dependency and code vulnerability scanning that
blocks deployment on a critical finding; scheduled automated boundary and authentication testing;
network segmentation as infrastructure-as-code with hard barriers against lateral movement; system
hardening that strips unused services, ports and default permissions; privilege-escalation and
lateral-movement monitoring; and event-driven automated isolation of a compromised container,
service or endpoint.

**The operator explicitly delegated the "how"**, with a standing instruction to pivot where an
implementation would bottleneck, harm, or break what is already running. That delegation is
load-bearing: several of these tactics are actively dangerous against a stack with no staging
environment, and the intent must be enforced by a safer route rather than implemented literally.

## Links

- relates-to: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
- relates-to: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
- relates-to: the-breakers-are-standing-attackers-run-as-periodic-war-games-2026-09-01
- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
