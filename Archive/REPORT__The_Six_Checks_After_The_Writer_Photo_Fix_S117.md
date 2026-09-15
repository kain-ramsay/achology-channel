# REPORT: the six checks Kain asked for after the writer-photo fix

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Method:** all 197 published articles' live pages fetched fresh and read, not sampled; the theme's code searched whole for every other place a person is resolved and drawn.

---

**1. Proved the fix on all 167, not just the two sampled.** All 197 published articles checked. Zero carry the mid-body photo outside `instructor-attributed`.

**2. Checked the 30 instructor pages the other way.** All 30 still show it. The fix removed nothing it should not have.

**3. Searched the whole theme for the same mistake.** Every other place a person's photo is drawn was read: the course page's instructor photo (real instructors, correct), the book note's real-world book-author portrait (a different field, a different person, correct), the footer signature card and the Knowledge Hub card byline (both meant to show whoever the true author is, on every type, which is correct by design), and the Listen bar's narrator credit (same reasoning). **One thing worth naming rather than treating as clean: `single-quote.php` resolves an author the same way the buggy code did, but never draws a photograph from it today**, because the quote page's build is not finished. Nothing wrong yet; worth the same care when that feature is built, so this is not rediscovered.

**4. Checked for a gap left by the removal.** None found on any of the 197.

**5. Checked whether the authors make sense.** The split: Benjamin Lockwood writes all 51 "who is this philosopher" biography pieces and 9 of the school-subject articles; Charlotte J. Avery writes 84 of the school-subject articles; Declan Fitzpatrick 12; Evelyn Montgomery 11. One clear owner per content type, no scattering, nothing that reads as randomly assigned. **This checks the pattern, not the judgement**: whether Evelyn was the right choice for her specific eleven is not something a machine can confirm, only that the assignment is deliberate-looking rather than accidental.

**6. Checked the header image on all 197.** None show a staff photo as the page's main picture.

**One small, harmless thing found along the way, not related to the bug:** `single-book_note.php` resolves Benjamin Lockwood's data for the reading bar and then passes an empty string instead of using it. It draws nothing either way and nothing on the live site is wrong; it is dead code, not a defect, and worth a line whenever someone is next in that file.

---

OWED BACK: nothing. Both files are closed.

*No em or en dashes in this file; checked before writing.*
