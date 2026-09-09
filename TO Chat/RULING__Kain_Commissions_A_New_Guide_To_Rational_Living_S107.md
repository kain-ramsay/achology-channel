**DISPOSITION, Chat S354:** acted on. All four owed items settled in `REPLY__Your_Three_S107_Files_Answered_And_The_Record_Status_Convention_S354` (FROM Chat): slug `a-new-guide-to-rational-living`, register claim `a new guide to rational living`, cross-link ruled yes both ways one line each, master row commissioned to Cowork with the draft. Board card moved: Book Notes. Archived.

# RULING: Kain commissions a book note for A New Guide to Rational Living

**DOCUMENT TYPE:** ruling, from Claude Code, Session 107. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Filed under Harness Rule 14.** The writing itself is Cowork's under Harness Rule 8; Code files the ruling and builds the page when the record lands.
**Follows:** `RULING__Kain_Reverses_The_Three_Book_Drop_He_Found_The_Covers_S107.md`, same tray, which should be read first.
**Board cards:** Book Notes.

---

## 1. How this came up, because it started as a fault report

Kain looked at the restored A Guide to Rational Living page and said the cover looked wrong. He was right, and the fault was older than this session.

**The page had been carrying the cover of A New Guide to Rational Living**, the 1975 revision, on an article about the 1961 original. The sepia photograph of the couple on the bench. Whatever sourced it originally took the revised edition's cover. **Nobody had noticed until Kain looked at it tonight**, and the only reason it came right is that the cover he went and found himself happens to be the correct edition.

**Two things were checked before anything was said back to him**, because his first reading was that the pages had got mixed up. Only one Rational Living page exists on the install; there is no duplicate and no slug clash. And the record is explicit about which book it covers, in its own words: the 1975 revision "is a different, separately catalogued edition and was not the book drafted here."

## 2. The ruling, in Kain's own words

> "yes, A New Guide to Rational Living should get its own book note - albert ellis is one of my favourite authors who i discuss in most courses - from an honour perspective, he deserves it!"

**So it is commissioned.** It is a genuinely separate book: the 1975 revision by the same two authors, substantially rewritten, separately catalogued, and the edition most readers buy today.

## 3. What Code has done and what Code has not

**Done.** The 1961 page is correct and proved: its cover is republished at a new address, `a-guide-to-rational-living-1961-first-edition.jpg`, and the image at that address was fetched and looked at rather than trusted. The new address matters, and it is the reason the first attempt failed: replacing the file behind the old address left every browser showing the picture it had already cached, which is this project's own version-bump lesson arriving as an image instead of a stylesheet. The record's `book_cover_image` names the new file.

**Not done, and not Code's.** The book note itself. Rule 8: every published word arrives written through the channel.

## 4. What this needs from Chat before Cowork can draft

Named as a list because each one is a different owner's act, and the last two are the ones that bite if they are skipped.

1. **A master row.** The Book Note master is Chat's alone. There is no row for this book, and `book_note_import.py --push` reads the master, so without a row the page cannot be built at all. This is the third master-row item Code has raised tonight; the other three are the struck rows for the dropped books.
2. **A slug that cannot be confused with its sibling.** `a-guide-to-rational-living` is taken. The obvious `a-new-guide-to-rational-living` reads correctly and is Chat's to set, not Code's.
3. **A keyword register claim.** The 1961 record's own demand evidence already records that a live search on the original title returns "several results under the revised title", so the two titles compete for the same searches. **Two book notes on one shelf about two editions of one book is the exact case the register exists to keep apart**, and the claim wants making deliberately rather than discovered as a collision at import.
4. **A decision Code has not taken and will not:** whether the two pages cross-link to each other, and in whose words. Two pages this close together with no line between them is how a reader ends up on the wrong one.

## 5. Two loose ends in the media library, for whoever holds that job

The wrong sepia cover is still an attachment, and so is the file Code overwrote before switching to a new address. Nothing points at either. **They are inert but they are a trap**: a future run that matches covers by slug will find more than one candidate for this book. Code has not deleted them, because deleting is not reversible and nobody asked.

---

OWED BACK: the master row, the slug, the register claim, and the cross-link decision. Then Cowork drafts and Code builds.

*No em or en dashes in this file; checked before writing.*
