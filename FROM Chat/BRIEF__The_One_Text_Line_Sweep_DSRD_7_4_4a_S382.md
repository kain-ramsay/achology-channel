> **CODE DISPOSITION, S131: WAITS ON a theme session.** Read in full on arrival. It changes theme CSS and renders five components for Kain's eye, and Kain ruled this session backlog only, no design or template work; it goes first in the theme queue.

# BRIEF: the one text line sweep, DSRD 7 section 4.4a, all 44 built pages

**Needs from Code:** apply the rule below to `MEASURED__Left_Text_Edges_On_44_Built_Pages_S131`, straight swap what you can, and bring back one list of what you cannot.

**From:** Claude Chat, S382, Wednesday 23 September 2026. **To:** Claude Code.
**Answers:** the line at the head of `MEASURED__Left_Text_Edges_On_44_Built_Pages_S131.md` asking for this brief.

## The rule, DSRD 7 section 4.4a, quoted

"Within a page, every block's words begin on one vertical line, whatever that block sits on. The container edge belongs to panels, and to nothing else." A panel's own padding sets the line; a block with no panel takes the same inset, so its copy starts in the same place. The number is not the rule, the line is.

## The three things your own measurement note already named as not violations

Apply these first, mechanically, across every page in the table before looking for anything else.

1. **A list item's own indent.** `li` text starts right of its bullet or number. That is the list, not a second line. Never a violation.
2. **A genuine second column.** An article's sidebar, a pricing tier's second or third card sitting beside the first, a course card grid column. These are a different reading region, not the same block sitting on a different edge. Never a violation. Where you find one, name it once in your reply (which template, which selector) so the list of known second columns is on record.
3. **A paragraph wrapping beside a floated picture.** The wrap is the picture's doing, not the block's own start. Never a violation.

## What a panel is, for this sweep

A panel is a block with its own visible boundary, background, or card treatment, drawing its own padding. Its child text is allowed its own line, set by that padding, so long as every other child of that same panel starts on the same line. What is not a panel is bare text sitting directly on the page container with no boundary of its own; that text takes the page's one line, the same inset as every other unboxed block on the page.

## What is a real violation

Two or more unboxed blocks on the same page, at the same width, starting at different left edges, once list indent, second columns and float wrap are excluded. Also a block inside a panel that does not match its own panel's other children.

## What to do

For each of the 44 pages in the measurement, at each of the three widths:

1. Drop every edge explained by list indent, a second column, or float wrap. You already flagged which ones these are in the raw notes; confirm each on the live page rather than from the class name alone.
2. Of what is left, where every remaining block already shares one line, the page passes, nothing to do.
3. Of what is left, where a genuine violation exists, straight swap it to the page's one line: move the offending block's inset to match the rest, same hue of fix as the school colour sweep, nothing a reader would call a design change. List each swap: page, selector, old edge, new edge.
4. Where a block sits inside a panel and disagrees with its own panel's other children, the same straight swap applies inside that panel.

## Centred blocks, held out, never a straight swap

Every centred block in the measurement is the same handful of repeating components, not forty individual design questions. Rule each component once and it settles every page carrying it:

- **`h2.warm-room__title` and `p.warm-room__body`.** Appears on twenty of the forty four pages: all seventeen instructor profiles, `/about/instructors/`, `/about/founders-letter/`, `/reviews/`, `/testimonials/`, `/about/`. One rendered ruling: is the warm room block an approved exception to the one line rule, being a pull quote style panel, or does it move to the line.
- **`p.ap-works__count`.** Appears on four of the seventeen instructor pages: Frederick S. Martin, Charlotte J. Avery, Benjamin Lockwood, Kain Ramsay. One rendered ruling, same question.
- **`p.lite-cite` and `p.lite-quote`, `/testimonials/` only.** One rendered ruling.
- **`h2.founders__title` and `p.founders__text`, `/about/` only.** One rendered ruling.
- **`p.help-contact__line`, `/help/` only.** One rendered ruling.

Render each on its real page, tabbed against the one line version, standing rule 16. Five rulings closes every centred block the measurement found, not twenty five.

## Report back

One line per page: pass as is, or the swaps made. One line per centred component: which page it is rendered on for Kain's ruling. Named second columns, once each, for the record.

*No em or en dashes in this file; checked before writing.*
