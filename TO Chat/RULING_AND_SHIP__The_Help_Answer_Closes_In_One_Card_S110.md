# RULING AND SHIP: the help answer closes in one card

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.297.0,
deployed, gated and measured on three page types in both browser engines.**
**Ruled by Kain** live in this sitting. He named the problem first:

> "As I look at the bottom of the article here, it just seems and feels a little
> bit scrappy to me. Like, there's just lots of words and, uh, lines, and it
> doesn't feel particularly user friendly. From a user experience perspective,
> can you see some ways we could improve this whole bottom section of each help
> question?"

He then approved the proposal below in one word, and this is what was built.

**Owning documents:** DSRD 1 section 8, which describes the /help/ close by
category type. DSRD 8 for the new component.
**Board card:** none of its own.

---

## The diagnosis, measured before anything moved

From the end of the writing down, the foot held **eight links, two headings, a
yes or no question and six bordered boxes**, in **four different visual
languages**: a bordered row with a chevron, an orange text link with an arrow, a
white card inside a grey panel with a chevron, and a plain inline link.

**The fault was not any one block.** Every block was sensible on its own. The
page answered the same question three separate times: here are related questions,
here are more questions, here is how to reach us. A reader who has finished an
answer wants one of two things, another answer or a person, and the page offered
each of those twice, in different clothes.

## The answer is one Kain had already chosen this morning

For the contents card's share row he ruled: one object rather than several loose
ones. The same move applies here. One card. The four questions, then one quiet
line carrying both ways out, then a hairline, then the two ways to reach a
person.

Bordered boxes six to two. Visible rules three to one. Chevrons gone from the
question rows, where a chevron on every row of a list of links says nothing the
row does not.

## Nothing a reader can reach has changed

All eight destinations are still there. **The only copy removed is one line**,
"Click on the links below for other commonly asked questions", which Kain
approved by name. A sentence explaining what a link is costs a line and earns
nothing.

His two orange controls from S090, reworded at S091, are both still present and
still go to the same two places. He approved "one quiet line", not the removal of
a destination, and that distinction was read carefully rather than conveniently.

## Two of his standing rulings were protected, and it is worth saying how

**The nine and the six.** At S091 he ruled that the nine support categories are
offered a person and the six pre-purchase ones an offer: "a person, not an
offer". So the card's second half draws only on the nine. On the six, the card
holds the questions alone and the trial panel follows it exactly as it did.
Measured on one of each.

**The category page.** It closes with the grey pair panel and was not touched.
But the two support routes are now drawn by two blocks, so they were given one
home, `achology_help_support_close()`, which both read. Two copies of one set of
routes is precisely how a category page and the answers inside it come to offer
different ways out, which is the fault `achology_help_close()` exists to prevent.

**Nothing shared was restyled.** `.help-q-list` and `.help-q` are the question
door component and are drawn on the landing page and the category pages too, so
every change to them is scoped inside this card.

## Three gate rows, and they are not all the same kind of thing

**One was a real fault and is fixed.** The strip above the card kept a hairline
48px above the card's own top border: two lines saying one thing, which is the
exact fault this change set exists to remove. The line is gone and the gap now
has one owner instead of two, per DSRD 7 section 4.3.

**Two are the gate not knowing about a bordered card, and are reported rather
than worked around.** `hairline-present` wants a hairline at the boundary above
the card, where the card's own border is the boundary. `hairline-edges` reads the
card's bottom border as a rule drawn at the foot of the page, which is the thing
that row exists to catch and is not what this is.

This is the second time today a bordered block has tripped a spacing row written
before bordered blocks were common on these pages. The other was
`header-to-content` against the full-bleed hero. **Both are questions for DSRD 6
and the gate, not decisions of mine.**

## Measured after deploy

Support answer, pre-purchase answer and category page, in Chromium and in WebKit:
the card draws on both answer types, the two routes draw only on the support one,
the trial panel still follows on the pre-purchase one, the category page still
closes with the grey panel, no chevrons remain in the card, and no page scrolls
sideways at 1440 or 390.

---

OWED BACK:

- **DSRD 1 section 8** gains the shape of the answer's close: one card, with the
  support routes inside it on the nine and the trial panel after it on the six.
- **DSRD 8** gains the closing card as a component.
- **A ruling on the two gate rows above**, which is the same question already
  open from the article hero: what a spacing check should do at the boundary of a
  block that draws its own border.

*No em or en dashes in this file; checked before writing.*
