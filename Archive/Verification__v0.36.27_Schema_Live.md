# Verification — v0.36.27 schema, checked LIVE

From: Claude Code · 2026-07-24
First verification using new direct SSH + WP-CLI access to achologytest.com
(WordPress 7.0.2, theme achology 0.36.27 confirmed active). Pages fetched fresh
(cache-busted) and their JSON-LD read directly.

## Confirmed working (the S219 schema brief)
- **/help/ hub, FAQ category, KH category** — each emits **exactly one**
  `CollectionPage` and **one** `BreadcrumbList`, from the theme. Rank Math's
  duplicate `CollectionPage` and breadcrumb are gone. Dedup (Standard 2) holds;
  the FAQ-category Standard 3 breach is resolved. Trails correct:
  Home > Help, Home > Help > [Category], Home > Learn > [Category].
- **Our People** — one `CollectionPage` + one `BreadcrumbList`
  (Home > About > Our People), and **no `Person` node** on the hub. Decision (d)
  live and correct.
- **#organization naming** — the org node now reads `name` = **"Achology"** +
  `legalName` = **"Achology Transactions Ltd"** live (seen on the homepage graph
  and everywhere Rank Math prints it). Naming conflict resolved.

## Two polish items the live check caught (neither is a failure)

**1. Doubled-but-merged Organization/WebSite reference on the co-emitting pages.**
On /help/, FAQ category and KH category, the theme's `CollectionPage` carries
`about` → EducationalOrganization and `isPartOf` → WebSite as **typed** nested
refs, and Rank Math emits the full nodes too. **Both use the same `@id`**
(`/#organization`, `/#website`), so they merge into one entity — harmless to
Google — but it shows as two blocks of the type, which brushes the letter of
Standard 2. Clean fix available: make those two refs **bare `@id`** (drop
`@type`/`name`) on the three co-emitting templates, so exactly one typed block
remains. It's a same-entity merge today, so I'd **bundle this tidy into the next
theme ship** rather than spin a re-upload just for it. Flagging for the page gate
so it's a known, logged item, not a surprise.

**2. WebSite name mismatch — a real (tiny) inconsistency.** Rank Math names the
`#website` node **"achology.com"**; the theme's WebSite ref names the same `@id`
**"Achology"**. Same entity, conflicting `name`. Low impact (WebSite name isn't a
display/ranking factor), but worth aligning. **This is a Rank Math dashboard
setting**, so it's added to the Rank Math configuration runbook (site/WebSite
name → "Achology"), not a code change.

## Note
This is the first time the theme's schema has been verified against the *running*
plugin rather than by static reading. The two items above are exactly the class
of thing static analysis can't see, which is why the live check matters.
