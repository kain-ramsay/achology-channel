> CHAT DISPOSITION, S360: CLOSED, ARCHIVED. Section 5's owed-back ("Kain's choice between the three") was answered later the same S114 sitting: he chose to draw them, approved in `RULING__Kain_Approves_The_Drawn_Author_Mark_S114.md`. The nineteen without a photograph now draw the approved mark. `rick-hanson.webp`'s unrecorded licence (section 4) is named as separate housekeeping in `REPLY__The_Book_Note_Batch_From_S114_And_S115_Answered_S360.md`, not a live gap, since Rick Hanson draws the mark regardless.

# REPORT: five author portraits placed, two wrong faces struck, and the report that said twenty six was reading one folder of two

**DOCUMENT TYPE:** report, filed by Claude Code, Session 114, theme session. **Date:** Monday 14 September 2026.
**Shipped:** Theme 0.392.0, deployed and verified on the live install.
**Answers:** Kain's question at the S114 open, "how do we get the additional images we need right now", and the OWED BACK line in `REPORT__The_Author_Photograph_Sourcing_Position_S113.md`.
**Board cards:** Book author portraits; Book note template.

---

## 1. The number Kain was given twice was wrong, and the fault was the instrument

`achology_book_author_photo()` reads two folders in order: the book authors folder first, then Achology's own people folder. That second read exists because two of the people whose books this site writes notes about are also Achology's own, Gerard Egan and Kain Ramsay, and their photograph is kept once rather than twice so that replacing it cannot leave a stale copy. It has been in the theme since 0.384.1.

`absent_book_author_portraits.py` read one folder. So it named both men as having no photograph, and Kain was told twenty six at the S113 close and again at the S114 open. Two of the twenty six had been drawing correctly on the live site the whole time.

**This is the third time this one file has reported confidently off ground it could not see.** S050's green check over a broken thing, S113's ninety nine notes carrying no author slug, and now this. It reads what the theme reads now, in the theme's order, and the correction is written into the file beside the two earlier ones rather than filed away from them.

## 2. Five placed, and every face was looked at before it shipped

600 by 750, the 4:5 DSRD 7 section 12.1 sets, WebP inside section 12.3's 60KB budget, one crop rule for all of them, and each crop looked at afterwards.

| Slug | Licence | Credit owed | What was on screen |
|---|---|---|---|
| `admiral-william-h-mcraven` | Public domain | none | the official US Special Operations Command portrait |
| `niccol-machiavelli` | Public domain | none | the Santi di Tito portrait |
| `daniel-siegel` | CC BY-SA 3.0 | Gage Skidmore | speaking on stage, the right man |
| `albert-ellis` | Public domain | none | the 1960s dust jacket photograph |
| `david-brooks` | Public domain | Jay Godwin | the LBJ Library evening, 2022 |

**One of those was a naming fault rather than a missing photograph.** The record asks for `niccol-machiavelli` and the folder carried `niccolo-machiavelli`. A second case of the same shape is still open: three notes ask for `judith-s-beck` while the folder carries `judith-beck`, and that file cannot be placed because its licence was never recorded. See section 4.

## 3. Two faces are struck from the record as the wrong person

Both came through the fetcher's name-search route, both carry a clean licence, and both were sitting in the source folder under a correct filename waiting to be published.

- **`dan-sullivan`**: a young film director photographed at a MoMA festival, not the Strategic Coach founder.
- **`william-ury`**: an oil painting of President William McKinley.

`david-brooks` was a third, a Victorian engraving captioned DAVID W. BROOKS, and `credits.json` already carried its row. It is corrected rather than struck because the right photograph was found.

**So the S358 hold was right and its reason was exact.** Three of the four held faces looked at this session were the wrong man. A clean licence is not evidence of a correct face, and nothing but a human looking will ever make it one.

## 4. A third way to have no picture, which nothing reported

The theme refuses to draw a portrait with no row in `credits.json`, on the ground that a photograph whose source nobody wrote down does not go on a site that takes card payments. So a file can sit in the folder, correctly named, be counted as present by every count in the report, and draw nothing.

Two were doing exactly that. The report names them now. **`rick-hanson.webp` is the one a published note asks for**, and its licence has been unrecorded since S113, which makes it a live gap on the Rick Hanson page whose gate is already open.

## 5. Where it stands, read off the live install after the change

| | |
|---|---|
| Book notes published | 99 |
| Distinct authors with a portrait | 69 |
| of those, resolving from Achology's own folder | 2 |
| Distinct authors without | 19 |
| Notes carrying no slug | 0 |

**The nineteen do not move by fetching again, and this was tested rather than assumed this session.** Wikidata holds no chosen portrait for any of them, and the Commons name search returns coin catalogues, a chip shop in Lower Heath and a cargo ship. They are living authors whose publicity photographs belong to the photographers who took them. The decision between leaving them blank, drawing them, or buying them is Kain's and is unchanged, as section 3 of the S113 report sets it out.

OWED BACK: nothing from Chat on sections 1 to 4, which are Code's own work reported. On section 5, Kain's choice between the three, which the S113 report already asked for and which is still the only thing that moves the nineteen.

*No em or en dashes in this file; checked before writing.*
