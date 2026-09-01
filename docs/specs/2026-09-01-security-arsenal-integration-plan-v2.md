# Security Arsenal — integration plan, v2

**Supersedes** `2026-09-01-security-arsenal-integration-plan.md`, which was rejected by three blind
reviewers (AJ: REJECT, Hestia: BLOCK, Bayamanaco: INADEQUATE) on independent grounds.
**Status: SUPERSEDED, 2026-09-01. Not adopted. Do not implement from this document.**
The operator ratified the Brain Trust slate on 2026-09-01 under Option A, which **split this plan**.
Its fleet half, with the panel's conditions applied and four items it did not contain, is now
`docs/runbooks/2026-09-01-phase-0a-security-remediation.md` (BINDING). Its R7 half is
`docs/briefs/2026-09-01-r7-containment-brief-UNSCHEDULED.md` (not work). This file is kept for the
audit trail only. Sections 1 (fact table) and 6 carry **no panel authority** and contain claims the
review refuted — see the decision record before citing anything here.
**Review outcome (2026-09-01):** the Brain Trust sat five seats and rejected I1 (adopt as written) 3-2
and I5 (self-hosted runners) 3-2, passed I2/I3/I4/I7 with binding conditions, passed I6 4-1, and
rejected its own composition 5-0. A separately-run cold security architect returned 13 findings, three
of them refuting factual claims in section 1 of this document. See
`docs/decisions/BRAIN_TRUST_DECISION_RECORD_2026-09-01.md`. A v3 is owed against that record.
**Verification stamp:** Stag-Fleet `aad9650`, The-Geo-Suite- `73a58ce`. Both refs check out —
v1 cited `a428c6a`, which is not a valid object.

---

## 0. Compliance

*Present because Mandate 2 is a hard gate: every build spec ships a compliance section from the
first spec. v1 had none, on a patient-data spec, and nothing caught it because
`mandates_gate.py` scans only `<stag-fleet>/specs/` non-recursively.*

**Privacy.** This plan governs a system whose defining requirement (R7) is that patient information
never leaves the hospital system. Every control below is classified as *integrity* or *containment*
(§3) and no control is adopted without answering: **where does it run, and what does it see?** Any
control that transmits code, dependencies, logs or findings off-premises is a containment breach
regardless of its integrity benefit. Recording consent, audio at rest and in transit, and the
consent event log are first-class assets here (§6), not workflow details.

**Accessibility.** This plan produces no user interface. Where it produces operator-facing output —
gate failures, alerts, the war-game record — that output must be readable in a terminal without
colour as the sole signal, and must state the remedy, not only the fault.

---

## 1. What the stack actually is

Verified at the refs above. **v1's headline figure — "34 gates, 7 wired" — was wrong, and was copied
from a candidate note in a document claiming inspection.** Correcting it properly means reporting
that the fleet's two instruments disagree:

