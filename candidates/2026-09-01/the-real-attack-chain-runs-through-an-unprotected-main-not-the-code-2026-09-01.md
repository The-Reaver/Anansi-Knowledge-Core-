---
id: the-real-attack-chain-runs-through-an-unprotected-main-not-the-code-2026-09-01
type: finding
status: candidate
source: "Recovery session, 2026-09-01 — adversarial panel (AJ, Hestia, Bayamanaco) against docs/specs/2026-09-01-security-arsenal-integration-plan.md; this finding independently re-verified against the repositories by the session relaying it"
project: geo
tags: [security, attack-chain, branch-protection, ci-secrets, railway, critical]
supersedes: []
superseded_by: null
---

# One unreviewed push to GEO's main exfiltrates the entire production environment

## Body

**Verified in the workflow files.** `deploy-verify.yml` declares:

```yaml
on:
  push:
    branches: [main]
...
  RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
  run: railway run --service "The-Geo-Suite-" -- python scripts/deploy_verify.py --check-env
```

`railway run` injects the **live production environment** into that process. GEO has **no PR gate**
— stated in its own workflow headers. So anyone who can push one commit to `main` can rewrite that
`run:` line and exfiltrate every production secret: the Railway token, the Supabase service-role
key and DB URL, and the vendor key-encryption secret.

Nothing intercepts it. Every security workflow is advisory by construction, and Railway has already
auto-deployed by the time CI runs — a blocking check on a PR enforces nothing where nothing opens
PRs.

**The lesson that generalises:** the fleet's security effort has gone into controls that run
*inside* CI, while the door to CI itself is unlocked. **Branch protection is a repository setting —
free, server-side, and the one control no clone can opt out of.** It is the property the fleet has
been trying to buy with hooks and gates, available for nothing, and it was diagnosed in the plan's
own analysis and then never prescribed.

## Links

- relates-to: every-geo-security-scanner-is-advisory-by-construction-2026-09-01
- relates-to: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
- relates-to: geo-pushes-straight-to-main-with-no-staging-environment-2026-08-31
