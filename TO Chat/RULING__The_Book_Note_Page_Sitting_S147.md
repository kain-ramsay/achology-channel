Needs from Chat: write Kain's S147 book note ruling home (DSRD 9 book note section; the side panel and quote page design folders for the shared foot), with a dated line; theme session.

# RULING: the book note takes the quote page's structure (S147, theme session)

**Kain's words, in the Safari sitting on Words That Change Minds:** "a definite yes to the bubbles behind the book ... I think we just actually need to apply the same page structure to book notes as what we apply to the quote articles. Where we have a panel for explore more book notes underneath the actual article and that just frees up the right panel to allow the book to float right down the page."

**Shipped, theme 0.707.83 and 0.707.84, live on the test site:**
1. "Explore More Book Notes" sits after the signature's hairline: the quote page's block, markup and S130 rules (six, or three, or none; two columns from 768; arrow at the right edge). Lines are other book notes in the same category, newest first, written "Book Title by Author" from the two source book fields. Mark: the registry's book-open, upright. A sixth contents entry, "Explore More Book Notes", appears where the block does.
2. No Related Further Reading in the side column on book notes. The panel, with the cover, now travels to the hairline closing Explore More Book Notes and rests 48 above it (measured at 1440 and 1210: block ends 4145, hairline 4193, panel's last item 4145).
3. Three Achology bubbles behind the hero cover, the quote page's sizes, from 1200 up; the band trims the large bubble at its edge (it caused a 27px sideways scroll at 1210, fixed at 0.707.84).
4. The More list's CSS moved from quote.css to knowledge-hub.css so both page types read one copy; quote pages unchanged.

**Measured:** no sideways scroll at 1440, 1210, 768, 375; page gate boundary lines pass; the gate's remaining fails are the page's earlier content and image lines, unchanged.

**Open, with Kain:** (a) the line under the heading: the quote page has Kain's own subtitle, the book note block has none yet, so its icon tile is squashed to 30 tall until his words arrive; Code does not draft it. (b) Below 1200 the foot still draws Related Further Reading after the courses (the shared foot's narrow copy), so a phone reader meets two "read next" lists; the quote page draws the same narrow copy. Principle 3 says keep one; asked of Kain.

**Later in the sitting, shipped 0.707.85 and 0.707.86:**
5. The panel's cover and Amazon button lock to the foot of the screen from 1200 up on screens 760 tall or more (Kain: "lock to the bottom of the screen ... right now you've got it floating, which just creates white space underneath the book"; then "Yes, that's much better").
6. The line under "Explore More Book Notes", Kain's approved words (0.707.91, read back live): "Each Book Note highlights a book's key ideas, helping you to decide which one to read next."
7. Kain asked for ten design improvements; Code proposed ten (covers in the list, key ideas box, pull quotes, section numbers on body headings, narrower reading column at about 90 characters a line today, drop cap, ratings as a visual, numbered takeaway cards, a faint tint of the book's colour in the band, a reading progress line). Kain took number 1 first, from four rendered tabs: tab 2, "absolutely brilliant": each line opens with the book's own cover, 56 wide, title then author beneath in grey. Covers drawn at WordPress's medium size, 12 to 15KB each (the full files are 230KB to 1MB).

8. Proposal 4, tab 1 of four, shipped 0.707.87: each section heading in the writing carries the contents' number (01 to 05) as a small orange label before the words, by a counter, hidden from screen readers. Page gate unchanged at 51 passed, 10 failed (the same lines as before).

9. **Proposal 5 REFUSED, a standing ruling:** the reading column's width and the body text size are standardised across every content type and are not changed. Kain: "we can't go playing around with font size ... this is standardized across the entire website ... we just need to make a decision here and move forward ... no changes here at all, must remain as it is." Measured at 1440: the writing is 800 wide at 18px on the book note and on the quote page alike (both start at 168). Nothing shipped. Chat: write it home so the width and size are never reopened.

10. Proposal 7 (ratings as a visual) DROPPED by Code on the record: Kain's own v0.167.21 ruling makes the Essential Reading badge the rating's only visible mark, and the Goodreads score has never been shown (third-party score, his call if ever).
11. Proposal 10 SHIPPED 0.707.88 on Kain's word ("just do it ... drive the session forward"): a 3px brand-orange reading progress line over the header's bottom hairline, book notes only, filling as the writing is read (0 at the top, 0.5 at mid-article, 1 at the writing's end, measured). Four tabs built (full width, thin on a grey track, column only, deepening orange); tab 1 shipped as Code's recommendation, Kain may switch in one word.
11b. **A site standard, 0.707.89:** Kain then chose tab 2 ("thin line on a gray track looks really good ... this might as well be a standard that we apply to all article types ... workbooks as well"). Now on articles, book notes and quote pages: a 2px brand-orange line on a hairline-grey track over the header's bottom hairline, one script and one rule (knowledge-hub.js, knowledge-hub.css), verified present on one live page of each type. Workbooks take it when the workbook page is built (its brief, BRIEF__Build_The_Workbook_Page_On_The_Karpman_Workbook_S366, is still open): Chat, carry that into the workbook spec.
11c. **No Related Further Reading on a book note at any width, 0.707.90** (Kain: "yes, remove it"): the narrow-screen copy at the foot was the last place it drew, so phones met two read-next lists. Measured at 375: signature, Explore More Book Notes, the courses, then the footer; gate spacing lines pass. Side effect to note: the guarded "all articles from this book" line (ruled S361) rode inside that list, so it no longer shows on book notes. Chat: say if it should move into Explore More Book Notes.
11d. **Transparency on the author line, 0.707.92:** Kain: "we're kind of presenting these books as though these different authors have written directly for Achology ... a new layer of transparency". Each line now reads the book's title, then "A book by {author}" (Code's first wording, live for his correction, read back on all six lines).
12. Proposals 6 (drop cap) and 9 (a tint of the book's colour) set aside by Code: both touch the type scale or the brand colours, which Kain ruled fixed at S147 (item 9).
13. **For Chat, words owed if wanted:** proposals 2 (a "key ideas at a glance" box under the opening), 3 (one pull quote per long section) and 8 ("What You Can Take From the Book" as numbered takeaway cards) need new words per book note. Chat: say whether to put them to Kain as a commission for Cowork; Code builds the shapes once words exist.

**New gate line, not hidden:** the six list covers fail image-filename (WordPress's "-199x300" size suffix), image-format (JPG) and image-responsive (no srcset), joining the hero cover's own existing JPG and budget fails. Every book note cover is a master JPG in the media library; WebP copies for all book covers belong on the Image and Icon Optimisation card. Chat: say whether that card takes it.

**Owed (Rule 14 fold-back):** the book note design folder's prototype and build sheet to this state, with the quote page's S146 fold-back still owed.

OWED BACK: Chat writes the ruling home with a dated line.

*No em or en dashes in this file; checked before writing.*
