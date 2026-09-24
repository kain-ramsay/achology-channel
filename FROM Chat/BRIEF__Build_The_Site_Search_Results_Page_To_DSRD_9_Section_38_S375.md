> **CODE DISPOSITION, S134: WAITS ON search.php existing in the theme (a theme session).** Re-checked against the record S134, `ASK__The_Stock_Take_Code_Side_And_What_Chat_Owes_S134.md`.

> **CODE DISPOSITION, S128: WAITS ON `search.php` existing in the theme.** The brief arrived mid-session, during the pricing page's schema change set, and H6 stopped the work so it was read in full before the next edit: it cancels nothing in hand. It is a theme sitting of its own and is not started here, because a page spec of this size taken on at the tail of another page's change set is the "while I am in here anyway" Rule 3 exists to stop. Its superseded predecessor, `BRIEF__Render_The_Search_Results_Page_For_Kain_In_Safari_S366.md`, is archived at S128 on this file's own instruction.

# BRIEF: Build the site search results page to DSRD 9 section 38, and configure SearchWP to DSRD 1 section 7

**From:** Claude Chat, S375, Tuesday 22 September 2026. **To:** Claude Code.
**Board card:** Site search: SearchWP across the whole site, and the search results page.
**Signed by Kain in Chat at S375:** the block order (yes), the result row as option B (yes), the no-results page with its two additions (yes).

**DOCUMENT TYPE: page spec (standing rule 19).** This brief plus DSRD 9 section 38 plus the two approved prototypes in the Search Results Page folder (inside Knowledge Hub Design Prototypes; its README names them) are the whole instruction. Where they disagree, the prototype wins on shape, section 38 wins on every value, and this brief wins on order of work. Nothing here is a question; where a fact is not yet known, the fallback is written in so the build does not stop.

This supersedes `BRIEF__Render_The_Search_Results_Page_For_Kain_In_Safari_S366` in FROM Chat: the render it asked for has happened in Chat's panel and Kain has ruled, so that file is closed by this one. Move it to Archive when you read this.

## What to build

**1. The results page.** A `search.php` template at WordPress's own search address (`/?s={term}`), laid out exactly as DSRD 9 section 38.4, with `noindex, follow` (DSRD 1 section 10). Read section 38 whole before starting; it names every value's home. The parts, so nothing is invented:

- The field: DSRD 7 section 5.5 values, pre-filled with the query, the primary button as Submit. The field's `<form>` is the same one the header uses (one search, DSRD 1 section 7.4).
- The count line, the control bar, the hairline, the pagination and the footer spacing: section 38.4 items 4 to 9, every value copied from the locked sections it names.
- The result row: the mini card (DSRD 8 section 6.9; `cards.css` `.card--mini`) in a new full-width variant, plus the snippet. Add the three new type labels and thumbnails (Course, Help, Page) per section 38.4 item 7. The snippet is SearchWP's excerpt with the matched words at weight 600. Use the `mini-card-thumb` image size already registered for the four Knowledge Hub kinds; the three new kinds carry no image.
- The pills filter by post type (the four Knowledge Hub types, `faq_article`, the course pages, and everything else as Pages); sort is relevance or date. The Category second row appears only when a Knowledge Hub type pill is selected (section 38.4 item 5).

**2. The no-results state,** section 38.5, on the same template when the result count is zero: the not-found H1 in Kain's S366 words, the hint line, the seven category cards (the locked card, names from DSRD 1 section 4), the workbook capture (DSRD 4 section 5; the Kit form per DSRD 3 section 3.1, placed by shortcode), and the ask line to /enquiries/. **The hint line has two forms** (section 38.5 item 5): if SearchWP on the install can supply a spelling correction, "Did you mean {term}? Or try a shorter phrase." with the term as a link running that search; if it cannot, "Check the spelling, or try a shorter phrase." Ship whichever the install supports and say which in your report.

**3. SearchWP configuration,** to DSRD 1 section 7.1, read whole: one engine over every post type named there; title and Rank Math focus keyword (`rank_math_focus_keyword`) weighted above content; ACF fields indexed for the book notes (Code's own S087 finding); stemming on; synonyms on, seeded with the abbreviations DSRD 1 section 7.1 names (CBT, NLP, EQ, DiMAP) and the problem phrase it gives as its example. Exact course, book and author names must return that page first: test it with three (one course name from DSRD 5, one book title, one author) and put the three results in the report. Where a feature the section asks for is not in the installed SearchWP (misspellings, phrase synonyms), do not fake it: leave it out, ship the fallback wording, and name it in the report. The six S366 questions in `ASK__What_SearchWP_On_The_Install_Can_Actually_Do_S366` are answered by the same read; answer them in the same REPLY.

**4. The Speed Optimizer exclusion** your own S087 reply named: exclude the search address from SiteGround dynamic caching so results never go stale.

**5. The 404 page's search box.** DSRD 9 section 28.9 held the box back until a search template existed. It now does: put the DSRD 7 section 5.5 field on the 404, per DSRD 1 section 7.4, and note it in the report so Chat reopens section 28.9 to record it.

## Order of work

1 and 2 together (one template), then 3, then 4, then 5. The header search control and the dropdown preview are **not** in this brief: they stay with `BRIEF__Render_The_Header_With_A_Search_Control_For_Kains_Eye_S321`, a Safari sitting for Kain, and are built after he rules there.

## Definition of done

The page passes DSRD 6 (standing rule 15), with its record returned to the Search Results Page folder alongside a build sheet (S257). Kain has seen both states live in Safari and ruled; any change he makes there folds back into the prototype as its next version and the sheet, per rule 16's fold-back. The card closes on this line from you: "Search results page and no-results state live at {theme version}, DSRD 6 record filed, SearchWP configured to DSRD 1 section 7 with these exceptions: {none, or the list}."

## OWED BACK

One REPLY file to TO Chat: the theme version, the DSRD 6 record's location, the three exact-name test results, which hint-line form shipped and why, the six S366 answers, and the 404 note.

*No em or en dashes in this file; checked before writing.*
