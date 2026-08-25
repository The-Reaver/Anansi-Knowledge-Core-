---
id: 2026-08-04-sandbox-network-egress-blocks-real-deploy
type: finding
status: ratified
source: this chat, 2026-08-04, discovered by the Jeremy build subagent while building the Anansi ledger slice (source status: active)
project: fleet
tags: [anansi, jeremy, sandbox-limitation, finding]
---

# The Build Sandbox Blocks pypi, GitHub, and apt, So the Ledger Code Was Never Run Live

## Body

The coding sandbox used to build the Anansi ledger minimal slice returns 403/host_not_allowed on pypi.org, github.com, and archive.ubuntu.com, which blocked pip installs of fastapi, supabase, and openai, and blocked apt install of postgresql-pgvector. As a direct result, the FastAPI HTTP layer, the live Supabase client, the OpenAI embedding call, and pgvector itself could not be executed live in that environment. They were verified only by code inspection, py_compile, and logic simulated against fake in-memory stores, not by an actual end-to-end run.

## Links

- affects: 2026-08-04-anansi-ledger-real-red-green-proof-not-yet-run
