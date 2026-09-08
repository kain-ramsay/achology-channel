# SESSION REPORT: S107, a factory session

**From:** Claude Code, Session 107. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Assembled from the version control log for the session**, per Harness Rule 13, with hand-added lines marked as such. Ten change sets across the two repositories.

---

## What finished, one line each

| # | Work | Board card |
|---|---|---|
| 1 | **All 92 book note titles take the ruled form**, the book's title then "Summary and Key Ideas". Read back: 91 in the colon form, the 92nd correctly without one because its title ends in a question mark. | Book Notes |
| 2 | **The publish gate can read every live Knowledge Hub body**, not only the article's. `publish_gate_body_acceptance.py`, 13 cases, proved red before green. Theme `2af3133`. | the harness and instruction sets |
| 3 | **The channel-file process line is off 16 live book note pages.** Found by the gate on its first run after fix 2. Zero pages carry it now, down from 16. | the 65 published book notes |
| 4 | **`publish_gate` gains `--retire`**, the route a live page comes down by, refusing unless a proved 301 already covers it. 15 acceptance cases, red before green. Theme `a4747fa`. | Book Notes |
| 5 | **`publish_gate` gains `--write-redirect`**, the first sanctioned route to write a redirect at all, proving each by asking the server. Theme `439542d`. | the redirect map |
| 6 | **The three dropped books were retired, then restored on Kain's reversal** when he sourced the covers himself. Live book notes 92 to 89 to 92. | the 65 published book notes |
| 7 | **The 39 author biography bodies are pushed.** Zero of 51 still emit an H3, down from 39. Three read back off the rendered page. | Author Biography Articles |
| 8 | **The fifteen help answer placements are applied and re-scored.** All fifteen now score 93, one at 96. | the 250 help articles |
| 9 | **`watch_due` written on 289 published records**, so stage 8 has a clock for the first time. Project `422d666`. | the harness and instruction sets |
| 10 | **`.bn-body` joins `page_gate`'s `PROSE_HOSTS`** on Kain's S353 ruling. Theme `1dd670e`. | the 65 published book notes |
| 11 | **The density check quotes the band in force**, not the one S318 replaced. Theme `05c3592`. | the harness and instruction sets |
| 12 | **Chat's three small tool faults, and the folder maps.** Project `28d2011`. | the harness and instruction sets |
| 13 | **Post 375: keyword claimed and set, with its title and description. Score 20 to 87.** | the 250 help articles |
| 14 | **The two DSRD 2 extracts sent**, five sessions late. | the keyword cluster plan |
| 15 | **The Skilled Helper and The Ultimate Life Coaching Handbook** both now carry an external source link and both read 88. | the 65 published book notes |
| 16 | **Sliced captures of all eighteen instructor articles**, three widths, 260 slices, in `_captures_S107` beside the records. Hand added: images are gitignored so they have no commit. | the 18 instructor articles |
| 17 | **The page gate run on all eighteen**, which is chapter 7's automated floor. Output held for the DSRD 6 machine halves. | the 18 instructor articles |

## Started and NOT finished, in those words

- **The DSRD 6 records for the rescued 117, Karen's twelve, the new 25, and I18's eleven chapter lines.** Not started. It was the first of the seven jobs this session opened with and it is the one that did not get reached. The eighteen page gate run above is the raw material for I18's.
- **The 92 book notes' machine chapters re-run** against the corrected `PROSE_HOSTS`. Chat's S353 section 1, second half.
- **The cross-linking card's guarded block and the `source_reference` answer.** Sixth of the seven jobs.
- **The Karpman workbook render.**
- **The 255-record status pass** (see below).
- **The semicolon answer** on the redirect map.

## Four rulings from Kain, filed separately

`RULING__Kain_Rules_The_Book_Note_Title_Form_And_Orders_The_Gate_Fixed_S107`, `RULING__Kain_Reverses_The_Three_Book_Drop_He_Found_The_Covers_S107`, `RULING__Small_Editorial_Corrections_Are_Codes_S107`, `RULING__Kain_Commissions_A_New_Guide_To_Rational_Living_S107`. The third narrows Rule 8 and wants writing into the document that owns it.

## The finding that matters most, and it is not on the list above

**255 records disagree with the install about their own status; 92 say `publish` while no page exists at all.** Full table in `REPORT__Two_Findings_From_Section_3_And_255_Records_That_Disagree_With_The_Install_S107`. Every count of "what is published" taken from records rather than the install has been wrong, in both directions, and that is the root of several of the five errors the S106 close recorded.

## What this session got wrong, since a report that only lists wins is not a record

- **A body pushed with the wrong tool broke 16 live pages**, removing the decorative rule, the heading level and the working contents list. Kain caught it on the rendered page. Repaired, then two older pages carrying the same fault were repaired with it. **The cause was checking the words and never opening the page.**
- **A cover was replaced at its own address**, so every browser kept showing the old picture and Kain saw the wrong book on his screen. Republished at a new address. This project's own version-bump lesson, arriving as an image.
- **An apostrophe question travelled to Chat that should not have.** Kain ruled it back.
- **Two of Code's own checks reported faults that were not there**, one on post 273 and one on the rendered apostrophe. Both corrected and both recorded in the files that carry them.

## Hand-added lines, so a reader can tell what rests on the log

Items 1, 6, 8, 13, 15, 16 and 17 touched the install or produced images rather than repository files, so they have no commit of their own and are written from the measurements taken at the time, each of which is quoted in the file that owns it.

---

OWED BACK: nothing from Chat for this report. The six unfinished items above are Code's and carry to the next factory sitting.

*No em or en dashes in this file; checked before writing.*
