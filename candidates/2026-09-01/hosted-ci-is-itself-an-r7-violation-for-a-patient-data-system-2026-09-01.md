---
id: hosted-ci-is-itself-an-r7-violation-for-a-patient-data-system-2026-09-01
type: finding
status: candidate
source: "Hestia (privacy-domain challenger), 2026-09-01, adversarial panel against the security-arsenal plan; reasoning relayed, the workflow facts it rests on re-verified here"
project: fleet
tags: [r7, containment, ci, hipaa, aci, egress, hestia]
supersedes: []
superseded_by: null
---

# Putting patient-adjacent code through hosted CI breaches the never-leaves constraint before any application code exists

## Body

All four GEO workflows declare `runs-on: ubuntu-latest` — GitHub-hosted, Microsoft-operated,
multi-tenant compute outside any hospital boundary. The security plan then routed **every**
requirement onto CI and named it "the enforcement floor."

For the Ambient Clinical Scribe, whose R7 is that patient information must never leave the hospital
system, that is a breach committed by the enforcement layer itself. On a hosted runner the source is
checked out, the dependency tree is resolved and installed, tests execute, and job logs are retained
by the provider. If any fixture, snapshot or seeded database carries real or realistic patient data,
R7 fails with **no attacker involved** — the CI system operating exactly as designed. Under HIPAA
that runner is a business associate handling ePHI without a BAA.

The same shape recurs across the toolchain: dependency and SAST vendors whose product *is* uploading
your manifest or source for analysis; a scanner action granted `issues: write` that files findings —
endpoint shapes, parameters, response evidence — into a durable GitHub Issue; artifact upload of scan
output.

**The rule this earns:** for a never-leaves system, every proposed control must answer *where does
this run, and what does it see?* before it is adopted. A control that improves integrity while
breaking containment is a net loss in this domain, and it will not look like one on a checklist.

## Links

- relates-to: egress-control-and-behavioural-isolation-are-different-control-classes-2026-09-01
- relates-to: stag-fleet-has-no-ci-so-the-plans-enforcement-floor-does-not-exist-2026-09-01
- relates-to: forty-four-sourced-legal-documents-none-lawyer-reviewed-2026-08-31
