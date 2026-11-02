ARCHIVED, Chat S452 (2 November 2026): written home in DSRD 9 section 25 (policy page).

# RULING and SHIP (Kain, Code's S203 theme main session, 2 November 2026): the legal policy pages list their sections under the opening

First line: Chat, write this into the policy page template's layout (DSRD 9, the policy page; its signed spec in the Policy Page design folder).

Kain made the Privacy Policy the exemplar for every legal policy page and asked Code for at least five improvements that could reach them all. Code named six: a contents list, a reading progress line and back-to-top, an "In short" box (Chat's words), clearer section breaks, an "Other policies" strip, and a closing block. Kain took the contents list first. From four placements in the shared Change Viewer (previews/policy-contents-s203: Side Panel, Code's recommendation; List Under the Opening; Pinned Bar; Number Rail), Kain's words: "2 List under opening".

The look: under the opening, "On This Page" in the article page's Table of Contents look (knowledge-hub.css .kh-aside, now loaded on these pages) on the warm cream, one entry per section heading, two columns from 768; each entry jumps to its section, landing clear of the menu. Built from each page's own headings, so no list is typed by hand; a page with under four headings carries none. The three founder pages do not take it.

Shipped at 0.707.696 and 0.707.697 (template-policy.php, functions.php, policies.css; theme commits b21301d7 and 1ffff25b), deployed, local, server and zip agree. Read on the build site: Privacy 20 entries, Terms 15, Cookie 9, Refund 14, Trust 8, Disclaimers 15, Accessibility 10, How We Write 9; every entry's jump lands on its heading; one cream frame at 1280, one column at 390, no overflow.

**Corrected the same sitting (Kain: "it's kind of pushed too far in", then "ok" to Code's fix):** the article panel's marker slot, link inset and reading track are removed, so the section names start under the heading and both columns read alike; from 1040 the cream box bleeds 32 each side with 32 inside, the locked inset panel (DSRD 7 section 4.4), so its label, heading and first column sit on the page's left edge (measured at 1280: title, label, heading and first column all at 240); below 1040 the box is flush, as the rule says. Shipped at 0.707.700 and 0.707.701 (theme commits ab882486 and e9bc8d11).

Two copy points from the review, for Chat: the Privacy Policy's opening line repeats its first paragraph almost word for word; and its first section is headed "1. Full Privacy Policy", which now shows in the list too.

Still to come, one round each: the other five improvements, built once for all eight pages.

OWED BACK: the ruling written home, and Chat's call on the two copy points.

*No em or en dashes in this file; checked before writing.*
