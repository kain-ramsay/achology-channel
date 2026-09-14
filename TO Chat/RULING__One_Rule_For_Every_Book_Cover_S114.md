# RULING: one rule for every book cover, and the side column takes the hero's

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 114, theme session. **Date:** Monday 14 September 2026.
**Filed under Harness Rule 14.**
**Shipped:** Theme 0.397.0, deployed and verified on two live pages.
**Board card:** Book note page template.

---

## 1. Kain's words

He opened two book notes side by side and found it himself:

> "You got Jordan Pearson's Maps of Meaning ... and radical compassion is just a square image ... you have different two completely different contradictory rules assigned to these two images. There needs to be one standardized rule for every single book image. And the Tara Black one has square corners."

## 2. What he had found, measured

The same cover file was drawn two different ways on one page. The hero filled its 2:3 box. The side column fitted the picture inside the same box, so any cover that is not exactly 2:3 shrank, left a white sliver down each side, and lost its rounded corners.

| | file | in the side column |
|---|---|---|
| Maps of Meaning | 600 x 900, exactly 2:3 | fills the box, corners round correctly |
| Radical Compassion | 1249 x 2000, a little taller | 240 wide in a 256 box, white either side, square corners |

## 3. Why the corners went, because it is not obvious and it is why this survived

The corner was on the wrapper, with overflow hidden, and that is correct for a filled box. **A fitted picture sits inside the wrapper with clear space beside it, so the rounded clip lands on that clear space and never touches the picture.** The picture's own corners stay square and nothing looks broken. It simply reads as a slightly smaller, square cornered cover.

**So the fault was in every cover all along, and only the ones that are not exactly 2:3 could show it.** That is why it looked random from book to book rather than wrong everywhere, and it is why it was never caught by looking at one page.

## 4. What now holds

The side column takes the hero's rule, copied rather than written afresh: fill the 2:3 box, centre the crop, take the standard card corner. Two details are deliberate:

- **The corner is set on the picture itself** rather than left to the wrapper, so it survives whatever shape the picture turns out to be.
- **The crop is centred rather than top aligned**, which is what it carried before. A top aligned crop takes everything it loses off the bottom, and the bottom of a book cover is where the author's name is.

## 5. What this does not fix, and whose it is

**The 99 cover files are still different shapes.** This makes them all render identically, which is what was asked for, but it does it by cropping the ones that do not fit rather than by their being right in the first place. The real fix is at source and it is already commissioned: `BRIEF__The_Book_Cover_Becomes_A_Drawn_Book_Everywhere_From_Clean_Covers_Fetched_By_ISBN_With_A_Baked_PNG_S357`, whose first half fetches clean covers by ISBN. That brief is dispositioned as waiting on the fetch.

**One line for Chat to weigh against that brief:** its `ach-book` component draws a three dimensional book from the cover image, and it will inherit whatever shape the file is. If the covers are not squared up at source first, the drawn book will carry the same variation this ruling has just papered over.

OWED BACK: nothing on the change. On section 5, whether the ISBN fetch should normalise every cover to 2:3 as it lands, which would retire the crop rather than keep it.

*No em or en dashes in this file; checked before writing.*
