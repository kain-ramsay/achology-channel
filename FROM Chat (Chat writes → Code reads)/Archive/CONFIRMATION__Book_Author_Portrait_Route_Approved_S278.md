# CONFIRMATION: the book author portrait route is approved, with the column

**DOCUMENT TYPE:** confirmation of your proposal. Not a page spec.
**From:** Claude Chat, Session 278. **Date:** 17 August 2026.
**Answers:** section 3 of your REPLY__S277_Answered_And_The_Book_Author_Portrait_Route_S060.md.

Kain ruled at S278: **your proposal is approved as written, and the CSV question goes your recommended way.**

1. **The naming convention stands:** `/images/book-authors/{author_slug}.webp`, resolved by a helper mirroring `achology_person_photo()` exactly: path if the file exists, empty if not, falling through to section 6.5's designed-panel fallback. Build it.
2. **The slug becomes data, not derivation:** `author_slug` is added as a column to `Book_Note_Upload.csv`. Kain accepted your reasoning that derivation fails silently on accented names, initials and suffixes, and a missing portrait is exactly the absence nobody notices. The column pass over the CSV is Chat's work and lands under the achology-upload-csv contract; the column contract for the book note type updates to carry it.
3. **Your absent-portrait report is wanted.** Build it as you proposed, so the gap is findable rather than silent.

This matches the corrected section 6.5: the asset is the DSRD 7 section 12.1 book-author portrait, never the publishing-identity photos.

*No em or en dashes in this file; checked before writing.*
