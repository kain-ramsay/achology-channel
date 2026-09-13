# RULING: the book note page takes the article's layout, and the $7 panel comes off it

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 113, factory session. **Date:** Sunday 13 September 2026.
**Given by Kain live in the S113 sitting**, on the rendered pages at achologytest.com.
**Filed under Harness Rule 14.** Theme 0.381.0 is live on the build ground and every ruling below is in it.
**A theme change made in a factory session**, named as Rule 1 requires: it is Kain's word in the sitting that authorised it, and that word is named in every commit.
**Owning documents:** DSRD 9 sections 22 and 32, DSRD 7 sections 3 and 4, DSRD 8 sections 26 and 27. Chat writes them.

---

## 1. His words

> "Book notes template right now, please."

Then, on being shown the grid change and told what differed:

> "Could I ask you first to be really thorough, please? Do literally a section by section comparison of the book notes page up against the article page... you do your best effort first, to then come back to me."

Then, asked whether the $7 membership panel should come off the book note as it came off the article at S112:

> "yes"

And, as a question that turned into a finding:

> "What happens to the article image on the article page that doesn't happen to the image on the book note page?"

## 2. What was measured, and it was measured rather than read

Both pages were walked block by block in a live browser at 1440, and every edge was read off the rendered page. **Nine differences. Eight closed. One left with Kain.**

1. **The reading bar was in the wrong place.** Date and reading time sat at the top of the writing, a screen below the title. Now in the hero directly under the lead, which is where Kain put the article's at S110.
2. **It still carried the writer.** Benjamin Lockwood's photograph and name were drawn there, on a page whose author card at the foot carries both. Removed, on Kain's S112 ruling for the article. The argument is passed empty; the component is untouched.
3. **The lead was a step below the body.** 16 over a 46 letter measure, against the article's standfirst at 21 over 55. Both now read 693px on the rendered page. **This overturns Kain's own S249 approval of 46**, and says so in the stylesheet: his S112 ruling is the later word on the same question.
4. **There was no way to share a book note.** No share row at the foot at all. It now lands at 716 to 968, which is the article's own position exactly.
5. **The side panel drew a second share row.** So the marks appeared twice, at 1016 in the strip and 868 in the foot. The call now passes `panel`, which is what the article has passed since S112.
6. **Related Further Reading printed twice.** Six in the strip and nine at the foot, four of them the same four books. The full width block is off, on the article's own S112 ruling.
7. **The foot was on the wrong left edge entirely.** Signature, author, separators and courses sat at 320 while everything above them had moved to 168. Three left edges on one page. All five now read the article's set: 168, 168, 716, 168, 168.
8. **The $7 membership panel.** Off, on his word above. The book note was the last content page still drawing it, so the two page types now end identically: writing, author with the share marks on his own line, two courses, footer.
9. **The cover did not follow the reader.** The article's picture opens at the top of the side column once the hero scrolls away, 256 square. The book note's cover left with the hero and never came back. The block was present on both pages and silently empty on one, because it read the WordPress featured image and a book note has none. `achology_article_aside()` now takes an optional picture; a caller that passes nothing is untouched. The book note hands in its cover and the cover variant keeps 2:3 rather than being cropped square, 256 by 384, because cropping a jacket to a square cuts the title off the one picture whose job is to show it.

## 3. The one left with Kain, and it is open

**The band's ground.** The article's hero band is the article's own picture, washed almost out, so every article's banner takes its colour from its own subject. The book note's band is a shared bookshelf photograph, the same file on all ninety nine of them. He was asked whether the book note's band should take its ground from the book's own cover instead, and has not yet answered. **It bears directly on `BRIEF__The_Book_Cover_Becomes_A_Drawn_Book...S357`**, which is dispositioned as waiting and carries a head line pointing at this.

## 4. Two things Chat should carry into the DSRDs with care

**One rule, two hosts.** Forty seven selector lines inside the S112 rebuild's own media block in `knowledge-hub.css` now read `:is(.kh-article__body, .bn-body)`. The rail's rules exist once and reach both page types, so a future ruling on the strip reaches both without anybody remembering to copy it. DSRD 9 section 32 should say the book note's reading area is the article's, not a copy of it.

**One property had to be repeated, and why.** `.bn-body { display: flow-root }` earlier in `book-note.css` carries one class, and so does the shared `:is()` selector, so the later sheet won on source order and the grid's `display` never landed while its columns did. One line of `display: grid` sits in `book-note.css` for that reason alone. Found by measuring the deployed page, not by reading the file.

## 5. Recorded because it happened

A stray PHP open tag inside a PHP block broke `knowledge-hub-parts.php`. `deploy.py` refused the whole change set and sent nothing to the server, which is what it is for. Nothing reached a reader.

OWED BACK: Kain's answer on the band's ground in section 3; DSRD 9 sections 22 and 32 written to section 2; DSRD 8 section 26 gaining the aside's optional picture.

*No em or en dashes in this file; checked before writing.*
