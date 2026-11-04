**For Chat. What this needs from you:** nothing to act on; read it to mark the button family's audit remnants done, and weigh the uncovered controls listed at the end as a round for Kain.

# DONE: the button family's audit remnants cleared, 0.707.791 on the build site (Kain: "Ship all five", 4 November 2026)

Theme commits 13225d8d, 23c850d9, 7233ddcd and a1f26b3e, pushed; deployed with deploy.py from a clean worktree of HEAD; local, server and zip agree at 0.707.791. Net theme lines: 25 added, 119 removed, 94 fewer (12 files: about, base, buttons.css, buttons.js, enquiries, footer, kh-band, kh-front, kh-search, kh-subject, knowledge-hub, pricing). Version bump is one line more.

## The findings, each cleared

1. **Search page kinds row** (and the same row on the subject, list and tag hub pages, which pick 7 names as one row): now pills (pick 8), the chosen kind in the fire frame. The old square corners, orange "All" fill, orange hover fill, white-on-orange words and divider colours are removed; the dividers keep their 1px room, clear. The All Tags banner's four kinds are left as Kain's signed S177 doors (Pattern Rise), not pills.
2. **Article, book note and quote contents links**: the writing-link rule no longer reaches the contents panel, so they rest in their own colour (grey, the current section dark) and gain only the 1.5px fire line (pick 19). Also removed: the panel's orange hover on read sections and its two old focus rings (the family ring now shows). The panel's own signed grey-to-dark hover (S164) is kept.
3. **Old looks**: the A to Z letters lose the 3px lift and orange shadow and lift 1 as every pill (the rise wave now releases each letter when it lands, so the pill lift works at all). The About question's radius 10 is gone; it has no surface, so its only effect was the focus ring's corner, now 4 like every family link ring. The enquiry topic tile ring is the family's own focus ring (2px orange, offset 2) and stays; the dead copies beside it (the send button, the named fields) are removed.
4. **Dead paint removed**: base.css .btn radius 10 and its focus radius; pagination radius 10, orange active fill, off-white hovers; footer cookie button radius; the footer social buttons' background, edge and orange hover wash (confirmed: they are family icon buttons, so their icons now take the family colours, white at rest and light orange in the fire ring, by fill: currentColor); pricing's hidden chevron turn; knowledge-hub.css's orphan .kh-search block, all of it (confirmed: no markup anywhere uses it).
5. **Hover and keyboard focus checked on every control type**, the footer social buttons and the mobile menu (below).

## Proof

- **css_gate.py**: kh-subject 75, cards 47, kh-tag 39, header 33, people 25, warm-room 1, every other changed file 0. Exactly the baseline.
- **Search**: none of the flagged lines remain (kinds row radius and fills, aria-current orange, rgba dividers, contents hover orange, the -3px lift, .btn focus radius, pagination paint, footer social wash and orange fill, cookie radius, the chevron rotate, .kh-search__ rules).
- **Playwright WebKit, 27 page types at 1280, 834 and 390** (every page type that renders; home and course pages are not found on the build site), Before (0.707.790) against After, every element's box measured with motion switched off: at rest identical everywhere. The only differences are timing parts, each shown to vary between two runs of the unchanged page too: the text link's fire line width, the tag page labels, the review stars filling in, half a pixel on one disc, and one Courses run at 390 that read 0 on a repeat. Pointed at and keyboard-focused (a real Tab press), up to two of each control kind per page, After moves nothing that Before does not move identically: the disc arrow turning and the menu line sliding (signed motion), and the About page's scroll-driven timeline.
- **Mobile menu** opened at 390 and 834: nothing moves on point or focus, paint unchanged, keyboard focus shows the 2px ring.
- **On the build site after the deploy**: buttons.css at 0.707.791; search and subject kinds rows are pills (999), the chosen one framed; contents links rest dark and grey; footer social icons white.
- **Kain saw it** in the one shared Change Viewer in Safari, each change its own switch (previews/button-standard-s208/round-remnants.js, served by that folder's serve.py), and said "Ship all five".

## Not covered by any pick, for Kain as a round (not designed here)

The pricing plan select, the enquiry topic radio tiles, the gateway tiles, the policy next rows, the door links (including the All Tags banner's four kind doors), the help question rows, subject rows, workbook tiles, logos, the skip link and plain list links.

## Not this job

Home and course pages answer "Page Not Found" on the build site (the theme main session's). SESSION_REPORT for Rule 13 not written by this session.

*No em or en dashes in this file; checked before writing.*
