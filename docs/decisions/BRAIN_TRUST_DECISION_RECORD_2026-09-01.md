# BRAIN TRUST DECISION RECORD — 2026-09-01

**Docket:** `docs/specs/2026-09-01-security-arsenal-integration-plan-v2.md` (v2), eight issues.
**Seated:** Elijah (product and delivery), Orlok (build and execution), Celestina (architecture), Amadeus (framing), Oluwole (research and sourcing).
**Not seated:** AJ (barred by `AJ/AJ_HARDWIRING.md` — "Holds no Brain Trust seat, no vote, no build or Orlok role, ever"), TYR (verification and risk), PrivacyDomain/Hestia (privacy and compliance).
**Separate cold reviewer:** one senior security architect, no fleet context, run outside the panel per mandate `review-depth-reversibility-test`. Not a seat and holds no vote.
**Procedure followed:** blind independent pass (five parallel agents, no seat could see another), then chair synthesis, then majority vote. Nothing here is final until the operator ratifies.

---

## 1. Per-seat vote matrix

| # | Issue | Elijah | Orlok | Celestina | Amadeus | Oluwole | Result |
|---|---|---|---|---|---|---|---|
| I1 | Adopt v2 as the security architecture for the fleet **and** the Ambient Clinical Scribe | REJECT | AWC | AWC | REJECT | REJECT | **REJECT 3–2** |
| I2 | Integrity/containment class distinction; containment blocks day one, integrity report-only | AWC | AWC | AWC | AWC | AWC | **PASS WITH CHANGES 5–0** |
| I3 | Run Phase 0 parallel with Phase 1 | AWC | AWC | AWC | AWC | AWC | **PASS WITH CHANGES 5–0** |
| I4 | Integrity scanning report-only for two weeks, named owner, dated auto-escalation | AWC | AWC | AWC | AWC | AWC | **PASS WITH CHANGES 5–0** |
| I5 | Self-hosted CI runners inside the hospital boundary for Red repos | AWC | REJECT | AWC | REJECT | REJECT | **REJECT 3–2** |
| I6 | Ask the hospital security lead whether R7 is physical or contractual, before choosing architecture | APPROVE | APPROVE | APPROVE | AWC | APPROVE | **PASS 4–1** |
| I7 | Behavioural isolation stays deferred; four conditions become dated remediation items | AWC | AWC | AWC | AWC | AWC | **PASS WITH CHANGES 5–0** |
| I8 | Proceed at five seats (no privacy lens, no verification-and-risk lens) | REJECT | REJECT | REJECT | REJECT | REJECT | **REJECT 5–0 — ESCALATED** |

AWC = approve-with-changes. No abstentions. No true ties.

---

## 2. Passed clean

**I6 — Settle R7 with the hospital's security lead before any architecture is chosen.** 4–1, the only issue on the docket with a straight-approve majority, and the only one every seat called high-leverage. Two caveats attach without changing the verdict:

- **Orlok:** it is not "one phone call," because no design-partner site exists yet. The action is *get a site*, then ask.
- **Amadeus (the dissent, recorded as AWC):** the question is not this document's. `PROJECT_BRIEF_AMBIENT_CLINICAL_SCRIBE_2026-08-30.md` §4 already names the physical-vs-contractual distinction "the highest-leverage open question in the whole project" and §8 already names it "the single cheapest next action." Restating a recorded next action two days later is not performing it. Amadeus approves it as a **standalone operator action item with a date, routed outside this plan**, and rejects any construction where fleet security remediation waits on the hospital's answer.

The chair adopts Amadeus's routing: I6 is ratified as an operator item, not as a gate inside the security plan.

---

## 3. Passed with changes — the conditions are the decision

### I2 — control-class distinction (5–0 AWC)

Every seat accepted the distinction — an outage is recoverable and bounded by duration, a disclosure is monotonic — and every seat independently found the same defect: **v2 misfiles its own controls into the class it just defined.**

The §3 table justifies "containment blocks day one" with a false-positive mode of *"a build-time failure on an undeclared destination."* §4 Phase 1 then ships *"default-deny egress at the boundary… acts in-path."* Those are two different controls, and the runtime one inherits a safety case built for the build-time one. Celestina puts it as a static call-path analyser sitting in the containment class where it does not belong; Elijah notes a build-time static check cannot know whether bytes left, so by the table's own first row it is an integrity control.

