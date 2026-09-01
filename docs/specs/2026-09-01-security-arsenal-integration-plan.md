# Security Arsenal — integration plan for Hestia and Bayamanaco

**Status:** proposal, for adversarial review by AJ, Hestia, Bayamanaco, then the Brain Trust.
**Nothing here is implemented.** Written 2026-09-01 against the real stack, verified by inspection.

---

## 1. What the stack actually is

Verified in `The-Reaver/Stag-Fleet` @ `anansi-home-dashboard` and `The-Reaver/The-Geo-Suite-` @ `a428c6a`:

| Fact | Consequence for this plan |
|---|---|
| **34 gates exist, 7 are wired** | The bottleneck is wiring, not gate count. Adding gates makes it worse. |
| Hooks: `pre-commit`, `commit-msg`, `prepare-commit-msg` declared; **`pre-push` installed by hand, undeclared** | Hook-based enforcement is per-machine and invisible to a fresh clone. |
| `.git/hooks` is **empty in a fresh clone** | Every hook-based control is off by default. CI is the only enforcement that cannot be opted out of. |
| GEO has 4 workflows: `tests.yml`, `deploy-verify.yml`, `security-scan.yml`, `cfr-watch.yml` | There is already a CI surface to extend. Stag-Fleet's CI surface needs checking. |
| **No staging environment** — stated in `security-scan.yml` itself | Anything that acts on production acts on the only environment. |
| GEO **pushes straight to `main`, no PR gate** | A blocking check on PRs enforces nothing if nothing opens PRs. |
| Secret scanner produces false positives on `flask-`, `task-`, `risk-` | A noisy blocker trains the override reflex. Ratified precedent. |
| `.claude/settings.json` declares **zero hooks** | Session-level automation lives in one machine's user settings. |

## 2. The three rulings this plan is bound by

1. **A false block destroys a gate's authority and takes its true positives with it.** So no new control ships in blocking mode on day one.
2. **An unperformed check is not a clean check.** So every control fails closed, and "could not run" is a failure, never a pass.
3. **Safeguard existence does not imply invocation.** So every control here must be provably *invoked*, not merely present — the installed-hook gate's own standard.

## 3. Where each requirement lands, and where I am pivoting

| # | Requirement | Where it goes | Pivot from the literal ask |
|---|---|---|---|
| 1a | Dependency + code vulnerability scanning, blocks deploy on critical | **CI workflow**, not a git hook | Hooks don't survive a fresh clone. CI is the enforcement layer. |
| 1b | Scheduled boundary / auth testing (automated red team) | **Scheduled CI job**, against a disposable target | **Not against production.** See §4. |
| 2a | Network segmentation as IaC | **Terraform/compose in Stag-Fleet**, staged behind a plan-only gate | Apply requires a human. `terraform plan` in CI, `apply` never automatic. |
| 2b | System hardening — strip unused services, ports, default permissions | **Container build stage + a hardening gate** | Enforce at image build, where it is reversible, not on running hosts. |
| 2c | Privilege-escalation / lateral-movement monitoring | **Detection and alert only** | See §4 — no automatic action. |
| 3 | Event-driven automated isolation | **Deferred. Detect → alert → human confirms.** | See §4. This is the one I am refusing to build as specified. |

## 4. The one requirement I am not implementing as written, and why

**Automated isolation of a container, service or endpoint on anomalous behaviour.**

Against this stack, as it exists today, that is a self-inflicted outage generator:

- **There is no staging.** The isolation logic cannot be exercised anywhere but production. Its first real run would be its first run.
- **The detector has no baseline.** "Highly anomalous" needs a learned normal. There is none, so the first weeks are false positives — and each one takes down a live service for a paying customer.
- **The fleet's own ratified precedent says this backfires.** A false block trains people to override the control. A false *isolation* trains them to disable it, and then it is not there for the real event.
- **No on-call.** An automatic isolation at 03:00 with nobody watching converts a possible intrusion into a certain outage.

**What I will build instead, which satisfies the intent:**

1. **Detect and alert**, with the isolation action **written, tested, and one command away** — a runbook plus a script, human-triggered.
2. **Log what it *would* have done**, in shadow mode, for a defined observation window. That produces the false-positive rate as a number rather than a guess.
3. **Flip to automatic only when two conditions hold**: a staging environment exists to exercise it, and the shadow-mode false-positive rate is measured and acceptable.

That is not a softer version of the requirement. It is the only version that ends with the control still enabled a month later.

## 5. Sequence — wiring before building

**Phase 0 — make the existing battery real.** Nothing new. Wire or retire the 27 unwired gates; add `pre-push` to the installer so it stops being one machine's secret; give every gate a `fail-open`/`fail-closed` docstring plus a test. Until this is done, new controls inherit the same invisibility.

**Phase 1 — CI as the enforcement floor.** Dependency + SAST scanning on every push, **report-only for two weeks**, then blocking on critical. Report-only first is not timidity; it is how the false-positive rate gets measured before the control earns the right to block.

**Phase 2 — hardening at build time.** Minimal base images, explicit port allowlists, no default credentials, enforced by a gate that fails closed on an unparseable config.

**Phase 3 — segmentation as code.** `terraform plan` in CI on every change; `apply` stays human. Hard barriers between services so a compromise of one does not reach the next.

**Phase 4 — detection.** Privilege-escalation and lateral-movement monitoring, alerting only.

**Phase 5 — isolation, gated on §4's two conditions.**

## 6. How Hestia and Bayamanaco divide this

They perform the same duties, independently, and must **fail differently** — the rule already ratified for the Breakers. Concretely: different scanning engines, different rule sets, and ideally different model families, so a blind spot in one is not a blind spot in both. A finding either raises alone is a finding. Agreement is corroboration, not a requirement for action.

Neither certifies its own work: the ratified `tyr-never-certifies-itself` principle applies to them as it does to TYR.

## 7. What I could not do, and why

I have **read-only** access to `Stag-Fleet`. Every control above must land in that repository, so this document is a plan and not a patch. Handing it to a session with write access — the architecture session — is the next step, not more drafting here.

## 8. Open questions for the panel

1. Is `report-only for two weeks` the right observation window, or does the ACI patient-data context demand blocking from day one and accepting the false-positive cost?
2. Should Phase 0 (wiring the 27 gates) genuinely block Phase 1, or run in parallel?
3. Does refusing to build automated isolation as specified violate the operator's intent, or honour it? §4 is the argument; the panel should try to break it.
4. Two enforcers doing identical work is duplicated cost. What is the evidence that the pair catches materially more than one well-configured enforcer?
