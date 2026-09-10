> CHAT DISPOSITION, S357: read. The on-scale values recorded in DSRD 8 section 26 ruling 7; the two class prefixes noted there. Archived.

# SHIP: the reading bar is on the design system's steps. Theme 0.231.0

**From Code, S109. Deployed, cache purged, photographed before and after on both
pages that carry it, and shown to Kain in Safari.**
**Board cards:** Quote page template; 250 help articles.

## Kain's instruction, in his own words

> "tokenify the top article info component to match the others from a layout
> perspective"

Given live in the S109 sitting on the quote page in front of him. He asked
whether it made sense; it did, and the spec was already on his side.

## What was wrong, quoted from the documents

DSRD 7 section 3: **"Every text size on the site sits on a step; nothing sits
between steps."** DSRD 7 section 4: **"Base unit: 8px. All spacing uses this
scale."**

The component broke both. Three values sat between steps: the bar's bottom
padding at 18, the listen button's vertical padding at 9, and the narrator's
name at 13. Two more were correct but typed as numbers rather than named, so
nothing tied them to the site's buttons: the label's 14 and the corner's 10.

## What changed

| value | was | is |
|---|---|---|
| bar, bottom padding | 18px | `var(--sp-md)`, 16 |
| listen button, vertical padding | 9px | `var(--sp-sm)`, 8 |
| narrator's name | 13px | `var(--text-14)` |
| listen button, label size | 14px typed | `var(--text-14)` |
| listen button, corner | 10px typed | `var(--radius-button)` |

The row now reads at one size at both ends instead of three. It is four pixels
shorter, and nothing else on either page moved. **Nothing was redesigned:** the
two-ends layout Kain ruled at S108 is untouched.

**One value stays off the scale and is recorded rather than swept:** the bar's
40px least height. It is not spacing, it is the row's own minimum, holding the
hairline in the same place on a page whose recording does not exist and whose
control is therefore hidden. DSRD 7 section 4 already counts a measure of this
kind as a component measure rather than a step, which is how it counts the 540
quote column.

## What was measured after the deploy

On the live quote page and the live help answer, through a real browser: bar 51
high, padding 16, button 8 by 16, corner 10, name 14, both pages identical, both
serving 0.231.0. Local, the server and the zip agree.

## The line you asked for at S355

`COMPONENT_REGISTRY.md` carries the listen bar's class prefixes as TO CONFIRM.
**They are `ach-listen-bar` and `ach-listen`.** The bar and its facts slot take
the first; the control, its button, its icons and the narrator link take the
second. Both are in components.css and nowhere else, apart from one margin
override on the quote page.

---

OWED BACK: nothing. The two prefixes above close your S355 section 1.5.

*No em or en dashes in this file; checked before writing.*
