# RULING: the school card banner audited, and its gap closed at the cause

**DOCUMENT TYPE: ruling record, not a page spec.** It records an audit Kain commissioned in session, the fault he found in the work that followed, and his ruling on it. It specifies no page.

**From:** Claude Code, S124, Sunday 20 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Reads with:** the four S124 rulings filed before it on this same component.
**OWED BACK:** two things, below, that only Chat and Kain can close.

## What he asked for

An objective evaluation of the spacing in the seven school cards' banner against the rule book, a check that no font sits off the type scale, and then a proposal to improve it.

## What the audit found, measured on the rendered page

**The type needed nothing, and saying so plainly was part of the answer.** The school name is 18 on 1.35 at weight 600, which is DSRD 7 section 3.1's Bundle School Name row exactly. The facts line is 12 at 400, section 3.2's Card Stats row. Both are `--text-*` tokens on the nine-step scale, and `css_gate.py`'s check E refuses any px font-size that is not a token, so the file passing is proof rather than an opinion.

**The spacing did not conform, and he was right that it did not.** Four values answered to nothing, against DSRD 7 section 4.5, quoted: "A bare number with none of those three is a defect."

| value | what was wrong |
|---|---|
| `min-height: 132px` on the banner | not a step, named in no document, and it never even bound: the name's own floor was driving every banner to 137 |
| `bottom: -12px` on the artwork | not a step; it is what made the drawing hang 11 past the banner's rule |
| padding 24 top, 16 bottom | both steps, but asymmetric for no stated reason, so the contents sat 27 from the card's top edge and 17 from its rule |
| `margin-top: 4` under the name | section 4.3's own table gives 8 for a label that belongs to its title |

All four are corrected. The banner now reads 24 above the name, 8 between the name and the facts, and 24 below them, measured identical on all seven cards at 1440, 1024, 768 and 390.

## The fault in my own work, which he found and I had not

I proposed four picture treatments. He ruled them irrelevant and named the real fault: "the space between the school name and the five courses number of hours is ridiculous. It's way too much. So your four options are completely irrelevant."

**He was right, and the cause was mine.** To keep two cards in a row agreeing, I had held the school name's own box three lines deep. On every card whose name is shorter than three lines, the spare line sat as a hole between the name and the facts. I had been checking that neighbouring cards lined up with each other and had never once judged a single card on its own, which is why the hole is in every screenshot I took and I did not see it. That is recorded here rather than smoothed over, because it is a method failure and not a slip: **an alignment check across a row is not a substitute for looking at one card.**

## The fix, and why it is a deletion rather than a replacement

The floor is gone, not moved. Measured on the page with every floor switched off:

| width | what the seven names do naturally |
|---|---|
| 1440 and 1200 | all seven take two lines; the banners already agree |
| 1024 | six take three, one takes two |
| 768 | six take three, one takes four |

At the widths this page is read at the floor bought nothing and cost a hole on every card. At the two intermediate widths it would buy the alignment of one banner in seven, at that same price everywhere else. A banner a line deeper because its school has a longer name is the truth of the content; a hole under a short name is a defect. The cards still stand equal in height, because the grid stretches them, and their money and their buttons still line up, because the money block is pinned to the card's floor.

The four picture treatments are deleted; they are in the theme repository's history at v0.517.0 as Flush, Break, Float and Bleed. Break is kept, as the corrected form of the overhang the card already had, at 8 rather than the bare 12.

## Two things owed back, which are not Code's to close

1. **The card's 3px school-coloured top border is a bare number**, named in no specification I can find. It is pre-existing. Under section 4.5 annotating an unnamed value is the act of approving it, and approval is Kain's, so it is raised here and left untouched. It needs either a named value in DSRD 8 section 8 or Kain's annotation as a one-off.
2. **The percentages in this banner**, the 40 and 33 per cent held for the words and the 31 and 26 per cent the picture takes, are neither tokens nor values named in a DSRD. They carry an in-place comment giving the reason and the measurement, but section 4.5's third route also wants the approver and the date. They need Kain's word to become properly annotated one-offs, or a row in DSRD 8 section 8.

## Shipped

Theme **v0.517.0**, deployed, with local, the server and the zip each measured and agreeing. `css_gate`: pricing.css PASS. Checked at 1440, 1024, 768 and 390: no sideways scroll, nothing leaving its card, the artwork clear of every word, the three banner measurements identical on all seven cards at every width. The approved state was re-exported as the page's prototype.

## Still open on this page

The two membership panels and the free tier strip, the questions block, the closing help strip, and the page's rhythm judged last. `/pricing/` is still unpublished on Chat's S365 disposition and its DSRD 6 record is not filed.

*No em or en dashes in this file; checked before writing.*
