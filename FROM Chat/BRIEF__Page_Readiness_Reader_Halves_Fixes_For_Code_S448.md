> CODE DISPOSITION, S190: WAITS ON a theme session (read in full by the S190 factory session, which runs the book note import and touches no theme file).

**Needs from Code: eleven small jobs found by Chat's reading of 27 page readiness records on the build site, each with its own done test. Theme jobs; open after BRIEF__Operation_Cleanup_Finish_The_Small_Jobs_On_The_Board_S448, because R2 widens its T10.**

# BRIEF: the fixes from Chat's reader halves on the page readiness records

**From:** Claude Chat, Session 448, Tuesday 27 October 2026. **To:** Claude Code.
**Status:** Operation Cleanup work under Kain's yes on the Operation Cleanup page. Every wording change below is Chat's call inside an approved frame, and Kain may overturn any of them on the page. Nothing here changes how a page looks except where a job says it goes to Kain as rendered options.
**Why:** Chat ran chapters 1, 6, 7 and 8 of DSRD 6 on every built page whose record still read "not run" or carried an old fail there: the Help landing, a Help category and the Help answer template; the Knowledge Hub front page, a subject page, the Articles list, the Quote Articles list, the book note, the quote page, All Tags and search results; the four About pages and the nine policy records; the Courses directory, Enquiries and Pricing. Each record's "Reader half, written by Chat (Session 448, 27 October 2026)" section, in its page's design folder, holds the evidence. The five tag page faults are already yours as T10 to T14 and are not repeated, except where R2 widens T10.

**How each line is read.** What to do, where it shows, and the done test. Measure again before you act: the state below was read on 27 October 2026, with axe-core 4.10.2 at 1280 and 375 wide and a keyboard focus check.

---

## Theme jobs

**R1. Stop the footer's Cookie settings button hiding under the cookie plugin's tab (WCAG 2.2, 2.4.11), site-wide.** The footer carries its own Cookie settings button (`.footer-cookie-settings .cmplz-manage-consent`). The cookie plugin's styles make it `position: fixed` at the bottom right, half below the screen's edge (top 785 on an 800 high screen), exactly under the plugin's own floating Cookie settings tab. A keyboard user who tabs to it focuses a control that cannot be seen. It is on every page. Keep the footer button in the footer's flow (or drop it if the floating tab is the one you keep); which is your technical call. **Done when** tabbing through the footer at 1280 and 375 on any page lands on a Cookie settings control that is fully visible, and only one such control exists in the tab order.

**R2. Widen T10 to the subject bar.** On the seven subject pages, the eight Articles lists, the Quote Articles list and search results, the dark subject bar (`.np-darkbar.is-pinned`) pins beneath the header and runs from 72 to 144 pixels down the screen, while the scroll padding stays at 80. A link brought back to the top by Shift and Tab lands under it. It is the same fault T10 names on the tag page's counter bar, so fix both in one change. **Done when** T10's done test also passes on /learn/psychology/, /learn/articles/, /learn/quotes/ and /?s=confidence at 1280 and 375: a link tabbed to from below, then shift-tabbed back up, is never covered by the header or a pinned bar.

**R3. Spell out CPD in one Help category description.** On /help/ the Accreditation and Certification description reads "how CPD hours work"; CPD appears nowhere else on the page. It becomes "how Continuing Professional Development (CPD) hours work". It is the term's description in the admin (faq_category), so the category page shows the change too. **Done when** /help/ and /help/certificates-cpd-accreditation/ show the new words.

**R4. One banned word in one tag description.** The Build Mental Resilience topic's description reads "remain steady through life's inevitable difficulties"; the steady family is always banned (Content Standard Part 16 rule 5). It becomes "keep your footing through life's inevitable difficulties". It is the kh_tag term's description, so it changes on /learn/tags/ and on the tag's own page. **Done when** no page the build site renders carries "steady", "steadier", "steadily" or "steadiness" outside a quotation.

**R5. Give the course card's student count a word.** On the shared course card (DSRD 8), the count ("169,171") sits beside an icon hidden from screen readers, so it is read as a bare number (open since S391). Two parts. (a) Now, with no visible change: add hidden text so the count reads as "169,171 students". (b) For Kain's Safari afternoon (BRIEF__One_Safari_Afternoon_Every_Sitting_Waiting_On_Kain_S448): four rendered options for a visible word or label on the count, on the Courses page, at 1280 and 375, one of them a reading he did not ask for, with your recommendation named. **Done when** (a) the accessibility tree on /courses/ reads each count with "students", and (b) the four options are ready in the Change Viewer for that afternoon.

