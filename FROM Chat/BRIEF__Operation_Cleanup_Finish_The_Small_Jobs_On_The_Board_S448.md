> CODE DISPOSITION, S186: WAITS ON the founder pages' sign-off (Kain, S186: finish those pages first); theme jobs start after it.

**Needs from Code: the small jobs that stop open board cards from closing, each with its own done test. Theme jobs first, then factory jobs. Do them in the order written, unless one is waiting on the thing named beside it.**

# BRIEF: Operation Cleanup, finish the small jobs on the board

**From:** Claude Chat, Session 448, Tuesday 27 October 2026. **To:** Claude Code.
**Status:** approved by Kain on the Operation Cleanup page, 27 October 2026 ("Yes, thank you Claude"). It sits at the head of the queue file, behind only the S448 quote import. The board cards it names were rewritten the same day to match it.
**Why:** Kain, today: "Our goal here right now in Operation Cleanup is to start finishing things." Chat checked all 22 open cards on the Website Project Board against the build site and the channel. Most are not stuck on anything hard. Each is waiting on one or two small jobs that nobody has picked up. This brief collects Code's share in one place, so the cards can close.

**How each line is read.** What to do, where its specification already lives, and the done test that closes it. Every specification named here already exists; nothing below asks you to guess. Where a line waits on Chat or Kain, it says so and you skip it until that arrives. Measure again before you act on any line: the state below was read on 27 October 2026.

---

## Theme jobs

**T1. Put the 36 tag pages into the sitemap.** Today the sitemap index lists articles, book notes, quotes, Help answers, Help categories and the seven subject pages, but not the tag pages: `kh_tag-sitemap.xml` answers 404. This is a Rank Math setting for the `kh_tag` taxonomy. Card: Knowledge Hub Nav pages. **Done when** the sitemap index lists a tag sitemap and it holds all 36 tag pages. While you are there, confirm `workbook` should not have a sitemap yet (no workbook is published) and say so in your report.

**T2. Enter the Rank Math title and focus keyword on each of the 36 tag pages.** Today every tag page's title is WordPress's default, for example "Build Confidence Archives". **Released the same day:** the words are in RULING__The_36_Tag_Page_Search_Titles_And_Focus_Keywords_S448, approved by Kain. **Done when** all 36 tag pages show their new titles in the page source on the build site, read back one by one.

**T3. Build the Accreditation page and the Certification page together.** Both specifications were signed and both prototypes approved at Session 364, in the Accreditation Page and Certification Page design folders (Homepage and Commercial Design Prototypes). Neither page exists on the build site. They go live together. **Done when** both pages answer 200 on the build site, match their prototypes at the three widths, and are ready for Kain's one Safari sitting, where he writes the final words with you and supplies the two certificate pictures.

**T4. Build the course page template.** Its specification was signed at Session 333 and lives in the Course Page design folder (Academy and Courses Design Prototypes). None of the 28 course pages exists on the build site yet; the address for a course redirects elsewhere today. **Done when** one course page renders on the template on the build site, ready for Kain's Safari sitting on the six visual decisions in section 6 of the specification.

**T5. Build the What Achology Believes page.** The brief is already in your tray: BRIEF__The_What_Achology_Believes_Page_And_The_Seven_Beliefs_Series_One_Brief_S390. Your own S139 disposition said it waited on a content type for the series in content_gate_standards.json. That is a technical choice and it is yours: pick the type, write it, and carry on. **Done when** /about/what-achology-believes/ answers 200 on the build site, ready for Kain's Safari sitting on italics, the close and the course page link.

**T6. The plugins still open.** Named on the Plugins card. Which product to use is a technical choice and is yours; choose the lightest that meets DSRD 3.
1. Email sending. WordPress's own mail on the host already delivers the enquiries form (Kain confirmed the test arrived, Code's S180; DSRD 4 section 5.3). Whether a mail sending plugin is still needed for reliable delivery at launch, as DSRD 3 section 3 names, is your technical call: either install it and prove a test email arrives, or record why the host's mail stands. **Done when** that decision is in your report with its proof.
2. ~~The enquiries contact form~~ **Already done, struck by Chat the same evening:** built at 0.707.501 with mistake reports routed to editorial@ at 0.707.505 (DSRD 4 section 5.3). Chat listed it from an out-of-date board card.
3. Google Tag Manager, with the ten named events in DSRD 10 section 10. **Mind the one irreversible hazard on the Hosting and Go-Live card:** the build site holds the live site's Google Analytics property, and Rank Math Analytics must never be switched on here. **Done when** the container loads on the build site and each of the ten events is seen firing in preview mode.

**T7. Open the site to AI crawlers as the Plugins card lists:** the per-crawler allow rules, the machine-readable pointer file (`/llms.txt` answers 404 today), and removing any snippet-limiting directives from Knowledge Hub and Help pages. The build site stays hidden from search until cutover; build these so they switch on with it. **Done when** each piece exists and is listed in your report with how it switches on at cutover.

**T8. Merge the four small decisions Kain approved at your S169 sitting.** First open line of 000__THE_THEME_QUEUE.md: branch `factory/four-decisions-s169`. Write the carve-out's test, merge, deploy, and check one Help answer, one unknown Knowledge Hub address and a course page with `?opt-hero=2`. **Done when** the line is struck in the queue.

