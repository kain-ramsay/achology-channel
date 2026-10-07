> CODE DISPOSITION, S154: WAITS ON the theme version moving past 0.707.155 with these fixes (read in full at S154; Kain's subject page sitting runs first).

**Needs from Code: three small theme fixes found by Chat's page read of the three exemplars, then one re-run of the readiness sweep on those three pages. Theme session or factory session, no Kain needed.**

# BRIEF: the author name hover, the article picture's description, and one link's spoken name (Chat, S414)

**From:** Claude Chat, S414, Thursday 8 October 2026. **For:** Code. **Board card:** Project Cleanup, every built page's readiness record.
**Context:** Chat wrote its reading lines into the three exemplar records today (`ASK__Reading_Page_Records_What_Is_Left_S152` is now closed). Read with Playwright at theme 0.707.155. Three faults belong to the theme. Each fix below is already settled by a standard; no visual decision is needed.

## 1. The author name link fails contrast on hover and focus (all three templates)

The author name in the author card (Frederick S. Martín on the quote page, Gary Kennedy on the article, Benjamin Lockwood on the book note) rests at 10.48 to 1, then turns brand orange rgb(237,105,34) on white when hovered or focused: 3.16 to 1 at 16px 600, under the 4.5 to 1 that DSRD 6 section 7 requires.

**The fix:** that hover and focus colour becomes `--color-orange-link` #B8460F, DSRD 7 section 1's orange for small text (5.35 to 1 on white). Check every other place the author card appears uses the same rule.

## 2. The article page's own picture has an empty description

On /learn/psychology/articles/what-is-jungs-shadow/ the band art (`.kh-article__band-art img`, what-is-jungs-shadow.webp) renders `alt=""`. It is the article's own picture and carries its idea, so it needs a description (DSRD 2 section 3.11).

**What Code finds out and does:** whether the template emits an empty alt on purpose or the record's image description is empty. If the template, it reads the record's description; if the record has none, say so in your report and Chat sends it to Cowork. Report how many built articles render an empty band-art description.

## 3. One Amazon link's spoken name runs two words together (book note template)

On the book note page the first "View the Book on Amazon" link's accessible name reads "View the Book on Amazonopens in a new tab": the hidden words follow with no break. The second Amazon link reads correctly. **The fix:** give the first the same hidden text as the second (", opens in a new tab").

## 4. Push Cowork's two S411 copy fixes on the same two pages

Cowork fixed both at source at S411 (`NOTE__Two_Small_Copy_Fixes_From_Codes_Checker_S411` and her S411 DONE): "GP" spelled out at first use on what-is-jungs-shadow, and every abbreviation spelled out on words-that-change-minds. Neither is on the build site yet. Push both records, after the gate passes them on those lines.

## 5. One gate line for workbooks, not covered by the S412 gate brief

The S412 brief (`BRIEF__Two_Gate_Changes_For_Workbooks_Standard_Version_13_S412`) adds the phrase count. Cowork's checkers also found seven-word runs a workbook shares with Help answers, which the Content Standard's Part 6 rule 8 forbids and the gate does not measure. Add a check for runs of seven or more words shared with any other published record, and exempt the workbook's fixed template copy (DSRD 2 section 3.4.1).

## 6. Then

Teach `page_gate.py` the new DSRD 6 section 1 carve-out (Chat, S414): an acronym inside another page's title in a reading-list block (Browse More Achology Articles, Explore More Book Notes, Explore More Quote Articles, any related-reading row) is recorded as a named carve-out, not a fail. Then re-run `page_readiness_board.py --sweep` on the three exemplars and write the machine lines. Leave Chat's lines alone; Chat updates its own after your report.

OWED BACK: a DONE file naming the theme version, the three fixes, the band-art count from item 2, the two pushes, the new gate line, and the re-run.

*No em or en dashes in this file; checked before writing.*
