# REPORT: the Manifesto and Code of Ethics walked through the gate, one fix shipped, plus the findings that are yours

**From:** Claude Code, S042. **Date:** 2026-07-29.
**Continues:** the DSRD 6 one-page-at-a-time walk. The policy family's seven records are closed to the extent a build site allows (see REPORT__Policy_Family_A11y_And_UX_Walks_S042.md); these are pages 8 and 9 of the walk order.

## The ship brief first

**What changed (theme v0.36.34, one change set, commit 80b756a):** the document-header variant used by /about/manifesto/ and /about/code-of-ethics/ kept a 2026-07-15 design where the hairline ran only under the header text, stopping beside the floated document image. page_gate failed both pages on DSRD 7 §4.3 ruling 1 at all three widths. Rulings 1 and 2 (Kain, S224) supersede the old design, so the variant now inherits the standard full-width separator with the standard spacing, 48/48 desktop and tablet, 32/32 phone, measured and confirmed. At the same time the template now renders the word Achology in the brand accent inside the H1, per Kain's standing S227 heading rule, which these two titles were missing. The 640px policy-table stack point also now carries the in-place annotation DSRD 7 §4.5 ordered (one of the two named S223 exceptions).

**Why:** the walk instruction's step 3, fix only what a written standard fails. Kain approved the change on preview in Safari before it shipped, in his words: "yes, go ahead, claude" (starting the two pages) and "yes, ship it" (after seeing both previews). Those words are this change set's brief, covering both pages.

**What I need from Chat:** nothing for the fix itself. The rulings below are what these two pages wait on.

## Where the two pages stand

Both pages pass everything the policy family passes: structure and headings clean, metadata inside limits, schema emitted (AboutPage and BreadcrumbList), all assets load, all links resolve, zero dashes, no horizontal overflow at any width, and the §7 and §8 template checks from the policy walk hold here too (same header, footer, menus). The hairline fix removes their only machine-gate failure apart from the site-wide canonical. The gate re-runs against the live pages once Kain uploads the zip, and each page's DSRD 6 record files then with its printout.

## Rulings needed

**1. Which §12 row do the Manifesto and the Code of Ethics belong to?** DSRD 6 §12's table names policy pages and About pages, but neither row names these two, and the walk instruction groups them with the policy family. It matters for §6: both pages show an adoption date ("This organisational standard was adopted on 17 Aug 2019"; "This code of professional conduct was adopted 28 July 2022") rather than a last-updated line. If the policy-page logic applies, is an adoption date the honest equivalent of the visible date §6 requires, or do they need a last-updated line as well?

**2. The three template rulings already asked in the policy-family report** (sticky header, footer buttons, date-line grey) apply to these two pages equally.

## Copy findings, yours and Kain's, none touched

- **Code of Ethics: SoMAP is never spelled out.** The page says "issued by SoMAP" and the full name, the Society of Modern Applied Psychology, appears nowhere on the page. DSRD 6 §1's acronym rule fails on this one. The Manifesto page does it correctly ("developed by the Society of Modern Applied Psychology (SoMAP)").
- **Manifesto: a heading misspells the name as SOMAP.** "Our Commitment to the SOMAP Code of Ethical Practice" against the canonical SoMAP, which the same page's body uses.
- **Code of Ethics: spaced hyphens standing in for dashes.** "Our code of ethics - also referred to as our ethical framework - asks two things": the house standard replaces these with commas or colons.
- **Code of Ethics: the adoption line reads "was adopted 28 July 2022"** where the Manifesto's parallel line reads "was adopted on 17 Aug 2019"; one of the two is missing its "on", and the two dates also format differently (17 Aug against 28 July).
- **Code of Ethics: the document image's filename is page-01.webp.** DSRD 6 §11 item 4 checks filenames hardest because renaming after upload breaks references; "page-01" describes nothing. Flagged for whenever the image is next touched rather than as a rename now.
- **Both browser titles capitalise connecting words** ("The Code Of Ethics For Practitioners Of Applied Psychology"), the same pattern noted on Terms and Refunds.

*No em or en dashes in this file; checked before writing.*
