> CHAT DISPOSITION, S357: answered. DSRD 8 section 26 (ruling 9 and the arrangement rule); DSRD 9 section 22.4. Nothing else owed. Archived.

# RULING AND SHIP: the reading bar joins up at the left where there is no Listen control

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.284.0,
deployed and measured on all four page types that draw this bar.**
**Ruled by Kain** live in this sitting, off the rendered article. His words:

> "We probably just need one set rule for the articles that carry a table of
> contents, which is gonna be the main articles and the book notes. I don't think
> we're gonna need them on the workbooks page, and the quote articles are too
> short to justify having one. We definitely want to lose the word count because
> it duplicates now. And also, I think what we just need to do is move the
> written by Benjamin Lockwood right to the left hand side of the component. With
> the date and the six minute read just following right on from it. So they're
> all kinda joined together. So that means that there's not actually going to be
> anything in the right hand side of that component."

**Owning documents:** DSRD 8 section 12.3, which owns this component and its
promotion, and whose sealing rule is the thing this change had to be built
around. DSRD 9's records of the article and book note page types.
**Board card:** none of its own; site-wide.

---

## What is on the page

On the article and the book note: the writer's photograph and name at the far
left, then the date, then the reading time, one joined group, and nothing at the
right hand end. No word count.

On the help answer and the quote page: exactly what was there before. Facts at
the left, Listen control at the right, word count still among the facts.

## The thing worth recording is HOW the bar knows which it is

This component's own rule, written at its head when Kain had it promoted at S109,
is that **a page says what goes in the bar and never what the bar is.** Nothing
about how it looks is a parameter, on purpose, because four pages drawing their
own copy is what caused the whole S109 sitting.

So an `align` argument was not available, and the two page types could not be
named in the component either: a component that knows post type names is a
component with four copies of the same drift waiting in it.

**What the two page types he named actually have in common is that their bar has
no Listen control.** The article and the book note both pass `speaks => false`;
the help answer and the quote page both pass `speaks => true`. That is not a
coincidence to route around, it is the real reason the arrangement differs: a row
with a control in it has three things to place and needs the two ends to place
them, while a row without one has two things and reads better joined.

**So the test is the control.** No page passes an alignment, and a page type that
later gains or loses a recording gets the right arrangement without anybody
remembering to go and change it.

## Two smaller decisions inside it

**The writer is first in the markup, not moved by CSS.** An `order` property
would have put the writer at the left for a reader looking at it and at the right
for a reader hearing it. The writer's link is built once into a string and
written out at one of two points in the row, rather than being written twice,
because two copies of one link is how two copies quietly stop matching.

**One property changes and no new number enters the component.** The facts carry
`margin-right: auto`, which is what throws everything after them to the far end;
in the joined arrangement that is removed. The gaps are the component's own
existing two, 16 between the writer and the facts and 8 between one fact and the
next, so the group reads as a writer and then their facts rather than three equal
things in a line.

## The word count came off two templates, not four

The help answer and the quote page keep theirs. Neither carries a contents card,
so neither says the number twice, and taking it off them would be removing a fact
from a page to match a page it has nothing in common with.

## What was measured after it shipped

Article and book note: joined, the writer's element starting at the bar's own left
edge at zero, the facts following, nothing at the right, and no word count. Help
answer: unchanged in every respect, measured rather than assumed.

**One thing could not be rendered.** Every quote page on the build ground is still
a draft, so there is no public address to photograph. Its template was not touched
in this change set and it takes the identical branch the help answer takes, which
was measured; that is the strongest proof available today and it is named here
rather than dressed up as a fourth green check.

---

OWED BACK: the article and book note entries in DSRD 9 describe this bar as the
writer, the date and the reading time, joined at the left, with no word count. The
DSRD 8 component entry gains the rule that the arrangement follows the presence of
the Listen control.

*No em or en dashes in this file; checked before writing.*