Elijah supplies the fleet's own empirical refutation of "blocking from day one": `prepush.py` exited RED at three minutes, and the recorded conclusion was that *"wiring it naively would have blocked every push and been bypassed with `--no-verify` within a day."* Orlok supplies the substrate objection: GEO runs on Railway, a PaaS with no customer egress firewall — both `railway.json` files are eight lines of healthcheck config — so there is no boundary to default-deny at.

**Conditions (binding on ratification):**
1. Split Phase 1 into two controls. The **build-time egress gate** (fail the build if Red-classified code has a call path to a frontier provider) ships blocking day one — it costs nothing today because zero Red code exists. The **runtime default-deny boundary** does not inherit that safety case.
2. The runtime allowlist runs in observe mode until the destination inventory is *enumerated and read once* across both repos — registry, base images, telemetry-capable dependencies, error reporting, backup, log aggregation, model APIs, and Railway's own build-time fetches. Enumerating that list is the learned baseline the document claims it does not need.
3. The runtime control does not go blocking before a staging environment exists (see I7 condition 2).

### I3 — Phase 0 parallel with Phase 1 (5–0 AWC)

Parallel is right. **The stated reason is false.** v2 §8.1 justifies parallelism by calling Phase 0 "settings changes and small fixes"; between them Elijah, Orlok and Oluwole identified three to four of the eight items as engineering with a live blast radius on the revenue product's only deploy path:

- **Item 3** (OIDC, stop materialising the prod env into a shell): Railway issues project tokens, not OIDC federation. `railway run --service … -- python scripts/deploy_verify.py --check-env` *is* the mechanism; injecting the live environment is what makes `--check-env` compare against reality. That gate caught four production config bugs 985 green unit tests missed. As written, item 3 reads "redesign or delete the one gate that has actually caught a production defect."
- **Item 4** (dependency pinning): this is GEO's `S-34b`, recorded **open and blocked on tooling choice** at `master-todo.md:225`.
- **Item 5** (wire `omar_security_gate`): see the chair's note — it is not a one-liner.
- **Item 7** (Dockerfile defects): includes a deliberate, documented shell-form `CMD`; see I3 condition 4.

Two further sequencing bugs, found by Amadeus and Celestina independently:
- §4 opens *"Phase −1 — Data classification. Blocks everything."* Read literally, a fleet-wide Red/Amber/Green PHI manifest — for data that exists in neither repo — now sits upstream of turning on branch protection. The document's own §8.1 answer contradicts its own phase list.
- Phase 0.1 requires a "required status check"; Phase 0.5 is "stand up CI in Stag-Fleet. It has none." Stag-Fleet has no `.github` directory. There is no check to require.

**Conditions (binding on ratification):**
1. Strike "blocks everything" from Phase −1. Phase −1 does not gate Phase 0, and is deferred entirely until the ACS is scheduled.
2. Split Phase 0 into **0a** — branch protection, CODEOWNERS, push protection, wire `omar_security_gate` correctly, delete the three dead `.pre-commit-config.yaml` paths — hours, this week, no production risk; and **0b** — items 3, 4 and 7, which get slice numbers in `master-todo.md` and land inside GEO's Phase 1, not "in parallel" by a second team that does not exist.
3. In Stag-Fleet, Phase 0.5 precedes the required-status-check half of Phase 0.1. Required-PR-and-review can land immediately.
4. Phase 0 item 7 drops the shell-form `CMD` change. It carries a nine-line comment explaining it exists so `$PORT` expands at container start per Railway's manifest; "fixing" it breaks the healthcheck. Dropping `build-essential` is deferred behind a staging environment because of the `psycopg`/`cryptography`/`weasyprint` wheel builds. `USER` and `.dockerignore` proceed — and cover **both** `backend/Dockerfile` and `frontend/Dockerfile`, which the plan does not count.

### I4 — report-only window with dated auto-escalation (5–0 AWC)

The mechanism is right and **the document contains no instance of it.** v2 convicts v1 of "two weeks with no owner, no date and no forcing function, which is how a control stays report-only forever," then writes "a named window ending on a calendar date with a named owner" and names nobody and sets no date. That is v1's defect restated as a requirement rather than fixed.

Orlok adds the fleet's demonstrated failure mode from `reports/STAG_BRAIN_TRUST_LEDGER.md`: `bink_golden_dataset_runner.py` was built, correct, and its judge step **sat unrun for six-plus weeks with a live API key.** Elijah adds the unmodelled interaction: Phase 0's required status check plus a dated auto-escalation hands a third-party CVE feed the power to stop GEO shipping on a date nobody is rostered to watch.

