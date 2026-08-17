# DELIVERY: the build-vs-sheet gate, all three acts

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.57.3.
**Answers:** `COMMISSION__Build_Vs_Sheet_Gate_S257.md`.
**Your prerequisite is met:** the S256 fixes were built and shipped earlier this session, so the gate measured a build carrying the S256 rulings.

## Act 1: the folder is under git

Its own repo, initialised at **Component Design Prototypes** rather than at Card System alone. You gave me the repo choice, and the wider scope is the better one: the Form Controls folder was created this session for the filter bar and has the identical need, so one repo per sibling folder would have given one system three histories. Card System, Form Controls and Header + Footer are all tracked.

**One thing worth naming.** The first commit captured seven zero-byte iCloud placeholders instead of files: all five superseded card prototypes in the Archive folder, and both header and footer prototypes, had been evicted from local disk. Git tracked the pointers. Pulled back and committed properly, so the archive is a real archive. Worth knowing because a repo full of placeholders looks exactly like a working one until you open a file.

## Act 2: section 2 is corrected and complete

Every UNKNOWN filled, every CODE row verified against the theme this turn, and the table replaced whole. Sixteen rows now: the template part and its three helper functions, the shared DNA and book note style blocks with their line ranges, all four content sources, the stylesheet, the full enqueue order, the grid class and the specimen page.

**Two naming differences, reported not reconciled, as you asked.**

1. The prototype's cover echo is `.card__cover-echo`. The theme's is **`.cover-echo`**, no block prefix.
2. Both call the blurb slot `.card__subtitle`, but since S256 ruled it takes the article excerpt styling exactly, the theme carries `.card__excerpt` and `.card__subtitle` as two rules identical in everything but name.

Neither is a defect and neither has been changed.

**One correction to your own sheet.** Its header named proof v2 as the signed record; the folder holds v3, approved at S259. Updated to v3.

## Act 3: the gate

`component_gate.py`, in the theme beside css_gate and page_gate. It imports page_gate's mirror, cache purge and SSH warm-up rather than copying them, so the two instruments cannot form two ideas of what the server is serving.

**Wired into H5, not H4, and this is a deliberate departure from "the way the dash ban is enforced".** The dash check is local and instant, so per-edit is right for it. This gate drives a real browser against the live site behind a cache purge and takes the better part of a minute. Wired per-edit it would make editing unbearable, and a gate that makes work unbearable is a gate that gets switched off. It now sits on the completion hook, where it blocks a change set from closing while the built component disagrees with its sheet, which is also where it means the most. It arms only when the change set edited a file the sheet's own section 2 names, so the trigger comes from the sheets rather than from a list inside the hook.

**Acceptance test, run on the real path.** Deployed a deliberate one-pixel drift to the live site, cover panel 200px to 201px, and ran the whole chain: H5 armed on the cards.css edit, ran the gate, and blocked the close with the printout naming the row. One row moved and no other. Reverted and re-verified clean. I ran this because a green check that cannot go red is worse than none, and the only way to know which one I had built was to break the thing on purpose.

## The first run, and its catch

**67 passed, 6 failed, 0 uncomparable, 4 rows unchecked.**

All six failures are one thing: **the three S259 rulings that are not built.** The soft grey author line, the title as the card's only focus stop, and the 145px watermark at -36.9px. Nothing else in the sheet disagrees with the theme, which is the result I would want from a first run: it found precisely the gap we already knew about and invented nothing.

Your S259 note says the build brief follows once the remaining ten cards are reviewed, so these are not mine to build. They are recorded in `component_gate_waivers.md`, one line each, keyed on the assertion copied verbatim from the sheet, naming what each waits on. A waiver excuses a known gap and cannot absorb a new one: change the sheet's value and the waiver stops matching and the failure comes back. All six print on every run with their reason.

**Delete those six lines when the S259 build brief lands.** A waiver that outlives its reason is drift wearing a permission slip.

## The table shape change, proposed rather than made silently

You asked me to propose this through the channel, so here it is, already built as a worked example on the book note sheet only. The other five sheets are untouched and the gate skips them.

**A fifth column, `Check`, holding the row's value as an assertion.** The Value column is unchanged and stays what a person reads. Grammar, assertions separated by ` ;; ` and fields by ` :: `:

    css SELECTOR :: PROPERTY :: EXPECTED        attr SELECTOR :: ATTRIBUTE :: EXPECTED  (* = present)
    text SELECTOR :: EXPECTED                   count SELECTOR :: N

**Why a column and not a parser.** Section 1's Value column is prose written for a person: "height 160px, radius 3px, shadow 4px 4px 16px rgba(0,0,0,0.3), centred, z-index 1". A parser guessing its way through that would be confident and wrong. So the design decision is stated once for a reader and once for a machine, in the same row, where a drift between the two is visible.

**Three consequences you should rule on with the shape.**

1. **A `**Specimen:**` line is needed in the sheet header**, giving the address where the component actually renders. Without it there is nothing to open. The book note's is `/cards/`.
2. **Two values are written in the browser's computed terms**, because a computed style has no other spelling: `0.08em` at 11px computes to `0.88px`, and `line-height: 1.35` at 17px computes to `22.95px`. The Value column keeps the authored form. This is the one place the two columns say the same thing in different units, and it is unavoidable.
3. **Selectors in the Check column are the theme's own.** That is deliberate: it makes section 1 state the real names alongside section 2, and it is why the `.cover-echo` naming difference above is now visible in two places rather than none.

## What the gate does not see, and why that number is printed

Four rows on this sheet carry no assertion, and the printout says so every run rather than passing them:

- **The hover state** needs a state the probe does not enter.
- **The two horizontal-variant rows** need a variant no template emits, which page-cards.php already records as having no live component.
- **The blurb's 120 to 135 character rule** is a content standard, not a rendered property; it belongs to the article gate.

Two further parts of otherwise-checked rows are also out of reach and are named in the sheet: the watermark's `top: 50%` and `translateY(-50%)` compute to px values that change with the card's height, so centring needs a geometric probe this gate does not have yet; and the cover panel's "no stray pseudo-element" cannot be reached by `querySelector`. Each is a real limit, written down rather than papered over with an assertion that would always pass.

## Whether the sheet worked, since you asked

**It did, and the thing that made it work is that section 1 is a table.** Every row is one decision with one value, so turning it into an assertion was transcription, not interpretation. The one place I had to think was where a single Value cell held five values at once, and even there the row boundary told me they belonged together.

**Two honest criticisms.**

1. **Section 1 mixes rendered properties with content rules and prose findings.** The author line row carries a colour, a text pattern, an approval note and the superseded value's contrast ratio, all in one cell. The colour is measurable; the rest is history and belongs in DSRD 8 by your own ruling 3. As the sheets multiply, that mixing is what will make them drift.
2. **"Kind" is not doing work.** Token, shared DNA, one-off and ruled are useful to a reader once, but nothing reads that column, and a value being shared DNA does not change how it is verified. If anything replaces it, the more useful column would be which components share the value, because that is what tells you the blast radius of changing it.

Neither is a reason to change anything now. The sheet met its four requirements and I would keep it.

## One question back

**Do you want the Check column rolled out to the other five card sheets and the filter bar sheet, and if so, by whom?** I can write them, but each assertion is a claim about what the prototype approved, and under ruling 4 the sheet must match the prototype, which is yours to read. The safest split is that you write the Check cells when you write the row, and I only report when the theme disagrees. Say which and I will follow it.

*No em or en dashes in this file; checked before writing.*
