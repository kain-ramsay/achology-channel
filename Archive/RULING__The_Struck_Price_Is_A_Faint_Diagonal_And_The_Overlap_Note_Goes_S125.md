# RULING: the struck price is a faint diagonal, and the overlap note goes

**From Code, S125. Two rulings by Kain in one sitting, both on the pricing page.**
**Shipped in v0.554.0, deployed and verified.**

---

## 1. The strike through the full school price

He raised it first as a detail, in his own words:

> "Just one thing, Claude. Um, small attention to detail, and that's just in the
> total school price that's been crossed out. I noticed you just have a
> horizontal line through the... I think it's the the bottom quarter of the of
> the actual amount. I'm just wondering if you could change this. so that the
> stroke travels through the full amount from the bottom left to the top right.
> Does that make sense?"

He was describing a real fault rather than a preference. A browser's own
line-through is drawn as a horizontal rule at a fixed height off the font's
baseline, and on these particular digits at this particular size it sits low
enough to cross only their bottom quarter. So it was replaced with a stroke
drawn corner to corner across the figure's own box, which is the one way of
getting a true diagonal on seven different numbers: an angle typed in degrees
would be right at one school's price and wrong at the next, because the box is
only as wide as the number inside it.

That shipped at v0.553.0, and he looked at it and ruled again:

> "Claude, that's kinda too much. Um, and sorry. I maybe didn't communicate
> clear enough here. I said from the bottom left to the top right, that's what I
> meant. But I think it just needs to be a faint line. Like, that's just kinda
> too much. Can you kinda make that line a bit more subtle, please, in the
> direction that I've asked? Thanks."

**The direction was right and the weight was wrong**, which is worth recording
as its own kind of correction: the first pass got the geometry he asked for and
then drew it at full strength, so a mark that exists to be glanced past became a
mark that is looked at.

Three things quieten it in v0.554.0, and none of them touches the diagonal:

1. **It takes the palette's decorative grey**, the value DSRD 7 section 1
   reserves for separators, meta and marks that are not read, rather than the
   figure's own text colour. A strike is punctuation around a number, not part
   of the number.
2. **It is drawn thinner than a hairline**, so a screen renders it softened
   rather than solid.
3. **It is pulled in off the top and bottom of the line box**, which carries
   leading the digits never fill. The stroke now spans the number instead of
   overshooting it at both ends, which was most of what made it read as heavy.

**The general rule this leaves behind**, for Chat's record and for any later
page that strikes a price: a struck figure is a faint diagonal in the
decorative grey, bottom left to top right, spanning the digits. It is not the
browser's line-through, and it never takes the figure's own colour.

## 2. The overlap note under the seven schools

> "Please delete this text - A course can belong to more than one school, so
> check the included courses before buying more than one bundle."

Deleted, with nothing in its place, because copy is his.

**The fact it carried is untouched.** That a course can belong to more than one
school is DSRD 5 section 2's own sentence, and it is the reason the seven school
totals do not add up to the catalogue; that explanation still sits in the note
above the commerce card data, where the sums are worked out. What he ruled out
was printing it on the page, at the point where a reader is deciding.

**Why he is right, in a sentence Chat may want for the standards:** it is a
warning about the shape of the catalogue standing in the buying block, and the
courses inside each school are already listed in full on each card, so a reader
who wants to check is not being told anything the card does not show them.

**Nothing was orphaned by the deletion.** The paragraph carried a class that no
stylesheet anywhere in the theme styled, which is itself worth noting: it was
drawing nothing of its own and never had been.

---

## What Chat may want to do with this

Two candidates for a standard, both Chat's call rather than Code's:

- the struck-price rule above, which is currently true on one page and would
  hold anywhere a saving is shown against a former price;
- whether a "check before you buy" caveat belongs anywhere in a buying block,
  now that one has been removed from this one.

Nothing is blocked on either. The page is shipped and correct as it stands.

*No em or en dashes in this file; checked before writing.*
