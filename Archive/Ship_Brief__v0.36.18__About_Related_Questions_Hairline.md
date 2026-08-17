# Ship brief — v0.36.18, the Related Questions block on /about/

From: Claude Code · 2026-07-23 · pushed, zip rebuilt.
Closes the first of the two `/about/` findings raised in the v0.36.16 brief.

**What changed.** The Related Questions block read 32px of air both sides on
`/about/` and 48px both sides on the Code of Ethics, which are the same block on
two pages of the same family. `about.css` carried a scoped override pulling it
down to the About page's 32px section rhythm. That override is removed, and the
block now takes its values from `.policy-body .help-popular` in `policies.css`,
the rule every other quiet page already used. Kain ruled it in.

DSRD 7 §4.3 is what settles it: a block arriving with its own separator standard
keeps that standard on a densely ruled page too, because the page tier governs
section rhythm and not blocks that specify their own. The Code of Ethics was
already right; `/about/` was the page out of step.

**One thing worth your attention.** That override was not drift. It was a
deliberate decision taken while the About page was being built, and its comment
said in as many words that the block "joins the page's 32px one". So §4.3, as
rewritten this session, reverses a specific build decision on a shipped page. It
is removed rather than left contradicting the standard, and the comment now in
its place records what it did and why it went, so nobody reinstates it from the
stylesheet alone. If §4.3's clause was written without that page in view, this is
the moment to say so, and it is a one-line change to put back.

**Verified before shipping**, live at 1440 and 375: the block moves from 32/32 to
48/48 at both widths, keeps its hairline and its zeroed bottom margin, and 48px
holds at phone, which is correct — a block carrying its own standard does not
take the page's 32px phone tier. The Code of Ethics measured 48/48 at both widths
already, so the two pages now agree.

---

## Still open

`.about-grid__paths` reads 18px above its line and 16px below. It sits inside the
About grid, which DSRD 8 §12.1 records as page-local, so §4.3 may not govern it
at all. That is a question about scope rather than a defect I can measure my way
out of, and it is still Kain's call.

The four schema decisions in `Report__Per_Page_Type_Schema_Inventory.md` §3 are
also still with you.
