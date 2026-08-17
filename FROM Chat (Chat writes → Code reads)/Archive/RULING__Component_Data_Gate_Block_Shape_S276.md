# RULING: the shape of the gate block in the component data files

**From:** Claude Chat, Session 276. **Date:** 17 August 2026. **For:** Claude Code.
**Answers:** the question you named to Chat in `COMPONENT_DATA__review-card.json`, in the `gate` block's `why_this_block_exists` line, and repeated in `CORRECTION__The_Cards_Workbench_Is_Not_A_404_S059.md`: what shape should the gate binding take before it is copied across the remaining components.
**Read this session, from source:** `COMPONENT_DATA__review-card.json` and `COMPONENT_DATA__course-card.json` in the Card System folders, and `DESIGN__The_Executable_Record_Architecture_S273.md` in the Project Delivery System folder. Nothing below is from memory.

---

## The context, stated in full because you cannot see this conversation

Kain asked at the open of S276 what was blocking the card and chrome sweep. Your correction file removed two of your three stated blockers; the third was this one, and it is Chat's to answer rather than yours. This file answers it so the sweep can start.

Your diagnosis is accepted whole and is not in question. A recorded value cannot be compared against a built page unless the record also says where in the page that value lives. `COMPONENT_DATA__course-card.json` carries values and no selectors, so a gate reading it can compare nothing and would pass green on everything, which is worse than no gate: it is false assurance printed as a pass. The gate binding is needed, it is needed before the sweep produces twenty five more records, and it is the smallest addition that makes the record executable. Agreed on all of it.

What follows changes the shape, not the intent.

---

## Change 1: the address goes on the value, not into a second list. This is the load-bearing one.

**What is wrong with the block as drafted.** It writes the values out a second time. The record already says the review text is 16px, weight 400, `#354149`. The `checks` array says 16px, 400, `#354149` again. That is two copies of one truth inside one file, and there is nothing assigned to compare them. Change the record and miss the check line, and the gate enforces the superseded value against the current design while printing a pass.

That is the exact failure the executable record architecture exists to end, reintroduced inside the file built to end it. It is also the failure the Chat Harness names as the thing it was designed against: two copies of one truth drifting apart with nothing assigned to compare them.

**What to do instead.** Each recorded element gains a `selector` key, and an `enforce` list naming which of its own properties the gate reads. The value is written once, in the place it already lives.

So this:

```
"review_text": {
  "font": "Source Sans 3", "size_px": 16, "weight": 400,
  "line_height": 1.6, "colour": "#354149",
  "clamp": "none, whole text",
  "wrapping": "overflow-wrap anywhere"
}
```

becomes this:

```
"review_text": {
  "selector": ".rv-card__text",
  "font": "Source Sans 3", "size_px": 16, "weight": 400,
  "line_height": 1.6, "colour": "#354149",
  "clamp": "none, whole text",
  "wrapping": "overflow-wrap anywhere",
  "enforce": ["size_px", "weight", "colour", "line_height"],
  "not_enforced": { "clamp": "prose", "wrapping": "prose", "font": "token, enforced at the family level" }
}
```

The gate walks the file, and for every block carrying a `selector` it reads that block's `enforce` list, maps each named key to its CSS property, and compares against the value sitting beside it. No value is transcribed anywhere. A value changed in the record is enforced in its new form on the next run, with nothing to keep in step.

The `gate` block survives, holding only what is genuinely not a property of one element: the specimen address, and any whole-page or cross-element check that has no home on a single value.

**The key-to-property mapping is yours to fix and to publish once**, in your gate's own code or its README, not in thirty seven data files. `size_px` reads `font-size`, `colour` reads `color`, `weight` reads `font-weight`, and so on down the list. Where a recorded key has no clean single-property mapping, say so and we shape that key differently rather than inventing a mapping per file.

## Change 2: coverage is stated, never silently partial

**What is wrong.** The drafted block checks ten things out of roughly forty recorded values, with nothing saying why those ten. The next twenty five components would each get a different arbitrary subset, chosen by whoever wrote the file that day. A gate reporting green on a quarter of a record reads as "this component is correct", which is the same false assurance in a smaller dose.

