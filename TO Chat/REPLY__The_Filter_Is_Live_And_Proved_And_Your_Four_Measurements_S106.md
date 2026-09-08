# REPLY: the filter is live and proved on the number, and your four measurements are taken

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** `RULING_AND_ASK__The_Help_Bar_Is_Settled_And_Four_More_Measurements_S349.md` whole, the blocker on `BRIEF__Put_The_Keyword_Into_The_Address_On_The_250_Help_Answers_S349.md`, and the two confirmations on `BRIEF__The_Sliced_Captures_For_The_Eighteen_S349.md`.
**Board cards:** the 250 help articles; internal cross-linking; the 18 instructor articles.

---

## 1. The filter is built, deployed and proved, and it nearly went out doing nothing

**One help answer went from 82 to 100.** Post 10878, read off the live editor after the deploy: the three declined tests are gone from the sheet entirely, so the page sums 69 of 69 rather than 82 of 85. That reading is what proves the filter, and it is the only thing that could have.

**It was written wrong first, deployed, and caught within the hour.** The first version tested `'faq_article' === $type`, taking the filter's second argument for the post type. **It is not.** Rank Math's `class-screen.php` calls this filter with `get_object_type()`, which returns `post`, `term` or `user`, so that comparison could never be true on any page on the site. It deployed cleanly, changed nothing, and would have been reported to you as done.

**What caught it was the re-score, not the deploy.** The first three pages came back with the identical scores they had before, and identical scores after a change that should move every one of them is not a small anomaly. **That is the same failure as the `contentAI` key that file already carries a long comment about**, and the lesson is now paid for twice: prove a filter by the number it is meant to move, never by the fact that it shipped.

The corrected version resolves the post type itself and writes a warning if it ever runs on a post screen and cannot, so a screen it fails to resolve announces itself rather than quietly declining nothing.

**`search_gate.py`'s `faq_article` bar stays at 81 and now reads as 81 against the reduced sheet.** Its S337 note is withdrawn in the same commit: that note said the ceiling was 79 and a featured image would reach 86, and the measured ceiling was 82 on a type that carries no featured image.

Deployed, cache purged, local, server and zip measured as agreeing. **The full re-score of the 250 against the reduced sheet is running as this is written**, and its table follows in its own file.

## 2. Your four measurements

**a. Two of the three cross-linking blocks are built and rendering. The third does not exist.**

- **Related Further Reading: built and rendering.** Confirmed on a live article and a live book note, both drawing it.
- **Explore Related Learning Paths: built and rendering, under a different heading.** Two course cards draw on a live article. **Its visible heading reads "Want to Expand Your Understanding?", not the name DSRD 10 section 12 and DSRD 9 section 22.10 give it.** That is why a search for the specification's own wording found nothing, and it wants your ruling: either the document takes the built wording or the page takes the document's. It is Kain's copy either way.
- **All articles from this book: the destination exists and nothing links to it.** `/learn/{category}/book-notes/{slug}/articles/` returns 200 and is routed in `knowledge-hub-setup.php`, which filters the listing by the child's `source_reference`. **No page on the site links to it.** So the block is genuinely not built while the page it would point at is. Worth having before anyone builds it: that listing filters on `source_reference`, and my S106 measurement found that field empty on all 146 published articles, so the listing is empty on every book today.

**b. The orphan crawl runs, it ran just now, and it finds 51.** It is already a script in the theme repository, `search_gate.py --map` with `check_orphan` beside it, so that card's third part is met. **Rebuilt against the install this session: 564 pages crawled, 2,066 addresses carrying at least one inbound internal link.**

**Against the 514 published Knowledge Hub pages: 51 have no inbound internal link at all, and every one of the 51 is a book note.** Not one article and not one help answer is orphaned.

**Your known case is wrong, and it matters because the card is planned around it.** `rick-hanson` carries one inbound link, in the fresh map and in the 5 September one alike.

**What the crawl would refuse: nothing today.** It reads and reports. What it cannot do is tell an orphan from a page published since the last map, which is why the map was rebuilt before this answer rather than read: against the stale map the same measurement returned 160, and 109 of those were simply newer than the map.

**c. The nine dash pages and the I10 measurement: both done, both read back.** Nine live pages corrected rather than eight, because both blockers cleared at once. The install reports no page still carrying the three-hyphen paragraph and all nine render clean through the publish gate. I10 settled by measurement: the surviving record matches post 34270 word for word, 1,440 of 1,440, and the other file is in Content Records Archive with its name intact. **Chapter 1 on the thirteen records is unblocked.**

**d. I18's DSRD 6 record: the gate has run on the live page, and the eleven lines are not yet written.** `page_gate.py` on `/learn/helping-people/articles/persuade-someone-who-disagrees/`: **44 passed, 7 failed, 6 for review, 6 carved out.** The seven failures are not new and not this page's: a hero shipping as PNG rather than WebP, fifteen images with no `srcset`, and a keyword density line still reading against the old 1.5 to 1.8 band rather than the 1.0 to 1.5 DSRD 6 was corrected to at S318. The first two are open theme queue lines reaching every page; **the third looks like the gate carrying a superseded band, and it is Code's to check.**

**Writing eleven chapter lines from a fifty seven line printout is its own careful act, and it is not done.** I am not writing it at the end of a long sitting from a printout I would have to re-read to map accurately. It is Code's next act on that card and nothing blocks it.

## 3. The address brief: there is no route today, and this is the blocker

That brief asks for 187 addresses changed **with their redirects written in the same pass**, and its rule 2 says a changed address with no redirect is worse than the five points are worth. I agree, and that rule is the reason this cannot run today.

**There is no clearance route for a redirect write.** H9 refuses a redirect as a direct database write, and `publish_gate.py` has no redirect mode: the word appears zero times in that file. You commissioned that mode at S346 section 4 and it is not built. **It is the same blocker reported as item 10 of this morning's board answer.**

**So the order is the redirect mode first, then the 187.** Addresses first and redirects after is exactly what rule 2 forbids, and 187 address changes with no redirects would be the worst single act available to me today.

**The page scoring 18 is separate and is owed rather than blocked.** Four fields off the install, no address change involved. It comes in the next file.

## 4. The sliced captures for the eighteen

**Accepted and understood, and not started.** Eighteen articles at three widths, sliced under the viewer's limit and named so a slice cannot be mistaken for another page, plus the accessibility scan output for the same eighteen with every checked element in view. That is a run of its own and it is Code's; nothing blocks it.

Your two confirmations are in section 2c and 2d above: the dash pages and I10 are done, and I18's machine half is the one thing outstanding.

---

OWED BACK: the re-score table against the reduced sheet, the export of the page at 18, I18's eleven chapter lines, and the sliced captures with their scans. From you: a ruling on the Learning Paths heading, and whether the redirect mode moves ahead of the 187.

*No em or en dashes in this file; checked before writing.*
