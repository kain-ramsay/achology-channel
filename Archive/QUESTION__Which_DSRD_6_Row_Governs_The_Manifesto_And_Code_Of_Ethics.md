# QUESTION: which page type are the Manifesto and the Code of Ethics?

**From:** Claude Code, S047. **Date:** 2026-08-05.
**Blocks:** the final verdict on pages 8 and 9 of the walk. Everything else about them is measured and recorded; this decides two rows each.
**Status:** waiting on ruling. I am not choosing, per Rule 5.

## The gap

Two documents both have a row that could govern these pages, and neither names them.

**DSRD 6 section 12's exemption table** has these two candidate rows:

> "| About pages (founders, our people, accreditation) | section 6's author and date lines | The page is about its people, so a byline would be circular; and a visible page-updated line is inappropriate on a main feature page (Kain, S238). **The schema still carries datePublished and dateModified** |"

> "| Policy pages | section 6's author line, the date stays | Same logic; a policy's last-updated date genuinely matters |"

The About row's parenthetical names founders, our people and accreditation. It does not name the Manifesto or the Code of Ethics.

**DSRD 3 section 5.3's schema map** has the same problem:

> "| About / Founders | AboutPage | Rank Math auto | None needed | None |"
> "| Reviews, Testimonials, Free Coaching, Free Events, AAA, Policy pages | WebPage | Rank Math auto | None needed | None |"

Again, neither row names these two pages.

## Why it is not obvious either way

The evidence points both ways, which is exactly why I am asking rather than deciding.

**Reading them as About pages:** DSRD 1 section 2 puts both under `/about/`, at `/about/manifesto/` and `/about/code-of-ethics/`. The built pages emit `AboutPage` schema, which Rank Math derives from that placement. Neither shows a "Last updated" line, which is what the About row requires. The footer files them under the About column.

**Reading them as policy pages:** they are built on `template-policy.php` with `policies.css`, they carry the policy page's breadcrumb and header pattern, they sit in the policy family in the walk instruction's own order, and the walk has been treating all nine as one family since page 1.

## What actually differs, and why it matters

It is not academic. The two readings require different things, and the built pages currently satisfy neither cleanly:

| | If About pages | If policy pages |
|---|---|---|
| Visible date line | Correctly absent | **Missing, and required** |
| `datePublished` and `dateModified` in schema | **Missing, and required** | Not required |
| Schema type | `AboutPage`, which is what they emit | `WebPage`, which they do not emit |

So whichever way it is ruled, one thing needs fixing on each page, and I would rather do it once knowing the answer than guess and do it twice.

**Measured on the live Manifesto this turn:** the JSON-LD carries `AboutPage` and `BreadcrumbList`, and contains no `datePublished`, no `dateModified` and no `author`. There is no "Last updated" line. There is a different date, in the page's own words: "This organisational standard was adopted on 17 August 2019", which is an adoption date and not a last-updated date, and I do not think it satisfies either row as written.

## What I recommend, offered as a view and not acted on

Treat both as About pages, and add the two schema dates. Three reasons: it matches where DSRD 1 puts them, it matches what the build already emits, and the About row's reasoning fits them better than the policy row's does. A manifesto's "last updated" date is not the reader-critical fact that a refund policy's is; its adoption date is the meaningful one, and the page already states that in words.

If you take that route, the tidy version is that DSRD 6 section 12's About row and DSRD 3 section 5.3's About row both gain these two pages by name, so the next person does not have to infer it either.

## What I have done meanwhile

Recorded every other chapter for both pages and carried on, per Rule 5. The two rows in each record are marked "waiting on ruling" rather than passed or failed.

*No em or en dashes in this file; checked before writing.*
