**For Chat. What this needs:** write the last two lines of the type scale, the weight rule and the phone rule, into DSRD 7 section 3, from this file. Then tell Code to switch on the stylesheet gate for them.

# RULING (theme, S189): the weight rule and the phone rule are written from what the site already does

**Kain's words** (Safari afternoon, 27 October 2026, brief item 7), on Code's recommendation to write down the existing pattern rather than build four options per rule: "Yes. Write down what the site already does and show me only the odd ones that would change."

**The result: nothing changes.** Code read every stylesheet at theme 0.707.640, and measured the odd cases on the build site in WebKit at 1268 and 390. Every case that breaks the pattern turned out to be one of Kain's own signed rulings. So there was nothing to show him, and no page moves.

## 1. The weight rule (what each weight means)
Counts are declarations outside media queries.
- **Como 700:** page titles and hero headings (33 and 42), and the big figures (50 declarations).
- **Como 600:** section headings, card titles, labels, buttons and links (196; the site's working weight for Como).
- **Como 500:** small interface text such as navigation and quiet labels (20).
- **Mulish 400:** reading text (81).
- **Mulish 600 and 700:** emphasis and bold inside reading text (33).
- **Named exceptions, each a signed ruling, stay as they are:**
  - 800 on the About page's display figures: the odometer, the community count, the story proof numbers and the faint backdrop number (Kain S142; the odometer is already a named size exception).
  - 800 on the Full Money Back guarantee badge (Kain S136, "letters at their natural shape").
  - Mulish 300 italic on the third paragraph of an author profile (Kain, Code's S097: "italic paragraph 3 in a lighter weight").

## 2. The phone rule (what type does on a phone)
**Below 768, text steps down one step on the scale:** 33 to 28, 28 to 24, 24 to 21, 21 to 18, 18 to 16, 16 to 14, 14 to 12. The 42 hero steps to 28. That pattern covers 29 of the 34 size changes in the theme.
**Named exceptions, each a signed ruling, stay as they are:**
- **Knowledge Hub list, subject and navigation page titles stay at 33 at every width.** This is Kain's S178 ruling ("title 33 on all 76 KH list/nav pages"), held in kh-subject.css. The older phone rules on `.kh-hub__title` and `.kh-listing__title` (33 to 24) are dead: no page draws those classes. Code removes them in a tidy change with no visible effect, proved by machine.
- **The About page's community stages drop two steps on a tablet or phone:** the count goes 42 to 21 and the stage name 18 to 14. The About page is signed as built.

**For the gate:** the weight check passes a weight only if it fits section 1 or is a named exception. The phone check passes a phone size only if it is one step down, or is a named exception. Code switches both on after Chat writes the two lines home.

OWED BACK: the two lines in DSRD 7 section 3, dated, then a NOTE so Code switches on the gate.

*No em or en dashes in this file; checked before writing.*
