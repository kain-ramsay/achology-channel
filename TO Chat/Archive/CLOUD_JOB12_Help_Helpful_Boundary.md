# Job 12: the help answer boundary `help-single__body | help-helpful` (read only, facts only)

Read at `kain-ramsay/achology-theme` `origin/main` `2bc5aeb` and `kain-ramsay/achology-record` `main` `1e91422`. Nothing was changed and nothing is recommended. Both local clones were shallow; I unshallowed them (history only, no file touched) to answer (d). `page_gate.py` lives in the theme repo, not the record repo.

## Summary

- The line comes from a no-hairline boundary the gate counts as a block boundary: the answer body and the "Was This Article Helpful?" strip are two sibling blocks, nothing sits between them, and the 32px is the strip's own top margin.
- DSRD 7 §4.3 says every block boundary carries a hairline. Neither DSRD 7 nor DSRD 8 names this boundary. DSRD 8 §29 names the *other* edge of the strip (strip to closing card) and says its hairline was removed.
- There is no recorded carve-out for this boundary in `page_gate.py` or in the DSRD 6 record. The gate carves out five other cases by name; none matches.
- The CSS that sets the gap has been as it is since 2026-07-16 and the hairline above the strip was removed that day, before the gate existed (2026-07-28). Whether the gate ever scored this boundary as a pass: cannot tell.

## (a) What the markup puts between the body and the strip, and where the 32px comes from

**Markup** (`single-faq_article.php`): the body is `<div class="help-single__body">` at line 464, filled by `echo $ach_body_html;` (line 493) and closed at line 495. The next thing is an HTML comment (line 497, `<!-- Micro-feedback ... -->`) and then `<section class="help-helpful" ...>` at line 498, which closes at 507. No element, rule, border or spacer sits between them. Both are direct children of `.article-container`, whose children, in order, are: `breadcrumb-bar`, `help-single__header`, `ach-listen-bar ach-listen-bar--joined`, `help-single__body`, `help-helpful`, `help-close` (measured on a stand-in render of the real template, below). That order is why the gate numbers this "boundary 4": breadcrumb|header is 1, header|bar 2, bar|body 3, body|strip 4, strip|closing card 5. Credits and the trial panel follow after the closing card.

**The 32px** is the strip's own top margin: `help.css:768`, `margin: var(--sp-xl) 0 0;` inside `.help-helpful` (rule at 763). `--sp-xl` is 32px (`base.css:220`). The rule's `padding` is 0 (since S110) and it has no border on any side. The body above has no border, padding or margin-bottom of its own. Its last paragraph carries `margin-bottom: var(--sp-md)`, 16px (`help.css:690-694`); the two margins collapse, so the gap is the larger, 32. Measured on the stand-in render: gap 32 at 1280 and at 390 wide; strip margin-top 32px; strip border top and bottom 0; last child of the body `P` with margin-bottom 16px.

**What the gate does with it** (`page_gate.py`): a block is a direct child of the content container; `gap` is `rb.top - ra.bottom`; a line is looked for on the facing edges only (the bottom border of the block above or the top border of the block below, lines 708-714). For a pair with no line, no breadcrumb/bar/signature case, and no boxed card on either side, the code at `page_gate.py:1335-1337` fails it: `"%s: no hairline, gap %.1fpx"`, cited as DSRD 7 §4.3 ruling 1. The measured gap is only reported; with no line it is not compared with 48.

The three page_gate commits of 4 October (`4ca046c`, `7bbb66c`, `2bc5aeb`) change how a boundary that already has a line is measured; on reading the diffs, none of them is reached for a boundary with no line, so they do not bear on this one.

## (b) What DSRD 7 and DSRD 8 say

