**Needs from Chat: update the page records' reader lines and the board from this; the three held items wait on TO Chat/ASK__Two_S448_Briefs_Need_Their_Type_Line_And_One_Tag_Line_Rule_S203.md.**

# SHIP: S448 small fixes, theme side session (S203 family), 0.707.671 and 0.707.673

**From:** Claude Code, theme side session, 1 November 2026. Deployed by the theme main session (deploy.py). Everything below was read back from the server over SSH (SiteGround's bot check blocks this Mac).

## BRIEF__Page_Readiness_Reader_Halves_Fixes_For_Code_S448

- **R1** checked once: shipped S188, the footer button's fix is in the deployed footer.css. Nothing changed.
- **R2** handed to the theme main session: the pinned subject bar's scroll padding belongs in kh-subject.css, the bar's home, which is held under the main session's Lost Rulings CSS board.
- **R3 DONE, 0.707.671.** The words are changed in faq-setup.php, and the term is changed with `wp term update` (the theme's description refresh is a one-time job that has already run). /help/ shows "how Continuing Professional Development (CPD) hours work" once, and /help/certificates-cpd-accreditation/ four times. Neither page still shows the old words.
- **R4 HELD.** The line is in kh-tag-setup.php, not in a term, under Kain's S177 rule "no line may grow"; the new words grow it by four letters. Question in the ASK.
- **R5 (a)** already shipped S189: courses-setup.php carries the hidden " students" on the course card count (deployed copy checked). R5 (b) is for Kain's Safari afternoon and is not started here.
- **R6 DONE, 0.707.671.** /learn/quotes/ shows The Quote, What the Quote Might Be Saying, What Can We Take Away From It?, A Question Worthy of an Honest Answer; the old names are gone. 175 of the 293 published quote articles carry these headings; about 118 still carry the older set (named in the ASK).
- **R7 half DONE, 0.707.671.** "Ten ways into everything Achology offers" stands under Ten Different Ways to Experience Achology on /about/. Reach: the same shared block is on /reviews/ and /testimonials/, and it changed there too. "Achology's journey is one for the history books." is HELD: the H2 page gate intake refuses edits to page-about.php under this brief, which has no DOCUMENT TYPE line.
- **R8 DONE, 0.707.671.** /pricing/ shows "members at the senior and master levels of Achology's five-level certification pathway".
- **R9, R10** not this session: R9 belongs to the site search brief, R10 to the Safari afternoon.
- **R11** waits on the theme main session's CSS board shipping.

## BRIEF__Operation_Cleanup_Finish_The_Small_Jobs_On_The_Board_S448

- **T8 DONE, 0.707.673.** Branch factory/four-decisions-s169 is merged into main: the school button hover shade, the workbench key on course layout options, and the page_gate help-strip carve-out (its test passes 6 of 6). knowledge-hub-setup.php keeps main's 0.707.669 version. Read back: a Help answer answers 200 with its helpful strip, and /learn/anything-at-all/articles/ answers 404. The `?opt-hero=2` course page check cannot run yet, because the build site has no academy page and so no course page. The theme queue line is struck, but its "Also owed" pricing measurement stays open.
- **T15 HELD:** page-workbook-thank-you.php is refused by the same intake. This brief has no DOCUMENT TYPE line either.

Folders: none added, renamed or moved.

OWED BACK: nothing beyond the ASK.

*No em or en dashes in this file; checked before writing.*
