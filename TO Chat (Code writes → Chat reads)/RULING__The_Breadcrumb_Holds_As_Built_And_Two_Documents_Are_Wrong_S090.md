# RULING: the breadcrumb holds as built, and two documents describe something else

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Authority:** Kain, in session, in Safari, on three whole rendered pages.
**Closes:** sitting 2 of the four chrome sittings, `COMMISSION__The_Four_Chrome_Components_Are_Safari_Sittings_S282` and `BRIEF__The_Four_Chrome_Sittings_Are_Unparked_S302`.
**Filed under:** Harness Rule 14. A ruling live in the build and absent from its owning document is the drift this project's harnesses exist to prevent.

---

## What he was shown

Three whole pages in Safari, live, at desktop: the Privacy Policy, the About page and the Policies index. Not a component on a blank page, and no reconstruction.

## What he was asked, and what he said

He was asked one question: **does the trail hold as it is?**

**His words: "yes, it holds, please correct the document."**

## The second question this sitting existed for was already answered

The commission asks, for the breadcrumb only: **are `breadcrumb` and `policy-breadcrumb` one thing written twice?**

**They are not two breadcrumbs, and there was nothing left to rule on.** Settled at S080 by measuring every computed visual property across four page families. What exists is one component, one wrapper and one colour variant: `.breadcrumb` the trail itself, `.breadcrumb-bar` the nav around it, and `.breadcrumb--on-dark` for the book note's dark hero. The wrapper was called `policy-breadcrumb` while serving seven page families, which is the name that sent both of us hunting a duplicate that does not exist. Renamed at S080, theme v0.84.0.

**Verified again this session rather than recalled:** `policy-breadcrumb` appears nowhere in the theme, in any stylesheet or template; `breadcrumb-bar` appears in 13 templates.

**One line to correct on your side.** `000__THE_FOUR_CHROME_COMPONENTS.md` still describes the breadcrumb as "two families", `.breadcrumb` and `.policy-breadcrumb`. That was true when it was written and has not been true since S080.

---

## The correction he ordered, and it is yours to make

**Two documents say the breadcrumb sits at the 1200px page frame. The build does not, anywhere, and he has ruled that the build is right.**

- **DSRD 8 section 25**
- **DSRD 9 section 27**

**What the build actually does, measured this session on the live pages:**

| Page | The trail | The writing beneath it |
|---|---|---|
| Privacy Policy, at 1280 | left 330, width 620 | left 330, width 620 |
| Policies index, at 1440 | left 280, width 880 | left 280, width 880 |
| About, at 1440 | left 280, width 880 | left 280 |
| Reviews, at 1440 | left 280, width 880 | left 280 |

**The rule, in one sentence, for whichever document owns it: the breadcrumb aligns with its own page's content column, never with the 1200px page frame.** That is what makes each page read as one column, and it is what he approved by eye.

---

## What was filed on this side, per the commission

The commission requires the approved state exported as the component's prototype, a data file with a gate block, the folder README, this ruling, and this note to you. They are in the Breadcrumb folder inside the Component Design Prototypes folder.

**One thing that folder's README said was true until today and now is not.** It said the folder would stay empty because Kain had approved no component there. He has now approved one, on a rendered page, so it takes its prototype and its data file exactly as the commission requires.

## What is still open on this component, and it is not his

DSRD 8 section 25 was created for the breadcrumb by Chat at S303, so the component now has a home for its decision record. This ruling's decision section belongs there.

OWED BACK: the correction above written into DSRD 8 section 25 and DSRD 9 section 27; this ruling's decision section added to DSRD 8 section 25; and the stale "two families" line corrected in `000__THE_FOUR_CHROME_COMPONENTS.md`.

*No em or en dashes in this file; checked before writing.*
