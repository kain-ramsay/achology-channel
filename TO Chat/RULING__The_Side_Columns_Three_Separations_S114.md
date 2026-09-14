# RULING: the side column has three separations and nothing else, on book notes and articles alike

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 114, theme session. **Date:** Monday 14 September 2026.
**Filed under Harness Rule 14.**
**Shipped:** Theme 0.399.1, deployed and read back on both page types.
**Board card:** Book note page template; Article page template.
**This is a standard rather than a fix**, so it wants a home in DSRD 8 beside the column's other rules.

---

## 1. Kain's words, and they changed the shape of the work

> "I don't want you to look at granular components of the sidebar. I want you to look at the whole thing objectively. Right? So that we can standardize the entire thing. Right? This is a design strategy. Right? Not one little tweak within a side column. Do you understand?"

He was right to stop it. Everything before this in the sitting had been one part at a time, and each fix was correct in isolation while the column as a whole still had no rule.

## 2. What the whole column measured, before anything changed

Measured on a book note and on an article. **Three different jobs were being done by four different gaps: 24, 32, 40 and 49.**

**And the important one was backwards.** The gap holding a label to its own list was 49. The gap separating two entirely different blocks was 24. So every heading in the column read as belonging to the thing above it and detached from the list underneath it.

That single inversion is what Kain had been naming, piece by piece, all sitting: the contents heading looking stuck to the button above it, the spacing "in between each of the heading titles" looking larger than the space above the heading. One fault, described from several angles.

## 3. The standard, one job each, identical on both page types

| Gap | Job |
|---|---|
| **16** | A label to the list it labels. The smallest gap in the column, because a label and its list are one object and nothing may read as sitting between them. |
| **24** | Between items inside a list. Both lists already used this on both page types, so nothing moved. |
| **48 and a hairline** | Between one block and the next. Kain's standing rule for every hairline on the site, and his own suggestion in this sitting: "I think you need to put a hairline underneath the image across book notes and articles." |

**It costs no height.** The two label gaps give back 57 and the two block separations take 40, so the column came out about 17 shorter than it was.

**Read back on the live pages, both types identical:** 48 above the hairline, 48 below it, 16 from label to list, 24 inside each list.

## 4. Two gaps are deliberately untouched, and both are structural

The space above the Know Your Psychology panel is whatever the screen-height box has left over, because the panel is pinned to the foot of the reader's screen. **That is Kain's S112 effect and he asked for it twice that day.** Earlier in this sitting Code proposed fixing it at a step and he agreed; reading the rule behind it showed the proposal would have undone his effect, and it was withdrawn rather than built.

The space above the reading list is the sticky track, which already ends on a hairline with 48 above and below. It was keeping this standard before the standard existed.

## 5. One thing the read-back caught that no amount of reading would have

The reading label's gap was changed to 16 and still measured 24. **A second declaration of the same selector and the same property sat two hundred lines further down the same stylesheet and won.** Both now say 16, and the second is left in place rather than deleted: removing it would leave the first looking authoritative when the cascade is what decides, and the next person to change the value would watch nothing happen, exactly as this did.

Three margins stacking into one gap was the same shape of fault in the same block: the header declared 16 while the title and an empty subtext inside it each added their own, making 40.

OWED BACK: a home for section 3 in DSRD 8, so the three numbers are a standard the next column can be built against rather than something recoverable only from this file.

*No em or en dashes in this file; checked before writing.*