**Conditions (binding on ratification):**
1. The owner's name and the escalation date appear in the document before adoption. The panel's expectation is that the named owner is the operator, said so explicitly.
2. The escalation is **a check that runs** — a scheduled job that reads a date and flips the flag — not a calendar note. If the escalation is not code, this is a policy in a markdown file, which is the thing the operator's directive rejects.
3. The clock starts on the **first green run against the real target**, not on adoption (Celestina).
4. Escalation covers only findings observed inside the window, not all future publications, and carries a declared severity scope (Elijah, Celestina).
5. The escalated gate is not wired into `main`'s required checks until staging exists, or it ships with a logged single-operator override.

### I7 — behavioural isolation deferred, conditions become dated items (5–0 AWC)

The deferral is sound on the merits. The sentence that distinguishes it from v1's permanent excuse is not.

§5 states the four conditions "are scheduled for removal rather than treated as permanent"; §4 Phase 5 states *"Each of those is now a dated remediation item in Phase 0–3."* Checking Phases 0 through 3: staging appears nowhere as a work item (only as a price in §5); `numReplicas > 1` appears nowhere; a named responder appears nowhere; only the measured false-positive rate has a home, and it is Phase **4**. **No phase in the document carries a date at all.**

Two of the four are also mispriced. `numReplicas: 1` is not "a config line": `backend/app/services/worker/outbox.py` ships `InMemoryOutboxStore` and `InMemoryDedupStore` and nothing else, so a second replica gives two processes with two private dedup sets — that is a build item already sitting in GEO's Phase 5. "Staging at under $3/month" is a compute figure lifted from a code comment in `security-scan.yml`; the work is a second Railway environment, a cloned Supabase project, and keeping the two in sync.

**Conditions (binding on ratification):** each of the four conditions gets a slice number in `master-todo.md`, an owner, an hours estimate and a date — or the claim in Phase 5 is deleted and the document says plainly that they remain undated. Celestina flags the fourth (a measured false-positive rate) as a data dependency that will quietly stay a permanent excuse unless its date is the date the measurement starts.

---

## 4. Rejected

### I1 — adopt v2 as the security architecture for the fleet **and** the ACS. REJECT 3–2.

The two AWC votes (Orlok, Celestina) and the three rejections agree on the substance and differ only on whether it is fixable in place. **All five seats say: split the document.**

- **The bundle is the objection.** Roughly two-thirds of v2 is keyed to R7 and therefore to the scribe: Phase −1's PHI classification, Phase 1's default-deny egress, Phase 3's `terraform plan` against IaC that exists in neither repo, and §6's consent interlock, audio-at-rest key custody and breach clock. The ACS brief states in its own §8 that the project is "**Not started. Not scheduled**." Adopting a scribe security architecture is how a frozen project acquires a live workstream, a named owner and a claim on hours without anyone voting to start it. §8.8 of that brief is the governing instruction and v2 does not cite it once.
- **Celestina, on the architecture:** it is not an architecture for the ACS at all — no data-flow model, no trust-boundary model, no key-custody model — and §10 concedes it.
- **Orlok:** the ACS half is unbuildable as written, because Phase −1's own BAA rule disqualifies every surface this fleet owns.
- **Oluwole, on sourcing:** v2 silently widens R7 from "patient information" to "code, dependencies, logs or findings" with no authority for the widening; it contains one file citation that does not resolve and one false repo claim; and its load-bearing §3 is an uncited reproduction of a candidate note written the same day.
- **Amadeus, on framing — the finding the chair considers the most important on this docket.** v2 answers *"what security programme does a never-leaves-the-hospital patient-data system require?"* It was asked *"how do we weave a security arsenal into our existing governance architecture without breaking what is already running?"* The cost of that substitution is visible in what the plan omits: `BRAIN_TRUST_DECISION_RECORD_2026-08-27.md` records that `/sites/pipeline` **shipped a live cross-tenant vulnerability on 2026-08-23** — it returned every agent's sites to every agent — that the first fix was itself wrong, that `audit_results` has no tenant column, that its only RLS policy is `is_operator()`, and that `SupabaseAuditResultsRepository` reads through `get_supabase_admin()`, which bypasses RLS by design (confirmed at `backend/app/core/supabase_client.py:68`). That is the one security failure this fleet has actually experienced, in the one live product with real clients. Phases −1 through 5 contain supply chain, CI, egress, container hardening, segmentation, detection and isolation. **Not one control addresses tenant isolation or authorization.**

