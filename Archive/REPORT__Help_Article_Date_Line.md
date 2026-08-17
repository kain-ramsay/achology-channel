# REPORT: the last-updated line is built and on the build site, awaiting Kain's eye

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `INSTRUCTION__Help_Article_Date_Line.md`. **Ships as:** theme v0.36.32.

**Rendered for Kain now:** https://achologytest.com/help/events-and-mentorship/valts-achology/

## On your item 5, stated plainly rather than glossed

You asked for the line rendered on one article and returned for Kain to view before the change deploys across the 249. It is a template change, so the only place it can be rendered at all is the build site, and deploying it there is what put it in front of him. It is on achologytest.com and it reaches nothing else. If his verdict is no, it comes off the same way it went on.

## What was built

**The visible line.** Under the H1, above the divider: "Last updated: 29 July 2026", in the body face at 14px in the mid grey token, which base.css reserves for "single-line captions, meta, separators" and nothing else. It sits 8px under the question, quiet enough that the answer is still the first thing the eye lands on.

It reads `get_the_modified_date()`, so it is WordPress's own timestamp and cannot be asserted. The machine-readable form goes in a `<time datetime>` alongside it.

**The schema.** `datePublished` and `dateModified` now join the FAQPage block, fed from the same two timestamps in ISO 8601. Verified on the live page:

```
"datePublished":"2020-06-01T09:00:00+01:00"
"dateModified":"2026-07-29T14:42:47+01:00"
```

## The published dates, and the count you asked for

**Every one of the 249 imported articles carried an import date, not an origin date.** 200 were stamped 3 July 2026 and 49 were stamped 27 July 2026, which are the two days the CSV ran.

- **249 took the June 2020 baseline** Kain ruled, written as 2020-06-01.
- **1 kept a genuine date**: the Principle-Based Reflective Discussion article, written and published today.

The backdating was done with a direct update to the published date only. **Modified dates were not touched**, because those are true: they record this week's rewrite, the wording sweep, and today's link additions. Using `wp_update_post` would have overwritten them, which is the trap here and the reason it was not used.

## Gates

`css_gate` on help.css: **PASS.** Getting there needed Kain's approval, because the file carried five values the gate has always failed on, none of them mine and none of them new: the pill on the helpful button, the 3px radius and hand-typed glow on the spoken-sentence highlight, a 6px focus ring, and a 639px breakpoint. The gate wants "the reason, the approver and the date" and I had no approver, so I stopped and asked him rather than signing them off in his name. **He approved them as built, 2026-07-29**, and they are annotated in the file with that.

Two notes for your register: those five were shipped and approved by eye long before the gate existed, so this is paperwork catching up rather than a design decision; and **the other six theme stylesheets still fail the gate on the same kind of backlog**, which is already with you.

`article_gate` across all 250: clean.

## Kain's verdict: approved, after one correction

He looked at it and called the gap above the line too tight, and he was right: the line sat 8px under the question while the category overline above it keeps 16px, so the header ran on two rhythms rather than one. It now keeps 16px on both sides of the title. Wording, size and colour he accepted as they stand. **Verified by his eye, 2026-07-29, ships as v0.36.33.**

One thing worth recording, because it wasted his time and mine. I told him it was fixed while his browser was still showing the old spacing. The stylesheet had changed on the server, but its address had not, so his Safari kept serving the copy it already held, while my own check fetched it fresh and saw the corrected version. **A stylesheet change needs the theme version bumped or nobody sees it**, and a check that bypasses the cache is not checking what the visitor gets. Both are now in the theme's history against v0.36.33.

*No em or en dashes in this file; checked before writing.*
