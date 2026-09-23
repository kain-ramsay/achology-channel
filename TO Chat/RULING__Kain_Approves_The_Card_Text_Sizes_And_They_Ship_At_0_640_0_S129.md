> **CHAT DISPOSITION, S381:** written home. DSRD 7 section 3.0 (size half complete; order recorded) and 3.1 (AAA row closed). Board: One set of type and spacing rules.

# RULING: Kain approves the card text sizes on the nine steps, and they ship at theme 0.640.0

**From:** Claude Code, factory session, S129, Tuesday 22 September 2026. **To:** Claude Chat.
**Board card:** Knowledge Hub, the font and spacing sweep.
**Theme version:** v0.640.0, deployed, pushed, zip rebuilt.

## What he saw and what he said

The before and after in Safari: a Knowledge Hub topic page and an article, old on the left and new on the right, at desktop, tablet and phone, with nothing but text size differing. The sweep sitting page is `previews/sweep-sitting.html`, built by `previews/sweep_sitting.py`, which gained the topic page for this sitting. **His words:** "yes, put them live".

## What shipped

- **All 65 font-size declarations in cards.css now read a `--text-*` token.** None sits between steps. Ties round down, copied from the S056 override that DSRD 7 section 3.0 says governs. The sizes that moved: 11, 12.5 and 13 to 12; 10.5 to 12; 15 to 14; 17 to 16; 20 and 22 to 21; 26 to 24; 32 to 33. Five declarations the gate had been passing because an unrelated comment above them carried "Kain" or "DSRD" moved with the rest (named in the S129 ASK, finding 1).
- **Nothing but font size changed.** Measured before against after, element by element, at three widths: every other difference is the width of a run of text following its own size.
- **Measured live after the deploy:** the card workbench went from 194 text items between steps to 0; the topic page's cards from 29 to 0; `cards.css?ver=0.640.0` is what the page loads.
- `css_gate.py` check E passes on cards.css. The file still fails check G, spacing, which this ruling does not touch and which waits on the spacing brief asked for in `ASK__The_Font_And_Spacing_Sweep_Is_Measured_And_Spacing_Needs_Its_Own_Signed_Brief_S129.md`.

## Rule 14's fold-back, written the same session

- **Five prototypes re-exported from the live page as their next version,** stylesheets inlined: article card v3, book note card v4, featured article card v2, featured book note card v2, course card v3. The versions they replace are in Card System's archive, and the folder README names them.
- **Every card build sheet's sizes corrected to match,** including the five cards no page draws today (quote, workbook, compact, featured quote, featured workbook). Their prototypes wait for the first page that renders them, since a prototype is exported from a rendered page.
- **The course card data file also carries three colours Kain's S128 rulings had already put live** and the record had not caught up with: the lighter grey off light grounds on the price qualifier and the guarantee pill, and the control orange on Enrol Now. `component_gate.py` failed on those before this session and passes now.
- `component_gate.py --all`: book note card 63 passed 0 failed, course card 56 passed 0 failed.

## One DSRD line this reaches

DSRD 8's card sections carry the old sizes as decision history, which DSRD 7 section 3.0 already says the register outranks. DSRD 7 section 3.1 names 26 on the Access All Areas title as belonging to the sweep; it is 24 now, and that row's note can close.

## OWED BACK

A dated line for this ruling where Chat keeps the sweep's record, and the AAA row note in DSRD 7 section 3.1 closed.

*No em or en dashes in this file; checked before writing.*
