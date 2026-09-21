# RULING: Kain rules Ribbon, sets the pass drawing himself, and rules Lift for the block of eight

**From Code, S126. Three rulings from one sitting on the pricing page.**
**Shipped v0.568.0 through v0.571.0, deployed and verified at four widths.**

---

## 1. Ribbon, for the Access All Areas card

His ask at the S125 close was a visual sweep over the card. Four directions
were built, each changing exactly one thing and leaving the rest of the card
alone, so his yes would be a yes to one thing. He ruled:

> "I like the ribbon option."

**What Ribbon is.** The seven colour bars were drawn on the rows' own edges and
the rows touch, so all seven ran together into a single unbroken stripe down
the side of the card. Each is now a chip with air above and below it and a
round cap, and the hairline between rows runs the full width underneath them.

**Why it is worth keeping as a reason and not only as a choice.** Spectrum
exists because this card is the only place on the site where all seven school
colours legitimately stand together. A gradient says "a spectrum"; seven
separate marks say "seven schools", which is the sentence the card is making.

**The three that lost are deleted rather than parked** and are in the theme
repository's history at v0.568.0. Banner made his drawing much larger on a
deeper head; Measure drew the head's three facts as figures with his own words
under them; Tally did the same to the seven rows' twenty-one figures.

**Nothing he turned down at S125 was offered again.** Compact, Schools,
Headline, Count and Sentence lost the Inventory ruling; Crest, Tag and Panel
lost the Spectrum ruling. None of the four put to him was one of those eight
wearing a different name.

## 2. The pass card's drawing, given by Kain himself

Not chosen from options. He gave it in his own words and then settled it by eye
on the render, in four passes.

> "Move the image up slightly ... drag this image up to the top left ... there
> needs to be a similar amount of space between the actual card, not the full
> image, not the brain behind it, just the card. There needs to be similar
> space to the right hand side of it as there is to the top of it ... and then
> just kind of enlarge the cards a little bit so it makes better use of the
> space."

And, in the same breath:

> "Even if that means that some of the image cannot be seen within the card,
> that's okay."

Then, by eye: too far up, so smaller and pushed back in; left by ten; right by
twenty; and smaller again.

**The thing being spaced is the ticket and not the file, and that is the whole
difficulty.** The drawing is a ticket and a face on a halo of dots, and the
halo runs to all four edges of the file, so anything positioned by the file's
edges spaces the dots rather than the ticket. Measured off the file, and
measured twice: the first pass asked where the solid drawing is and answered
with the face and the ticket together, which put the right edge 8 points in
when the ticket's own is 2. Both gaps are written from one measure now, so the
ticket keeps the same air on the top and on the right at every screen width by
construction rather than by a pair of offsets that agree at one size.

**One mechanism is worth carrying to any future card**, because it was wrong
first and would have stayed wrong quietly. A percentage inside `top` is read
against the containing block's height, and a card head is as deep as its own
words, so the ticket landed 44 below the card's top instead of 24 and would
have moved again every time a line wrapped. A percentage inside `margin-top` is
read against the width, like `right` beside it.

## 3. Lift, for the block of eight

His ask, on the ruled card:

> "Can I ask you to look at these school cards now as a block of eight? I've
> looked at them all objectively and make some suggestions on how we can
> improve the look and feel of this further. I think there's a few things we
> can do to improve this. Can't quite put my finger on it."

Four directions were built and he ruled:

> "Yes, go with Lift please."

**What Lift is.** Every card was outlined in the same hairline its own course
rows use, so the block was drawn in one weight from edge to edge and nothing
said where a card stopped and a row inside it began. The outline goes and a
soft shadow takes its place, so a card is told from the page by depth rather
than by a line, and the only edge it wears is its school's colour along the
top. The cards stand a step further apart.

**What he could not put his finger on, named.** One weight of line doing three
different jobs at once: the card's boundary, the row's separator and the head's
floor. The eye had nothing to rank.

**The three that lost are deleted** and are in the theme repository's history at
v0.570.0. Fill shared a short card's spare height out among its courses so no
card carried a gap above its price; Colour deepened each card's own school wash
and set its price in that school's colour; Quiet took the hairline out from
under every course.

## 4. Single, for the course names that were turning onto a second line

His note on the ruled block:

> "An Entrepreneurs' Guide to Launching and Growing a New Business has sprawled
> over onto two lines in desktop view. I really don't want this."

**Measured first, across nine widths, because the answer depended on where it
happens and it was not where it looked.** The page's container stops growing at
1200, so from 1200 upwards every card is 492 across, its course column is 430,
and not one of the fifty names turns. Below 1200 the two cards abreast share a
shrinking row: three names turn at 1152, fifteen at 1100, forty-one at 1024.
The longest wants 397 where the card offers 316. Eighty-one points is more than
tightening can find, so it is a column problem and not a type problem.

Four directions were built and he ruled:

> "Yes, go with single."

**What Single is.** Between 768 and 1200 the eight cards stop standing two
abreast and take the full width one at a time. It was the only one of the four
where not one name turned, at every width from 1024 to 1600.

**The three that lost are deleted** and are in the theme repository's history at
v0.571.0. Tight narrowed the gap between the cards and their own padding, which
took 41 turning names at 1024 down to 18; Smaller dropped the course name one
step on the type scale, which held to 1100 and left seven at 1024; Hang kept the
turn and indented the second line so a name still read as one item.

**One thing in this is worth carrying beyond this page.** Both card drawings are
a share of their own card, so giving a card the whole block took the school
drawing from 152 across to 267 and the pass card's ticket from 168 to 298. On
the school cards the head is only ever as deep as its two lines of type, so most
of the drawing was cut off. On the pass card it would have silently undone the
four passes Kain had just spent settling that ticket by eye. **A drawing sized as
a share of its container is undone by any change to that container, and a
ruling made on one is only safe while the container holds.**

**One boundary is a declared exception.** DSRD 7 sections 4.1 and 4.5 name 768
and 1024, and this uses 1200, annotated in the stylesheet as a one-off. 1024
would have left untouched the whole band Kain is actually reading the page in.
The correct instrument is a container query on the card itself; this theme has
none, and admitting its first one is a change of a different size from a pricing
page sitting. **If Chat would rather that boundary did not stand, it is one line
to change and it comes back as a question.**

## 5. The course block's tab row, given directly

Two things, both given on the rendered row and both built as given rather than
turned into options.

> "You have kinda placed the number after each of the categories, which I just
> don't think is necessary."

The row was saying it twice: every category name already ends in the word
Courses, and the list underneath is the count. Deleted rather than hidden:
markup, both rules and the per-route arithmetic. The partition check that
arithmetic also served is kept, because that is what stops a course going
silently missing behind a tab nobody opens.

> "Pay in 3 and Pay in 5 are fine, but the text is kinda left aligned inside of
> the box."

The cause was the clear mark. It is held in the pill's width at rest so that
pressing a pill never makes it wider, but it was held only on the right, so the
wording sat off centre by exactly the width of a mark that is not being drawn.
The same space is now held on the left.

**Code's own view, offered and not acted on:** the word Courses appears on all
three tabs, in a row sitting directly under a heading about courses. Losing it
would shorten all three. That is copy and it is Kain's.

## 6. Under, for the membership block, and his own copy for it

His ask, on the rendered page:

> "Let's tackle the entire membership block as one. Currently what I'm looking
> at is like one big down arrow that's just consuming the entire page, which is
> obviously a mistake. I also know that there is content hidden underneath the
> see what membership includes ... I think what we can also do with this one is
> build it into a grey background panel that's just kinda got the same rules
> applied as the pricing and access panel right at the top of the page."

Four arrangements were built and he ruled:

> "Go with Under please."

**Under is the order the block already had**, with nothing hidden. So the whole
of this sitting's change to the block is the three things that were never a
choice, and that is the finding worth carrying: **he was shown four
arrangements and kept the one that moved nothing, so what was wrong with the
block was never its order.**

- **The arrow was the chevron on the fold-away's summary**, the one icon on the
  page with no size rule of its own, so it drew itself as wide as the block.
  Sizing it would have hidden the cause. The control it belonged to should not
  have been there, so the control went and the icon went with it.
- **Seven reasons to join were behind that control**, on the one block whose
  job is to say what joining gets you. They are on the face of the block now.
- **The block sits on the panel**, with the top of the page's three rules read
  from that panel rather than retyped.

**The three that lost are deleted** and are in the theme repository's history
at v0.574.0. Lead put the inclusions first as the argument; Split stood them
left with the cards stacked right; Doors made the free tier a third card so all
three ways in stood on one row.

**His copy for the block, typed as he gave it:**

> "The Achology Community: Subscription Options / You don't have to buy a
> course to begin learning with Achology. You can try the learning community
> before you commit."

The word Achology is accented in the heading and not in the line below it,
which is DSRD 7 section 3.0 rather than a choice made here.

**One fault the four found is worth the whole method.** The actions did not
line up across the cards: each pushed its button down by however much its own
words needed. It was found on the arrangement that put three cards in a row,
where it was obvious, and it had been there on two all along. **The option he
did not choose is what found the fault in the one he did.**

## 7. The questions block becomes the help article's own card

Told twice, because the first build took the frame and not the thing. His
second telling:

> "I want uniformity throughout the website ... it's just a completely
> different panel from the questions at the bottom of the help section. So I'm
> gonna ask you once again just to model the exact structure of the panel that
> is in the bottom of the help questions and pull through just relevant
> associated price related questions."