| Source | What it says |
|---|---|
| `gate_coverage_report.py` (the fleet's own tool) | 33 gates scanned — live 9, hook-only 0, tested-only 21, **orphaned 3** (`branch_name_gate`, `hook_parity_gate`, `stale_stage_guard`) |
| `scripts/hooks/install-git-hooks.sh` (read directly) | references **7** gates, including `hook_parity_gate` and `stale_stage_guard` |

**The tool calls two gates orphaned that the installer demonstrably wires.** It is not reading the
installer. So the fleet has no trustworthy count of its own coverage, and *that* is the Phase 0
finding — not a number. **Work item: make `gate_coverage_report.py` read the installer, then publish
the per-gate table and restate scope against it.**

Other facts, each verified directly:

| Fact | Consequence |
|---|---|
| **Stag-Fleet has no `.github` directory — no CI at all** | v1's enforcement floor did not exist in the repo v1 targeted. AJ's 2026-08-09 audit already carried this as recommendation #1. |
| GEO: `deploy-verify.yml` runs `on: push: [main]` with `RAILWAY_TOKEN`, injecting the live prod env | One unreviewed push exfiltrates every production secret. |
| GEO has **no PR gate**; Railway auto-deploys before CI runs | A blocking PR check enforces nothing where nothing opens PRs. |
| All GEO scanners `continue-on-error` / `fail_action: false` | The scanning surface is a dashboard, not a barrier. |
| `nuclei-action@main` — mutable branch ref | Upstream code executes in a repo holding prod secrets. |
| `requirements.txt` pins 2 of 10; no lockfile; Railway rebuilds on deploy | Supply chain reaches prod without repo access. |
| `.git/hooks` has no active hooks in a fresh clone | Hook enforcement is opt-in per clone. |
| `.pre-commit-config.yaml` declares `detect-secrets` + `bandit` against **3 paths that do not exist** | Declared security tooling is mis-wired, not merely unwired. |
| `backend/Dockerfile`: no `USER`, ships `build-essential`, no `.dockerignore`, shell-form `CMD` | The running production image is unhardened. |
| `omar_security_gate.py` exists, tested, **never wired** (`verify.py:529` says so) | The fleet's one built security gate is inert. |
| No staging — and `security-scan.yml` prices one at **under $3/month** | Its absence is a decision, not a constraint. |

---

## 2. Principles this plan is bound by

**Stated honestly, because v1 called these "ratified precedent" when they are not.** All three are
`status: candidate`, authored 2026-08-31 by the same session that wrote v1. They are cited here as
**candidate reasoning the author finds persuasive**, not as governance. If they are to bind, ratify
them first.

1. A false block destroys a gate's authority and takes its true positives with it. *(candidate)*
2. An unperformed check is not a clean check; "could not run" is a failure. *(candidate)*
3. Safeguard existence does not imply invocation. *(candidate)*

Genuinely ratified and load-bearing here: `2026-08-06-breakers-gauntlet-four-breaker-types-and-rules`
and `2026-08-06-tyr-never-certifies-itself-aj-plus-second-breaker-do`.

---

## 3. The correction that reorganises everything: two control classes

v1's central error was not a missing control. It was a missing **distinction**.

| | **Integrity** controls | **Containment** controls |
|---|---|---|
| Question answered | Is the code sound? | Did bytes leave, and to whom? |
| Needs a learned baseline | Sometimes | **No** — the allowlist is declared |
| Needs staging to exercise | Often | **No** — deterministic, testable offline |
| False-positive mode | A blocked commit | A **build-time** failure on an undeclared destination |
| Failure is | Recoverable, bounded by duration | **Monotonic and irreversible** |
| Ships | Report-only, then graduates | **Blocking from day one** |

Every control in v1 was an integrity control. R7 is a containment property. **A plan made entirely
of integrity controls does not address R7 by one requirement** — it makes existing infrastructure
trustworthy, which is a different problem wearing the same words.

---

## 4. Phases

### Phase −1 — Data classification. Blocks everything.
Every repo, path, service and dependency tagged **Red** (may touch PHI or audio), Amber, or Green,
in a machine-checkable manifest. Nothing Red is built, scanned, or deployed on a surface without an
executed BAA. Without this, no later phase can tell which rules apply where.

### Phase 0 — Stop the bleeding. Days, not weeks.
Not new architecture. Closing what is verifiably open:
1. **Branch protection on `main`** in both repos — required PR, required review, required status
   check. Free, server-side, un-bypassable per clone. *The single largest enforcement hole, and v1
   diagnosed it and prescribed nothing.*
2. **CODEOWNERS on `.github/workflows/`** so the file holding the deploy token cannot be edited in an
   unreviewed push.
3. **Scope the deploy credential** — OIDC short-lived, and stop materialising the whole prod env
   into a shell.
4. **Hash-locked dependencies**, built from the lockfile only. SHA-pin every third-party action.
5. **Wire `omar_security_gate`** — the fleet's one built security gate.
6. **Fix or delete the three broken `.pre-commit-config.yaml` paths.**
7. **The four `Dockerfile` defects.**
8. GitHub secret-scanning **push protection** — free, server-side, not opt-out-able per clone.

### Phase 0.5 — Stand up CI in Stag-Fleet.
It has none. Everything after this depends on it existing.

### Phase 1 — Containment. Blocking from day one.
**Default-deny egress** at the boundary, with a named allowlist justified per entry: container
registry, base images, telemetry-capable dependencies, error reporting, backup destination, log
aggregation, model APIs. Plus an **egress gate** failing the build on any call path from Red code to
a frontier model provider. No observation period — see §3.

### Phase 2 — Integrity scanning. Report-only, with a date.
Dependency + SAST scanning. Report-only for a **named window ending on a calendar date with a named
owner**, then blocking automatically absent a recorded written extension. v1 said "two weeks" with
no owner, no date and no forcing function, which is how a control stays report-only forever.

**Every engine named, with a BAA and written proof of local-only analysis, before it touches Red
code.** "Could not obtain that proof" is a failure, not a pass.

### Phase 3 — Hardening and segmentation.
Minimal base images, explicit port allowlists, non-root containers, no default credentials.
`terraform plan` in CI; `apply` stays human. **R6 transport design** — mutual TLS on hospital-issued
PKI or private interconnect, no vendor-terminated TLS on the path — specified before this is written.

### Phase 4 — Detection, with numbers.
Privilege-escalation and lateral-movement monitoring. **MTTD and MTTR targets set and measured**, per
the hunting-team ruling; without them the detect-and-alert substitute has no safety case at all.

### Phase 5 — Behavioural isolation.
Gated on: staging exists, a measured false-positive rate, `numReplicas > 1`, and a named responder.
**Each of those is now a dated remediation item in Phase 0–3, not a permanent excuse.**

---

## 5. What is refused, and what is not

**Behavioural isolation on unbaselined production is still deferred** — and this time the four
conditions that justify deferring it are scheduled for removal rather than treated as permanent:
staging is priced under $3/month, the baseline is what Phase 4's shadow mode produces,
`numReplicas: 1` is a config line, and "no on-call" is refuted by the substitute depending on a human.

**Egress control is not deferred.** It needs no baseline, no staging, and acts in-path. §3 explains
why the same caution does not transfer.

---

## 6. Assets v1 omitted entirely

Audio at rest on capture devices (encryption, key custody, buffer TTL, wipe-on-loss); audio in
transit; the **consent event log** as a Red asset; a **fail-closed pre-recording consent interlock**,
blocking from day one, since recording without consent in an all-party state is criminal exposure;
enforced retention and destruction; audit logging (tamper-evident); encryption at rest and in
transit with key management; RBAC, least-privilege and break-glass; backup and restore; and an
incident-response path with a **breach-notification clock**.

Also: **a rule on what may be written into logs.** Every control here generates logs, and the Core
already records that "no PII stored" scoped to one store is not "no PII logged."

---

## 7. Hestia and Bayamanaco

Same duties, independently, required to **fail differently** — different engines, rule sets, and
model families. Neither certifies its own work.

**Stated honestly:** the ratified "independent of the builder and the fleet" rule they borrow is
conditioned on independence *from* the fleet, and these two are fleet agents enforcing on the
fleet's own work. That is a weaker independence than the Breakers have, and the difference should
be acknowledged rather than assumed away.

---

## 8. Decisions — menus with recommendations

*Per mandate `advise-with-options-and-recommendation`: an open question with no menu and no
recommendation is a defect, not neutrality. v1 ended with four bare questions.*

**8.1 Does Phase 0 block Phase 1?**
(a) Yes, sequential — safest, slowest. (b) **No, parallel — Phase 0 is settings changes and small
fixes; containment design is thinking work.** (c) Phase 1 first — leaves the front door open.
→ **Recommend (b).**

**8.2 Report-only window for integrity scanning?**
(a) Blocking day one — accurate but noisy, and noise disarms the control. (b) **Two weeks, named
owner, automatic escalation on a calendar date.** (c) Indefinite report-only — the failure mode.
→ **Recommend (b).** Containment is unaffected; it blocks day one regardless.

**8.3 Self-hosted runners for Red repos?**
(a) **Self-hosted inside the boundary** — cost and maintenance, satisfies R7. (b) Hosted with a BAA
— cheaper, depends on R7 being contractual not physical. (c) Red code never enters CI — safest,
sacrifices automated checking where it is most needed.
→ **Recommend (a), contingent on 8.4.**

**8.4 Is R7 physical or contractual?**
(a) **Ask the hospital's security lead** — one conversation, moves the project's difficulty by an
order of magnitude. (b) Assume physical — safe, expensive, possibly unnecessary. (c) Assume
contractual — cheap, and wrong is catastrophic.
→ **Recommend (a), before any architecture is chosen.** This is the cheapest high-value action in
the whole programme and it costs one phone call.

---

## 9. Review path

Per `review-depth-reversibility-test`, this class of document needs a **cold** reviewer and a Brain
Trust panel — *neither being the session that wrote it*, and, per the panel's own finding, **no seat
this document creates**. So: not Hestia, not Bayamanaco. AJ may audit, since AJ predates this
document and holds no seat.

---

## 10. What this plan still does not cover

Stated so the gaps are visible rather than implied: the ACI's own application architecture; key
management design beyond naming it; vendor selection; the hospital's own network topology, which is
unknown here; and cost. **Silence is not scoping — these are open, not handled.**
