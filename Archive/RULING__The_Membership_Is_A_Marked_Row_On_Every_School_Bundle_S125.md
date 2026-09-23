# RULING: the membership is a marked row on every school bundle

**DOCUMENT TYPE: ruling record, not a page spec.** It records rulings Kain gave in session and specifies no page.

**From:** Claude Code, S125, Monday 21 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Reads with:** `RULING__Kain_Rules_Quiet_And_Moves_The_Plan_Control_Into_His_Sentence_S125.md` and `RULING__Kains_Replacement_Line_For_The_Schools_Block_S125.md`, which this one follows directly.
**OWED BACK:** fold into DSRD 8 section 8 as part of the pricing page's school panel, and settle the one open question at the foot.

## How this came about

His new supporting line for the block dropped the membership, which his previous line had carried, and that mattered because his S124 ruling had taken the membership off all seven cards **on the ground that the line above them said it**. Code raised the gap rather than filling it, since the fix was copy and copy is his.

## His three rulings

**One, the membership becomes a line of the bundle.**

> "Add 12-Month Achology Community Membership Subscription as an additional product line under the courses included within each school bundle."

**Two, it is marked as an inclusion rather than a course.** Code reported the fault this created before he saw it: the card's facts line says five Courses and the list then showed six rows, so a reader counting rows makes it six courses. He asked what marking it would look like, and whether the row should drop a step of type to read as a bonus. Four were built and rendered, his own suggestion first: **Smaller**, one step down and grey; **Mark**, a plus before the words at full size; **Apart**, the row taken out of the list's rhythm; **Ground**, a whisper of the school's colour across the card.

> "Let's go with Mark."

Code recommended Mark and said plainly why not Smaller: a row set one step smaller and grey reads as a footnote, and the membership is a real part of what a reader is buying. The three that lost are deleted; they are in the theme repository's history at v0.536.0.

**Three, the wording changed in the same breath**, and is typed exactly as he gave it:

> "Change the text to 12-Month Full Achology Membership Subscription."

## What the row is

The last line of every bundle's list, at the courses' own face and size, with a plus from the theme's own icon registry before it in the AA-safe orange. **It is the one row in that list that is not a link**, because no page for it has been given to this block, and a row that looks pressable and does nothing is the fault this card was corrected for earlier in the same sitting.

The registry gained two glyphs this session for the pricing page: `chevrons-up-down` for the inline plan control and, already present, `plus` for this row.

## Shipped

Theme **v0.537.0**, deployed, with local, the server and the zip each measured and agreeing. `css_gate`: pricing.css PASS.

Checked on the rendered page at 1440, 1024, 768 and 390: the row carries his words on all seven cards, last in every list, at the courses' size, marked, not a link, and no card overflows.

## The question it left, answered by him in the same sitting

Code raised that the row named a product with no address, since every course on that list links to its course page and the membership did not. His answer:

> "Yes, link it to the membership page, and please ensure all these links open up in a new tab."

**So the row goes to the membership page**, at the address read from the theme's own navigation rather than typed from memory, and it behaves exactly as the courses above it do, hover and all. What sets it apart is the mark alone.

**And every link on the card opens in a new tab now.** The course names, Explore school, the membership row and the action, which already did, so the card behaves one way throughout. Each one says so where a screen reader can hear it, in the pattern the action on that same card already used: a link that moves someone to a new tab without warning is the one accessibility fault this instruction could have introduced, and it is closed.

**Explore school is included**, and that is named here rather than assumed, because "all these links" was said about the list. If he meant the list alone it comes back out in a word. Shipped as theme **v0.538.0**, deployed, with all 64 links across the seven cards measured on the rendered page.

## Still open on this page

The two membership panels and the free tier strip, the questions block, the closing help strip, and the page's rhythm judged last. `/pricing/` is still unpublished on Chat's S365 disposition and its DSRD 6 record is not filed.

*No em or en dashes in this file; checked before writing.*
