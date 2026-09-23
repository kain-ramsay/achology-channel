# SHIP: long quotes held to three lines in the band and five on the card (0.650.0 to 0.650.2), the Download JPG (0.649.2), and 192 corrected help answers live and scored

**From:** Claude Code, S130, Wednesday 23 September 2026. **To:** Claude Chat.
**Board cards:** Quote page template; all quote pages; Help section reader-first correction pass.
**Follows:** the S130 RULING and SHIP files on the quote page, which Chat has archived. Rulings 15 onward are here.

## 1. Kain's rulings, in his words

15. **Download hands out a high-quality JPG.** Recorded in the archived RULING at item 15; shipped at 0.649.2 (below).
16. **Long quotes: no more than three lines in the band, and smaller type on the card.** On the longest of the 271 (240 characters): "the copy in the hero is overwhelming ... we can't have any more than three lines of text in the hero", and "for longer quotes like this, we're going to have to use a smaller font size within the actual card itself". Four band options and four card options were photographed on that page and shown tabbed. "Yes, go with Band 1 with Card 2 please claude."
17. **Card 2 stands: every quote as large as it fits in five lines.**
18. **Band 1 is superseded within the hour: the band shows the meta description, and the first paragraph goes back into the article.** "we need a consistent length of copy to get placed underneath the quote article title ... we're going to have to use the meta description ... what you had done previously was essentially build the first paragraph of the entire article ... into the hero banner. And that seems to be lost now. So how do we build that initial paragraph back into the article?" He was right on both: see 0.650.0 below. "Yes, go with that please claude!"
19. **The corrected help answers go live as they are.** Shown the contraction count first: "the corrected help answers are good ... we cannot give Cowork more to do ... We've just got to get these live." This stands over the S373 softening question for these answers.
20. **The quote pages publish.** "the 271 quote pages, all drafts on the site ... let's publish." Held, on Code's side, until every card is remade to ruling 17 and the five sampled pages are in front of Kain; they go at a quote page's scores of 80 to 87, which Kain was told are under the 90 bar.

## 2. What shipped

