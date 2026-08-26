> **CODE DISPOSITION, S085: WAITS ON** the first page that needs the component being specified and signed. S084 confirmed no section-header class family exists in any stylesheet; the book note page hand-writes the pattern as kh-section__header, and whether kh-section becomes the component is the open question in FINDING__The_Header_Was_Never_Checked_And_The_Section_Header_Was_Never_Built_S084.

# APPROVED BRIEF: the section header component exists, is approved, and is yours to build

**DOCUMENT TYPE:** approved brief. Not a page spec. **From:** Claude Chat, Session 282. **Date:** 18 August 2026.
**Board card:** "Cards + Chrome Sweep: Review all Unreviewed Components + give each a Prototype + Data File".

---

## What happened, in one paragraph

Kain approved the section header component in the Chat side panel today. It was rendered to the S258 render standard at 1200, 768 and 390, with real subtext copy read from DSRD 9 section 20.10 and the card grid shown as neutral placement blocks marked as such. He ruled it, and the fold-back is complete on this side: the approved prototype, its data file and a folder README are filed in the **Section Header** folder under Component Design Prototypes, the component registry carries its row, and DSRD 8 carries its decision section 23.

## Why this one came to the panel and not to Safari

The dividing question in standing rule 16 is whether the built theme already holds the thing. **It does not.** `base.css` carries `icon-section-header` and `icon-section-header-container`, and has for a long time, but the header block itself has never existed in the theme. The Reviews page writes its own inline and says in the file that it is deliberately not shared. So there was nothing built for you to render, and the panel was the correct surface.

This is worth naming because the same check sent the other four chrome components the other way. The site-wide header, the site-wide footer, the breadcrumb and the Where Next panel are all in the theme already, so those four are Safari sittings with you, not panel renders from me.

## What is in the folder, and what governs

The **Section Header** folder holds three files: the approved prototype, `COMPONENT_DATA__section-header.json`, and the folder's own README. Per standing rule 19 the prototype is the signed record and the data file completes the build instruction. Precedence: prototype wins, the data file must match the prototype, the theme code must match the data file.

The data file carries a **gate block** in the same shape as the review card's, with a selector and property binding for every value worth checking, so your build-versus-record gate can actually compare something rather than passing green on an empty comparison. Its `specimen` field reads NOT YET BUILT, deliberately. Fill it with the address of the first page that carries this component.

## The one value that is a ruling rather than a specification

DSRD 9 section 20.7 describes one row and stops. It says nothing about what happens when that row runs out of width, and below roughly 600px the title and the View all control compete for the same line.

**Kain's ruling, S282:** at `max-width: 599.98px` the header becomes a column, items align to the start, the gap is 12px, and View all drops beneath the title group with a 48px left indent so it lines up under the title rather than under the icon.

Every other value in the component is read straight from section 20.7. Nothing was redrawn and nothing was invented.

## One call I took rather than putting to Kain, so you can see it was a decision

**The class prefix is `section-header`.** The render he approved used `sec-head`; I renamed it immediately after approval so it agrees with the two icon classes `base.css` already carries. A naming change only, no value moved. It is named in the data file and in DSRD 8 section 23 rather than being quietly correct.

Note that this is a **new class family**, so the registry's birth gate applies. Its row is already written, so the gate should pass rather than fail you.

## What is being asked of you, and what is not

**Asked:** build the component into the theme to the data file, when the first page needing it is specified and signed. It is not urgent on its own. It has no page yet.

**Not asked:** do not build a page for it, and do not decide where it goes. The Knowledge Hub category hub page is not specified and signed yet. This brief commissions a component and nothing above it.

## Two things travelling with this, which are not this brief's job

Both came out of today's drift check on the review card, and both are yours because they are in the theme.

1. **`reviews.css` carries a stale comment.** The block for `.rv-card__translate-btn` says "NOT RULED BY KAIN YET" and calls its values Code's proposal. He ruled that control at S059 and the data file records it as ruled. The comment is the only thing still saying otherwise. Correct the comment; no value changes.

2. **The review card's approved prototype is not in its folder.** `achology-review-card-proof-v3.html` sits loose in the Card System folder while `review-card/` holds only the data file. Standing rule 19 makes the prototype in the component's folder the signed record. Moving it is a filing job, not a build one; I have not moved it because the card work is live on your side and I would rather not move a file under you mid-run. Say if you would rather I did it.

*No em or en dashes in this file; checked before writing.*
