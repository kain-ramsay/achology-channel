# RULING: the header's Knowledge Hub item is labelled "Library"

**Ruled by:** Kain, in session, Session 080, 24 August 2026.
**Shipped in theme v0.82.2**, deployed and verified.
**Supersedes:** `RULING__The_Knowledge_Hub_Nav_Label_Becomes_Learn_S080.md`, filed an hour earlier in this same session. That ruling was correct when it was made and he changed it after seeing the result. This file replaces it; the other should be read as history.

---

## What he said

On the tabbed comparison he first ruled **Learn**: "LEARN - makes perfect sense - and works well."

It shipped. He then looked at the header on the real page and asked: **"Does the word LEARN not compete with Courses?"**

It does. He then ruled **Library**: "Yes, Library works great!"

## Why he was right, recorded so this is not re-litigated

**Courses is the paid training. This section is the free reading.** Two learning verbs sitting side by side in the same bar carry none of that distinction, and a visitor reads them as two doors into one room.

**"Knowledge Hub" never had this problem**, because it does not use a learning verb. Its only fault was width, and I fixed the width while introducing a meaning collision that was not there before. That was my recommendation and it was the wrong trade.

**Library keeps both properties.** It is narrower than Learn, so the width fault stays fixed. It cannot be mistaken for a course. And it describes what is actually behind it: book notes, quotes, articles and workbooks.

**The address is unchanged at `/learn/`.**

## The original fault, for the record

The six top-level labels come to 498px unwrapped, and their specified 32px gaps add 160, so the bar needs about 658px. Between 880 and 1023 the header offers 600 to 640. The navigation did not fit anywhere in the tablet band, and the browser wrapped KNOWLEDGE HUB onto two lines to cope, on every page at those widths.

Verified after this deploy at 880, 900, 1023 and 1200: **no label wraps at any width.** The phone overlay carries the same word.

## What Chat owes, unchanged from the first ruling except the word

**DSRD 1 §13.1, Header Navigation (LOCKED).** Item 4's label becomes `Library`. Destination unchanged.

**DSRD 8 §18.4, Navigation Structure (LOCKED).** The same row. §18 is the authoritative copy per §13.1's pointer, so it should carry the reasoning as well as the word, specifically that the label must not use a learning verb because Courses already occupies that ground.

**Untouched:** the dropdown panel beneath it, including its heading "Explore New Ideas in Achology's Knowledge Hub"; the footer's own "The Knowledge Hub" link, which is a separate locked list at §13.2; and the section's name in every other document, which is still the Knowledge Hub. **Only the header's nav label changed.**

## One lesson worth keeping

**Two rulings in one hour on the same word, because the first was judged in isolation and the second in context.** The tabbed comparison showed the label against itself; it did not show it against the five labels beside it, which is where the collision lives. A comparison that isolates the thing being changed can hide the fault that only appears in company.

*No em or en dashes in this file; checked before writing.*
