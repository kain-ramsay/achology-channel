**For Chat (theme session item): should the readability faults found on the Listing and Category hub pages be put to Kain in a planned sitting, and where in the queue? Asks one decision of Chat.**

# ASK: four values on the Knowledge Hub navigation pages fail WCAG AA (S151)

Found by the page checker's axe run after 0.707.137, measured in the browser:
1. Card "Read this Article": #ED6922 on white, 3.16 to 1 (needs 4.5). The article card build sheet names #ED6922; DSRD 7 section 1 and base.css say small orange text takes --color-orange-link #B8460F. Sheet and standard disagree.
2. Selected pill (category and A-Z): white 12px on #ED6922, 3.16.
3. "Category" overline on the hub: mid grey #8A9199, ruled DSRD 9 D11, fails for small text.
4. Card author line: #B0B8BE, 2.01. Its signed build sheet says soft grey #5E6B75 (S259). The code is simply wrong; Code corrects this one without a ruling unless Chat objects.

Items 1 to 3 change colours Kain can see, so they need his choice. Four rendered options exist in the theme's `previews/contrast-s151/` (open `hub.html`); Code recommends option 3, the AA orange for text and the control orange #C85015 for fills, as base.css describes each token's role. The cards are site-wide, so the fix reaches every card.

Kain stopped this in the S151 sitting as outside the plan. It blocks both pages' DSRD 6 chapter 7 regardless.

OWED BACK: Chat's placement of this in the queue.

*No em or en dashes in this file; checked before writing.*
