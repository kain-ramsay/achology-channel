# REPORT: the prototypes are re-cut against Mulish, and the count was not 23

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Closes:** `RULING__All_23_Signed_Prototypes_Are_Re_Cut_Against_Mulish_S311.md` and its OWED BACK line.
**Tool:** `tools/recut_prototypes_mulish.py` in the theme, with a `--dry` mode. The run is repeatable and its printout is the record.

---

## What was changed, and the line I did not cross

Your ruling's own sentence governed every decision here: **"Change nothing but what the face change carries."**

So the re-cut touches **live declarations only**: the Google Fonts family clause, `--font-body`, a `--font-heading` fallback where it named the old face, and a hardcoded `font-family` rule. Both values were read out of the shipped theme rather than typed:

- `base.css` line 53: `--font-body: 'Mulish', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif`
- `functions.php` line 381: `family=Mulish:ital,wght@0,300..900;1,300..900`

**28 files re-cut. One named and left. Three needed nothing.**

Read back afterwards: 17 of the 18 body tokens in the folder now read Mulish, and one live Google Fonts request still names the old face. Both belong to the same skipped file.

## The count, because it is not 23

| | |
|---|---|
| Prototype HTML files outside the Archive | 20 |
| Already carrying Mulish, captured after it shipped | 3 (breadcrumb, site footer, where next panel) |
| Superseded and deliberately left | 1 (course card v1) |
| **Prototypes re-cut** | **16** |
| Build sheets and data files re-cut | 12 |
| **Total files changed** | **28** |

**The ruling says 23 approved prototypes and the folder holds 20 live prototype files**, three of which were already right. Two of the 20 are menu fragments rather than components in their own right, `achology-header-menu.html` and `achology-footer-menu.html`, and they carry live declarations so they were re-cut. I have not tried to reconcile 20 with 23: **that is a count in a ruling against a count on disk, and correcting a ruling is not mine.** What I can say is that no live prototype outside the Archive still names the old face, except the one below.

## The one I stopped on, which is what the ruling asked for

**`Card System/course-card/achology-course-card-proof-v1.html`.** Superseded by v2 in the same folder rather than sitting in an Archive. Re-cutting a replaced record puts work into something nobody should read, and moving it is a filing decision rather than a face change. **Named rather than guessed**, per your own line: better nineteen clean and one named than twenty quietly guessed.

**It is worth moving to the Card System Archive**, on the same grounds S282 gave for the review card's own prototype. That is a filing job and it is yours or Kain's to say.

## Two findings that came out of doing it

**1. The comments still name the old face, on purpose, and I want you to see the reasoning before you read it as unfinished work.**

Dozens of comments across these files name Source Sans 3, and they are of two kinds.

Some quote a DSRD sentence word for word, for example DSRD 8 section 8.5's `"Hour pill: Source Sans 3 10.5px/600, school text-safe..."`. **Rewriting a quotation would make the prototype claim a document says something it does not yet say.** You owe roughly ninety rows across DSRD 7, 8 and 9 by your own S311 line; until those land, the quotation is accurate and the face is not, and a corrected quote would be a false one.

The others label the declaration beside them. Those are genuinely stale, and they are the same class as the 33 theme comments your S311 ruling routed to "the next change set that opens each file". They are counted per file in the tool's printout, so the state is visible: 17 remain in the site header, 10 in the review card, 7 in the course card, 4 in the filter bar, 1 each in two build sheets, none anywhere else.

**My recommendation: leave them until your DSRD rewrite lands, then sweep them in one pass against the corrected sections.** Doing it now would mean writing the new sentence twice, once here from my reading and once there from yours, and those two would differ.

**2. The review card proof loads no web font at all.** It carries only the `COMO_FONT_INJECT` marker and no Google Fonts link, so its body text has always rendered in a system fallback rather than in Source Sans 3. Its token now reads Mulish, which is the honest record of what the theme uses; what the file displays is unchanged, because it displayed a fallback before. **I did not add a font link**, because that would change what a signed record renders, which is the one thing the ruling forbids. Named here so it is on the record rather than found later.

## The four Literata waivers on the book note card's sheet

Closed. `BUILD_SHEET__book-note-card.md` now carries no occurrence of Literata or Source Sans 3 at all, read back after the run. They went to Mulish, not to Literata and not to Source Sans 3, exactly as the ruling directed.

## Verification

Opened the re-cut article card proof in a browser and measured it rather than assuming: the `--font-body` token resolves to the shipped stack, `document.fonts.check('16px Mulish')` returns true so the face actually loads, and all 18 cards still render. Nothing Kain approved has moved: one token changed and one request changed, and the layout is untouched.

OWED BACK: two small things, both yours. Whether `achology-course-card-proof-v1.html` moves to the Card System Archive. And whether the stale comments wait for your DSRD rewrite, which is what I would do.

*No em or en dashes in this file; checked before writing.*
