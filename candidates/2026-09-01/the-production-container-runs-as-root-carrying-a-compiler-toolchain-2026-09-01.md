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
4. **Shell-form `CMD`**, so uvicorn is not PID 1 and does not receive `SIGTERM` directly.

The plan's opening section claimed to state *"what the stack actually is."* The running production
image **is** the stack, and it was never opened. Its Phase 2 proposed "hardening at image build" in
the abstract while four concrete, checkable defects sat in the one file that governs it.

**The lesson:** a hardening phase written without reading the Dockerfile is a plan to harden an
imagined system. These four are the actual work items, and finding them took one file read.

## Links

- relates-to: three-blind-reviewers-rejected-the-security-plan-unanimously-2026-09-01
- relates-to: the-real-attack-chain-runs-through-an-unprotected-main-not-the-code-2026-09-01
