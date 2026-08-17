# NOTE: what governs a component that has no build sheet yet (read with the S257 rulings)

**From:** Claude Chat, Session 257. **Date:** 2026-08-10.
**Why this exists:** Harness Rule 4 gained the component case today. Read literally, it would stop you on every component except one. This is the transition rule that stops that happening.

## The gap

Rule 4 now says a component's build instruction is its approved prototype plus its build sheet, in that component's design folder, with DSRD 8 holding decision history only.

**Exactly one component currently has both**: the book note card, whose prototype v2 and build sheet sit in the Card System folder inside Component Design Prototypes. Every other component named in DSRD 8 has neither. If the rule is read as written, you would either stop on all of them, or fill the gap with your own judgement, which Rule 5 forbids. Neither is what was ruled.

## The transition rule

**Where a component has no build sheet yet, its DSRD 8 section is the interim build instruction and you build from it exactly as before.** Nothing about DSRD 8 became void today. Its values are still the values, still read from the canonical file that turn, still quoted word for word under Rule 4's first paragraph. What changed is where those values will live once each component is carried across, and which artefact wins when two disagree.

So, per component, one of two states applies:

**Carried across** (book note card only, today): the approved prototype is the signed record, the build sheet is the instruction, DSRD 8 is history. Precedence is prototype, then sheet, then code.

**Not yet carried across** (everything else): DSRD 8 governs as it always has. Build from it. The S257 precedence does not apply, because there is no prototype or sheet for it to rank.

**Never guess which state a component is in.** The Card System folder's own README lists what exists there and what has a sheet, and it is the one place that changes when the folder's contents change. Read it rather than inferring from a filename. Components outside the card family have no design folder yet at all, which means they are in the second state by definition.

## How a component gets carried across, and who does it

Chat and Kain do it, not you, and it happens one component at a time as the card review reaches it. The sequence is: Kain approves the rendered component by eye, that exact file becomes the prototype in the component's design folder, Chat writes its build sheet beside it from the approved file, and DSRD 8's section for it is reduced to the ruling and its history with a pointer to the folder.

**What you should do if you find a component that looks carried across but is not.** A component whose DSRD 8 section has been reduced to history while no build sheet exists would leave you with no instruction at all. That is a genuine gap, and it stops the work: write it to TO Chat under Rule 5 rather than reconstructing values from the theme. Reading a value out of the code and treating it as the standard is the exact failure the S257 ruling exists to end, and it does not become acceptable because a document looks thin.

## One correction owed on a different matter

Your file `RULING__The_Reviews_Hero_Lead_Is_Kains_Wording_S052.md` asks Chat to note a figure question: the hero saying "tens of thousands of reviews" while the figures panel a screen below says 4,517 written reviews.

**That seam closed itself, in Kain's own third revision, which is the one live at v0.42.7.** The final wording says he has gathered "thousands of reviews", not tens of thousands, and thousands agrees with 4,517. Your analysis section was written against the second version and went stale within the same session. Nothing needs deciding and the distinction between ratings and written reviews does not need naming in the hero.

You were right to report it rather than edit his words, and right that the hero and the figures are one component making one claim at two scales. That observation is worth keeping for when the reviews component is carried across: the review count is a value its build sheet should hold once, so the two places that state it cannot drift apart. It is recorded in the plan.

Section 4 of `PLAN__Reviews_Page.md` now carries Kain's final wording, with the revision history and the reason for "thousands" written beside it, so the plan and the page agree again.

*No em or en dashes in this file; checked before writing.*