**What the panel would adopt instead, unanimously in substance:** Phase 0a as a narrow remediation ticket list against the two repos that exist, today, with no R7 vocabulary attached — **plus a new Phase 0a item: tenant-isolation and authorization review of `audit_results` and the `list_pipeline` ownership filter**, which outranks every other item on realised harm. Everything R7-shaped is filed as an unscheduled security brief sitting behind GEO, exactly where the operator has twice placed the scribe.

### I5 — self-hosted runners inside the hospital boundary. REJECT 3–2.

Both AWC votes are "correct answer, unratifiable today," so the panel is closer to unanimous than the count suggests.

- **The document argues with itself.** §8.3 recommends self-hosted runners "contingent on 8.4," and §8.4 says answer 8.4 "before any architecture is chosen." Recommending (a) contingent on an open question is still choosing.
- **There are zero Red-classified repos**, no hospital, and no design-partner site. This is procurement against a hypothesis.
- **Orlok, decisively:** self-hosted runners move *execution* inside the boundary and leave the *repository* — source, history, issues, artifacts, and the sixteen baselined credential-shaped findings in `research/knowledge-home/raw/` — on Microsoft-operated infrastructure. If R7 is physical, the containment breach has already happened at `git push`. Operationally it needs ephemeral per-job isolation (ARC on Kubernetes) or you get cross-job contamination on a PHI-adjacent runner, an image pipeline, patching, and a named owner inside hospital IT at 3am. Hospital IT will not put an internet-connected runner that long-polls github.com on a clinical VLAN without change control measured in months.
- **Celestina:** a self-hosted runner that pulls from GitHub and PyPI inverts the boundary it is meant to hold — and its core outbound function is the first thing Phase 1's default-deny egress must allowlist. The plan contradicts itself across two phases.

**Disposition:** record as contingent on I6, spend zero hours before a site is signed, and revisit when a design-partner site exists and R7 is answered.

---

## 5. Escalated to the operator

### I8 — panel composition. REJECT 5–0. **This is the one item the panel cannot decide for itself, and it is unanimous.**

All five seats rejected their own competence to rule this docket. The chair is escalating rather than proceeding, because a panel that unanimously finds itself under-composed cannot cure that by voting again.

**AJ's absence is correct and mandatory** and no seat objected. `AJ/AJ_HARDWIRING.md`: AJ "Holds no Brain Trust seat, no vote, no build or Orlok role, ever," and audits from outside on artifacts only. `skills/stag-brain-trust/SKILL.md:11` is wrong to list him and should be corrected.

**The other two absences are the problem, and the mechanism of one of them is the finding of the day.** Independently, Amadeus and Oluwole traced it, and Elijah and Orlok confirmed the shape:

> The operator's 2026-09-01 naming ruling renamed **PrivacyDomain → Hestia**. v2 §9 then rules, correctly, that no seat this document creates may review it — *"not Hestia, not Bayamanaco."* The consequence, which the document does not state, is that **the plan's own naming ruling disqualified the privacy seat from reviewing the plan.**

The panel lost its privacy lens *to the artifact under review*, on a docket whose defining requirement is a privacy containment property and whose §6 turns on HIPAA, BAA scope, all-party recording consent, retention and a breach clock. Not one seated lens owns any of that. Elijah's resolution is the panel's: the conflict attaches to Hestia's **enforcement** role, not to the privacy-and-compliance **review** lens, which predates the document — so seat privacy under a name this document did not create, recused from anything touching Hestia's own charter.

**TYR's removal is the least defensible.** TYR is the fleet's ratified security auditor and lead Breaker, *independent of the fleet* (`notes/2026-08-06-tyr-lead-breaker-and-security-auditor-approved.md`, status ratified) — a stronger independence than v2 §7 concedes Hestia and Bayamanaco have. Orlok found the sharpest form of it: v2 §7 leans on `2026-08-06-tyr-never-certifies-itself-aj-plus-second-breaker-do` (confirmed ratified) to invoke TYR's independence doctrine **on a panel seated without TYR**. Removing the verification-and-risk seat from a security review whose central charge against v1 is fabricated verification — a wrong gate count copied from a note, a commit ref that does not resolve — is the document's own diagnosis performed rather than fixed.