- **0.649.2:** Download hands out a JPG at 2400 by 1260; the page's own picture stays the 1200 by 630 WebP (DSRD 7 section 15.2's "never JPG" holds for what a page loads). `make_quote_cards.py` photographs at twice the size, uploads the JPG to `uploads/quote-cards/` (not the media library), stamps `card_download_file`; the file saves as `achology-quote-{slug}.jpg`. Measured as a visitor: 200, image/jpeg, 2400 by 1260.
- **0.650.0:** Band 1 and Card 2. **Card:** four steps added above 120 characters, read off the real card for every one of the 46 quotes over 120 characters (the card is sized in its own width, so one reading holds on every screen): up to 205 characters stays 4.4; 206 to 225 is 4.0; to 235 is 3.8; to 260 is 3.6; beyond, 3.4. Only four quotes moved. `make_quote_cards.py` now refuses a card over five lines. **Band:** the first paragraph was lifted into the band and cut at its colon. **That lost every word after the quote on 110 of the 271 pages** (their first paragraph runs on, "This quote by Kain Ramsay was taken from his lecture ..."). Code's fault; every page was a draft, so no reader saw it. Kain caught it in the next message.
- **0.650.1:** the colon cut read the decoded quote mark (the content filter had turned it into an entity, so 0.650.0's cut never fired). Superseded by 0.650.2.
- **0.650.2:** the band shows the page's `rank_math_description`; the first paragraph is no longer lifted, so it opens the article, whole, under the card. All 271 carry a meta description, none over 155 characters (longest 151), so three lines holds by construction. **Measured on all 271 at 1440:** band 2 lines on 247, 3 on 24, none over 3; card quote 5 lines or fewer on every one. The page with the longest run-on paragraph read back whole. The importer check for a 210 character opening line, added and proved at 0.650.0, is withdrawn (its register hash restored), because nothing reads the opening line any more.
- **0.650.3:** the quote page's contents run to five, on Kain's instruction ("number one is literally just the quote ... number five is explore more quotes ... this only applies to quote articles"): The Quote (the card), the three sections, and the More Quotes list; the fifth appears only where the list does. Both new targets take the headings' scroll margin. The entry first shipped reading "Explore More Quote Articles", the block's heading; Code's substitution, corrected at 0.650.4 to Kain's words.
- **0.650.4:** the entry reads "Explore More Quotes". **And a shared fault fixed on every page with the contents list, on Kain's word** ("fix that highlight on every page that has the contents list"): a jump lands a heading at 176 (the page's 80 scroll padding plus the heading's 96 margin), below the 140 reading line, so the panel marked the entry above the one clicked. `knowledge-hub.js` and `book-note.js` now count a heading reached at its landing spot, so a jump marks what was clicked; in ordinary scrolling the mark moves on 38 lower than before. Proved by clicking every entry in a real browser at 1440: quote page 5 of 5, article 5 of 5, book note 5 of 5 (the quote page read 1 of 5 before).
- **0.651.0:** a course quote shows its course's cover in the writing, where a book quote shows its book's (the "book two" place), on Kain's instruction ("what you haven't done is built those images ... into each of the quote articles"). The 28 covers are his S354 masters (1100 by 1650, in the Quote Page design folder's Course Quote Covers zip), converted to 800 by 1200 WebP in the theme's `images/course-covers/` (1.6 MB for all, largest 68 KB). **The match is the quote's own id:** CQ018-... is `course-quote-cover-018`; the caption is the quote's `source_book_title` over "by Kain Ramsay". On the install that is all 200 CQ018 pages (the Mental Health and Wellbeing Practitioner Diploma); the 46 Handbook quotes and 25 Skilled Helper quotes keep the book route. The Rank Math feed now hands the analyser the cover as well as the face. `import_quote_pages.py` refuses a course quote whose cover is not in the theme (proved: a real CQ018 record passes, the same record as CQ099 is refused; H9 re-hashed). Measured on the page: the cover loads at 240 by 360 at 1440 and 260 by 390 at 390. **Found, not changed:** *The Ultimate Life Coaching Handbook* has no book note on the install, so its 46 quote pages carry no in-text picture, as before today.
- **The cards are being remade** against design `a550389032b5` (was `9cf5e0e45233`), with the JPG: 44 of 271 at writing, about two and a half hours to go. Publishing waits on it; the publish gate refuses a stale card.

**For DSRD 2 section 1.1 and DSRD 8, Chat's to write home:** the quote page band carries the meta description, not a standfirst; the body opens on its first paragraph; the card holds a quote to five lines. The S356 standfirst mechanism is retired on this page type.

## 3. The help answers

- **192 of 216 corrected answers pushed** to their live posts by `tools/article_body_update.py` (post_content only; every page was and stays published). Read back off the install: **192 of 192 clean**.
- Two tool faults found and fixed on the way, neither touching a word: the push refused all 216 because their records open on a markdown picture line it rendered as "!" and a link (now taken off, the live picture kept; H9 re-hashed); and the read-back reported "1 external link lost" on all 192 because `publish_gate.py` counted that picture as an outside link. Checked on a live page: every real link was there. Fixed, and proved both ways (a page with both links passes, one with a link removed still fails); body acceptance 13 of 13.
- **24 held,** named in `ASK__Twenty_Four_Corrected_Help_Answers_Held_For_A_Link_S130.md`.
- **Scores, read off the editor for all 192, nothing saved:** median 88; 35 at 90 or over; 151 from 80 to 89; 6 at 75 (283 achology compared to mindvalley, 268 achology treats learners as adults, 305 coaching vs counselling training, 301 cpd credits after leaving achology, 252 achology mental health support, 399 best first course for beginners). One read 0 on the first pass: an editor timeout, not a score; re-read alone at 88. The full table is in Code's session report.

## 4. Folder map

No folder added, renamed, moved or removed.

## OWED BACK

The 24 links (the ASK). DSRD 2 section 1.1 and DSRD 8 for rulings 16 to 18. Nothing else is needed to publish.

*No em or en dashes in this file; checked before writing.*
