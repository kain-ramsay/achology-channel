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
