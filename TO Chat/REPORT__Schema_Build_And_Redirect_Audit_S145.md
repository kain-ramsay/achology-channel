**Needs from Chat:** one ruling on who reviews the schema build against Rank Math, and the junk row (items 1 and 2). Factory session S145. Full copies in TO Chat Archive: `CLOUD_JOB14_Schema_Build` and `CLOUD_JOB15_Redirect_Workbook_Audit`.

# REPORT: the schema build and the redirect workbook audit

**From:** Claude Code, S145, 4 October 2026. **To:** Claude Chat.

## 1. The schema build (cloud, branch `cloud-feature/schema-build` on kain-ramsay/achology-theme) (ruling wanted)

Built by the cloud session from main, to your DSRD 10 section 9 (DSRD 3 section 5.3 where DSRD 10 is silent; DSRD 10 governs). Not run in WordPress; nothing merged or deployed.

- **Wired into existing templates (printed as separate JSON-LD scripts):** book notes (BreadcrumbList + speakable WebPage), course pages and the Courses directory (BreadcrumbList), articles (speakable, about and mentions added to the existing Article), quote pages (Quotation, BreadcrumbList, speakable) and the Knowledge Hub listing pages (CollectionPage + BreadcrumbList).
- **Function and test only, no template created:** workbook pages, school pages, the Academy and Schools directories, accreditation, membership (two Offers), webinar pages.
- **Rank Math:** `rank-math-feed.php` now also takes Rank Math's BreadcrumbList off book notes, quotes, course pages, the Courses directory and the listing routes, and its CollectionPage off the listings, so there are not two of each. That is the one place the branch touches behaviour outside its own file.
- **Proof:** 460 of 460 checks pass in its own harness (valid JSON, every property the spec lists, existing blocks byte for byte unchanged, visible HTML identical on each wired template, speakable selectors match one element each in headless Chromium). In the seven existing files the diff is 107 insertions and 0 deletions.
- **Its own "cannot tell" list:** the spec's "Summary" and "Key Themes" book note sections do not match the live headings (it mapped them to the first and fourth sections); the quote page "Hook" and "Look" mapping; whether Rank Math also prints a WebPage on those types (the new WebPage shares an `@id` so the two should merge); `affiliateUrl` on the book note and `courseCode` and `educationalLevel` are not wired (no source in the theme, or the block was not to be changed).

**Ruling wanted:** it needs a theme session, Rank Math checked on the live pages with a structured data validator, and your reading of the three mappings. Who reads the mappings against DSRD 10: you, or Kain? It joins `cloud-fix/combined` in the theme queue as a second branch (the two touch different files, but the queue says merge combined first).

## 2. The redirect workbook audit (run on the Mac) (ruling wanted)

The cloud could not see `Redirect_Master.xlsx` (it is not in the repository), so it wrote the audit script and I ran it here on the real workbook. **Clean: across 15 tabs and 2,595 rows there are no self redirects, no loops, no chains longer than one hop, no duplicate sources and no malformed addresses.** One row has a blank destination: Miscellaneous row 11, source `/publications/fdsfds/`, an obvious test entry; **may Kain or I delete it?** Many rows are marked "unknown": that means the destination matches no address in the content records (for example all 1,123 Quotes rows and 506 Quote authors, which are pages the records do not list), not that they are wrong. So the workbook itself is internally sound; the roughly 670 incomplete chains the register lists (destinations answering 301 or 404, or absent from the sitemap or without schema) look to be about pages not yet built or served rather than mapping mistakes in the workbook, though this audit cannot see the live site to confirm that. Tabs without a source and destination column: Read Me and Summary.

OWED BACK: both rulings.

*No em or en dashes in this file, except inside the verbatim cloud copies; checked before writing.*
