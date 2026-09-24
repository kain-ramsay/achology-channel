**Record only; asks nothing.** Filed to the Archive per The Shared Rules section 6 (S380).

# SHIP: theme 0.662.2, the quote page hero picture back beside the words

**From:** Claude Code, factory session, S133, Thursday 24 September 2026.
**Board card:** the quote page template.

**Kain's words, in the sitting:** "Claude, our article images have broken" (on a live quote page, the picture drawn as a small pill beside the breadcrumb), then "Yes" to the fix put to him in plain words. A theme edit in a factory session, on his word.

**What broke, and whose it was.** Code's S132 book note hero rework (theme 0.659.0 to 0.661.1) made the band's container the grid and set the hero grid to `display: contents`. The book note wraps its cover in `bn-hero__aside`, which the rework placed; the quote page puts `bn-hero__cover` straight in the grid, which nothing placed, so on every quote page the picture fell into the 48 gap column beside the breadcrumb. The same rework deleted the `bn-hero__actions` rules the quote page still uses below 1200. The quote pages were not checked when the book note shipped.

**The fix.** `quote.css`, on `.single-quote` only: the S132 arrangement is switched off and the S130 hero grid returns, with the button row rules restored for quote pages. No design change: this is the S130 layout Kain approved (`RULING__Kain_Moves_The_Quote_Page_To_The_Book_Note_Layout_S130`). Book notes untouched, checked live (cover level with the breadcrumb at 1440). Commit 16a5d9f.

**Proof.** Before, at 1440: the picture 64 by 19. After, live at 0.662.2: 256 by 261, level with the words and their height, at 1440; 256 by 297 beside the words at 900; the phone unchanged at 390. `css_gate` passed on edit; `deploy.py` CURRENT (local, server and zip agree at 0.662.2). The pictures themselves were never missing: 16 sampled live pages across four types, every uploaded picture answering 200.

**Lesson kept.** A change to a shared hero is checked on every page type that borrows it, before it ships.

*No em or en dashes in this file; checked before writing.*
