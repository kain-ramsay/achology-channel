**For Code: change one line in the book note hero, deploy, and report back with the rendered page. Kain's ruling, S407.**

# BRIEF: the book note standfirst's closing line changes (Kain, S407)

**From:** Claude Chat, S407, Tuesday 6 October 2026. **To:** Claude Code, theme session (or a factory session, since this is Kain's word, named per the harness).

## The ruling

Kain, S407, in Chat, word for word: "Keep reading to decide if this book deserves a spot on your shelf."

This replaces the fixed sentence "Essential reading for all Achologists." that ends the standfirst on every book note. That sentence was his own call at your S102 sitting (v0.167.21). He now wants it gone because it reads as exclusive, and wants a line that is inviting and open to every reader. He keeps a closing sentence on purpose: he wants the header to carry about three lines of text so the space is used.

## What to do

1. In `single-book_note.php`, set `$ach_rating_sentence` to exactly: `Keep reading to decide if this book deserves a spot on your shelf.` Nothing else in the hero changes. The badge stays as it is.
2. Update the comment above it to record the S407 ruling and Kain's reason, so the next reader of the file sees why it changed.
3. Check the line appears nowhere else (cards, feeds, schema, `rank-math-feed.php`, any book note description field). If the old sentence is carried anywhere else, name it in your report rather than changing it.
4. Deploy, then look at four book notes at 1200 wide, including Born for Love and one with a long description and one with a short one. Report how many lines the standfirst runs to on each. If any falls short of three lines or runs well past it, say so; do not change anything else to fix it, because that is a visual call for Kain.
5. Return the rendered page links and the line counts in TO Chat.

## Owed back

Chat writes the ruling into DSRD 9 section 32.9 (which still names the S102 sentence) and the book note page record, in the same whole-document pass as your S150 rulings.

*No em or en dashes in this file; checked before writing.*
