**For Chat. What this needs from you:** nothing; a record that the button family's dead old code is gone, shipped as 0.707.789.

# DONE: the button family's dead old paint is removed (0.707.789)

Follows DONE__Sweep_The_Button_Family_Across_The_Build_Site_S453 (0.707.788). Kain asked whether the family left dead code behind, and said "Yes, clean it up".

## What was removed, and what was kept on purpose

- **Removed:** 59 old paint declarations in 26 rules on the family's buttons (main, second choice, the course card buttons, the pricing choice buttons, the header Sign In, the Listen button), across base.css, cards.css, components.css, header.css and pricing.css, 190 lines in all with the notes that described the removed hover fills. The family sets those same colours, fills, edge colours, corners, shadows and underlines on those buttons in every state, so none of the removed lines could ever show. Old dashes in base.css comments were replaced with plain punctuation.
- **Kept, because Kain's 3 November ruling keeps every layout as signed:** every size, padding, edge width, font and spacing of the old rules.
- **Kept, because they are still the fallback:** the old look of tabs, pills, icon buttons, fields and toggles. The family reaches those by script and leaves alone any one it cannot paint without moving it (a plain browser field); there the old look is the one that shows.
- **Kept:** --color-orange-hover, still used by about.css, book-note.css and components.css.

## Proof

- A search for old paint on any family button now finds 0 (it found 59 before).
- css_gate: base.css, components.css and pricing.css PASS. cards.css fails on 47 older spacing lines (48 before; none touched); header.css on its 35 older lines (unchanged).
- Every element on 29 page types, at 1280, 834 and 390 in Playwright WebKit, compared between the deployed family (0.707.788) and the cleaned code for position, size, colour, fill, edge colour, corners, shadow, underline and opacity: 87 of 87 checks read 0 changed. The same check against the page before the family finds 68 differences on Pricing alone, so it can fail.
- deploy.py from a clean worktree: the server, the theme and the zip identical at 0.707.789.

*No em or en dashes in this file; checked before writing.*
