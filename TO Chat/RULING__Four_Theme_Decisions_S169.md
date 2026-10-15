> Chat: please write the fourth ruling into DSRD 7 section 4.3 as a recorded exception (item 3); the other three need no document change beyond the build sheets noted. The code for all four is on a branch, not yet live.

# RULING: four small theme decisions, from the cloud session's branch triage (Kain, Code's S169 sitting, Thursday 15 October 2026)

Kain's words, in reply to Code's four recommendations: "Yes to all four of your recommendations: darker hover shade, measure the pricing school names first, record the help-gap exception, and the two invisible fixes."

1. **School button hover colour (cloud job 1, F5b).** `.btn-secondary--school:hover` fills with the school's text-safe shade, not the raw primary, so white text passes 4.5 on all seven schools (cbp 3.23 to 4.61, lc 3.85 to 4.60, pc 4.23 to 4.53, mh 4.35 to 4.67, pgd 3.38 to 4.59). The class is used on no page today, so nothing a visitor sees changes. Held commit `5c92f03`, applied to main on branch `factory/four-decisions-s169`.
2. **School names on the pricing bundle cards (cloud job 1, F4).** Measure the real page first; Kain looks only if it fails 4.5. Not yet measured (a browser measurement of the name against the gradient behind it, at the real position). Worth knowing: the code alone gives bounds of 3.90 to 5.44 depending on where the name sits in the wash.
3. **The gap above "Was This Article Helpful?" on help answers (cloud job 12, option 4 and 3).** Recorded as an exception, with no page change: the strip closes the answer above it at the 32px gap Kain set at S110, so the junction between the answer's body and the strip is not a block boundary. **For Chat to write into DSRD 7 section 4.3 as a named exception** (as Exception 3 was for the category hub), naming Kain's S169 ruling and the S110 foot ruling. The machine's record of it is a named CARVE-OUT row in `page_gate.py` (`help_strip_carveout`, same branch), so the 299 help answers' failing line becomes one named carve-out each.
4. **Two held invisible fixes from `cloud-fix/combined` (cloud job 3, SHOULD FIX).** (a) An unknown Knowledge Hub category address answers 404, not 200 with "being prepared" (`1b89a99`). (b) On course pages only the workbench key can pick a layout option from the address, so a visitor can no longer load the unratified layouts through `?opt-hero=2` (`bb30fce`; the `is_string` half had already reached main, so only the sitting check was added, merged by hand). Neither changes a page a visitor sees at its normal address.

All four are code on branch `factory/four-decisions-s169` (a separate copy of the theme at `~/achology-wt-four-s169`, cut from main at 37ac213). Not merged, not deployed: the theme session merges, runs `deploy.py` (which lints the PHP on the server before anything goes live) and checks the pages.

OWED BACK: DSRD 7 section 4.3's recorded exception for the helpful strip.

*No em or en dashes in this file; checked before writing.*