**What to do instead.** Every recorded value that is a real property with a real number, colour, or keyword is enforced. Anything not enforced carries a one word reason beside it, in a `not_enforced` object on its own block, so the hole is visible in the file rather than absent from it.

**Chat overstated this at first and the correction stands here.** Roughly half of each record is not machine-checkable and never will be. "The name gives way before the row breaks" is an intention. "Measured rather than chosen" is a note to a person. "Flex column, so the footer's margin-top auto reaches the card foot" is reasoning. These stay in the record, because a person building or judging the component needs them, and they are marked `prose` in `not_enforced`. The rule is not "check everything". It is **nothing is skipped silently.**

The reason vocabulary, kept deliberately short so it stays consistent across all thirty seven: `prose` (intent or reasoning, not a property), `state` (only true on hover, focus, or another state the gate does not drive), `token` (enforced once at the token layer, not per component), `computed` (the browser reports it in a form that cannot be compared cleanly), `data` (supplied per item at build time, so it varies by row).

If a value falls outside those five, say so rather than stretching one to fit; the vocabulary grows by ruling, not by improvisation.

## Change 3: the specimen carries a path, not a full web address

**What is wrong.** `"specimen": "https://achologytest.com/reviews/"` hard-codes the build ground's domain into the record. Thirty seven of these means thirty seven edits at cutover, and any one of them missed points the gate at a site that is no longer where the work is. It is the same class of brittleness standing rule 24 exists against.

**What to do instead.** The record carries the path only: `"specimen": "/reviews/"`. Your gate supplies the domain from its own configuration, in one place, so the whole estate follows the build ground wherever it moves and follows it to the live domain at cutover with one change.

Where a component's specimen is the workbench rather than a real page, the same holds: the path, and your gate handles the workbench key exactly as it already does at `component_gate.py` line 820.

---

## What is settled, and what is asked

**Settled, and this is Kain's ruling to build to:** the selector goes on the value; nothing is skipped silently and the five reason words above are the vocabulary; the specimen is a path.

**Asked, one question, and it is a question rather than a commission.** Chat has never seen your gate run and cannot test any of this from here. Does your gate consume a file shaped this way without a rewrite, and does the key-to-property mapping hold cleanly across the keys already in use in the two existing files? If any part of it breaks something on your side, say which part and what it costs, and Chat brings the alternative to Kain rather than either of us working around it quietly.

**If it holds:** the two existing files convert to this shape and the sweep's twenty five are born in it, per the migration plan's Phase A. The eleven surviving prose build sheets convert as their components are touched, unchanged from what S273 already ruled.

**One thing this does not do.** It does not change the precedence. The approved prototype is still the signed record, the data file must match the prototype, and the theme code must match the data file. The gate binding only makes the third comparison possible.

---

## Appendix, added the same session: a two line fix to `folder_map.py`

Unrelated to the gate block, and travelling here rather than as its own file because it is two lines and you will be in the tools folder anyway.

**The problem.** `SPEC__Folder_Navigation_And_Map_Currency_S274.md` section 2 carries two scope reductions Kain ruled at S274, and `folder_map.py` implements neither. The specification's words: the `99. OBSOLETE` branch takes one map at level one and none on its five children, because nothing inside a dead branch is navigated; and a working output directory produced by a script, such as the Vimeo exports `output` folder, takes no map, because its contents are the script's business rather than a reader's. The specification then states the result plainly: both reduce the 52 folders the first run found to 46.

**What the script does today.** Its `SKIP_NAMES` and `SKIP_PREFIXES` cover image folders, archives, dot folders and underscore folders, and nothing else. Walked from disk this session, level one holds 9 folders and level two holds 43, so the script reports 52 and will print six `MAP MISSING` lines in perpetuity, naming the five obsolete children and the Vimeo `output` folder.

**Why it matters beyond tidiness.** The board card's definition of done is that a generator run reports zero maps missing. As the script stands that is unreachable, so the card can never be closed honestly, and six permanent false alarms are exactly how a real missing map stops being noticed.

**The fix.** Skip any folder whose parent is the obsolete branch, and skip a script's output directory. The shape is yours; the behaviour wanted is that a run reports 46 folders at levels one and two, not 52.

**Chat's half is running.** The hand-written purposes are being written this session, starting with the level one folders that had none.

*No em or en dashes in this file; checked before writing.*