Two seats added a further note. Amadeus, from the framing seat: *"I do not carry privacy-law competence or verification-and-risk competence, and this panel must not treat my presence as covering for the two empty chairs."* Elijah observed the panel also dropped the accessibility lens while §0 contains an accessibility clause nobody left on the panel owns.

**Two options for the operator, both drawn from the seats' own reasoning:**

- **Option A — cut the docket (Amadeus, and the chair's recommendation).** Five seats are entirely adequate to decide "turn on branch protection, scope the Railway credential, wire `omar_security_gate` correctly, delete three dead pre-commit paths, harden two Dockerfiles, and review tenant isolation on `audit_results`." That docket touches no patient data and needs no privacy lens. Everything R7-shaped — I1's ACS half, I5, and the R7 half of I6 — comes off the table until the ACS is scheduled. **Under Option A, sections 3 and 4 of this record stand as written and are ratifiable today for the fleet half only.**
- **Option B — fill both seats and re-run.** Seat privacy under a name v2 did not create, and seat verification-and-risk (TYR or an equivalent independent security lens), then re-run I1, I2, I4, I5 and §6. Under Option B, nothing in §6 and nothing in the §1 fact table carries this panel's authority until the re-run.

The one thing the panel will not endorse is proceeding at five seats on the R7 half of the docket as though the vacancy were procedural.

---

## 6. Chair's note — the load-bearing thread

**The load-bearing thread is not any single issue. It is that v2 commits, four times, the exact defect it was written to correct.** v2's claim to authority over v1 is that it re-verified its facts at named refs. Its §2 principles are "an unperformed check is not a clean check" and "safeguard existence does not imply invocation."

- It convicts v1 of a report-only window with no owner and no date (I4), then writes one with no owner and no date.
- It states in Phase 5 that four deferral conditions "are now dated remediation items in Phase 0–3" (I7). Three appear in no phase, the fourth is in Phase 4, and no phase in the document carries a date.
- It says "answer 8.4 before any architecture is chosen," then chooses an architecture contingent on 8.4 (I5).
- It diagnoses "safeguard existence does not imply invocation" in others, then charters two new fleet-internal enforcers while the fleet's ratified, fleet-*independent* security auditor (TYR) has never been built — and concedes in §7 that the new pair has weaker independence than the Breakers. Amadeus's phrasing: the document reproduces its own diagnosis at the level of the org chart and does not notice.

**Three findings from the cold reviewer that no seat raised, and that the chair verified personally.** These are reported here rather than voted on, because the cold review sits outside the panel by mandate.

1. **F1 — the plan's headline Phase 0 finding is inverted, and its remedy is a regression.** v2 §1 claims `gate_coverage_report.py` "is not reading the installer" and that the fleet therefore has no trustworthy coverage count. **The chair ran it and read the source.** `gate_coverage_report.py:26` sets `PRE_COMMIT_HOOK = os.path.join(REPO, ".git", "hooks", "pre-commit")` — the *installed* hook — and `.git/hooks/` in this clone contains only `*.sample`. No hook is installed, so `hook_parity_gate` and `stale_stage_guard` genuinely do not run here. **The tool is correct.** Its docstring even documents the limit the plan accuses it of hiding. The prescribed work item — "make `gate_coverage_report.py` read the installer" — would replace measured state with declared intent and report two gates as covered in a clone where they do not execute, breaching v2's own principles 2 and 3 one page after stating them.
   **This resolves the panel's only direct factual disagreement. Elijah read the same evidence and concluded "the tool is wrong and the finding is real." Elijah is wrong on this point, and I record it plainly because I made the identical error in v2 myself.** The better finding, which nobody claimed: `hook_parity_gate.py` is the fleet's purpose-built control for exactly this drift, is declared in *both* `.pre-commit-config.yaml` and `install-git-hooks.sh`, and runs nowhere. A third gate, `branch_name_gate`, is orphaned and the plan never mentions it.
2. **F2 — §0's founding premise is false.** v2 asserts Mandate 2 is a hard gate and blames v1's escape solely on `mandates_gate.py` scanning `specs/` non-recursively. There are three reasons that gate could not have caught v1: the path scope; that the check is a *substring* match (`re.search(r"(?i)complian", t)`, so any document containing "compliant" once passes); and that `governance/.spec-compliance-allowlist.txt` is, by its own header, "a **100%-of-specs exemption list**" covering 79 of 126 specs. Enforcement is approximately zero, and broadening the path moves it from zero to zero. Worse: **v2 lives in a third repo the gate has never scanned**, and Phase 0 contains no fix for `mandates_gate` at all.
3. **F3 — "GEO has no PR gate" is false.** `the-geo-suite-/.github/workflows/tests.yml` has `on: pull_request:` and runs `python -m pytest -q` with no `continue-on-error`. What GEO lacks is *branch protection requiring* it — a different claim with a different remedy, and Phase 0.1 prescribes a "required status check" while the plan believes no status check exists. **This one is mine: I had read that file earlier in the session and wrote the opposite.**

**Two operational findings from Orlok that belong in Phase 0a immediately, and are not in v2 at all:**

- **`omar_security_gate.py:110` takes a positional `root`**, where every other gate in the battery is invoked `--root ROOT`. Wire it by pattern-match — which is what "wire the gate" reads as — and it exits 2 on argparse before scanning a byte: a gate that "runs" and asserts nothing, v2's Principle 2 failure committed by v2's own Phase 0. Wire it *correctly* and it exits 1 with **106 problems** repo-wide, with **no baseline mechanism at all**. Landing it blocking on day one red-lines every commit in the repo.
- **`research/knowledge-home/raw/` holds sixteen baselined credential-shaped findings** — DB connection strings with credentials, a Stripe key, JWTs, an AWS access key — in a pushed GitHub repository. Phase 0 item 8 (push protection) is forward-looking and does nothing about material already in history, and push protection plus CODEOWNERS are paid features on private repos. This connects directly to the open credential-rotation runbook.

**Chair's verification of the fleet's current state, since a plan to add controls should know it.** Orlok reported `verify.py` at `aad9650` as **RED, 25 real failures of 131 checks**, and characterised 23 as environment. The chair re-ran the battery and refines the split: of the 25 non-green items, **20 are `ModuleNotFoundError` (`dotenv`, `fastapi`) in this container** — an argument *for* Phase 0.5, not a code defect — and **five are real**: `audit_report_gate` (1 audit-shaped file below the floor, 6 violations), `test_discrimination_check` (9/10), `test_pre_commit_secret_check` (6/7), `spec_trace_gate` (8 gates `missing_spec_trace`, including five of the seven the installer wires), and — most seriously — **`secret_scan_gate`: 0 new findings and 11 REGRESSED**, meaning baselined credential findings the scanner no longer detects. That is precisely the regression class the gate was built for after the 2026-08-26 incident its own docstring narrates, and it is live and unremediated today. **v2 has no item that says "get the existing battery green first." That item should be Phase 0a's first line.**

**The single thing most likely to make this plan fail in execution**, which Elijah and Orlok reached independently: v2 names no person, no hour and no slice number anywhere, while the team that would execute it is one operator plus agent sessions already carrying 40–55 GEO slices at 160–220 agent runs on a product that is behind its deadline. The ledger's recurring escalation state across every prior review is *"blocked on Abad."* A plan with no line in `master-todo.md` does not lose the fight for the operator's time — it never enters it, and in three months Hestia's charter joins `omar_security_gate`, `prepush.py` and the attribution trailer on the fleet's own list of correct, committed, briefed mechanisms invoked by nothing.

---

## 7. What ratification would mean

On "ratify the slate," the following become binding and feed the runbook:

1. **I6** proceeds as a standalone, dated operator action item routed outside the security plan.
2. **I2, I3, I4, I7** pass with the conditions in §3 as their real content. The conditions, not the issue statements, are what was approved.
3. **I1 and I5 are rejected as put.** v2 is split: a narrow Phase 0a remediation list against the two repos that exist — with tenant isolation on `audit_results`, the `omar_security_gate` argv defect, the sixteen baselined raw-repo findings, and "get `verify.py` green" added — and an unscheduled R7 brief filed behind GEO.
4. **I8 is not ratifiable by this panel.** The operator picks Option A or Option B in §5. If Option A, items 1–3 above stand for the fleet half today. If Option B, §6 of v2 and its §1 fact table wait for a re-run with privacy and verification seated.
5. A **v3** is written against this record and the cold review, and v2 is marked superseded — the same disposition v1 received.

Nothing above is final until the operator ratifies.
