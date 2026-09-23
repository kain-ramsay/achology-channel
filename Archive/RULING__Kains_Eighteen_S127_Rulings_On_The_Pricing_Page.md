# RULING: Kain's eighteen S127 rulings on the pricing page, and two on the theme

**From Code, S127, Tuesday 22 September 2026. Theme v0.583.0 to v0.620.0,
every one deployed and verified on the rendered page.**

Three rulings already have their own files beside this one: the page drawing
right as a real page, Grouped for its rhythm, Quiet for its peak with the pass
button renamed, and Money for the saving with one width for its two lines. This
file carries the rest, so nothing he said today is live in the build and absent
from the record.

---

## 1. The page exists, and how it was made

`Pricing`, address `pricing`, top level, page 36845, and **published on the
build site at his instruction late in the sitting.** The name was taken from
DSRD 1 section 13.1's locked header row, not chosen; Kain stopped Code putting
it to him as a question and was right to.

> "you can do this by yourself, so please do"

H9 refuses every page-making command. Rather than work around it,
`tools/create_draft_page.py` was built and entered in the wall's reviewed
register with its three payloads quoted. It creates one draft and can do
nothing else.

## 2. The design rulings, in the order he gave them

| # | He ruled | What it settled |
|---|---|---|
| 1 | "Go with grouped" | the page's rhythm, three movements |
| 2 | "reinstate the hairline in between the courses and the schools" | one separator back |
| 3 | "Go with Quiet" | the peak made by quietening the seven, not enlarging the pass |
| 4 | "replace Enrol Now ... with Unlock All courses" | the pass card's action |
| 5 | "let's go with the money option" | the saving stated in money |
| 6 | "the save amount and the amount crossed out ... the same width" | the two small lines share a width |
| 7 | darker, larger, half a step heavier | the crossed-out price |
| 8 | "Compact please" | the money component's size, hairline out |
| 9 | "I think I like the column option" | each control over what it governs |
| 10 | "the Half option please" | the space under the control line |
| 11 | "Orange please" | the chosen control's colour |
| 12 | "I think the Wide option is fine" | the price column's width |
| 13 | "replace 3x and 5x with 3 Payments of and 5 Payments of" | the instalment mark |
| 14 | "reinstate the hairlines between every block" | five junctions, five lines |
| 15 | "Grow please" | the pass card's struck price at 18 |
| 16 | the bubble, inside the grey | the hero's watermark, and larger |
| 17 | "I really really like Bleed" | the school drawings, and two-line names |
| 18 | "Reach please" | the pass card's ticket, a fifth larger |

**Four copy replacements, all typed as he gave them:** the four choice card
buttons capitalised; the closing block's heading and line, twice; and the
course block's heading and line, twice.

## 3. Two rulings that reach past this page

**The primary button's fill is the AA-safe orange again.** Found by DSRD 6's
accessibility chapter: white on brand orange is 3.16 where small text needs 4.5,
and the hover was 3.89. He was given two routes and ruled this one. **It is a
regression repaired rather than a new decision, and the palette proves it:**
`--color-orange-press` exists only because the fill moved to
`--color-orange-link` at S096 for this exact reason. The token survived. The
fill did not.

**The stylesheet gate now checks spacing and stylesheet syntax.** He asked for
an audit of every space on the page, the gate could not answer, and its own
docstring said spacing was left to review. Check G is spacing; check H is text
outside a rule, an unclosed comment, unbalanced braces.

## 4. What Chat is owed

1. **The page's Rank Math and GEO metadata.** It has none. This is the chapter
   that will stay red until it is written, and it is copy.
2. **A component registry row for the pricing page's choice card.** Kain ruled
   that card at S122 and it was never registered, so the page gate reads its
   title as a block heading and objects that its label is too short. The fault
   is the missing row, not the page.
3. **DSRD 7 section 1 may want a sentence** saying a solid orange button's fill
   is the AA-safe orange, since the S096 fix came undone once already and
   nothing in the standard would have caught it.
4. **The theme-wide spacing sweep.** The new check finds 354 spacing values
   across the other stylesheets. Twelve of them in base.css blocked a ruled
   repair today and were split rather than swept: five took their tokens with
   no pixel moved, seven are annotated as unjudged and waiting on that sweep.

## 5. What is still Kain's, carried from S126 and not reached

Where his two pay-in drawings live now they are not controls; whether anything
at the point of decision should reduce risk; which name wins for the full price,
Enrolment Fee or One Time Fee; nine of 28 course rows printing the middle price
over the full price on a phone; and whether the Access All Areas Pass should
carry its own three, six and twelve month plans.

---

**OWED BACK:** the four items in section 4.

*No em or en dashes in this file; checked before writing.*
