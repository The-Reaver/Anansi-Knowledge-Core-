---
id: the-production-container-runs-as-root-carrying-a-compiler-toolchain-2026-09-01
type: finding
status: candidate
source: "Recovery session, 2026-09-01 — adversarial panel finding, independently re-verified against the repositories by the session relaying it"
project: geo
tags: [docker, hardening, root, container-security, geo]
supersedes: []
superseded_by: null
---

# GEO's production image runs as root, ships a build toolchain, and has no .dockerignore

## Body

**Verified in `backend/Dockerfile`**, the image running in production. Four defects, all squarely
inside the "system hardening" requirement the security plan claimed to cover:

1. **No `USER` directive** — grep returns 0. The container runs as **root**.
2. **`build-essential` is installed and never removed**, with no multi-stage build, so a full
   compiler and linker toolchain ships in the runtime image. That is a textbook
   privilege-escalation and lateral-movement enabler.
3. **`COPY . .` with no `.dockerignore`** anywhere — verified absent at the repo root and in
   `backend/`. Nothing constrains what enters the image from the build context.
4. ~~**Shell-form `CMD`**, so uvicorn is not PID 1 and does not receive `SIGTERM` directly.~~
   **WITHDRAWN — see the correction below. This is not a defect.**

The plan's opening section claimed to state *"what the stack actually is."* The running production
image **is** the stack, and it was never opened. Its Phase 2 proposed "hardening at image build" in
the abstract while four concrete, checkable defects sat in the one file that governs it.

**The lesson:** a hardening phase written without reading the Dockerfile is a plan to harden an
imagined system. These four are the actual work items, and finding them took one file read.

## CORRECTION — 2026-09-01, ratified in BRAIN_TRUST_DECISION_RECORD_2026-09-01

**Defect 4 is withdrawn, and it was the dangerous one to act on.** The shell form is
**deliberate and documented**: `backend/Dockerfile:33` is
`CMD python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`, and it is shell-form precisely so
`$PORT` expands at container start, per Railway's manifest. A nine-line comment in the file says so.
Converting it to exec form breaks the Railway healthcheck and takes production down.
`frontend/Dockerfile:38` (`CMD npm run start -- --port ${PORT:-3000}`) is shell-form for the same
reason. A hardening list that "fixes" this ships an outage.

**Defects 1–3 stand and are ratified into Phase 0a** (`docs/runbooks/2026-09-01-phase-0a-security-remediation.md`):
no `USER`, `build-essential` in the runtime image, no `.dockerignore` — re-verified absent at repo root,
`backend/` and `frontend/` on 2026-09-01. Removing `build-essential` is deferred behind a staging
environment because of the `psycopg` / `cryptography` / `weasyprint` wheel builds; multi-stage is the
right answer and is not a Phase-0-sized change.

**Undercount:** there are **two** unhardened production images, not one. `frontend/Dockerfile` also has
no `USER`. The original note said "the image running in production," singular.

**The lesson survives intact and gains a second edge.** A hardening phase written without reading the
Dockerfile is a plan to harden an imagined container — *and* a hardening phase written without reading
the **comments** in the Dockerfile is a plan to break a real one. Every apparent defect in a deployment
artifact should be checked for a deliberate reason before it enters a work list.

## Links

- relates-to: three-blind-reviewers-rejected-the-security-plan-unanimously-2026-09-01
- relates-to: the-real-attack-chain-runs-through-an-unprotected-main-not-the-code-2026-09-01
