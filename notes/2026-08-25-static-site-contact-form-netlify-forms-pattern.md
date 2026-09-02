---
id: 2026-08-25-static-site-contact-form-netlify-forms-pattern
type: decision
status: ratified
ratified: "2026-08-25 — Brain Trust + AJ ratification pass (seats: Celestina, Jasiah, Oluwole, Omar, Sentinel; AJ independent audit). Carried 3-2 with conditions; Omar B1/B2 and Sentinel N1 applied. Celestina's non-blocking split recommendation recorded as follow-up, not applied. See reports/STAG_BRAIN_TRUST_LEDGER.md."
project: agame-sports-rebuild
tags: [astro, netlify, static-site, contact-form, forms]
sources:
  - ref: "Contact form wired to Netlify Forms and verified in built dist/ output, turns 3-5, A-Game Sports rebuild, 2026-08-25; independently re-verified 2026-08-25 by the bridge-cse session after syncing the local clone to cb16c5e and rebuilding (data-netlify and hidden form-name both confirmed present in dist/contact/index.html)"
    reliability: high
    origin: "A-Game Sports rebuild remote session, 2026-08-25; transcript reconstructed manually and ingested into the Core by the bridge-cse session the same day"
provenance:
  archive: research/knowledge-home/raw/2026-08-25-agame-remote-diagnostics-and-content-sweep.jsonl
  turns: [6, 11]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

> **Provenance added 2026-08-25 on ingest.** This note was authored in a remote container with no
> access to the Core, so it originally carried no ADR-0005 provenance pointer. The session
> transcript has since been ingested (96 records) and the turn range above was read off that
> archive, not estimated. Ratified 2026-08-25 by the Brain Trust + AJ pass; the
> conditions that ruling attached have been applied to this note.

# Netlify Forms is the correct zero-backend fix for a broken contact form on a static Astro/Netlify site
- id: 2026-08-25-static-site-contact-form-netlify-forms-pattern
- type: decision
- status: ratified
- ratified: 2026-08-25 Brain Trust+AJ
- class: provisional
- source: A-Game Sports rebuild diagnostics session, 2026-08-25
- confidence: medium — markup implemented and independently re-verified in built static HTML output; deploy-time form detection has never been exercised (no Netlify site exists for this repo) and no submission has ever been observed to arrive
- verified: 2026-08-25
- tags: astro, netlify, static-site, contact-form, forms

## Body
A raw `<form>` with no `action`/`method` on a static-output Astro site (no adapter, no server) silently discards every submission — the browser just does a same-page GET. Once the deploy target is confirmed as Netlify, the fix requires no backend code: add `data-netlify="true"` and a `name` attribute to the form, plus a hidden `<input type="hidden" name="form-name" value="...">` matching the form name (Netlify's build system auto-injects this input for plain HTML forms; it is genuinely *required* only for JavaScript/JSX-rendered forms, so adding it unconditionally is the safe default. The POST-body parser matches the submission to the form on this value), and optionally a honeypot field (`netlify-honeypot="bot-field"` + a hidden `bot-field` input) for spam filtering. A honeypot stops naive form-filling bots only — anything that respects `display:none` or POSTs the endpoint directly defeats it, so it is not a substitute for `data-netlify-recaptcha` or rate limiting. The decoy input must genuinely resolve to `display:none`, because a visible one silently discards real leads. Note also that this creates an unauthenticated public write endpoint collecting name/email/phone into a third-party inbox — a data-handling decision on a client site, not just a wiring detail. Form detection is **not on by default**: it must be switched on once per site under Forms > Enable form detection in the Netlify UI, and submission notifications configured separately under Configuration > Notifications. Correct markup alone delivers nothing. Once enabled, Netlify's form detection happens at deploy time by scanning the *built* static HTML for `data-netlify` — verify by grepping `dist/` after `npm run build`, not by inspecting dev-server output, since the dev server doesn't run Netlify's build-time form scan. A branded `/thank-you/` redirect page (set via the form's `action` attribute) gives a better post-submit experience than Netlify's generic default; keep it out of the XML sitemap and content-collection nav via a sitemap-integration `filter` option and a `noindex` meta tag, since it's a transient confirmation page with no content worth indexing.

## Links
- relates, 2026-08-25-multi-agent-diagnostic-sweep-pattern.md, the sweep that surfaced the broken form this note fixes
- open, no `netlify.toml` and no Node pin exists for this repo; astro 7.2.1 declares engines.node >=22.12.0, so the first deploy can fail at install before form detection is ever reached (Omar N1)
