**For Chat. What this needs from you:** write the header search into DSRD 8 section 18 (a new subsection, the new registered string, and the menu button switch moving from 880 to 960), and close the trunk test "how do I search" fail on every page record at once.

# RULING: the header search control (Kain, Code's S179 theme sitting, 22 October 2026)

**What Kain ruled.** Code rendered four header search options in Safari on the About page at 1280, 834 and 390, each posting to the search results page. Kain proposed a fifth himself, Code rendered it as option 5, and he picked it.

His words, as he gave them:
- The design: "when someone clicks on it, the search box opens up ... when that search tab within the menu bar opens up, help just disappears. So we just lose the help option. Otherwise, we're kind of cramming all the rest of the menu items right up against the logo." His reason: "space efficiency."
- The words in the box: "How about just using Search Knowledge Hub?"
- On the tablet render: "the search box kind of covers over the hamburger. Which we shouldn't I don't think that needs to happen."
- The ruling: "Yes, Claude, I like option 5. Option 5 is fine. Apart from on tablet."

**What is built (theme 0.707.489, on every page of the build site).**
- A magnifier sits beside Sign In (beside the menu button below 960). Pressed, it opens a box in the bar reading "Search Knowledge Hub"; Help and the magnifier step out while it is open and come back when it closes (a cross, Escape, or a new page). Return sends the words to the search results page, the front end of SearchWP; an empty box does not send.
- From 1200 up the box sits between the links and Sign In and the other five links slide left, clear of the logo. From 960 to 1199 there is no room for the box beside five links, so it covers the links while open. From 768 to 959 it takes the logo's place and the menu button stays beside it, per Kain's tablet line. Below 768 it fills the bar.
- **The 960 finding, shown to Kain in the sitting.** The bar is full at 880 (logo, six links and Sign In leave no spare width), so the magnifier fits beside them only from 960. The menu button now takes over below 960 rather than below 880. Nothing came out of the bar.

**Measured** on the build site at 0.707.489 in WebKit, on six pages (front page, About, Knowledge Hub front page, Help, Pricing, a search results page) at 1440, 1280, 1200, 1024, 960, 900, 834 and 390: 48 of 48 pass. The magnifier shows and the box is hidden when shut; open, the box shows with every placeholder letter visible, Help and the magnifier are gone, the typing point is in the box, the menu button shows exactly from 768 to 959, nothing overlaps, the bar stays 72 high, no sideways scroll, no script error; Escape closes it. Typing "freud" and Return lands on /?s=freud.

**Fold-back (Rule 14), in the Header + Footer folder.** `COMPONENT_DATA__site-header.json` is record version 2: a new search block carrying Kain's words, the responsive switch at 960 with its reason, and new gate checks. The prototype is now version 3 (exported at 0.707.489, standalone, the search working in it), v2 moved to Archive (Superseded), and the folder README says so.

**Owed by Chat.**
1. DSRD 8 section 18: the search control as a new subsection; "Search Knowledge Hub" as a registered chrome string, Kain's own words; section 18.15 and DSRD 7 section 4.1's dependants list moved from 880 to 960.
2. The trunk test: the About record carries "how do I search" as a site-wide chrome fail (Chat's S321 finding). The header now answers it on every page, so that line closes on every page record together, not one at a time.

**Not touched.** The search results page itself. The 404 page's search box (part 5 of the S375 search brief) stays with the search work.

**Found in passing, not fixed.** header.css carried 38 older spacing-scale flags from the stylesheet gate before this change; every line added here passes. Left as they were, because changing them would move the signed header.

**Signed off.** Kain tried the built header in Safari at 0.707.489: "Yes, Claude, it is. It's fine."

*No em or en dashes in this file; checked before writing.*
