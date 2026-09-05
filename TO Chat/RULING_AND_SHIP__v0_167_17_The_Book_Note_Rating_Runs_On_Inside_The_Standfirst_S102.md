# RULING AND SHIP: v0.167.17, "Achology rating" leaves the book note page and "Essential Reading" with its ticks runs on inside the standfirst

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, on the rendered page after v0.167.16, spoken and transcribed by his dictation tool.
**His words, quoted exactly as transcribed:** *"I would like us to lose the words ecology rating on the page. And, um, then use essential reading with the ticks after it. Um, just build that into the the short description sentence. I... literally, just right after that full stop. So it's just the same the same font, um, as the actual description with the three text directly after that. The reason I say that is because that sentence is quite short anyway, um, has... carries... leaves quite a bit of space on the page. So by losing that full line, um, I think it just allows the the hero a little bit more kind of breathing space. Does that make sense?"* ("ecology" and "text" are the transcriber's hearing of Achology and ticks.)
**Filed under Harness Rule 14.** A theme edit made in a factory session on Kain's word, named in the theme commit `792603e`.
**Board card:** Knowledge Hub page designs.
**Supersedes, in part:** `RULING_AND_SHIP__v0_167_16_The_Book_Note_Rating_Line_Moves_Under_The_Standfirst_S102.md`. The author line's half of that ruling stands; the rating's own line under the standfirst lasted an hour and is replaced by this.

## What changed

In `single-book_note.php` the standfirst paragraph now carries the rating: after the excerpt's full stop and one space, the editorial scale's words ("Essential Reading" on this page) and the ticks, inside one span, `bn-hero__rating`. The words "Achology rating" appear nowhere on the page. The separate rating line from v0.167.16 is gone. Each half still renders only from its own data: a note with no standfirst but a rating gets the paragraph with the rating alone; a note with no rating gets its standfirst alone; a note with neither gets no paragraph.

In `book-note.css`: the rating span sets nothing but `white-space: nowrap`, so it takes the standfirst's own type and colour (16px, weight 400, white at 85 per cent) exactly as Kain asked, and the words and their ticks never split across a line break. The ticks keep their orange and their 12px Check glyph and gain `vertical-align: middle`, so they seat on the running line rather than its baseline. Deleted: the `.bn-hero__meta--rating` rule, the `:has()` rule that closed the standfirst up to it, and the `.bn-hero__meta-sep` rule, which nothing on any template used once the middle dots left the hero (checked across every PHP, CSS and Python file in the theme). The `.bn-hero__meta` rule now serves the author line alone; its comment says so.

**Measured on the deployed page.** At 1440: the standfirst runs three lines, the last reading "...building lasting emotional resilience. Essential Reading" followed by three ticks on the same line; author line to standfirst 24, standfirst to buttons 32 (the buttons sit where they did before v0.167.16); no "Achology rating" in the hero's text; stylesheet served at ver 0.167.17. At 390: the standfirst runs four lines, the rating phrase and its ticks sit together on the last one; the same 24 and 32. No horizontal overflow at either width.

## Shipped

Theme v0.167.17, `deploy.py` three proofs passed: server identical to local, zip 698 files matching the theme, server reporting 0.167.17. Commit pushed. Read in the in-app browser at the two widths above and opened in Safari for Kain as a new tab. **His approval of the rendered result is not yet given:** this file is written at the ship.

## Owed to the documents

DSRD 9 section 32.3's hero stack table: the author row stands as v0.167.16 left it (16 step, 24 below); the rating has no row of its own any more and is a clause of the standfirst row. Section 32.9 item 1 says the rating renders "in the hero as `Achology rating · {value}`, in the editorial scale's own words and never as stars": the words are still the scale's own and there are still no stars, but the label "Achology rating" is gone on Kain's word, so the item's wording is yours to bring to the page. The S050 tick-count question (does Recommended show one tick or three) still travels with the ticks and is still open.

OWED BACK: the section 32.3 standfirst row and the section 32.9 item 1 wording, yours.

*No em or en dashes in this file; checked before writing.*