**What was wrong with the first attempt, recorded because it is the general
mistake.** It borrowed the card's shell and left this page's own accordion
inside it. A component is its structure, not its frame: the help card is a list
of linked questions with their summary lines, and a card with something else
inside it is a second component wearing the first one's clothes.

**What it is now.** The section carries the help card's own class, so every rule
that shapes it on a help article shapes it here, and this page's stylesheet
gained no rule that touches a help class. The six rows are real help answers
from the two price categories, each linking to its own page with its own
excerpt underneath.

**The six written questions and answers came off the page**, on his word given
before any of it was built. Asked directly whether the six go and the block
becomes links to real help answers, he said: "yes, that is correct."

## 8. The page ends on the four doors, pointing outwards

Four ways to end the page were put to him, after he said he was not sure the
page needed a closing block at all. He took the one that returns the reader to
the four routes, and improved it in the same breath:

> "Rather than just using empty buttons like what you've done, just use exactly
> the same cards as what we've used up in the hero, except point the buttons
> out to the respective pages rather than to aspects of the page."

**He was right, and it fixed the one weakness in what he had been shown.** Four
bare buttons said nothing about what was behind them, so the block leaned on
the line above it to explain itself, and that line had already been flagged to
him as no longer matching its buttons.

**It is one card renderer used twice**, with a single argument choosing which of
each route's two addresses the button carries. The head and the foot of the
page cannot drift into two different sets of doors.

**The four addresses are DSRD 1's own**, quoted from its tables: `/courses/`,
`/academy/schools/`, `/access-all-areas/` and `/membership/`.

**And not one of those four pages exists**, checked against the install: none of
them is on it, published or draft. The addresses are correct and answer nothing
today. That is the build pointer's own stated condition for publication rather
than a new problem, and it is now written in the code beside the addresses,
because the same fault was found once already on this page at S125.

## 9. Kain approves the page for the build

His words at the close:

> "The first thing in the next session, I want you to build this page in the
> WordPress theme. Do you understand? It is good enough to build."

**What this settles.** The page has been designed and ruled block by block
across S121 to S126 in the preview, which exists because `/pricing/` does not
exist on the install and because a design is never iterated on the canonical
page. His approval opens the next step.

**What it does not settle, and both are named in the session report.** The
page's rhythm, judged last, was in his own running order at this session's open
and was not reached. And his line under the closing block is now wrong, which
he has deferred until after the build: it still offers the help desk and the
free membership, and that block offers neither.

**One condition this approval does not remove.** Publication still waits on the
four pages above existing. Building the page in the theme is not publishing it.

---

## Two repairs that were in every option, because a fault is not a choice

1. **The pass card's price stopped disappearing.** Found on the render: choose
   Pay in Two, Four or Six from the menu above the seven schools and the card's
   money row emptied, leaving the saving standing with nothing to save against.
   The script puts the chosen plan on every card in the grid and each card
   draws the figure that matches; the seven schools render four figures so one
   always matches, and the pass renders the full price alone. **The fix is not
   to give it the schools' figures**, because the till does not offer them.
   DSRD 4 section 1.1, quoted from the canonical file this session: "The plans
   are not uniform ... a single course offers three or five monthly
   instalments, a school bundle two, four or six, and the Access All Areas Pass
   three, six or twelve." So the card holds its one-time price whatever the
   schools' menu says, which is the only thing on it true at every setting.

2. **The seven school drawings came inside their cards**, closing a debt this
   page has carried since S125, whose own record reads: "a picture positioned
   over space held back by padding cannot be trusted ... the school cards have
   the same arithmetic and have not been checked." They have it: the space held
   back is a share of the card's content box, the drawing is a share of the
   head's own box, and the head is bled 24 wider on each side, so the two are
   shares of numbers 48 apart and the air between them moves with the screen.
   On the pass card that measured ten points at 1440, two at 1024 and a
   collision at 768. The seven also pinned the drawing to the head's padding
   box, which runs to the card's border, so every one of them was cut by the
   card's own right edge while everything else on the card was held in from it.

Also repaired: Kain's fact line on the pass card no longer breaks onto a
separator at 390, and no figure is split from the word that counts it.

---

## What is still owed on this page, unchanged from S125 except where marked

**A question that is his and is now blocking nothing:** the Access All Areas
Pass is sold on three, six or twelve monthly instalments while the schools'
menu offers two, four or six. The card holds its one-time price at every
setting of that menu, which is true but silent. Whether the pass should carry
its own three, six and twelve is a design and commerce decision and it is his.

Still owed and unanswered: where his two pay-in drawings should live now they
are not controls; whether anything at the point of decision should reduce risk,
which needs his words; which name wins for the full price, Enrolment Fee or One
Time Fee; and nine of 28 course rows printing the middle price over the full
price on a phone.

**Not reached on the page:** the two membership panels and the free tier strip,
the questions block, the closing help strip, and the page's rhythm judged last.
That is his order, given at the open of this session.

*No em or en dashes in this file; checked before writing.*
