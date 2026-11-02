**Needs from Chat: write the two Pricing rulings home in DSRD 9 section 36.9, and rule on four more spaces inside the learning block. For the theme session. Code, S209 theme main session, 2 November 2026.**

# DONE: Pricing's lift and course table, the trial card line, and the learning block's Exception 21 (theme 0.707.777 to 0.707.781)

**1. The Smooth Lift on Pricing's cards (Kain, "1, Smooth Lift", option 1 of four, previews/about-board-s209/round-pricelift.js), 0.707.777.** The four opening cards and the eight school cards rise 4 with the hover shadow in one ease-out of 0.35 seconds, the same lift as the Knowledge Hub cards and About's closing block. pricing.js lifts a card on pointer entry and drops it only when the pointer leaves the place it stood before rising, so it cannot flicker at its foot; mouse only; reduced motion keeps it still. Measured in WebKit at 1280 on the build site: 2.9 of 4 at 110 milliseconds, 4 settled, held with the pointer 2 inside the original foot, down on leaving, nothing moved at rest.

**2. The course table broken up (Kain, "I do like option one, school marks", option 1 of four, previews/about-board-s209/round-pricetable.js; then on the wasted space above the table, "Make an educated guess, Claude"), 0.707.778 to 0.707.780.**
- Each course shows its school under its name with a dot, in the school's colour; the full school names come from achology_school_bundles(), the bundle cards' own list.
- The three category tabs read dark at 600, with a sliding orange underline (the Fire Slide Kain chose at S208) under the tab in front.
- The payment control is one rounded switch, Pay in full, Pay in 3, Pay in 5, the chosen one dark. Pay in full is new and replaces the clear mark Kain asked for at S125 as the way back to the full price; the toggle-back in pricing.js is gone, since each button now sets its own plan.
- Tabs and switch share one line on a computer, switch at the right, and fold under the tabs at the left below 1200; the phone's stacked tabs take no extra gap.
- Measured in WebKit at 1440, 1280, 1024, 834 and 390: one line at 1440 and 1280, folded left at 1024, 834 and 390; the underline under the tab in front at every width; Pay in 5 on the third tab shows the monthly figures and Pay in full returns them; school marks on every visible row; no sideways scroll.
- The pill radius (50) is annotated as the button family's one-off until the sweep brings the gate's pill tier.

**3. Your S453 reply, item 2, 0.707.781.** The Membership Plans card reads "$7 trial" and "For your first 30 days". The two other "$7 Trial" pills (pricing-parts.php's monthly_pill and commerce-cards.php's membership pill) are other components and are unchanged; tell me if they take sentence case too. The card's second line, "Then $34.50 Per Month", and the other cards' lines ("Flexible Payment Plans", "Lifetime Access to Courses") are still in title case; your ruling that card lines take sentence case reaches them, so please confirm the words.

**4. Exception 21, 0.707.781.** Written for the component, not by route. page_gate.py has a new COMPONENT_SPACING_EXCEPTIONS list that carves out kfp-sign__review padding-top 120, kfp-sign__post padding-bottom 51 and kh-section__titles row-gap 2 wherever they render. image_gate.py's EXEMPT_GROUPS gains the block's tile drawings, gauge and stars (its arrows stay audited). The card links now carry the class kfp-door__link at the component's home (kh-front-setup.php), so the link hover wash no longer reaches them anywhere, and About's own override is removed. page_gate on /about/ at 0.707.781: icon-registry passes, the 19 drawings carved out under the exception, and the three spaces carved out at each tier.

**Four more spaces inside the block still fail spacing-scale on About, as they do on /learn/:** kfp-sign__sub margin-bottom 10.8 (desktop) and 2.1 (tablet), kfp-sign__fig margin-top 2.1 (tablet), all auto margins that set the gauge and its line in the band; and kh-section__header row-gap 12 (phone). Chat to rule whether Exception 21 takes them too.

OWED BACK: one line in FROM Chat on the four spaces and the card line words.

*No em or en dashes in this file; checked before writing.*
