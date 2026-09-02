---
id: 2026-08-21-pyproject-readme-path-outside-build-root-breaks-railway-build
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, pyproject, hatchling, railway, build-config]
sources:
  - ref: "Archive turns 511-514: the agent finds 'Your pyproject.toml has readme = \"../README.md\" — it points outside the backend/ folder ... hatchling reads that metadata first and can fail in seconds ... which matches your ~10s Build image failure', then removes the field since readme is optional"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [511, 514]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A `readme = "../README.md"` entry in backend/pyproject.toml pointed outside the Railway build root and made hatchling fail while preparing package metadata
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent found this by reading pyproject.toml directly, removed the field, committed the fix, and it was one of the two fixes that turned the failing build into a passing one
- verified: 2026-08-21
## Body
The backend's `backend/pyproject.toml` had a `readme = "../README.md"` metadata field pointing one directory above the Railway build root (which is `backend/` once Root Directory is set correctly). When `pip install .` runs with `backend/` as the build root, hatchling reads this metadata during package preparation and can fail quickly if it can't resolve the relative path outside its build context, which matched the roughly 10-second "Build image" failure seen on Railway. Because the `readme` field is optional in `pyproject.toml`, the fix was simply to remove it rather than try to make the relative path work across different build-root configurations. General lesson: package metadata paths in `pyproject.toml` (readme, license files, etc.) that reach outside the directory a build tool will actually run from are fragile across different CI/deploy environments that may set a different working/build root than local development does.
## Links
- related, 2026-08-21-railway-monorepo-service-needs-explicit-root-directory.md, the companion build-config bug found and fixed in the same troubleshooting sequence
