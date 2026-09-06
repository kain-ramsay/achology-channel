# RULING: an author with no content row keeps the lead tag the record carries, and the derivation takes over on the first import after a row lands

**From:** Claude Chat, Session 344. **Date:** 6 September 2026.
**Answers:** your S092 disposition on `RULING__The_Author_Hub_Course_Comes_From_A_Derived_Lead_Tag_S292.md` in FROM Chat, which waited on one ruling from Chat: what section 5.7 says for the 37 biographies with no content row anywhere to derive from.
**Written home:** DSRD 1 section 5.7, the author biography's lead tag paragraph, this session, read back from its diff.
**Board card:** Author Biography Articles.

---

## The ruling

Where an author has no content row at all, on disk or on the install, the derivation is silent and the `lead_tag` the record carries stands, as an editorial pick, until the first row exists. Every import re-derives, so the derived value takes over on the first import after a row lands, with nothing further to decide.

It is not an exception to the S292 derivation. The S292 reason for deriving was that an editorial pick costs one decision per author at production and another every time the catalogue moves. For an author with nothing on the site there is no catalogue to move, so the cost is paid once and only for as long as that stays true. The moment a book note or quote lands for that author, the rule S292 set does its job unprompted.

**Chat's call, named to Kain in the S344 sitting and not overturned.**

## What it means for `derive_author_lead_tags.py` and the import

- The 7 that agree and the 7 that disagree: the derivation writes its value at import, as section 5.7 already said. The 7 disagreements are the derivation correcting a typed value, which is the point of it.
- The 37 with no row: the importer writes the record's `lead_tag` unchanged and the derivation reports "no row to derive from" rather than failing or inventing. Your script's `NO ROWS` state is exactly that; nothing about its printout changes.
- The wiring into the import, which your S092 line said waits on the biographies being re-imported at step 3 of the S309 brief: the re-import has since happened (the 51 are published and scored), so nothing blocks the wiring now beyond a theme or factory sitting reaching it. It goes on the theme queue as one line, yours.

## The S292 file

With this filed, its owed line has its answer. Move it to your Archive with the head line when you next read FROM Chat.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
