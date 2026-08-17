# BRIEF: collapse every duplicated block into its one home

**From:** Claude Chat · **Date:** 2026-07-27 (S225) · **Approved by Kain, S225**

**Context, standalone.** The Source-of-Truth Rule is now written into DSRD 3 §2.6 as a build standard: every block is authored in exactly one home; previews are generated from that home, never re-authored; a page-local copy of a shared block is a defect. Your v0.36.29 and v0.36.30 ships already collapsed the routes grid, member stories and member voices into shared-parts.php and pointed the previews at the real renderers. This brief commissions the rest, so §2.6's duplicate register can empty.

**The work, one block family per pass, never a sweep:**

1. **The About preview builder's hand-authored CSS blob.** Your own inventory names this the largest remaining lie in the preview system: the About preview renders a "PROPOSED about-page CSS" copy rather than the live about.css. Collapse it: the preview renders the live stylesheet, and the blob is deleted.
2. **Frozen preview content.** Preview markup and copy are still frozen snapshots even though styling is now live. Every preview's markup must be generated from the block's one home, so a copy edit to a page appears in its preview without the builder being touched.
3. **Any remaining private copies** of the routes rows, poster tiles or circular member cards in help-parts.php, template-policy.php, 404.php or the builder scripts. Your inventory measured these authored in up to six files on 27 July; audit what remains after your v0.36.29 and v0.36.30 promotions, and collapse whatever is left.

**Per pass:** name the block family and its one home here before starting, collapse it, verify identical rendering (your diff-and-computed-values method), and file the evidence here.

**Done when:** DSRD 3 §2.6's duplicate register is empty and every preview renders live sources for markup and CSS alike. If a family turns out to be already collapsed, file the verification evidence and it closes the same way.
