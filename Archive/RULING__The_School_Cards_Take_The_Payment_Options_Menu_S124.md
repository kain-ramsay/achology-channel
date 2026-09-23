# RULING: the seven school cards take the payment options menu

**DOCUMENT TYPE: ruling record, not a page spec.** It records rulings Kain gave in session and specifies no page.

**From:** Claude Code, S124, Sunday 21 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Reads with:** `RULING__Payment_Options_Replaces_The_Budget_Box_And_The_Price_Grid_S124.md`, which this follows directly.
**OWED BACK:** the three items at the foot, and DSRD 8 section 8 folded to match.

## His two rulings

**One, the menu's resting words.** "I want there to be a very, very transparent term which says All Payment Options ... the course price in full remains as it is until a website visitor clicks to view a separate option ... that is how people are gonna know to click on the toggle and see what the options are."

So the menu no longer rests on the state it is already in, which teaches a reader nothing. It rests on the offer. Its resting entry carries no value and the price column falls back to the full price, so the page at rest is identical whether a reader has touched it or not, which is the half of his instruction that is easy to miss.

**Two, the same control on the school cards.** "We do want to use this functionality on the school cards too." Each card published three figures at once and now publishes one.

## Two calls Code took, named so they can be overturned in a word

**One menu for the seven cards, not one on each.** Seven fields in one block is seven objects where the reader has one question, and the index above answers the same question with one control for a list of 28. A reader comparing schools should be comparing them on the same footing, which a menu per card quietly breaks.

**The bundle's menu names a plan the card never published.** DSRD 4 section 1.1, quoted: "a single course offers three or five monthly instalments, a school bundle two, four or six, and the Access All Areas Pass three, six or twelve." The card published six and four and left two out. **A menu whose resting words are All Payment Options has to mean them**, so the plan the till offers and the page omitted is now on it. The four entries are One Time Fee, Pay in Two, Pay in Four, Pay in Six.

That is a correction to what the page published rather than a design choice, and it is raised here because it changes what a customer is told they can do.

## Shipped

Theme **v0.523.0** for the resting words and **v0.524.0** for the school cards, both deployed, with local, the server and the zip each measured and agreeing. `css_gate`: pricing.css PASS.

Checked at 1440, 1024, 768 and 390, driving both menus rather than reading the markup: each rests on All Payment Options showing the full price, One Time Fee shows the same figure, every other choice changes every figure in its own block, the two menus stay independent of each other, one figure a row and one a card at every width, the money level across each row of cards, nothing leaving a card, and no sideways scroll.

Two faults of Code's own were measured and corrected before Kain saw the block: the bundle menu stretched the full width of the seven cards, because in the index it takes its width from the tabs it shares a row with and here it stands alone; and it had to be brought onto the page's one text line with the heading above it, per DSRD 7 section 4.4a.

## Owed back

1. **Which name wins for the full price.** He gave "Enrolment Fee" earlier in the sitting and "One Time Fee" later, and ruled One Time Fee for both menus. The school cards' own figures still read "in full" beneath them.
2. **The school card's remaining unit words**, "over 2 months", "over 4 months", "over 6 months", now sit beneath a menu that names the same plan. Whether they stay is his.
3. **Two unnamed values on the school card**, still open from earlier in this sitting: the card's 3px school-coloured top border, and the percentages holding the artwork and the words apart.

## What he has said comes next

> "I think we can probably boil down these school cards and simplify them even further also."

So the card is expected to lose more, and Code is holding for his word rather than proposing it.

## Still open on this page

The two membership panels and the free tier strip, the questions block, the closing help strip, and the page's rhythm judged last. `/pricing/` is still unpublished on Chat's S365 disposition and its DSRD 6 record is not filed.

*No em or en dashes in this file; checked before writing.*
