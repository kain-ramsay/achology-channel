> **DISPOSITION, Chat S355:** acted on. All four corrections are written into DSRD 8 section 20.6: the label becomes a header across the card reading `Quote Source`; the description sentence is struck with the reason and the note that the data still exists; the cover's shadow is corrected off `--shadow-cover` with the condition that token was missing; and the controls are recorded stacked, with the width condition written in as the general rule and both of Kain's rulings kept in order. **This supersedes an edit made earlier in the same session**, which recorded the controls side by side spanning the full width from the previous ship brief. The two one-off values are accepted as annotated; neither becomes a token today. Archived S355.

# SHIP: the quote page's source book card, as Kain ruled it at S108

**From:** Code, S108. **Theme v0.176.0**, on the build site.
**DISPOSITION: WAITS ON** `DSRD_8_Component_Library.md`, section 20.6, for the
four corrections in section 3. The build is finished and verified; only the
document is behind.

---

## 1. How this one was decided, which matters more than what it decided

Kain stopped the session mid-flow to say this, and it is the reason every
decision below was taken on an offline harness rather than on the page:

> "No more building until we have agreed where the design and layout is gonna
> be. I've just had to wait ten minutes for you to build something that I did
> not want you to build. Alright? ... Do not touch the live site."

He was right, and the cause was mine. I had answered a design question by
building the answer into the live page and then showing it to him, twice, which
turns every one of his preferences into a ten minute wait and a deploy. From
that point the whole card was settled on one offline harness, one question at a
time, and nothing reached the install until he said "yes, go ahead and build it
please".

**The rule this session earns:** a design question is answered with a rendered
option, not with a shipped page. The harness costs minutes; the page costs a
version, a deploy, and his time.

## 2. What he ruled, in his own words, in order

| Ruling | His words |
|---|---|
| The description line goes | "No sentance at all please" |
| The label is reworded | "replace The Quote Source with Quote Source please" |
| The layout | "Label as a header AND then buttons beside the cover" |
| The cover's shadow | "Sitting on the page" (from five settings) |
| The mark, and its direction | "The house glyph - but please flip this horizontally" |
| The mark's presentation | "I like 3. In a soft tile best" (from five) |

**The card as built.** Three grid rows. The header takes row one across both
columns with a hairline under it, carrying the mirrored house glyph in a pale
orange tile. The cover spans rows two and three. The book's name and its author
sit in the top of the right column, the two controls, stacked, in the bottom of
it. Nothing runs the card's full width, so no height is left over anywhere.

**One earlier ruling of his was superseded by a later one, and both are
recorded.** At S108 he ruled the two controls sit side by side; later the same
session he chose the arrangement that stacks them, having been shown that cost
explicitly before he chose. The later ruling governs. The earlier one is kept in
the code comment rather than deleted, because a rule that quietly disappears
cannot be checked.

## 3. What Chat is asked to correct in DSRD 8 section 20.6

Four items. The first three are departures the build has taken deliberately;
the fourth is a gap the document has always had.

**One. The label is not in the words column.** Section 20.6 places the overline
above the title inside the column. Kain moved it to a header across the top of
the card with a hairline under it. Its type is unchanged: 11/600 uppercase in
the AA-safe orange. Only its position and its wording moved, and the wording is
now `Quote Source`, not `The source`.

**Two. The one or two sentences are not rendered.** Section 20.6 asks for "one
or two sentences at 14/400, line-height 1.6". This was built at S108, shown to
him on the render, and removed the same session on his ruling. In a column 200
wide the sentence ran to four lines and was the single thing making the card
feel crowded. Recorded so the omission is not read later as an oversight: the
field it would come from is the book note's own excerpt, and **all 92 published
book notes carry one**, averaging 120 characters and never longer than 193,
measured on the install this session.

**Three. The cover's shadow is not `--shadow-cover`.** Section 20.6 asks for
"the deep lift beneath". base.css records that token as the one shadow on the
site built from pure black rather than brand dark, drawn for the book note hero:
a 256px cover on a photograph under a dark wash, where a brand dark shadow
disappears. Section 20.6 names the value without carrying that condition. At
132px on a white card the throw is half the cover's height again at half
strength black, and Kain named it unprompted: "you have put too much in!" It is
now a contact shadow, both parts brand dark at the strengths the site's own card
shadows already use.

**Four, and this is the gap rather than a departure. The controls' width
condition is still missing.** I asked for this in the previous ship brief and it
is now more urgent, not less. Section 20.6 says "two controls side by side" with
no condition attached. On this page side by side is only possible where the pair
spans the card's full width; in the words column they need about 330 against the
200 available, overflow the card's own border and clip the Amazon arrow. Kain
has now chosen the stacked arrangement here anyway, so the document and the
build disagree twice over. **Whatever 20.6 ends up saying, it needs to say what
the width condition is, because the next person to build it from the document
alone will nest them and hit exactly what I hit.**

## 4. Two one-off values, annotated rather than tokenised

Both pass `css_gate` under its annotation rule, and both are named here so the
choice is reviewable.

- **The contact shadow.** No `--shadow-*` token carries one. Its two strengths
  are the site's own card shadow values.
- **The tile's 6px corner.** DSRD 7 section 5.3's smallest tier is 10, drawn for
  controls; on a 26px tile that is nearly a lozenge. 6 is the cover's 4 and the
  card's 12 met in the middle.

If either should become a token, that is Chat's call and I will take it.

## 5. Verification

Read off the live page by Code at v0.176.0, at 1440, 1024 and 375: the header's
wording and hairline; the tile's size, corner and ground; the glyph mirrored,
filled, with both registry paths present; the cover 132 by 198 at true ratio and
confirmed loaded; no sentence and no overline left anywhere in the markup; the
author italic at 14; both controls stacked beside the cover in white and brand
dark, no underline, each measured against the width its own label needs rather
than against a check that cannot fail; no overflow of the card or the page; and
no console errors at any of the three widths. The card was then captured from
the live page at all three and looked at.

*No em or en dashes in this file; checked before writing.*
