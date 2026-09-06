# SHIP and FINDING: the book note cover reaches the analyser, and 90 is out of reach without content

**From:** Claude Code, Session 103, theme session. **Date:** 5 September 2026.
**Shipped:** theme v0.167.27, deployed with its three proofs, local and server and zip all agreeing.
**Board card:** the Knowledge Hub score work, and the Codex theme audit.

---

## What shipped

The Rank Math analyser now receives the book note's cover.

The queue line described the cause as the cover being drawn outside the reading column. Measured on the install this session, it was something slightly different and worth having right: book note 33852 carries 7,867 characters of real editor content, so the feed's guard held it back on purpose, and the analyser read only the stored body. That body carries no picture at all, because the cover is drawn by the template from an ACF field. The guard was correct about words and wrong about pictures.

So a page with a full editor now keeps its own words, exactly as before, and is handed the pictures its template draws, and nothing else.

Two more things rode with it, both from the audit's small-hardening line:

The `<main>` extraction is a DOM parse rather than a regular expression. The old pattern stopped at the first closing main tag anywhere in the document, a comment or a third party's inline script included, and a page analysed on a fragment of itself scores low with nothing anywhere saying why.

The loopback fetch now verifies the certificate and waits five seconds rather than ten. It was sending `sslverify` false. The build ground's certificate verifies cleanly, measured before the line changed.

The cover's address and its alt now have one owner, `achology_book_note_cover()`, read by both the template and the feed, so the alt Rank Math tests is the alt a screen reader announces.

## The finding, and it contradicts the queue line

The queue line said a book note would read about 93 with the cover fed and the alt carrying the keyword. It reads 88 at best. Measured, not estimated, on two live notes after the deploy:

**33852, why-zebras-dont-get-ulcers:** stored at 85 before, reads 86 now.
**35418, the-skilled-helper:** reads 85 now, with `keywordInImageAlt` earning its full 2.

The reason the gain is small is that **Rank Math scores `contentHasAssets` at 1 of 6 for a page with images**. The other five points want a video. Feeding the cover earns one point, not six. That is the whole of the error in the estimate, and it was an estimate rather than a reading.

So the honest arithmetic for a book note today is 85, plus 1 for the cover, plus 2 where the alt carries the keyword: **88, against a 90 bar.**

The rest of the gap is content, not theme. On both notes `lengthContent` earns 3 of 8.

**This needs a decision that is not mine.** Either the bar for book notes comes down to 88, or book notes carry a video, or their bodies grow. The first is Kain's, the second and third are yours and Cowork's. Nothing in the theme can reach 90 from here, and I would rather say so than keep shipping small theme changes towards a number that cannot be met.

## One data fault found on the way

33852's alt reads `Why Zebras Don't Get Ulcers: Summary and Key Ideas cover` with a curly apostrophe, because the alt is derived from the page title. Its stored focus keyword uses a straight apostrophe. The two do not match, so that note alone earns nothing for its image alt while 35418 earns the full 2. Any book note whose title carries an apostrophe has the same fault. Yours or Cowork's to settle, at the keyword or at the title, not the theme's.

## Still owed on this line, and it is mine

The 65 live book notes carry stored scores taken before this change. They want one re-score run so the score table stops disagreeing with the pages. Not done in this sitting, which Kain set aside for clearing the theme queue.

---

OWED BACK: the ruling on the 90 bar for book notes, given the measured ceiling of 88. And a word on the apostrophe, which is a keyword or title decision.

*No em or en dashes in this file; checked before writing.*
