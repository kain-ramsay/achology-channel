# REPORT: everywhere in the project the body face is named, and what must change when it is chosen

**From:** Claude Code, Session 84. **Date:** 25 August 2026.
**Asked for by Kain in the sitting**, after he said the thing that was true: one candidate shown beside the current face is not a choice. He asked to see a spread first, and to know what carrying the decision actually costs before he takes it.

**Measured tonight by searching the whole project, not estimated.** 105 files name the body face. They are not one job; they are five jobs of very different size, and the point of this report is that the difference is enormous.

---

## The headline: the site changes in two places

**`base.css`, one line: the `--font-body` token. `functions.php`, one line: the Google Fonts request.**

That is the entire live change. Every other rule in all fourteen stylesheets reaches the face through `var(--font-body)`, so the token is the one place the name exists in anything that renders. Verified by reading every `font-family` declaration in the theme: the only other literal faces declared anywhere are Como's four `@font-face` blocks and one `--said-font` on the handwriting callout.

**So the choice is cheap to make and cheap to change again.** That matters for how this is decided: nothing here locks him in.

## Job 1: the theme. Two lines that render, twelve files that describe

| | Count | What it is |
|---|---|---|
| **Must change** | **2 lines** | the `--font-body` token, and the Google Fonts request |
| Should change | 33 mentions across 12 files | comments and docblocks that name the old face while describing a rule |

The comments are `base.css` (4), `cards.css` (9), `reviews.css` (7), `book-note.css` (3), `about.css` (2), `functions.php` (2), and one each in `components.css`, `header.css`, `footer.css`, `fonts.css`, `commerce-cards.php`, `index.php`.

**None of them renders anything.** They are a documentation debt rather than a defect, and left alone they are the kind of stale-comment drift this project keeps finding. Mine to sweep, in one pass, once the face is settled.

## Job 2: the component records. Four assertions go red, and they already have

**Fourteen component records name the face**, eleven build sheets and three data files. But only **four** of their statements are actually enforced by `component_gate.py`, all four in `BUILD_SHEET__book-note-card.md`, and all four went red the moment Literata shipped tonight.

They are waived in writing rather than left silent, and the waiver says the thing that makes this case unusual: **this is the one class of waiver where the code is right and the record is behind**, so the record is corrected, never the theme.

Every other mention in those fourteen records sits in a row the gate does not yet check. **That is not comfort. It is the same finding as tonight's other one:** the records describe far more than anything enforces.

## Job 3: the specifications. This is Chat's, and it is the biggest reading job

| Document | Mentions | What has to happen |
|---|---|---|
| **DSRD 7** | **7** | §3's pairing sentence; §3.2, whose heading is literally "Source Sans 3 Styles"; **§4's 620px reading column, which was derived FROM the old face**; and four rows in §12 and §14 |
| **DSRD 8** | **60** | component values, most naming the face inside a type spec |
| **DSRD 9** | **22** | page layout rows, same shape |
| DSRD 3 | 2 | the performance section's font-loading entry |
| DSRD 6 | 1 | the visual-value line |

**§4 is the one that will be missed.** It reads, quoted from the canonical file tonight:

> "A page of continuous prose sets its column so a line runs 45 to 75 characters. 620px is the value that delivers it at 16px in Source Sans 3, measuring 72 to 77 characters across the ten pages it now governs."

**The width was reverse-engineered from the face.** Change the face and 620px still exists but no longer delivers what the sentence says it delivers. Measured on tonight's four pages, every candidate serif shortens the line by roughly a tenth against the control. **That number has to be re-derived against whichever face wins, and it is a design ruling rather than a measurement Code should take alone.**

## Job 4: the signed prototypes, and this is the one nobody has thought about

**Twenty-three approved prototypes inside the Component Design Prototypes folder embed the old face in their own markup.** A further 22 sit elsewhere as page prototypes and superseded explorations.

Under the S257 and S273 precedence, **the prototype is the signed record**: prototype wins, the data file matches the prototype, the theme matches the data file. So a face change puts the top of that chain out of step with the bottom of it, on 23 components at once.

**I am not proposing that all 23 are re-exported, and I am deliberately not deciding it.** Two honest readings exist and they lead to different work:

1. **A prototype records what Kain approved on the day**, and a later foundation ruling does not retroactively unapprove it. Then nothing is re-exported and each prototype is re-cut the next time its component is touched.
2. **A prototype is the live standard the gate ranks above the code.** Then leaving 23 of them showing a face the site no longer uses is 23 records that disagree with the build by construction.

**My reading is (1), because re-exporting 23 prototypes tonight would replace records Kain signed with records nobody has looked at**, which is a worse failure than a stale typeface in a reference file. But it is Chat's call with Kain, and it should be a stated ruling rather than a thing that just quietly happens or quietly does not.

## Job 5: history, and it needs nothing

Eight intersession handover files and two skill files name the face in passing. They are a record of what was true when written. **No action, named so nobody sweeps them and calls it progress.**

## The order this should run in

1. **Kain picks the face**, from the seven-way sitting now built.
2. **Two lines change and it ships.** Same night, same as tonight.
3. **Chat rules the reading column** against the new face, because it is the only consequence that changes how a page looks rather than how it is described.
4. **Chat rewrites DSRD 7 §3, §3.2 and the four rows**, then DSRD 8 and 9 at whatever pace suits.
5. **Code sweeps the 33 theme comments** in one pass.
6. **Kain and Chat rule the prototype question above**, once, so it is not re-derived per component.

**Nothing after step 2 blocks anything.** The site is correct from step 2 onward; steps 3 to 6 are the record catching up with it.

## One thing I owe him, said plainly

I showed him one candidate tonight and he took it, and a single candidate is a recommendation wearing a comparison's clothes. The seven-way sitting is built now and Literata is one tab among seven, sitting in the middle of the spread rather than at the front of it. **If he lands somewhere else, the change is the same two lines and it costs nothing.**

OWED BACK: nothing. Two rulings named for Chat and Kain: the reading column width, and whether the 23 prototypes are re-exported.

*No em or en dashes in this file; checked before writing.*
