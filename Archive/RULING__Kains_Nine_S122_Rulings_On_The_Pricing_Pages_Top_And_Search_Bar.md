# RULING: Kain's nine S122 rulings on the pricing page's top block and its course search bar

**From:** Claude Code, S122, Thursday 17 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Session type:** theme.

**DOCUMENT TYPE: not a page spec.** It files rulings and specifies no page.

Read after the three S122 rulings already filed: The Chooser as the layout, his
own copy for the four cards, and a colour per card with "Edge and tint". This
file carries everything he ruled after them, in the order he ruled it. Theme
versions v0.474.0 to v0.489.0.

## The rulings

1. **The statement strip is gone.** "Lose this completely please." His two mini
   statements and everything that served them are deleted.
2. **The top of the page is one panel.** From four rendered answers: "I really
   like the one panel option." Everything from the eyebrow to the guarantees sits
   inside one off-white panel with the cards on it. **And no hairline under the
   cards:** "I think you can just remove the hairline underneath the four cards."
3. **The cards are white and the colour moved to the price.** In three steps,
   all his: "lighten each of the four cards' backgrounds ... maybe by like fifty
   percent", then "they need to be lighter still", then "make the current
   backgrounds white and use from one of your earlier designs, colour the pricing
   text, the second line down on each of the cards. So just assign the same
   colour as the CTA from each card to that line."
4. **The card's two lines are set apart by weight, not size.** "Weight not size
   is my choice." Both stay 12px Card Stats; the first takes 600 in brand dark.
5. **The top block is unified in three moves at once.** "Yes, i want All three
   please": the price drops to 28 so the page title is alone at the top size; the
   card names lose their small capitals so the eyebrow is the only uppercase in
   the block; and the two facts take the cards' own small voice.
6. **Three guarantees replace the two facts,** in his own words, on his reading
   that "the accompanying sentence just kinda says what the heading of the
   sentence has already said".
7. **Each guarantee links to the help answer that proves it.** His proposal, and
   his hybrid on four rendered options: "I choose Quiet, but please underline the
   following words, so that it's transparent a link is actually there." Then,
   seeing it: "just lose the underlining under the three words ... having the
   underlining appear on hover is probably enough ... like the deeper Achology
   orange. Just fainter."
8. **The course search bar is One row.** "I think one row needs to be our
   option."
9. **A panel that copies another panel copies its container rules too.** His
   question on the strip option, which caught a real fault: see below.

## What Chat needs to record, beyond the rulings themselves

**His link-hover question is already answered by his own ruling.** He asked
whether there should be one link hover standard site-wide "if that's not already
in place". There is: DSRD 7 section 1, ruled by him at S263, the AA-safe orange
#B8460F, with #D85A1B reserved for buttons so links and buttons never share a
hover. Nothing new was invented; this page now obeys it. **What the standard does
not cover is a link that rests in body colour rather than in brand orange**,
which is what his Quiet ruling made these three. That is a genuine gap.

**The course control bar was never built to DSRD 7 section 5.5**, whose own
sentence is that "a later control departs from these values only by a ruling
recorded here". Five departures were found by measuring the rendered page. Four
are corrected: height 46 and 48 against the standard's 44, so the three controls
in one bar did not line up with each other; type 16 against 14; focus ring 3
against 2; search glyph 18 against 17 and positioned so it drifted with the
field's height. **The fifth is not Code's to take:** both dropdowns are native
browser selects where section 5.5 specifies the site's own `.ach-select`, "built
because a native select draws its own option list and ignores CSS in Safari".
That component exists but lives inside `reviews.css` and `reviews.js`, so using
it anywhere else means moving it somewhere shared, which touches the Reviews
page. **Put to Kain, not taken on the way past.**

**Every section heading on the page owed its supporting line 16 and was giving
it 8.** DSRD 7 section 4.3's table is a lookup: 8 for a label that belongs to the
title, 16 for reading text under a section heading, 24 under the page title. A
supporting line is a sentence. All four headings on this page were wrong and all
four are corrected from one declaration. **Worth a check on other built pages**,
since nothing about this fault was particular to this page.

**A panel that copies another panel must copy where it sits, not only how it
looks.** Kain asked whether the strip option should take "the same container
rules as the grey background block above". Giving it the same tint, radius and
inset put its words 48 further in than every other block, because it sits inside
a block that has already taken that inset: measured at 264 against the page's
216. The fix is the outdent DSRD 7 section 4.4 already describes. **The general
lesson is worth a line in section 4.4a:** matching a panel's treatment without
matching its position breaks the one-text-line rule rather than serving it.

## The fold-back, complete this session (Harness Rule 14)

- Every ruling built, gated (`css_gate.py`: `pricing.css` PASS) and deployed, the
  last at theme **v0.489.0**; server, local and zip proved identical each time.
- The approved state exported as the prototype's next version after each ruling,
  in the Pricing Page folder inside Homepage + Commercial Design Prototypes.
- Everything measured on the rendered page rather than judged by eye, at 1440 and
  390, and the numbers are in the commit messages.

## OWED BACK

Nothing to answer. Write the rulings into the documents that own them, and
record the four findings above: the link-rest gap, the `.ach-select` question for
Kain, the section-heading spacing check for other pages, and the section 4.4a
line about matching a panel's position as well as its treatment.

*No em or en dashes in this file; checked before writing.*
