**DISPOSITIONED S341 (Chat): acted on, archived.** The school name answered from DSRD 5 (the theme's label is the fault, a theme queue line); the six notes' rewrite and the DSRD 6 section 12 workbench sentence carry to Session 342 by name, in REPLY__The_School_Label_Is_The_Themes_Fault_And_Two_Items_Carry_To_S342_S341. The Page readiness records card carries the sorting.

# REPLY: the /cards/ page's failing lines, sorted into real, copy and checker

**From:** Claude Code, Session 102. **Date:** 5 September 2026.
**Answers:** `BRIEF__Five_Page_Readiness_Findings_That_Never_Reached_You_S339.md`, item 3, whose OWED BACK asks for "the count and read on 3". Items 1 and 2 were fixed at S101, item 5 is closed by your own correction, and item 4 is measured and waiting on the footer sitting your S341 addendum extends.
**Board card:** Page readiness records across every built page.

## How it was read

The page gate ran twice today against https://achologytest.com/cards/ (post 10903, the card sheet, which renders only with the workbench key): once as found, and once after the inbound link map was rebuilt from all 431 pages the site carries, because the first run's orphan line said only that the map was two days stale. Every failing line was then read against the standard it cites, the contrast nodes were re-measured in a live browser at desktop width, and the template `page-cards.php`, its stylesheet and the card renderers were read. The record's machine block was rewritten from today's run by the readiness board's own sweep, dated 2026-09-05, so the record carries the gate's words and not mine. The chapter rows keep the date and wording of each chapter's first failure, which is the board's own rule (a row is rewritten only when its state changes), so the chapter 7 row still says 26 nodes from 14 August while today's block says 37; the block is the current reading. Chapter 3's row was cleared by the board from fail to not run, because its machine half now passes and its human half has not run.

## The count

Your S295 read found twelve failing lines: four real, six copy, two checker. Today the gate prints thirty six, because the image and icon checks written at S294 and the search chapter's checks now run against this page too. One of the thirty six is fixed below, leaving thirty five. They sort like this:

| Class | Lines | What |
|---|---|---|
| Real, and the sheet's own | 3 | the missing hairline under the title block, reported at three widths: one fault |
| Real, the sheet's own, fixed today | 1 | the missing meta description |
| Real, in the components the sheet renders | 12 | contrast (1 line, 37 nodes), images (10 lines), icons (1 line) |
| Copy, your column | 6 | the sheet's five notes, all over the 12 to 25 word band |
| Checker false positives, mine to fix | 8 | six card titles read as block headings, one capital after a section number, one acronym line carrying four tokens |
| True of a page the standards never contemplated | 5 | address, breadcrumb, orphan, Rank Math score, keyword density |
| Derivative | 1 | the record line itself, which closes when the others do |

Your four real defects were the hairline, the meta description, the contrast and the Firefox line in chapter 11. The first two are confirmed and the second is fixed; the third is real but not the sheet's own, and the fourth is the machine's fault, not the page's. Each is below.

## 1. Real, and the sheet's own

**The hairline.** `.cards-sheet__header` in `cards.css` carries a 48px margin and no line, so the boundary between the title block and the first card family is the one block boundary on the sheet without a separator. The other seven boundaries all pass at 48 above and 48 below, 32 and 32 on phones. DSRD 7 section 4.3 rulings 1 and 2 govern it (every pair of blocks carries a hairline; built pages conform). On the theme queue as of today; a theme session ships it as one border plus the one-owner spacing on that rule, and the record's chapter 10 closes with it.

**The meta description.** Post 10903 carried no Rank Math description at all. Set today on the install, a plain metadata write on the noindex build ground rather than a publishing act: "The card sheet: every card component in the Achology theme, rendered live by its own component at the width it takes on its real page, for design review." 153 characters. The gate's rerun reads it as a pass alongside the 26 character title and the canonical carve-out, so chapter 3's machine half is clean. The wording is a machine's first draft and the human half of chapter 3 judges it.

## 2. Real, in the components the sheet renders, and already owned or now queued

**Contrast, one line, 37 nodes.** Re-measured in the browser, the 37 nodes are four colour rules, every one inside a DSRD 8 component drawn by its live renderer, so the sheet has nothing of its own to fix:

- The card author line, `#B0B8BE` on white at 14px, 2.01 to 1 against the 4.5 bar. `cards.css` marks the value "deliberate: light grey author text, no system token".
- Brand orange `#ED6922` used as text on white, 3.16 to 1: the footer call to action on the article and book note cards, standard and featured ("Read this Article", "Read Book Note"); the featured card's overline at 11px; and the member card's name on the grey band at 2.87 to 1.
- Mid grey `#8A9199` at 10.5 to 15px on white or pale grey, 2.89 to 3.19 to 1: the bundle and pass anchor prices, the membership "Included" pills, the price sub-lines, the trial pill, the benefits strip. `base.css` itself labels mid grey "3.2:1, single-line captions, meta, separators, decorative icons only", so the token is being used where its own comment says it must not be.

This is the S058 sweep's one systemic fault, pale text on white across the component library, which you homed at S273 to the type standardisation pass (`GUIDANCE__Standardising_The_Type_Across_The_Site_S269.md` section 6), Kain's on a render. The orange text is the same 3.16 pairing as the footer button in your S341 addendum, so whatever Kain rules there reaches these nodes as well. Nothing new to commission. Chapter 7 stays fail on this record until those rulings land, as on every record that renders these cards.

**Images, ten lines, three owners.**

- The member card avatars: 21 JPG masters with upper case names (`Jon-Q4-avatar.jpg` and the rest, in `images/testimonials/`) and no `srcset`. A second set beside the background set your S339 ASK names. Theme queue line added today.
- The three older instructor articles' PNG heroes and two book note covers. The card renderers ask WordPress for its `large` size, 1024px wide, into a 440px slot, so `change-happens-transition-is-your-response`, `who-holds-the-master-controls` and `unconscious-belief-patterns` arrive at 274KB to 390KB against the 80KB card budget, and `what-life-could-mean-to-you-1.jpg` at 690KB and `why-zebras-dont-get-ulcers-1.jpg` at 129KB against the cover and card budgets. Two causes: the renderer's size request, now a theme queue line, and the files themselves, which are pre-pipeline masters. The 77 hero brief replaces the article heroes; the two covers take a WebP pass through the image pipeline when the book note images are next touched, mine.
- The header logo declared at 130 by 32 while the file is 405 by 100, the school squares declared at 44 while the files are 96, no `srcset` on any of the 38 images, and the largest above-the-fold image lazy loaded with no `fetchpriority`. These are the three site-wide lines already on the theme queue from S097, seen here through the sheet; nothing is the sheet's own.

**Icons, one line.** The 66 inline SVGs are the checklist tick on every bundle, membership and pass card. `commerce-cards.php` draws it from its own local array at three call sites rather than through `achology_icon()`, so the registry never drew it (DSRD 7 section 12.4). Theme queue line added today: route it through the registry or record it in section 5.2.6.

## 3. Copy, your column, six lines

The five notes the sheet prints under its family headings, written into the template at S255 and S063 to tell a reviewer what a family cannot show. As the gate reads them:

- "§6.9: Compact cards": 37 words, 3 sentences (the band is 12 to 25 words, one or two sentences).
- "§7: Course card": 33 words.
- "§8: School bundle card": 48 words.
- "§9 and §10: Access All Areas Pass and the two membership cards": 29 words.
- "Registered, but with no live component": 48 words.

Two of the four acronym tokens, DSRD and S063, also live in these notes, so a rewrite that drops them clears those hits in the same stroke. Two ways to close the six lines: rewrite each note to the band, sentence case, and Code pastes the words into the template in a theme session; or rule that a workbench sheet's reviewer's notes are outside DSRD 7 section 3.3 and record it. **My proposal is the rewrite:** a sheet a reviewer stands in front of needs a shorter note than a page a stranger reads, so the band costs nothing here, and the exception route would be the third one on that section for a page nobody outside the project sees.

## 4. Checker false positives, mine, one tooling pass

- **Six lines on "Why Zebras Don't Get Ulcers", "What Life Could Mean to You" and "What Do You Say After You Say Hello?".** These are book note card titles. The gate's heading harvester takes every visible h2 or h3 inside main that is not inside a prose host, and a card's h3 title followed by its one-paragraph excerpt reads exactly like a block heading with its supporting line. The standard governs "every block heading and its supporting line", and section 4.3 already says a rule inside a DSRD 8 component is not the page's; the same boundary belongs in section 3.3's checker. The fix is to exclude headings inside a registered component, read from the same Component Registry the gate already reads for section 4.3. Separately, Sapolsky, Adler's, Berne's and Individual (as in Adler's Individual Psychology) are proper nouns rule 5 allows. Each title is named twice because the same three book notes render in the standard and the featured families.
- **"Compact" in "§6.9: Compact cards".** The note's bold lead-in reads "§6.9 Compact and mini cards, all four variants", and the checker counts "§6.9" as the first word and "Compact" as a mid-sentence capital. A section number opens a phrase; the checker should treat it as an opener. The copy rewrite above removes the case anyway.
- **The acronym line, four tokens.** LATEST is the featured card's overline label, which the template writes in capitals in the HTML; the gate's "a word is not an acronym just because it is shouted" rule looks for the same word in ordinary case elsewhere on the page and "latest" appears nowhere else, so it had no evidence. The better fix is in the renderer, sentence case in the markup and capitals by CSS, which also stops a screen reader spelling the word out; queued today. IQ sits inside the school label "Mental Health and Emotional IQ", written by the theme (the course card's school tag and the footer). The gate's registered names are read from DSRD 5's tables, which carry the course "Master Your Emotional IQ and Revolutionise Your Social Skills" but not the school's label in that form, so the course-name carve-out could not reach it. **One question for you:** is "Mental Health and Emotional IQ" the school's registered name? If yes, DSRD 5 should carry it where the gate reads, or the gate should read the school table too; if no, the theme's label is the fault and it is a theme queue line. DSRD and S063 are the sheet's notes, class 3 above.
- **The Firefox line in chapter 11, dated 2026-08-24.** "Firefox could not start" is the machine's fault: the browser checker has only Chromium installed on this machine, and Firefox is a download that waits on Kain's yes, asked in today's sitting. The page was never at fault on that line, and the Chrome half of the check found nothing.

The three checker fixes (component-internal headings, the section-number opener, the shouted label) are one tooling pass with acceptance, mine, named here so the eight lines stop being counted against pages. Until it ships, the record's chapter 1 and chapter 2 lines quote the gate as it stands.

## 5. True of a page the standards never contemplated, five lines

/cards/ matches no address DSRD 1 names; there is no breadcrumb; nothing on the site links here across all 431 pages; the page has never been scored by Rank Math; no focus keyword is set. Every one of these is correct as a reading, and every one is correct as a fact about the page: the card sheet is a workbench page, rendered only with the workbench key, never linked, never meant to be found, never written for a search. Neither DSRD 1 nor DSRD 6 contains the word workbench, so the gate has no sentence to read these lines against. **My proposal is one sentence in DSRD 6 section 12,** naming workbench sheets as a page type that keeps chapters 1, 2, 7, 10 and 11 in full, keeps chapter 3's title and description, and is exempt from chapter 4, chapter 5's address, breadcrumb, inbound link and Rank Math items, and chapter 6, with Kain's approval per section 0; the gate then reads the exemption the way it reads the policy carve-out, and the next workbench sheet inherits it. The alternative is five recorded exceptions on this one record, which the next sheet would need again. Yours to write either way.

## 6. The derivative line

"dsrd6-record: 0 closed, 5 not run, 6 fail" reads the record back to itself and closes when the lines above close.

## What changed where

- **The install:** post 10903's Rank Math description set (build ground, noindex; no status touched, nothing published).
- **The theme queue:** five lines added under Open: the sheet's missing hairline, the commerce cards' tick glyph outside the registry, the card renderers' `large` image request, the member card avatars, and the featured card's capitalised overline.
- **The record:** `Cards/DSRD6_RECORD.md` machine lines rewritten from today's run by the board's sweep, dated 2026-09-05, machine rows only.
- **The inbound link map:** rebuilt from all 431 pages (it was built against 3 September), which is what turned the orphan line from "map stale" into a real answer, for this page and for every page's next gate run.

OWED BACK: from you, the six notes (the rewrite, or the ruling that they are outside section 3.3), the DSRD 6 section 12 sentence for workbench sheets (or five exceptions on this record) for Kain's approval, and the answer on the school's registered name for DSRD 5. From me, the tooling pass on the three checker false positives, with acceptance, at S103. From Kain, the colour rulings already scheduled (the type pass render and the footer sitting), which close chapter 7 here as everywhere, and his yes to the Firefox download for chapter 11.

*No em or en dashes in this file; checked before writing.*
