> **CHAT DISPOSITION, S342: READ, NOTHING OWED.** The S096 ruling's fold-back is complete: the prototype and the two sheet values exist in the Article Page design folder, the signed record for standing rule 19. Nothing for Chat to write back; the S337 reply's OWED BACK is met. Board cards: Knowledge Hub page designs and the eighteen instructor articles, stamped in the S342 walk.

# REPORT: the article page fold-back is done, the prototype exists and the sheet carries the two values

**From:** Claude Code, Session 102. **Date:** 5 September 2026.
**Closes:** section 2 of `RULING__The_Article_Page_Is_Approved_At_Three_Widths_And_Publishing_Waits_On_Its_Record_S096.md` and item 3 of `REPLY__Who_Runs_The_Article_Pages_Human_Chapters_And_The_Fold_Back_Is_Yours_S337.md`, which held the fold-back as owed. Harness Rule 14.
**Board cards:** the eighteen instructor articles; Knowledge Hub page designs.

## What now exists

**`PROTOTYPE__Article_Page_Hero_And_Reading_Column_S096.html`**, in the Article Page design folder beside the two single-block prototypes. It is the approved block as the server rendered it: the breadcrumb, the title block, the banner slot with the contents and share card beside it, the meta line, and the opening of the writing (the hook paragraph, the first heading and its first paragraph), cut from the live page `/learn/helping-people/articles/why-do-people-seek-counselling/` with the theme's twelve stylesheets inlined exactly as served. Its header quotes Kain's words and the ruling file, says what he ruled and what he did not, and names how it was made. 195KB, no en or em dash in it.

**The build sheet, `BUILD_SHEET__The_Article_Page.md`,** gains the two values the ruling owed it, in block 3 and nowhere else: the meta line's 32px before an unheaded opening paragraph (matched to a body H2's top margin, v0.136.0), and the 1104px banner and breadcrumb's release to the column width below 1152px at `max-width: 1151.98px` (v0.137.0), with the derivation the stylesheet records. A dated line under "Last amended" names the addition and points at the prototype. Nothing else on the sheet moved.

## How it was made, so the next fold-back is the same shape

A new tool, `tools/fold_back.py` in the theme, does the export mechanically, because Rule 14 makes this a standing duty and the S096 ruling's reason for not doing it by hand was right: a design folder should not acquire a file whose shape nobody agreed. It opens the live page in Chromium at 1200, lets the page's own JavaScript run so the contents list it builds is in the copy, clones the page's main element and keeps only the named blocks with their wrappers, cuts the reading column to its first five children, inlines every theme stylesheet as served with the comments stripped (they carry the dashes the record forbids and are not what renders) and relative references made absolute, and writes the header in the shape the S282 prototype set. Then it reopens its own output at 1200, 768 and 390 and prints what it measures. It judges nothing.

Its printout for this file:

```
  195086 bytes  PROTOTYPE__Article_Page_Hero_And_Reading_Column_S096.html
  kept 3 block(s) from 3 selector(s); 12 stylesheet(s) inlined
  desktop 1200 wide: document 1200px (fits), H1 in Como, meta line to first writing 32px, 1 of 1 pictures loaded
  tablet   768 wide: document  768px (fits), H1 in Como, meta line to first writing 32px, 1 of 1 pictures loaded
  phone    390 wide: document  390px (fits), H1 in Como, meta line to first writing 32px, 1 of 1 pictures loaded
  0 en or em dashes; the file can stand as a prototype
```

The 32px is the meta line's gap the ruling names, measured on the prototype itself at all three widths; the fit at 768 and 390 is the release working. The first cut kept the whole page below the opening, because a detached clone answers false to the browser's "is connected" question for every element in it; caught by reading the output rather than trusting the printout, fixed, and the check that would have caught it (one picture per width, not five) is in the printout above.

## Two honest limits

The pictures and typefaces in the prototype point at the build site by address, as the S079 artefacts do, so they load while the build site is reachable and not otherwise; the S282 prototype's approach of inlined tokens and a local font file was hand-built, and this one is generated, so it takes the generated shape. And the banner shows the placeholder picture the live page carries today, because no composite banner exists yet (signed spec section 8); when one does, the prototype is re-cut, not edited.

OWED BACK: nothing. The S337 reply's OWED BACK is now met in full, both halves.

*No em or en dashes in this file; checked before writing.*
