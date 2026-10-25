DONE, Chat S445 (25 October 2026): the five gate lines ruled recorded exceptions under Rule B and written into DSRD 7 section 4.3 as Exception 15; answered to Code as RULING__Courses_Page_Five_Gate_Lines_Recorded_As_Exceptions_S445 in FROM Chat; the band's phone foot named for Kain's next walk-through; board cards moved: none.

NEEDS FROM CHAT: read and rule the five gate lines below as recorded exceptions (or say which to change); nothing else waits on you.

# REPORT: Courses page gate exceptions and clean-up, S180 side session

From Code's theme side session on the Courses page, /courses/, 25 October 2026, theme 0.707.501 on the build site. Started from the S180 theme session on Kain's word in that sitting ("go ahead ... suggest if there's any improvements you would make").

## 1. The spacing check (DSRD 6 section 0), WebKit, 1280, 834 and 390, before and after two ticks

Every gap the page's own rules set reads on the scale: breadcrumb to overline 24, overline to title 8, lede to hairline 32 (24 phones), hairline to answers 48 (24 phones), answers to instruction 24, instruction to band foot 48, band to results 48 (32 phones), heading to cards 32, cards to Explore More 32, results to the FAQs hairline 48 (32 phones). No sideways scroll at any width. No page fault found.

## 2. Gate lines that disagree with a signed choice: no change made, exception proposed

1. **spacing-scale, cd-ticks row gap 12 (desktop, tablet).** Kain chose 12 between the answer tiles on the S143 options (RULING__Kain_Chooses_The_Courses_Page_Tick_Tab_Design_S143). The other eight off-scale spaces are the course card's (cards.css, DSRD 8 section 7), a site-wide component, not this page.
2. **hairline-spacing, boundary 2 (FAQs card to the UKRLP line, 32 not 48).** The FAQs block is a component since S142 (achology_faq_block, help.css), and Kain set the line "balanced, 32 above and 32 below" there. Not this page's to change.
3. **breadcrumb-above and breadcrumb-below.** Already noted in the record at S138: 24 below is Kain's S137 ruling ("48 set it adrift"); above reads 0 because the gate does not count the band's own padding (48, 32 phones, measured).
4. **acronyms: FAQs, ICO, DiMAP.** "FAQs" is in Kain's own heading (Amendment 4, S138). ICO is in the FAQs block's shared credit line. DiMAP is help answer 399's excerpt, still waiting on its corrected excerpt going live. None is in this page's files.
5. **image-lazy-below-fold, tablet and phone, course-007.** The S138 trade already in the record: the first card's picture loads early for desktop's first paint.

The band's foot is 48 on phones too while its top is 32. The build sheet says "48 below the instruction line" with no phone value, so it is left as signed; say if you want 32 there.

## 3. Invisible clean-up in the page's own files (not deployed; the S180 theme session deploys)

- template-courses.php: removed the hidden status line in the follow-along bar and its little script. It was never shown (Kain, S137: the bar carries the button alone) and, being hidden from screen readers too, never spoken. **This corrects chapter 8's note that picking a goal is "announced to screen readers": it was not, before or now.** An honest announcement would need words, which are Kain's; raised here, not built.
- The screen-reader question over the answers takes Kain's S138 cut ("or career" out), matching the lede.
- The sort's screen-reader label read "Sort the six courses"; it now reads "Sort the courses" (nine show since S138).
- Header comment and stale notes brought to the page as built; one dead style removed.
- courses-directory.css checked by swapping the local file into the real page in WebKit at all three widths, both states: every screenshot identical to the pixel, save one patch under the cookie banner from the test's own click.

## 4. Record

DSRD6_RECORD.md is not changed by this session: its chapters 2, 3, 4 and 9 still read not run, and the gate's own run does not map lines to them one for one. The record lines wait for the next full record run.

*No em or en dashes in this file; checked before writing.*
