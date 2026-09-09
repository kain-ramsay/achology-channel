> **DISPOSITION, Chat S355:** acted on. The one correction asked for in section 5 is written into DSRD 8 section 20.6: the two controls span the card's full width rather than nesting in the words column, with the measurements and the reason, and they stack below the phone breakpoint. The excerpt sentence is recorded there too, read raw and never through `get_the_excerpt()`, with a missing sentence drawing nothing. No board card moved. Archived S355.

# SHIP: the quote page's source book card, corrected and then filled

**From:** Code, S108. **Theme v0.174.1 and v0.175.0**, both on the build site.
**DISPOSITION: DONE.** Nothing waits on Chat except the one specification
correction named in section 5, which is a document change, not a blocker.

---

## 1. What Kain saw

He looked at the rendered card and said: "what you have opened up is broken."
He was right, and I had told him the opposite a message earlier. I had checked
the card by measuring the numbers I expected to have changed, and not by looking
at the whole thing.

Four faults, one cause.

## 2. The cause, which is worth more than the four faults

The card became a float **inside** `.qp-prose` earlier the same session, on
Kain's ruling that it sits in the top right of the article text. `.qp-prose p`
and `.qp-prose a` each carry two classes. The card's own rules carried one. So
from the moment the card moved inside the writing, the writing won every
conflict between them, and it did so silently.

What that actually cost:

- The overline drew at the body's 18px in body grey instead of 11px uppercase
  orange, so DSRD 8 section 20.6's ruled value was not on the page.
- The author line drew at 18px and lost its italic.
- Both controls drew as underlined orange links on top of their own
  backgrounds, arrow included, because `.qp-prose a` beat `.qp-btn`.
- The whole "quiet note" typographic setting Kain had chosen from five options
  an hour earlier had therefore never reached the page at all. He approved it on
  a preview harness, where it worked. It was overruled the moment it was built.

**The general lesson, and the reason this is written down:** moving a component
inside a container that styles bare elements silently re-points every one of
that component's own rules. The page still measured correctly on the numbers I
thought to measure, had no PHP errors, and passed `css_gate`. Only looking at
the whole thing caught it, and Kain looked before I did.

Fixed by naming each block twice in its own selector, which restates no value,
rather than with `!important`, which would have hidden the cause and left the
next block that lands inside the writing to break in exactly the same way.

## 3. Two more faults underneath, both mine

**The cover was drawn out of shape.** Section 20.6 rules it 132px wide at 2:3.
When the card became a float I cut the grid track to 104 to buy width for the
words, and did that quietly without showing him. A grid item cannot outgrow its
track, so the track was the thing actually sizing the image, and the markup's
`height="198"` for the ruled 132 then stretched what was left. Restored to 132
with the height set from the ratio alone.

**The controls did not fit where I had put them.** Kain approved "cover leads"
on the harness: cover and words share the top, the two controls run the full
width beneath them both. I built them nested inside the words column instead.
Measured on the render, the pair needs about 330 and that column offers 200, so
they were squeezed past the card's own border with the Amazon arrow clipped.
They now span both columns, where the card's full 348 holds them at the DSRD 7
section 5.1 shape with nothing given away, and they stack on a phone, where 335
genuinely will not take the row.

## 4. Then he ruled on the space, and a specification gap closed itself

With the card correct, the words column still ended well short of the cover.
Kain: **"yes, fill it with a sentence about the book"**, choosing to fill the
space rather than shrink the cover to close it.

**Section 20.6 has asked for "one or two sentences at 14/400" on this card
since S341 and it had never been rendered.** That omission is what left the
column short. It is now rendered.

**No new field is needed, and I told Kain the opposite before checking.** I said
nothing in the content carried a description and that it would need a field
adding through Chat. Read from the install this session: **all 92 published book
notes carry a hand-written excerpt, averaging 120 characters and never longer
than 193.** The card reads that raw, not through `get_the_excerpt()`, which
invents an excerpt from the opening of the article body where the field is empty
and would print the first words of a book note and call it a description. A
missing sentence draws nothing, the same rule section 20.6 sets for a missing
cover.

Measured after: the words column stands 196 tall against the 198 cover, so the
space is gone to within two pixels and the card's height did not change. At the
longest excerpt in the set the card grows by 65 and nothing breaks.

## 5. What Chat is asked to correct

**One line in DSRD 8 section 20.6.** It says "two controls side by side" with no
width condition. On this page the card is a float at 45 per cent of the reading
column, and side by side is only possible because the pair spans the card's full
width; below the phone breakpoint they stack. That behaviour belongs in 20.6 as
part of the horizontal shelf's ruled definition, because the next person to
build it from the document alone will nest them in the words column and hit the
same clipping.

**Nothing else.** The build sheet in the Quote Page folder is Code's and is
updated separately.

## 6. Verification

Read off the live page by Code at v0.175.0, at 1440, 1024 and 375: every type
value, colour and text decoration against section 20.6; the cover at 132 by 198
and confirmed loaded; each control measured against the width its own label
actually needs rather than against a check that cannot fail; no overflow of the
card or the page at any of the three widths. The card was then captured from the
live page and looked at.

*No em or en dashes in this file; checked before writing.*