**T9. Fetch the captions for the 14 member testimonial videos.** For the card Testimonials and Reviews pages: one full review of both, the improvements, then the 14 new videos (created S448; it replaces Finish Member Testimonials Page). Do not change either page yet: the review comes first, and you build every approved change to both pages in one go afterwards. Fetching captions does not need the speakers' names, so it does not wait on Kain: pull each caption track from Vimeo folder 20119371, or make a transcript from the audio where none exists. Today the page shows 9 videos. **Done when** 14 transcripts sit in the Video Testimonials Page folder, one file per video, named by its Vimeo number.

**Added the same day, from Chat's reading of the tag page's DSRD 6 record (chapters 1, 7 and 8, written into the Tag Landing Page folder's DSRD6_RECORD.md, Reader half, S448).** Five small fixes, each tested on /learn/tags/build-confidence/.

**T10. Stop the pinned counter bar hiding the focused link (WCAG 2.2, 2.4.11).** The scroll padding is 80px for the header, but the counter bar pins beneath it to about 113px, so a link brought to the top by keyboard sits under the bar. Raise the scroll padding on pages that carry the pinned bar so it clears both. **Done when** a link tabbed to from below, then shift-tabbed back up, is never covered by the header or the bar.

**T11. Stop the course card cutting off its third stat (WCAG 1.4.10).** "13+ hrs Video" runs past the card edge at 320 and 375 wide. This is the shared course card (DSRD 8), so the fix lands everywhere the card appears. How it wraps is your technical choice; nothing may change at desktop width. **Done when** every stat on the course card is whole at 320, 375 and 1280.

**T12. Name the pause's "Read This Quote Article" link.** The six quote cards' links each name their quote; the pause's link does not. Give it the same pattern of name. **Done when** the accessibility tree shows the pause link naming its quote article.

**T13. Turn off WordPress's guessing of a page from a missing address, site-wide.** Today a missing address is redirected to whatever post's slug starts with its last part: /academy/personal-growth/ (the unbuilt school page, which the tag page's Relevant School counter links to) lands on the article personal-growth-requires-discomfort; /people/ lands on people-first-leadership; /courses/life-coaching/ lands on a Help answer. A missing page must answer 404 until its real page exists, or the redirect map's checks cannot be trusted either. **Done when** those three addresses answer 404 on the build site, and every redirect you set on purpose still works.

**T14. One word on a shared line (Chat's call, inside the approved frame; Kain may overturn it).** In taxonomy-kh_tag.php and the shared panel in knowledge-hub-parts.php, "ready to delve into human psychology" becomes "ready to go deeper into human psychology". "Delve" is on the Content Standard's list of machine tells that always fail. Leave the verbatim reviews alone. **Done when** no page the theme renders carries "delve" outside a quoted review.

## Factory jobs

**F1. Finish the redirect map's road to staging.** Your brief is BRIEF__The_Redirect_Maps_Remaining_Build_Chain_Register_Through_Staging_S339. The order the card holds: add the redirect mode to publish_gate.py (row ruled in the workbook, the five chain facts TRUE, the one hop test passing, a 301), then type the eleven folded addresses from RULING__The_Eleven_Folded_Addresses_Row_By_Row_For_You_To_Type_S346, leave the homepage row with no redirect at all, then run the redirect checker on staging. **Done when** the checker's result on staging is in your report with its count of passing rows.

**F2. Mend the acronym check and re-run two machine chapters.** On the Project Cleanup card since Session 295: the acronym check gave wrong answers both ways (three of five chapter 1 verdicts were wrong), and every chapter 5 machine line was measured before DSRD 6 Version 7 widened that chapter, so all of them are void. **Done when** the check is fixed with a test, and chapters 1 and 5 have been re-run on every page record, with the count of records changed.

**F3. Answer one number for the Cards and Chrome Sweep card.** The card says 37 components; your census said 78. **Done when** you send the true count and a one-line reason for the gap.

**F4. Confirm two old items that never came back.** Both on the Plugins card. (a) The S317 ruling widening the publishing wall, H9, to cover unpublishing and deleting a live page: send its acceptance printout, or say it was never built. (b) The S329 question: four field groups (about videos, book note, review, workbook) show local JSON newer than the database; say which way each drifted, and sync nothing yet. **Done when** both answers are in your report.

---

## What is not in this brief, and why

Chat owes its own share and is doing it now: the 36 tag page titles (for T2), the tag page record's reading chapters and redirect plan, the one page plan for SearchWP, the workbook page specification, the reading chapters on the 13 page records left, and the welcome emails for the five sign-up forms. Kain's share is a handful of answers and one long Safari sitting with you, which Chat will set up as a single afternoon so it is not spread across a month.

## The report back

One SESSION_REPORT per session, as usual, with each line above marked done (with its proof), waiting (on what), or not started. Chat updates the board from your report the same day.

OWED BACK: each of the 18 jobs marked done with its proof, waiting on what, or not started, in your SESSION_REPORT, to TO Chat.

*No em or en dashes in this file; checked before writing.*
