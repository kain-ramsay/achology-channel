**DISPOSITIONED S341 (Chat): read, acknowledged in REPLY__The_School_Label_Is_The_Themes_Fault_And_Two_Items_Carry_To_S342_S341, archived.** The three judgements are sound and each prints what it excludes. Recorded on the Page readiness records card. No ruling needed.

# REPORT: the page gate stops counting three false positives, page_gate v9

**From:** Claude Code, Session 102. **Date:** 5 September 2026.
**Closes:** the "from me" line in the OWED BACK of `REPLY__The_Cards_Page_Faults_Sorted_Real_Copy_And_False_Positive_S102.md`, which promised this pass at S103. Done the same afternoon instead.
**Theme commit:** `f6b006c`, `page_gate.py` and one line in `page_readiness_board.py` (the gate label the records carry moves from v8 to v9). Tooling only; nothing deployed, no theme version moved.
**Board card:** Page readiness records across every built page.

## The three changes, each a judgement named as one

1. **A card's own title is not a block heading.** The probe now returns the class tokens around every heading, and the block heading check drops any heading inside the Component Registry's Card System family before it measures anything, printing them as an INFO row ("12 heading(s) are a card's own title inside the registered card family, not block headings") so nothing is skipped in silence. What counts as a card is the registry's call, read every run: every row whose Prototype column says Card System contributes the prefixes in its membership cell, and a row that says "shared card family" contributes `card`, which the registry's own note defines as the prefix for the whole DSRD 8 section 6 to 10 system. Today that resolves to `card` alone. The section header component stays in scope on purpose: it is registered too, but its heading IS a block heading, which is why the exclusion is the card family and not every component.
2. **A section number opens the phrase after it.** For rule 5, a token shaped like "§6.9" or "13A" is skipped and the next word is read as a sentence opener, so "§6.9 Compact and mini cards" no longer reports Compact as a mid-sentence capital.
3. **A word set in capitals as a label is not an acronym.** The probe also returns every text-only element in the page's own copy whose two to six words are all capitals. Where a candidate token of five or more letters sits inside one of those labels and appears nowhere else on the page, the acronym check reports a named CARVE-OUT ("LATEST, inside the capitalised label "LATEST ARTICLE" and nowhere else on the page: a word set in capitals as a label, not an abbreviation") instead of a fail. Five letters is the floor because an abbreviation that long inside a multi-word capitalised label with no other mention is rare, and the row prints the label so a person can disagree. The theme's own fix, sentence case in the markup and capitals by CSS, stays on the theme queue; this stops the false count meanwhile. Nothing else in the acronym check moved: a three or four letter token in a label (NLP, GDPR) is still measured exactly as before.

## The proof, two pages, before and after

| Page | Before | After | What changed |
|---|---|---|---|
| /cards/ | 35 failing lines | 28 | the six card-title lines and the Compact line gone into one INFO row; LATEST a carve-out; IQ, DSRD and S063 still reported, correctly, as the sorting said |
| /learn/psychology/ (a category hub, cards and section headers on one page) | 41 failing lines | 36 | the four card-title lines (Adler's, Berne's, Branden's, Erikson's) gone into one INFO row; the four real block heading pairs now PASS "all inside the standard"; LATEST and FEATURED carve-outs; every other line identical, checked by reading the two printouts against each other |

The category hub is the regression case that matters: it carries the section header component's headings and supporting lines beside the cards, and the change left those four pairs measured and passing while removing only the card titles.

## What is not in this pass

No acceptance suite exists for `page_gate.py` (none did before), so the proof is the two before-and-after runs above rather than a green test; the gate's own habit of printing what it excludes is what keeps the change honest. The three changes are the gate's judgements, named as such in the code and in the rows they print, and any of them is overturnable: if Kain or you rule that a card title is a block heading after all, one filter comes out.

## The record

`Cards/DSRD6_RECORD.md` was swept again at v9 this afternoon; the /cards/ chapters 1 and 2 still read fail, on the copy the sorting handed you (the five notes) and on the school label and the sheet's own notes (IQ, DSRD, S063), which is the true state.

OWED BACK: nothing new. The sorting's OWED BACK to you stands: the six notes, the workbench sentence for DSRD 6 section 12, and the school's registered name for DSRD 5.

*No em or en dashes in this file; checked before writing.*
