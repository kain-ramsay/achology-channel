CHAT DISPOSITION, S347, 6 September 2026: read and acted on. Kain's Essential Reading ruling recorded. It is now the one Essential Reading note on the site with no way to buy it, because its `amazon_url` is empty and its old field carries an untagged Amazon search address; that is the ASK on the eight book notes with no buy button, opened S104 and answered in FROM Chat this session. Board cards: Book Notes, the psychologist expansion; Amazon OneLink.

# RULING: The Ultimate Life Coaching Handbook is Essential Reading, and the Book Note Master needs the row

**DOCUMENT TYPE:** ruling, from Claude Code, Session 104, factory session. **Date:** 6 September 2026.
**Given by:** Kain, in the S104 sitting, directly to Code. Filed the same session under Harness Rule 14.
**Board card:** Book Notes, the psychologist expansion.
**Chat's action is in section 3 and it is the only thing owed.**

---

## 1. What was put to him, and his words

He had The Skilled Helper and The Ultimate Life Coaching Handbook open side by side and asked why one carried the Essential Reading badge and the other did not, and whether the badge had been baked into the template at all.

**It had, and it was working.** The badge is a switch and the switch is the book's rating, on his own S102 ruling written into `single-book_note.php`: "ONLY THE TOP RATING WEARS IT ... Recommended and Highly Recommended notes have no badge and the hero is exactly as it was for them." Read off the install rather than assumed: post 35418 The Skilled Helper carried `essential-reading` and wore the badge twice; post 35419 The Ultimate Life Coaching Handbook carried `highly-recommended` and wore neither.

So the only open question was whether the book was rated correctly, which is his. It was put to him as one yes or no and his answer was:

> "yes, make it essential reading please"

## 2. Done, at source first, and read back

**The record changed first.** `Content Records/book-note/the-ultimate-life-coaching-handbook.md`, `achology_rating` from `highly-recommended` to `essential-reading`. The record is the single source under The Publish Ready Pipeline, so changing only the install would have been drift that the next import silently reverted.

**Then the install**, `wp post meta update 35419 achology_rating essential-reading`, read back as `essential-reading`.

**Three things measured on the live page afterwards, not assumed:**

- **The badge renders twice**, hero and last section, which is what the template does for this rating and did not do before.
- **The schema's star rating moved from 4 to 5**, now reading `"ratingValue":5`. That is DSRD 2 §5.2 working as written: "Recommended = 3 stars, Highly Recommended = 4 stars, Essential Reading = 5 stars." **Named because it is the outward-facing half of this change** and it reaches Google rather than only the page.
- **The words on the page did not move, and correctly.** The standfirst still reads "Essential reading for all Achologists." on both notes, because Kain ruled at S102 that the sentence is fixed on all 65 whatever the rating, and the badge is the rating's only visible mark. Both pages carry the identical sentence, checked.

## 3. What Chat owes, and it is the whole reason this file exists

**The Book Note Master is true north for every book note row and Chat reads it alone** (The Shared Rules §4). It holds the `achology_rating` column DSRD 2 §5.2 names. **Code has not touched it and cannot.**

So the row for The Ultimate Life Coaching Handbook needs `achology_rating` set to `essential-reading` in the master. **Until it is, the master disagrees with both the record and the install**, and the next rebuild from the master reverts this to `highly-recommended` and takes the badge away again without anybody typing a thing.

## 4. One thing nobody asked and it is worth a line

**Nothing constrains how many notes may be Essential Reading.** DSRD 2 §5.2 sets the three tiers and their star values and names no quota, read from the canonical file this turn. So this is not a place in a ranking that had to be taken from another book, and no other note changes.

---

OWED BACK: the `achology_rating` row in the Book Note Master, so the master, the record and the install all read the same thing.

*No em or en dashes in this file; checked before writing.*