- **DSRD 7 §4.3 (line 429 on): says there should be one.** "Every boundary between two blocks within a page carries a visible hairline, with 48px above the line and 48px below it", 32 on phones; ruling 1: "There is no block boundary anywhere on the site without one." One-owner rule (line 443): the element carrying the line owns the space; neighbours supply zero. "Applies to" (line 455): the separators between page-level blocks, not rules inside a DSRD 8 component.
- **DSRD 7 §4.3 named exceptions** (lines 461 to 479): the category hub's section boundaries (Exception 3, no line), the quote page's listen bar (Exception 4, retired), the About story block (Exception 1, 48/32), the About header's text-column line (Exception 2). None is this boundary. Exception 3 says a second page wanting the same relief "needs its own ruling on its own render".
- **DSRD 8:** there is no section for the helpful strip. The one mention is in §29, the closing card (line 2418): "The strip above the card lost its hairline, because the card's own border is the boundary (DSRD 7 §4.3, one owner)." That concerns the edge between the strip and the closing card (boundary 5). It says nothing about the edge between the body and the strip, so for boundary 4 DSRD 8 says nothing.
- **Other documents that name the strip:** DSRD 7 §5.1 (line 568) registers the strip's controls as an exception to the button system and says nothing on spacing or lines; DSRD 2 §2.24 item 7 (line 818) gives the label, the type sizes and the GA4 event, and lists the strip as its own item between the Related Questions block (6) and the CTA block (8), separate from the article body (item 4); DSRD 3 §12.3 and DSRD 10 describe the event. None mentions a hairline or a gap above the strip. DSRD 9 line 666 (the one block standard, rule 2) repeats "one gap, owned once ... every hairline 48 above and 48 below" for the help answer among other types.
- **DSRD 6 §10** (line 331): "Two standing exceptions for the spacing rows" (a full-bleed band flush against the header; a block that draws its own border as its boundary), and "Any third case is a new decision, not a third entry by analogy."

## (c) Is there a recorded carve-out?

- **`page_gate.py`:** the hairline check has named carve-out rows for: the breadcrumb junction (line 1284, Kain S230), the reading bar's junction (1300, DSRD 8 §26), the author signature `kh-foot__signature` (1312, "the author signature closes the writing above it ... not a block boundary"), a card that draws its own border (1322, Kain S110, DSRD 8 §29), and the About header's uneven columns (1341). A search of the file for `help-helpful` finds nothing. The strip is not matched by any of them: it is not the breadcrumb, is not `ach-listen-bar`, is not `kh-foot__signature`, and neither side of boundary 4 draws a border on all four sides (the strip has none; the body has none), so the "boxed" test returns nothing. The boxed case does apply to boundary 5 (strip to `help-close`), because the closing card has a border.
- **Component registry:** the gate reads component membership from `COMPONENT_REGISTRY.md` in a `Component Design Prototypes` folder under `Achology Website Pages`. That folder is not in the record repository, so whether `help-helpful` is registered: cannot tell. The registry feeds the spacing-ownership check (check 4), not `hairline-present`.
- **DSRD 6 record** (`DSRD 6 Records (pages with no design folder yet)/Single Faq Article/DSRD6_RECORD.md`): chapter 10 reads `fail, 2026-08-13, ... desktop boundary 2 (help-single__header | help-divider): no hairline, gap 28.0px`; its machine half (run 2026-08-24, page_gate v8) says `13 of 29 checks failed` with that same message. It lists no carve-out row for the strip. The 299 help answer records (all run 2026-10-01, v9) carry the line in question: 157 say `6 of 29 checks failed`, 141 say `9 of 35`, one `12 of 38`. Their "§12 exemptions applied" sections read `none`. So there is no recorded carve-out, and the existing ones above do not apply because none of their conditions is met by body | strip.

## (d) Was it passing before, and which commit last touched what sets it

**Facts from the theme history** (`git log` on the rule and the markup):

| Date | Commit | What it did at this boundary |
|---|---|---|
| 2026-07-02 | `dd58f80` | Strip first built with `border-top` (a hairline between body and strip), margin 24 above. |
| 2026-07-16 | `9434f1a` | Margin above the strip 24 to 32 ("hairline air 32/32"). |
| 2026-07-16 | `0b278bd` | Strip becomes a left-aligned row; **the hairline moves from above the strip to below it**, margin above 48 ("48px gives the body's last paragraph its air"). From here the body | strip edge has no line. |
| 2026-07-16 | `5f80c2e` | Margin above 48 to **32**, the current value. The CSS comment records it as Kain's call: "paragraph, 32, strip, then 48 each side of the hairline". |
| 2026-07-28 | `1799ee0` | `page_gate.py` first added. |
| 2026-08-05 | `7ba4ebc` | Strip's label and markup reworded; margin unchanged. |
| 2026-09-10 | `46314f9` | "The help answer closes in one card" (S110): the hairline **under** the strip removed and its padding set to 0 (the CSS comment at `help.css:770-783`, the foot ruling in `single-faq_article.php`); the strip's top margin untouched. |

