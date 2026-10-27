> DISPOSITION, Chat S449 close (27 October 2026): read; founder pages items are written into DSRD 9; what remains rides on ASK__Founder_Pages_Rescore_And_Final_Reread_S188. Archived.

**For Chat. What this needs:** nothing new; read with ASK__Founder_Pages_Rescore_And_Final_Reread_S188, which still owes your chapter 7 re-read and the rescore put to Kain.

# SHIP (theme session, S193): 0.707.655, the policy template's schema names read as plain text

**What changed.** `template-policy.php` now passes the page name, the description and both breadcrumb names through the theme's existing `achology_schema_text()` before they go into the JSON-LD. Before, the Founders' Letter's AboutPage and breadcrumb named the page "Founders&#8217; Letter", the code itself, because WordPress turns the apostrophe into that code and a JSON-LD string takes it literally. Now it reads "Founders' Letter", as the H1 does.

**Why.** DSRD 6 section 4: "the facts inside the code match the facts on the page". Found running chapter 4 on the three founder pages.

**Nothing a visitor sees changed.** Deployed, cache purged, local, server and zip agree at 0.707.655.

**Reach.** The same template serves the seven policy pages and /about/'s children; every one now gets the decoded names. No other template was touched; the other schema templates already used the helper.

**Founder pages, where they stand now (records committed):**
- Chapter 3 pass on all three (title and description each unique among 2,387 stored on the install). The Letter's preview image is the site default; noted, not raised (sitewide OG handling).
- Chapter 4 pass on all three: Schema Markup Validator 0 errors 0 warnings (AboutPage, BreadcrumbList), Google Rich Results Test Breadcrumbs valid.
- Chapter 5: Manifesto pass (91). Letter 84 and Ethics 89 read fail until Kain's rescore. Two gate rows are instrument faults, measured round: orphan (inbound links are real, from /about/ and the sibling pages) and keyword density (rendered body: Letter 0.74, Manifesto 1.25, Ethics 2.56 per cent).
- Chapter 11 machine half pass: Chrome and Firefox render and agree on all three. Kain's eye owed at sign-off, with chapter 10.

*No em or en dashes in this file; checked before writing.*
