# RULING: install Amazon OneLink and tag every book link. Genius Link stays until the UK click test passes.

**From:** Claude Chat, Session 309, 25 August 2026. **Ruled by:** Kain, this session, under Harness Rule 11.
**Answers:** section 1 of `REPORT__The_Book_Note_Page_Audited_The_Amazon_Answer_And_The_Export_S083.md`.
**Account facts:** DSRD 2 section 5.1, the canonical home. Twelve country stores are linked into the UK Associates account. UK tag `kainramsay01-21`.

---

## The ruling

Kain rules Yes: put Amazon's OneLink script on the site. The record that said OneLink needs no script was wrong; your S083 measurement was right.

## What you do

1. Add the OneLink JavaScript snippet to the theme, loaded once on every page that carries an Amazon link (book note pages at least; site-wide is acceptable if simpler). Karen holds the snippet in the Associates dashboard under OneLink. If it is not in the channel or on disk, say so in TO Chat and Kain will get it from her as a file; nobody relays it by hand.
2. Append `?tag=kainramsay01-21` to every Amazon URL in the book note data, all 620 rows, at source (the CSV column), not in the template. OneLink swaps the store and the tag by country; the UK tag is the base because the UK account is the root.
3. Re-render `/learn/psychology/book-notes/mans-search-for-meaning/` and confirm: the script is in the external script list, both buttons carry the tag. File the readback.
4. Kain then does the UK click test in Safari: click the button, land on amazon.co.uk with the tag in the address. The click shows in the Associates report within a day. Nobody buys through it.

## What is not ruled

Genius Link is not cancelled. Karen cancels it only after step 4 passes and Kain says so.

*No em or en dashes in this file; checked before writing.*
