**For Chat. What this needs from you:** record the button family as shipped on the card, and write Kain's 3 November ruling below into DSRD 7 section 5.1 where it changes what 5.1 says.

# DONE: the button family is on every page of the build site (0.707.788)

Answers BRIEF__Sweep_The_Button_Family_Across_The_Build_Site_S453. Shipped as theme version 0.707.788 on 3 November 2026, on Kain's "Yes, deploy it", after he saw Before and After in the shared Change Viewer in Safari.

## What shipped

- **buttons.css and buttons.js**, new, loaded after every other stylesheet on every page (functions.php, achology_enqueue_button_family). The family from PICKS 1 to 21 as amended by 17 to 21: the clean flat action orange main button with the shimmer and the turning disc, the second choice button in the fire frame with its disc, text and arrow links (grey to dark, the mini disc, the fire line), links in the writing, the sliding fire line on the header menu and the fire line under breadcrumbs, contents and footer links, the Fire Slide tabs, the Fire Ring pills, the Ring to Fire icon buttons, the one plus and minus mark on every toggle, the fire focus on fields, all ten wow touches, reduced motion respected. School colours keep their own colour (pick 14); the cookie Accept and Reject wear the identical main button (equal prominence).
- **base.css** gains the family tokens (fire light, fire deep, fire frame, fire line, pill radius, sizes). header.css, footer.css and components.css lose the old nav hover colours and the footer's own drawn line, which the family's fire line replaces.

## Kain's ruling in this session (3 November 2026), for DSRD 7 section 5.1

"I want the design and the layout of all of these pages to be exactly the same as what it was before you applied this new button system." The family therefore changes how a control looks and nothing else: colour, edge colour, corners, rings, frames, discs, marks, lines and motion. It never changes a size, padding, margin, gap, font or display. Where the signed preview gave a control new sizes (46 tall buttons and fields, 40 tabs, 36 pills, 40 icon buttons, Como 14/600 on links, tabs and pills), each control keeps its own signed size and type on its own page; the look is the family's. A control that cannot take the paint without changing size (a plain browser search box) keeps its old look. This replaces the sizes in PICKS 2, 5, 6, 7, 8, 9 and 16; their looks stand.

## Proof

- css_gate.py: buttons.css, base.css, footer.css and components.css PASS. header.css fails on 35 older spacing lines, the same 35 before this change; none is a line this change touched.
- Layout: every element on 29 page types measured Before and After in Playwright WebKit at 1280, 834 and 390: 87 of 87 checks read 0 elements resized and 0 moved.
- Look: the built family compared with the signed family page in every state (rest, pointed at, focused, pressed) at three widths before the layout ruling; after the ruling the colours, frames and motion are unchanged and only sizes follow each page.
- Deploy: from a clean worktree of HEAD; deploy.py reports the server, the theme and the zip identical at 0.707.788; the Pricing page on the build site serves buttons.css and buttons.js at 0.707.788.

## Not done, and why

- The checker reads pages through the mirror; the build site's bot guard blocked this Mac once today for fast scripted reads (SiteGround unblocked it; it is not a permanent pass). Every script now fetches each page once, slowly, and keeps it. Kain was offered SiteGround's crawler review and left it optional.
- The course pages /academy/... and the home page currently render the not-found template on the build site (no front page is set), so their family was checked on that template.

*No em or en dashes in this file; checked before writing.*
