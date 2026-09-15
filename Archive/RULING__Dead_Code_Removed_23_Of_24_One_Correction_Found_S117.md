# RULING: dead code removed, 23 of 24, and one correction to my own list

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `REPORT__Dead_Code_Sweep_Across_The_Whole_Theme_S117.md`, on Kain's word to go ahead.

---

## What was removed

**21 CSS rules and 2 functions, exactly as reported.** Theme version 0.427.0, deployed and confirmed against the server. Checked afterward on five live pages spanning every template the removals touch (homepage, a book note, an instructor profile, a help answer, the Albert Ellis article): all render exactly as before, because nothing removed was ever drawing on screen.

## One correction, found while removing rather than before

**`achology_article_promo_card` was not removed.** Reading the function next to it, `achology_article_promo`, before deleting anything: its own comment records that Kain cut this card from the article page at S112 ("cut the dark course card first please") and that the card's code was deliberately left standing rather than deleted, in his own words at the time that a change of mind should not cost a rebuild if he wants the card back. That is not dead code. It is switched off, on purpose, with the reason written down. Removing it would have undone a decision rather than tidied one, so it stays. **23 of the 24 were genuinely dead; this one was not, and I should have caught it before putting it on the list rather than after.**

## One bigger thing this surfaced, worth a decision of its own

Three of the files this touched (`cards.css`, `faq-icons.php`, and `knowledge-hub-parts.php`, which I left alone) carry a large number of pre-existing em and en dashes in their code comments, dozens in `cards.css` alone. The site's own rule (DSRD 2 section 3.0) bans them everywhere with no exception named, and the harness enforces it the moment either file is touched at all, whether or not the edit has anything to do with the dashes. This is not new debt from today's work; it was already there. It means the next genuine edit to any of these three files will hit the same wall. Not fixed here, because scrubbing dozens of dashes out of long-standing code comments is its own piece of work, not a side effect of a dead-code sweep, and it touches wording rather than removing something unused.

---

OWED BACK: nothing on the sweep itself. The dash debt in those three files is worth a decision: whether it is worth a dedicated pass, and if so whether comments are read the same way as reader-facing copy for this rule's purposes.

*No em or en dashes in this file; checked before writing.*
