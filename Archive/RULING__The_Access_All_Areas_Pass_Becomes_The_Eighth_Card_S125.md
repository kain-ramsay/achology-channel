# RULING: the Access All Areas Pass becomes the eighth card of the schools grid

**From Code, S125. Kain's rulings across one long sitting on the pricing page.**
**Shipped v0.554.0 through v0.567.0, deployed and verified at four widths.**

---

## 1. The pass leaves its own band and joins the grid

> "It would make sense that we use the white space within the school bundles,
> the Achology schools, because the Access All Areas pass essentially just
> gives the website visitor the opportunity to enrol in all seven schools at
> the same time, access all of the courses, and get the twelve months of
> Achology membership. So I think it needs to be a different card. It can't be
> laid out the same as all the rest."

Seven cards in a two-column grid leave the eighth cell empty on the bottom row.
The pass now stands in it.

**The dark band below the seven is no longer drawn**, which is the consequence
of his instruction rather than a separate decision: a page does not make the
same offer twice. Its renderer is left standing and untouched, so one word from
him puts it back.

**Two things this is worth recording for the standards.** First, the pass
already sat directly under the seven, so nothing moved in the reading order:
the page simply lost a whole band and filled a hole. Second, the band was the
page's principal visual contrast, and the card is still the one dark object
among seven white ones, which is a sharper contrast from inside the grid than a
dark band underneath it was.

## 2. What the card says: Inventory

Seven treatments were built and he ruled this one:

> "Let's go with the Inventory option ... I think that's definitely our best
> viable option."

The card lists the seven schools, each carrying what it holds: courses, hours
and lectures. A manifest rather than a list. Every figure is the school card's
own, read from the record those seven cards print, so nothing is counted twice
or counted differently.

**The six that lost are deleted rather than parked** and are in the theme
repository's history: Compact, Schools and Headline at v0.556.0, Count and
Sentence at v0.555.0. A seventh, listing all 28 course names, was thrown away
before he saw it.

**The lesson that produced it is worth more than the ruling.** His words on the
first set of four:

> "The card's not shown me anything. It's just like a big dark grey card with
> literally next to nothing in it ... you're not giving me context to judge
> anything."

He was right. Three of those four carried three lines of text into a cell as
deep as a twelve-course school, and centring them in it made a hole rather than
a card. **A cell in a stretched grid is as deep as its deepest neighbour, and a
card standing in it must either have that much to say or decline the height
outright.** The 28-course version was the same fault mirrored: it made the pass
card half as tall again as its neighbour and moved the hole into the school.

## 3. How the card looks: Spectrum, and his own drawing

> "Let's go with the Spectrum please ... and if you look in the pricing page
> folder, I've just added an Access All Areas Pass image you can build into the
> hero."

**Spectrum** gives each of the seven rows a bar in its own school's colour. It
was the only one of four that used something the site already means: those
colours identify those schools everywhere else, and the pass is the one product
holding all seven, so **this card is the only place on the site where all seven
school colours legitimately appear together.** Crest, Tag and Panel are deleted
and are in the history at v0.559.0.

**His objection that produced the four** is also worth keeping:

> "The spacing's great and all that kind of stuff, but it doesn't stand out.
> There's no image for it."

The cause was structural rather than a matter of taste, and it is a thing to
check on any future card that belongs to no school: every other card in that
grid carries a drawing and a colour, and a card with neither reads as the one
nobody finished.

## 4. His copy for the head

Given in two parts. First:

> "UNLOCK ACHOLOGY'S FULL CURRICULUM / The Access All Areas Pass / 28 Courses *
> xxx Hours Video * xxx Lectures"

Then, to pay for the picture:

> "If you need to create more space to enlarge an image, then just lose the
> word Unlock."

And, across every card on the page at once:

> "Rather than use the full word Hours, just use the short abbreviated word,
> like Hrs ... and just apply that to all of the schools and also to that card."

**The two figures he left as xxx are 600+ Hours and 2,146 Lectures**, and how
they were arrived at matters more than the numbers:

- **Hours** are summed from the course registry by the method the school cards
  already use, and the method was proved before it was trusted: run over the
  NLP school alone it gives 162, which is what that card prints. Over all 28 it
  gives 600.5, rounded down because every figure it is built from carries a
  plus. Summing across all 28 is safe where summing across schools is not,
  because a course can belong to two schools and the 28 are distinct.
- **Lectures** are Karen's 28 course files, read with a CSV reader. 2,146 rows.
  Two other records in that folder state the same number independently. **It is
  not the seven school counts added up**, which come to 3,555 for the same
  overlap reason.

## 5. His two rulings on the seven school cards, which came first in the sitting

- **The struck price is a faint diagonal**, bottom left to top right, spanning
  the digits, in the palette's decorative grey. Not the browser's line-through,
  which draws a horizontal rule low across the digits, and never the figure's
  own text colour. **This is a candidate for a site-wide standard**: it would
  hold anywhere a saving is shown against a former price.
- **The overlap note is deleted.** "Please delete this text": the line saying a
  course can belong to more than one school and to check before buying two
  bundles. The fact is untouched and still lives in DSRD 5 section 2 and in the
  commerce card data. What he ruled out was printing a caveat about the
  catalogue at the point where a reader is deciding. **That, too, may be worth
  a standard.**

---

## Faults found and fixed, recorded because two are patterns

1. **The seven school links on the pass card pointed at pages that do not
   exist.** The bundle record is keyed by the school's three-letter code and
   the list read that key as a web address. It asks the school registry now,
   which is what the seven cards above it always did.
2. **A picture positioned over space held back by padding cannot be trusted**,
   and this bit twice. The space is a share of one box and the picture is a
   share of another 48 points wider, so the gap between them moves with the
   screen: measured, ten points of air at 1440, two at 1024, and a collision at
   768. Both sides are now written from one measure. **The school cards have
   the same arithmetic and have not been checked**, which is a thing for their
   own turn, not this one.
3. **The card's hairlines were the light page's own**, near-white on a dark
   card, because the override was aimed at the top of each row and the divider
   is drawn on the bottom. Kain saw it as a design choice: "the hairlines are
   just way, way, way too bold."
4. **Spreading a list to fill a card puts all the surplus on one side of every
   divider.** His words: "really standardize the space either side of the
   hairlines. This is kinda pushing the whole thing out." The answer is equal
   rows rather than equal gaps, so the surplus sits inside the rows.

---

## What is still owed on this page

Not reached: the two membership panels and the free tier strip, the questions
block, the closing help strip, and the page's rhythm judged last. Kain closed
the session before them and has asked for a visual sweep over the pass card
first thing next session.

Still owed to him and unanswered: where his two pay-in drawings should live now
they are not controls; whether anything at the point of decision should reduce
risk, which needs his words; which name wins for the full price; and nine of 28
course rows printing the middle price over the full price on a phone.

*No em or en dashes in this file; checked before writing.*
