> **CODE DISPOSITION, S135: WAITS ON the sweep's own theme change set (header images done ahead of it at 0.668.0, see TO Chat/REPORT__Policy_Pages_Header_Images_And_Scores_S135.md); order after the Reviews close as briefed.**

**Needs from Code:** one sweep across all eleven policy pages and the site chrome images, so every policy page closes its DSRD 6 record the way How We Write did.

# BRIEF: the policy pages sweep

**From:** Claude Chat, S386, Monday 28 September 2026. **To:** Claude Code.
**Answers:** the sweep Kain asked for in the S135 sitting, carried in `REPORT__How_We_Write_Card_Closes_S135.md`. Kain: none of the policy pages has been reviewed since the font change.
**Where it sits in your order:** after the Reviews page close (`BRIEF__Close_The_Reviews_Page_Card_S386`) and before the Knowledge Hub navigation pages.

## The work

1. **Site chrome images, once, for every page:** `fetchpriority` on the header logo, `srcset` on the ten chrome images, per DSRD 7 section 12.3. This clears chapter 9 on every page at once.
2. **The orphan crawl** (`search_gate.py --map`) run to completion across the site; any real orphan reported.
3. **All eleven policy pages** (the policies index, the seven legal policies, How We Write and the rest of the family, read from the policies index itself): each read against the current type, spacing and the 800 reading width, the gate run, and faults fixed on the tokens. **No policy page's words change**; where copy is the problem, name it for Chat.
4. **Kain's eye in Safari** on the whole family in one sitting, tabbed where there is a choice.
5. **One DSRD 6 record per page**, filed, with no fail and no not run. Chat writes the human lines (chapters 6, 7 human half, 8) from the live copy once each record's machine lines are in.

## One rule, decided now so it is not asked page by page

**Keyword density on theme-built pages.** DSRD 6 section 5 item 11 reads the editor body, which is empty on every page whose words live in the theme. For these pages the density line is measured from the words the theme hands Rank Math (`rank-math-feed.php`), and where a policy page carries no focus keyword it records "not applicable: policy page, no focus keyword set" as a named exception rather than a fail. Chat writes this into DSRD 6 section 5 item 11 at its next edit of that document. Tell me if the feed cannot supply the words to the gate.

## Also recorded

The Rank Math "recalculate every score" run you stopped: noted, no harm, nothing owed.

## Added S390, on Kain's ruling: no page may say the site is being built or rebuilt

The Accessibility Statement says achology.com "is currently being rebuilt" (section 4), refers to a "post-rebuild accessibility assessment" (sections 4, 5 and 9) and says it "was prepared on 1 July 2026 as part of the rebuild" (section 9); its section 5 is a placeholder promising a list of limitations "once the assessment is complete". Kain, S390: a site being built from scratch must never tell visitors it is being built. Remove all of it. The statement keeps what is true today (the commitment, what is built in, how to report a barrier, the Equality Advisory route) and drops the rebuild and placeholder wording. **The formal accessibility audit is a pre-launch check, done last (PRD deliverable D4: WCAG 2.2 AA verified on the homepage, course, article and FAQ templates, audit report saved, by the `accessibility-verification` skill), so the statement's conformance and known-limitations wording is finalised only after that audit, from its report.** Until then, it makes no conformance claim and says nothing about a rebuild. **Two things to fix now:** the statement's target is WCAG 2.1 AA and the PRD's locked standard (S77) is WCAG 2.2 AA; and its fixed date "1 July 2026" is replaced by the modified date. Chat brings the replacement wording to Kain rendered on the live page. Also search every page on the site, not only the policy family, for "rebuild", "being built" and "under construction" and report any hit to Chat.

The connection list for the whole policy family, drafted from the ten pages read in full, is `DRAFT__How_The_Policy_Pages_Should_Link_To_Each_Other_S390` in the Policies Design Prototypes folder. Kain rules each change on the live page in this sitting.

## OWED BACK

One REPORT in TO Chat: the eleven addresses, Kain's rulings, the eleven records' machine lines ready for Chat's.

*No em or en dashes in this file; checked before writing.*
