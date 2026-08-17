# RULING: the course card's Enrol Now button carries no outbound arrow

**Written S252 by Claude Chat. Answers the open conflict in `RULING__Course_Grid_Three_Two_Two_And_Three_Cards_S050.md`.**

## Kain's ruling

Put to him as the conflict you named: DSRD 7 §1.0 wants a visible arrow inside every external link's label, DSRD 8 §7 is a LOCKED card whose §7.1 fixes its CTAs as two plain buttons, and Enrol Now is now external.

He ruled: **leave the arrow off.**

## What is written into DSRD 7 §1.0

A recorded exception, in the section itself:

> **One recorded exception: the course card's CTAs (Kain, S252).** The DSRD 8 §7 course card is a LOCKED component whose §7.1 fixes its CTAs as two plain buttons. Its Enrol Now button became external at S050, when its target was corrected from an invented internal address to the product's real Circle.io checkout URL from DSRD 4. **That button carries requirements 1, 2 and 4 and does not carry the arrow.**

The reasoning recorded with it: adding the glyph would change the appearance of a component Kain approved by eye, to satisfy a rule written after that approval. The arrow serves sighted readers; the hidden "opens in a new tab" serves everyone else and is present, so no reader loses the warning WCAG 2.2 asks for.

**The exception is the glyph alone.** `target="_blank"`, `rel="noopener"` and the visually hidden text stay mandatory on that button and on every external link everywhere. The exception covers the DSRD 8 §7 course card and nothing else; a second component wanting the same relief needs its own ruling.

So the card as you built it is correct and needs no change.

## Three other things from your two files

**1. Your defect report on the course grid was the right call and is recorded as one.** DSRD 8 §7.0 already specified 3 / 2 / 1 columns and `cards.css` already carried `.product-section__grid`, unused by any template. Nothing needed ruling to make the row three across; a spec that was open needed applying. DSRD 8 §7.0 is therefore unamended, exactly as you set out.

**2. The card count amendment is Kain's and is being written into DSRD 9 §32.1 item 6:** three cards at desktop, two at tablet, two stacked at phone, with the third withdrawn below 1024px in CSS.

**3. Learn More stays pointed at the DSRD 1 §2.3 course page address.** It reads as planned-not-built at the gate, which is honest. Do not repoint it at the checkout; two buttons going to the same place is worse than one that waits.

## The cards session

Kain raised it himself and you were right to flag it as his side of the road: he is not certain the built card matches what he approved, and the Book Note prototype carries a prototype rendition rather than the real component, so the two have never been compared side by side. That is now on Chat's list to put to him. **Build nothing new on the course card until it is settled.**

*No em or en dashes in this file; checked before writing.*
