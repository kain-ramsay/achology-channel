# FIX BRIEF: the cards sheet misrepresents the Knowledge Hub cards, and the member row is empty

**From:** Claude Chat, S256. **Date:** 2026-08-10.
**Approved by:** Kain, S256.
**Follows:** COMMISSION__Build_The_Card_Sheet_For_Review_S255.md and your DELIVERY__The_Card_Sheet_And_The_Build_Facts_S051.md.

## Context, standalone

The card sheet is live at /cards/ and the S256 design review opened on it today. Kain's first look found every section 6 Knowledge Hub card stretched to the full page width at desktop. We diagnosed it in session before writing this.

## Fault 1: the sheet page does not load knowledge-hub.css

The .kh-grid rules live in knowledge-hub.css (1 column base, 2 at min-width 768px, 3 at min-width 1024px, gap var(--grid-gap)). That stylesheet loads on the Knowledge Hub pages but not on the cards sheet page. Measured live on /cards/: .kh-grid computes display: block, grid-template-columns: none, and the first card measures the full container width. So every section 6 card on the sheet renders outside its real grid, at a width it never has on a real page.

The delivery said the grids were the real ones. The class is real; the rules never reach the page.

**The fix:** make the cards sheet page load knowledge-hub.css, or otherwise render the section 6 cards inside their real grid. Your call on mechanism; the outcome is the acceptance test below.

## Fault 2: the section 13A member row is empty

Measured live on /cards/: the .lite-grid element renders with zero children. The grid shell is there (its columns resolve correctly from components.css) but achology_member_voices() emitted no cards on this page. On /testimonials/ the same component renders the cards.

**The fix:** make the member row on the sheet render its cards as it does on Testimonials.

## Acceptance

On /cards/, at a desktop viewport at or above 1024px:
1. The standard Knowledge Hub cards sit at their real 3-column grid width, not full width.
2. The featured cards span 2 of the 3 columns, per cards.css.
3. At 768 to 1023px the grid is 2 columns; below 768px, 1 column.
4. The section 13A row shows the member cards.

Deploy and reply through TO Chat with the pass confirmed on the rendered page. The S256 review of the section 6 cards and the member row waits on this; the course cards are being reviewed today from the sheet as it stands, because product-section__grid resolves correctly from components.css.

*No em or en dashes in this file; checked before writing.*
