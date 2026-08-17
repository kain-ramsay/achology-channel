# Ship brief — v0.36.16, the policy header hairline

From: Claude Code · 2026-07-23 · pushed, zip rebuilt.

This is the first of the two defects I reported to you in
`Reply__Preview_Provenance_And_Hairline_Measurements.md`. Kain saw it on the
cookie policy page within minutes of reading it, and ruled the correction in, so
it is built rather than waiting on a brief.

**What changed.** `.policy-header` held 24px of air above the line and 48px
below, at every width, on the seven legal pages. It now reads 48/48 at desktop
and 32/32 under 768px, which is DSRD 7 §4.3's default tier. The rule simply
predates §4.3.

**What deliberately did not change.** The document header variant, used by the
Code of Ethics, the manifesto and `/about/`, measures 32/32 at both widths
already, which is §4.3's dense tier and correct. The 404's 43px above the line
is your recorded optical correction (DSRD 8 §12.5) and is untouched. The phone
rule is scoped past both variants explicitly rather than relying on source
order, so neither can inherit the 32px by accident later.

**Verified before shipping**, in a live browser at 1440 and 375, by applying the
new rule to the rendered pages and reading computed values either side of the
line: cookie policy moved 24/48 to 48/48 and 32/32; Code of Ethics, manifesto,
`/about/` and the 404 did not move at either width.

---

## Still open from that reply, and two new ones

**The `.policy-endnote` hairline is now done too, in v0.36.17** — Kain ruled it
in minutes after this brief was written. See
`Ship_Brief__v0.36.17__Endnote_Hairline.md`. Both halves of the mirrored defect
are closed, and the family's default-tier air now has one home in the stylesheet.

**Two more found while measuring `/about/` at his request:**

1. **The Related Questions block reads 32/32 on `/about/`** but 48/48 on the
   Code of Ethics. §4.3 says a block arriving with its own separator standard
   keeps it on a densely ruled page too, so one of those two pages is wrong and
   it is `/about/`. Worth checking whether the About page's own rules are
   reaching into a block that owns its spacing, which is the same class of leak
   `policies.css` already guards against for the prose rules.
2. **`.about-grid__paths` reads 18px above and 16px below.** It sits inside the
   About grid, which DSRD 8 §12.1 records as page-local, so §4.3 may not govern
   it at all. Flagging it rather than judging it: if the grid is a component with
   its own internal rule, it is out of scope and should say so somewhere.

Neither is fixed. Both move pixels, so both are Kain's call.
