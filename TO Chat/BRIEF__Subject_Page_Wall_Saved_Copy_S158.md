# BRIEF: Subject page saved copy, Editor's Picks and the audit, S158 (theme session)

For: Chat. Asks: the two items in the OWED BACK line. Everything else is a record of what shipped.

Shipped, all on main and deployed to the build site:
- 0.707.179: each category wall's built data is saved in a transient keyed by theme version (counts, the 48 cards as finished markup, picks, faces, topics, course), cleared on any piece, category or tag change. Logged-out Psychology load fell from 0.62 to 0.37 seconds; the output is the same size.
- 0.707.180 and 0.707.181: Editor's Picks are articles only. The lead article is never also a pick, and a gap is filled from the newest other articles. Why: Kain's screen snap showed a book note's upright cover cropped to the 104 by 72 thumbnail, title cut in half.
- Data change on the install: the ach_picks field of all seven categories held book notes (the original lists are in RULING__Subject_Page_Audit_Fixes_S158). Replaced with the newest articles. Three of the lists also repeated the lead article; the code now removes that.

Full audit, S158, run on the live build site at 1440, 768 and 375 wide, all seven categories: 0 pictures failed to load, 0 distorted, 48 cards built (45 to 48 shown after the layout trims), no sideways scroll. Measured in a real window: four columns on desktop, three on tablet, two on phone. Not yet done: the watch of Kain's own Safari (his Safari lets me read the screen but not drive it, and he has not yet scrolled the wall for it).

Cloud job 20 (branch cloud-work/job20-theme-picture-derivatives), reviewed by Code against the real files, NOT merged per Kain: it merges into main with no conflicts (tested without merging). The code is the new helper achology_derivative_attrs in shared-parts.php, which returns nothing when a copy is missing, so a missing file cannot break a picture; the CSS keeps the original as the fallback line before each image-set. The copies named in the code exist on the branch. Not proven: a live render, because that needs a deploy. Held with jobs 18 and 19 until Kain says the subject pages are right.

OWED BACK:
1. Chat writes "Editor's Picks are articles only; the lead is never a pick" into the build sheet and DSRD 9 section 20.0b.
2. Chat names who chooses the Editor's Picks (open since S153).
