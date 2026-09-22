# RULING: Kain puts the school cards' courses behind a control, reversing his own S123 instruction, and narrows S125 in the same sitting

**From:** Claude Code, theme session, S128, Tuesday 22 September 2026. **To:** Claude Chat.
**Board card:** Pricing page.
**Theme version:** v0.629.0, deployed and pushed.

Two rulings here, given in one sitting, and one record problem underneath them that Code cannot settle.

## 1. The courses go behind a control, and it reverses S123

Kain raised it himself after reading an outside assessment of the page. **His words:**

> "with the school cards you've essentially dismissed the suggestion to make the courses expandable ... why don't we just make viewing the courses that are included within each school optional, so someone could press click here to view courses included with the school ... and that could just be the same for all seven schools, and then for the access all areas pass that can be optional as well ... we're not giving viewers any options to expand and be autonomous."

**This reverses his own S123 instruction, and he was told so in the sitting before anything was built.** `pricing-parts.php` carried his S123 words at that exact spot: *"it's really good that each of the cards just shows the different courses that are included within it."* The courses were behind a disclosure then and came out on that instruction.

**His S128 argument is a different one rather than a change of mind about the same one.** At S123 he was judging whether a card shows its contents. At S128 he is judging the page's consistency: the 28-course index above lets a reader open it or leave it, and these eight cards gave them no such choice.

**Built as native `details` and `summary`,** which is Code's technical call: no JavaScript, keyboard operable and announced to a screen reader with no aria attribute typed, and every course name stays in the delivered markup whether open or shut, so the cross-links still count and a reader with no JavaScript loses nothing.

**One line was needed that the ruling does not work without, and it is named because it is a real change rather than plumbing.** The grid stretched every card in a row to the deepest one. The moment a reader opened one card, that stretch dragged its neighbour to the same depth and left the neighbour holding the "large dead middle" the S123 disclosure was dropped for. Cards are now their own height. Nothing moves in the shut state, where all eight carry the same content anyway.

## 2. The membership row folds in, which narrows S125

Code first left the membership row outside the disclosure, on the reading that S125 put it on every bundle so it would always show. Kain looked at the render and corrected it. **His words:**

> "you've left that hanging kind of outside of the dropdown option and it doesn't make any sense ... just fold that in, into the dropdown with each of the seven schools, then all eight cards will actually be exactly the same size, there won't be any imbalance."

**He was right about what it did.** The pass card carries no membership row, so leaving the row outside made seven cards one row taller than the eighth.

**S125 is narrowed rather than overturned, and that is the line for the DSRDs.** The row is still on every school bundle, still last in the list, still carrying the plus, the same wording and the same address. What changed is that a reader now asks to see the bundle's contents before seeing it.

## 3. What it measures

Seven school cards at 282 and the pass card at 285, so **level to within three rather than exactly equal**, which is stated plainly rather than rounded off. The block is 1202 against 2369 before, a little over half. Eight disclosures, all shut on load, no membership row painted on any shut card. 57 links inside them, the 50 courses and the seven membership rows, all still in the delivered markup. `css_gate` pricing.css PASS. axe 4.10.2: zero WCAG 2.2 AA violations.

## 4. THE RECORD PROBLEM, and it is the reason this file matters beyond the two rulings

**The filed S123 ruling and the live page disagree about the course index, and Kain's S128 argument reasons from the live page.**

`RULING__Kain_Rules_The_Course_Index_And_The_Monthly_Figures_S123.md`, ruling 1, quoted: *"The 28 courses are one line each, carrying the course name and its price, all 28 in the page at once, with no expand control. The three that lost are deleted: the price list (eight rows then View all 28), By school ... and By learning route ..."*

**The live page shows nine rows and a "View All 28 Courses" button.** That is the losing option, near enough. The button's own wording comes from another of his S123 instructions carried in the markup, *"replace See all courses in the CTA with View All 28 Courses"*, so both cannot describe the same settled state.

Kain's whole S128 case is that the course index gives the reader a choice and the school cards did not. **That premise is true of the page and may not be true of the record.** Either the ruling file describes an option that was never built, or the build drifted afterwards and no ruling was filed for the change.

**Second, smaller, and the same kind of thing.** The S123 words that governed this exact decision, *"it's really good that each of the cards just shows the different courses"*, live only in a code comment. No filed RULING carries them. So the fact of that ruling is evidenced and its words are not, and a code comment is not a source under the Shared Rules.

This is Chat's to resolve, because it is a question about which record is true, and Code never edits a DSRD or a ruling file.

## OWED BACK

The S128 disclosure ruling and the S125 narrowing written into DSRD 8's school bundle card rows and DSRD 9's pricing page layout. And a ruling on the course index: whether the page or the S123 file is right, with the loser corrected, so the next person to reason from either one is not reasoning from a page and a record that disagree.

*No em or en dashes in this file; checked before writing.*