**R6. Make the Quote Article Anatomy match the quote articles' headings.** On /learn/quotes/ the anatomy names the four parts "An Idea That's Worthy of Your Consideration", "What the Quote Might Be Suggesting to Us", "What Can We Learn From the Idea" and "A Question That Deserves an Honest Answer". The quote articles carry "The Quote", "What the Quote Might Be Saying", "What Can We Take Away From It?" and "A Question Worthy of an Honest Answer". The anatomy takes the headings the pages carry, word for word, and keeps its Part 1 to Part 4 labels. **Done when** the four anatomy names on /learn/quotes/ match the four headings on any quote article.

**R7. Two filler lines on the About page.** On /about/: delete the sentence "Achology's journey is one for the history books." (the line before it already says what the story holds); and "A gateway into every aspect of Achology's learning ecosystem" becomes "Ten ways into everything Achology offers". "Journey" and "ecosystem" are on Part 16's flagged list and carry no weight here. **Done when** /about/ shows neither old line and the new one stands under Ten Different Ways to Experience Achology.

**R8. Identify "Senior and Master Achology members" on the Pricing page.** The free sign up line reads "a handful of FREE live events that our Senior and Master Achology members make available to the general public each week". It becomes "a handful of FREE live events that members at the senior and master levels of Achology's five-level certification pathway make available to the general public each week". **Done when** /pricing/ shows the new words.

**R9. A search that finds nothing must say so.** Today /?s=zzqxv reports "1 result for zzqxv", with a quote article as Best Match and another as Related, though neither contains the word. Add this as a done test to BRIEF__Site_Search_One_Search_For_The_Whole_Site_S448, which rebuilds the search: **done when** a search for a string no page contains says that nothing matched and offers a way on (the A to Z topics, or the Knowledge Hub), with no Best Match shown.

**R10. Four options for the topic quilt on a phone, for Kain.** On /learn/tags/ at 375 wide the 36 topics show as 36 coloured icons with no words; the legend names only the four colours, so a reader taps blind (a DSRD 6 chapter 8 hindrance, open since 21 October). The quilt is Kain's approved design, so this goes to the Safari afternoon: four rendered options at 375 and 320, in the Change Viewer, one a reading he did not ask for, with your recommendation named. Nothing changes at desktop width. **Done when** the four options are ready for that afternoon.

**R11. The "Quote Articles" door's arrow is cut off on a phone.** On /learn/tags/ at 375 wide, the arrow on the Quote Articles door in the four kinds of reading runs past the door's edge. Make the label and arrow fit; how is your call; nothing changes at desktop width. **Done when** all four doors show their whole label and arrow at 320, 375 and 1280.

---

## What is not in this brief, and why

- **Three questions for Kain**, on the card Decisions for Kain: renaming the Deep Dive tag (an always-fail phrase), renaming the Empowerment topic (an always-banned word), and whether the Knowledge Hub's navigation labels (Workbooks, schools, the tag page counters) count as wayfinding. A fourth asks whether the Pricing page's closed question answers take the exception Kain approved for the About page. If he says yes to a rename, Chat sends the words as a ruling.
- **The machine halves** of chapters 1 and 7 on several records still carry old fails that no longer reproduce (the "LATEST" acronym, the subject page's August contrast fail, the Enquiries link fail, DiMAP). They are yours to re-run under job F2 of the Operation Cleanup brief; Chat has not touched a machine line.
- **Cosmetic findings** are logged in each record and not sent: the repeated lead sentence on every policy page, two Pricing phrasings, the Articles list's description, the "Quotes" tab name, and the 320 wide two-column newest grid on /learn/.

## The report back

One SESSION_REPORT as usual, with R1 to R11 each marked done (with its proof), waiting (on what), or not started. Chat updates the records' reader lines and the board from your report the same day.

OWED BACK: R1 to R11 marked done with proof, waiting on what, or not started, in your SESSION_REPORT, to TO Chat.

*No em or en dashes in this file; checked before writing.*
