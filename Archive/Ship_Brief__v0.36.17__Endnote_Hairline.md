# Ship brief — v0.36.17, the endnote hairline, and one home for the family's hairline air

From: Claude Code · 2026-07-23 · pushed, zip rebuilt.
Completes the pair started in `Ship_Brief__v0.36.16__Policy_Header_Hairline.md`.

**What changed.** `.policy-endnote` held 48px of air above its line and 24px
below, at every width, the exact mirror of the header defect. It now reads 48/48
at desktop and 32/32 under 768px, DSRD 7 §4.3's default tier. Both halves of the
mirrored defect I reported are now closed on the seven legal pages.

**One home, at Kain's instruction.** He asked for this to be set once and inform
every page rather than page by page. It cannot come from a token, and §4.3
already says why: the spacing tokens do not change at breakpoints, so the phone
value has to be an explicit media query. What it can be, and now is, is one
labelled block: §3 of `policies.css` carries both carriers and the single phone
media query, with a comment saying that is where the family's default-tier air
lives and that a new section hairline joins those selectors rather than
declaring its own numbers.

**One thing worth recording in §4.3 itself.** The two carriers keep separate
declarations inside that media query, and must. A `border-bottom` carrier takes
`padding-bottom` above the line and `margin-bottom` below it; a `border-top`
carrier takes `margin-top` above and `padding-top` below. I grouped them while
building, caught it before it shipped, and split them again: grouped, it sets all
four properties on both elements and adds air on the side neither carries. §4.3
states the principle ("never split the space across two elements") but not this
consequence, and it is the exact trap someone tidying the stylesheet will fall
into. Worth a sentence in the section.

**Verified before shipping**, live at 1440 and 375, reading computed values
either side of every hairline on each page: refund policy moved 24/48 to 48/48 at
the header and 48/24 to 48/48 at the endnote; cookie policy read 32/32 at both
lines on phone; the Code of Ethics kept all six of its hairlines unchanged at both
widths; `/about/` and the 404 did not move.

---

## Still open, unchanged

The two `/about/` findings in the v0.36.16 brief stand: the Related Questions
block reads 32/32 there against 48/48 on the Code of Ethics, and
`.about-grid__paths` reads 18/16. Neither is fixed, both move pixels, both are
Kain's call. And the four schema decisions in
`Report__Per_Page_Type_Schema_Inventory.md` §3 are still with you.
