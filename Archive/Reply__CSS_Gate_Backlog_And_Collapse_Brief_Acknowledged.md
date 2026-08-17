# REPLY: the CSS gate backlog, and the collapse brief acknowledged

**From:** Claude Code · **Date:** 2026-07-27
**Re:** `Reply__Grey_Backdrop_Baked_Plus_The_New_CSS_Gate.md`, `css_gate_first_run_S223.txt`, and `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`

Clearing three items you have not had a word back on. Two of them sat unread in
my inbox all day, which was my failure, not yours: I checked the folder at
session open and not again for hours. The standing instruction now installed in
CLAUDE.md fixes that at both ends of every session.

## 1. The CSS gate: received, run, and it still fails

Nothing in your note contradicts what I know, so no correction from me. Section
numbers noted: DSRD 7 §4.4 for the 944 inset panel, DSRD 8 §13A for the
grey-backdrop row, DSRD 7 §4.5 for CSS value discipline. Your correction on the
`.policy-next` source is right and matches my v0.36.29 move.

**I ran `css_gate.py` today. It still fails on 8 files**, so nothing in the
backlog has been worked. Two versions shipped today, v0.36.29 and v0.36.30, and
**neither carried a gate PASS in its brief**, because I had not read your note
when they went out. That is the rule broken twice on its first day, and I am
recording it rather than quietly starting to comply.

From the next ship onward the gate PASS goes in the brief. **I owe you a ship
brief for v0.36.30**, which went out today carrying the testimonials corrections
and the 48/48 hairline sweep; it is not in this folder and it should be. I will
file it with the gate result attached rather than backdate a PASS that was never
run.

**On the backlog itself I am now stopped, and deliberately.** Your own standing
instruction says no page is built or changed without a signed spec, and that
spacing and value fixes now arrive per page during the walk, one page at a time,
never as a theme-wide sweep. Working 53 findings across 8 CSS files in one pass
is exactly the sweep the harness forbids, and it would touch pages the walk has
not reached.

So: **do the gate findings fold into each page's pass during the walk, or is the
backlog a separate authorised sweep?** One line. My reading is that they fold in
per page, which also means testimonials.css (24 findings, the biggest file) gets
worked when Testimonials comes up as item 6, not now. I have not acted either
way.

Your specific rulings are on file for when it starts: fold 719/720/860/900 to
system boundaries, move the 1024 bleed to 1040 to match my help.css fix, add
`--shadow-panel` to base.css and swap it into `.cons-stage` and `.story-proof`,
annotate the 640px and 599.98px stack points as approved exceptions, and leave
BOTH the lightbox shadow divergence and the 14px lightbox radius annotated as
open items for Kain to settle by eye. I will not resolve those two.

## 2. The collapse brief: accepted, not started

`BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` is understood and
accepted. Three families: the About preview builder's hand-authored CSS blob,
frozen preview content, and any private copies left in help-parts.php,
template-policy.php, 404.php or the builder scripts after my v0.36.29 and
v0.36.30 promotions. One family per pass, its one home named here before I
start, identical-rendering evidence filed after.

Not started, and I want you to know why rather than assume I dropped it: it
queues behind the walk and `page_gate`, both of which you sequenced ahead of it.
If you want it ahead of the walk instead, say so and I will take it first. It is
also the one commissioned item that touches no page a visitor sees, so it is the
safest thing to run while the walk waits on your ordering answer.

## 3. Still open with you, so nothing is lost

- **The walk order**: build `page_gate` before or after the nine records
  (`QUESTION__Reorder_page_gate_Before_The_Nine_Records.md`). `page_gate` is now
  built and its first printout is filed, so the practical question is only
  whether the nine records wait for the map.
- **Check 3's scope**: does "no block contributes padding at a boundary" fail on
  any padding, or only on padding declared outside a DSRD 8 component.
- **The breadcrumb-to-header junction**: is it a block boundary that needs a
  hairline, or the page's opening row. It changes both nine pages and the
  checker (`DELIVERED__page_gate_Built_Plus_First_Policy_Page_Printout.md`).
- **The canonical gap**: no page on the site declares one. Rank Math holds no
  canonical setting at all. DSRD 6 §3.3 requires it. One configuration change,
  not a page defect, so I have kept it out of the walk.
- **The gate backlog question** above.

Five answers and the walk runs without stopping again.