**The last commit to touch the margin or markup at this boundary:** `5f80c2e` (2026-07-16) for the 32px margin (`help.css:768`); `7ba4ebc` (2026-08-05) for the strip's markup in `single-faq_article.php:497-507`; `46314f9` (2026-09-10) for the strip's border and padding. The body's own paragraph margin (`help.css:690-694`) was last touched by `e1ac525` (2026-09-11, "S111 sweep, family one: the reading pages take Kain's nine rulings"). None of these changes the 32.

**Passing before?** The hairline above the strip existed from 2026-07-02 to 2026-07-16; the gate did not exist until 2026-07-28, so it never measured a line there. From the gate's first day the edge had no line and a 32 gap, and the check code at that boundary reads the same way. I could not find a recorded gate result that names boundary 4 before 2026-10-01: the earliest run in the record history for this template is 2026-08-13 and 2026-08-24, which name boundary 2 as the first failing message and count 13 failed checks without listing them, so whether boundary 4 was among them: **cannot tell**. The first appearance of the boundary 4 message in the record history is the commit of 2026-10-01 18:32 (`155a009`). Between August and October the template changed (the divider row `help-divider` that boundary 2 named is no longer in the markup; the reading bar `ach-listen-bar` stands there), which is why boundary 4 is now the first failing line and boundary 2 no longer is.

## (e) Possible resolutions, with the one-line consequence of each

1. **Add a hairline between the body and the strip in the theme** (48 above and 48 below, 32 on phones, the owner declaring the space and the neighbours zero). Consequence: the page changes on all 299 answers (a line returns above the strip, which was ruled out of the foot at S110 and the strip's spacing was set at 32 by Kain on 2026-07-16). **Touches a design Kain approved.**
2. **Make the strip part of the answer block in the markup** (for example inside the body wrapper), so it is not a separate block. Consequence: no boundary 4 to measure; if the CSS is kept equal the look need not change, but the DOM shape, the help-article.js selector (`.help-helpful`) and the one-job-one-block reading of DSRD 9 would need checking. Whether it changes the look: cannot tell without a render. Touches the approved look only if the render moves.
3. **Record a named carve-out in `page_gate.py` and on the DSRD 6 record** (a row like the author signature's: the strip closes the writing above it). Consequence: 299 failing lines become one named CARVE-OUT row each; no page changes. DSRD 6 §10 says a third case is a new decision, so it needs a ruling. **Touches no approved design.**
4. **Change the standard**: add a recorded exception to DSRD 7 §4.3 for this boundary (as Exception 3 was done for the category hub), or amend its "Applies to" sentence so a sign-off strip is not a block. Consequence: the gate follows by item 3; no page changes; it amends a standard Kain ruled in five decisions at S224, so it needs his yes. **Touches an approved standard, not an approved page design.**
5. **Change the gate's definition of a block** so the strip does not count (a generic rule rather than a named case). Consequence: affects every page type that shares the structure, not only help answers; the S145 comparison of seven pages the factory has been running shows what a gate change can move. Touches no approved page design.
6. **Remove or relocate the strip.** Consequence: drops a specified feature (DSRD 2 §2.24 item 7, DSRD 3 §12.3, the `faq_helpful` GA4 event and Kain's S245 strip ruling). **Touches approved design and specification.**
7. **Leave it.** Consequence: chapter 10 stays failing on all 299 records and none of them reads ready (DSRD 6 §0), though the record's own rule is that a machine fail is evidence to reproduce, not a verdict.

Of these, items 1, 2 (if the render moves) and 6 touch a design Kain has already approved; item 4 touches a standard he ruled; items 3, 5 and 7 touch neither.

## Notes and limits

- **Stand-in measurement, not the live gate.** WordPress cannot run here. The 32, the sibling order and the margins in (a) were measured on a render of the real `single-faq_article.php` with stand-in WordPress functions and the theme's own CSS at 1280 and 390 wide. The live gate's numbers (all 299: desktop gap 32.0px) agree. Tablet and phone results for boundary 4 are not in the records (they quote the desktop message only): cannot tell.
- **A second observation, outside the question, from the same stand-in:** the gap from the strip to the closing card measured 48 at 390 wide as well as at 1280, where DSRD 7 §4.3 wants 32 on phones; whether the live gate flags it: cannot tell, the records quote one message per chapter.
- **One message per chapter.** Each record quotes only the first failing check for chapter 10, so I cannot say what the other 5 or 8 failing checks per record are.
- The commit dates above are the author dates in the repository; commit text was read, not the sessions behind it.
