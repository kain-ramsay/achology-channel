# Note for Chat — live schema findings, as input to the page checklist

**From:** Claude Code, 2026-07-22
**For:** the page-readiness checklist Kain is assembling with you, and the
DSRD 10 §9 schema map it will lean on.
**This is input, not spec. Claude Code writes no DSRD or checklist — this is
ground truth from the live test site for you to fold in as you see fit.**

## Why this is useful to you now
Kain is building the finished-page checklist — the operational detail beneath
DSRD 6's gate (schema, metadata, alt text and image metadata, speakable markup,
and the visual specifics: font/text sizes, spacing, hairline spacing above and
below). The schema layer of that checklist should be built on what the site
*actually emits*, not on the DSRD 10 §9 map alone, because that map carries its
own warning: its "Rank Math auto" rows were written for Yoast and are marked
provisional until verified at "the Rank Math configuration session." That
session effectively happened today. Here is what verification found.

## What the live pages emit (achologytest.com, theme v0.36.5, Rank Math Pro)

| Page checked | JSON-LD emitted | Read |
|---|---|---|
| FAQ article (`/help/.../what-is-achology/`) | FAQPage + BreadcrumbList | Correct, one of each. **No duplication** between theme and Rank Math. |
| `/help/` landing | EducationalOrganization + WebSite + CollectionPage + BreadcrumbList | Correct. Confirms the theme's `EducationalOrganization` fix is live — not generic Organization, and no fake physical-location schema. |
| Our People (`/about/instructors/`) | BreadcrumbList only | The Person schema sits on the individual profile pages, not the hub. |
| **About (`/about/`)** | **Nothing — zero structured data** | **Gap.** DSRD 10 §9 assigns it AboutPage; the page also has a visible breadcrumb with no BreadcrumbList behind it. Rank Math's "auto" is not firing on it. |

## Two things the schema layer of the checklist can settle

**1. The dedup fear is unfounded — so the check can be stated positively.**
There is no doubling-up anywhere tested. The checklist's schema line can
therefore assert the strong, verifiable rule: *exactly one block of each schema
type per page, and every page knows which source emits it* (theme template vs
Rank Math). Today's split, as built: the theme owns FAQPage, Person, Article and
their BreadcrumbLists; Rank Math owns the site-wide Organization/WebSite graph
and the CollectionPage on archives.

**2. The About page has no schema, and DSRD 10 §9 needs a decision, not a fix
from me.** The map says About = "AboutPage, Rank Math auto." In reality Rank
Math emits nothing there. Two ways to close it, and it is your call which the
spec records:
   - **Theme owns it** — the theme emits `AboutPage` + `BreadcrumbList` for
     `/about/`, exactly as it already emits FAQ, Person and Article schema. More
     consistent, and it survives any future Rank Math setting change. My
     recommendation.
   - **Rank Math owns it** — configured on, per-page or per-type. Fewer lines of
     theme code, but it is a setting that can be lost.

   Either way, DSRD 10 §9's About row should stop saying "Rank Math auto" once
   decided, and Claude Code builds to whatever you record. I have not touched
   the About page schema, to avoid building ahead of the spec.

## Offer
If it helps the checklist, I can produce a complete per-page-type schema
inventory from the live site — every type each template emits, with its source —
so the checklist's schema section and the DSRD 10 §9 map are both built on
verified output rather than the provisional Yoast-era mapping. Say the word.

*(Companion note `Note_for_Chat__Video_Schema.md` covers the separate
VideoObject gap for the testimonial and course videos.)*
