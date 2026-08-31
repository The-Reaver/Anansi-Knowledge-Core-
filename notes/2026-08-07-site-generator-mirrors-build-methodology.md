---
id: 2026-08-07-site-generator-mirrors-build-methodology
type: decision
status: ratified
source: "Cowork session 2026-08-07, operator on phone during the GEO Suite demo build; directed that the Site Generator feature itself run on the same principles the team develops by (Mandate 12, slice by slice, layering, nothing lost). (source status: active)"
project: geo
tags: [geo-suite, site-generator, methodology, slice-by-slice, layering, verification, provenance, mandate-12, demo]
supersedes: []
superseded_by: null
---

# The Site Generator builds sites the way the fleet builds software, slice by slice, layered, verified, never overwritten, captured

## Body

## Principle
The method the fleet uses to build (slice by slice, layer on layer, verify each slice, never overwrite, capture every step) becomes the method the Site Generator uses to produce a prospect's site. The product practices the development discipline.

## How the generator builds a site
- Ordered layers, each a slice: foundation and structure, then answer-first content, then schema markup, then compliance pass, then authority and trust, then local presence, then performance.
- Each layer verified before the next: green check only after its own check passes (schema valid, every medical claim cited or disclaimed). A failed layer retries alone.
- Never overwrite: each layer adds on top of the last; the site accumulates rather than rebuilds.
- Score climbs per layer, 38 up to 93, so each slice adds visible points instead of one jump.
- Every layer logged: what it did, and the before/after for its category. The log is the site's provenance and the same capture habit that trains the fleet.

## How it gets built (itself slice by slice)
- Confirm the base Site Generator screen first, then layer the verified, cumulative, logged behavior in as the next slice, so a working base is not overwritten to add the feature.

## Demo boundary (Mandate 7)
- Demo version generates the layered page live for the example practice, Pacific Coast Hyperbarics, clearly labeled. The any-prospect engine (ingest any existing site, generate from scratch for anyone) is the engine-room build, on the machine with Antigravity, after the demo.

## Links

- extends: 2026-08-06-geo-suite-demo-spec
- relates-to: 2026-08-06-antigravity-role-verdict
- relates-to: STAG_MANDATES_AND_PRIORITIES Mandate 12 (slice by slice, never overwrite)
