> **CHAT DISPOSITION, S351: read, acted on, ARCHIVED.** The test settles it: the S350 ruling stands, the 39 records go to two hashes at Cowork, and Code pushes each with `article_body_update.py`. Nothing changes on the Author Biography Articles card, whose next act was already Cowork's. Section 3's question, whether the record should say which tool last wrote a page, is answered in `REPLY__Your_Five_S106_Files_Answered_And_Two_Rulings_S351.md`.

# RULING: Kain takes the test re-import route, and it reverses Code's own recommendation

**DOCUMENT TYPE:** ruling, from Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Given by:** Kain, in the S106 sitting: "Tell chat to do the test re-import route please."
**Filed under Harness Rule 14**, with the measurement his ruling authorised, taken before this file was written.
**Board card:** Author Biography Articles.

---

## 1. His ruling, and what the test found

He ruled the route. The test is Code's, so it was run rather than scheduled, and **it does not say what I told you it would.**

**Two converters exist and they disagree, deliberately.** Run on the same record body, three hashes in:

| route | emits |
|---|---|
| the biography importer, `import_author_biographies.py` | **H2** |
| `article_body_update.py`, through the field-authority converter | **H3** |

The second one says so in its own words: *"H2 stays H2 and H3 stays H3. The older converters flatten every heading to H2 on DSRD 9 section 22.6's rule that the four sections are H2; that rule says nothing about a sub-heading inside a section."*

## 2. So my reading was wrong and your original ruling was right

**I told you correcting 51 records might change nothing, because the importer flattens.** That is true of the importer and it is beside the point, because **the importer cannot be the route.** It refuses any slug that is not free on the install, and all 39 of these pages are live. The only tool that can put a corrected body onto a page that already exists is `article_body_update.py`, and that one **preserves the level it is given.**

**Which means the record is the only thing that decides what those pages emit.** Records at three hashes give H3, records at two give H2. **Your ruling in section 3 of the S350 file, that the five section headings become H2 in the records, is the fix, and it is the only fix.**

**Confirmed on a real page rather than in the abstract:** `article_body_update.py` reads `kain-ramsay`, post 33613, as ready, from `Author_Biography_Kain_Ramsay_S298.md`, staying published, 12 internal and 1 external link. So the route works and waits only on the records.

**Nothing was sent.** No page was touched.

## 3. What this means for the 39, plainly

**Cowork's record work is necessary after all**, and I should not have suggested it might not be. **Correct the five section headings to two hashes in the 39 records**, and Code pushes each corrected body with `article_body_update.py`, which writes `post_content` and never a status, so a published page stays published.

**The twelve carrying H2 need nothing**, and the sharp two-way split is now explained: the twelve went in through the biography importer, which flattened them; the 39 were last written by `article_body_update.py`, which preserved what the record said. Two routes, exactly as the split suggested, but the opposite way round from my reading of it.

**One thing that follows and is worth a line in the standard.** Two converters in one toolkit disagreeing about heading levels is how this happened, and it will happen again on the next type that gets updated rather than imported. The disagreement is deliberate and defensible on its own terms, and the fault was that nobody knew which tool had last written a given page. **That is yours to rule on if it is worth ruling on; it is named here rather than fixed.**

## 4. The record of my own error, because it nearly cost a day of Cowork's work in the wrong direction

I read the biography importer, saw it flatten, and concluded the records were innocent. I did not check whether that importer could even reach a live page. **One measurement would have settled it and I reported the conclusion first.** That is the same fault as the 51 orphans and the filter that deployed doing nothing: a tool read, a conclusion drawn, no case checked by hand.

Kain's ruling to test rather than assume is what caught it, which is the argument for the rule.

---

OWED BACK: nothing on the route, which is settled. The 39 records to two hashes, Cowork's, then Code pushes them and reads one back off the rendered page.

*No em or en dashes in this file; checked before writing.*
