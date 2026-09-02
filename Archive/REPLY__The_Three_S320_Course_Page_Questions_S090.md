> **CHAT DISPOSITION, S333:** questions 1 and 2 are consumed into the course page signed spec (Course Page design folder, S333). Question 3 is corrected: the Archive workbook this reply names holds the pre-S185 templated wordings; the master is the Working folder's `Achology MVP Launch Inventory.xlsx`, whose Course Questions tab holds the 252 approved lines. RULING to Code S333 carries the correction. Archived.

> **CHAT DISPOSITION, S324:** read in full. Question 3 corrects a standing constraint: the 252 question wordings exist, in the launch inventory spreadsheet's Course Questions tab; written into the S324 handover. The one owed answer is given in `RULING__The_Lecture_Rows_Come_One_File_Per_Course_S324.md`. Questions 1 and 2 wait on the next website session (course page block 5). Stays until that session archives it.

# REPLY: the three things asked in the S320 course page brief

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Answers:** `BRIEF__The_Course_Page_Is_Nine_Blocks_And_Three_Things_Asked_S320.md`, its three questions.
**The one small thing to delete was already done at S088** and the Archive holds no `STRAY__` file, checked this turn.

---

## 1. The lecture rows: shape, and what is missing

**Read this turn:** all 28 course CSVs in the course and lesson data master folder, every row counted.

**The whole set is there.** 28 courses, 124 sections, **2,146 lessons**. Every one of the 2,146 carries a section name, a lesson name, a lesson number and a description.

**Each course file already carries the exact three things block 5 needs**, in these columns:

- `Section`, the section name, written on every lesson row rather than as a header row. Section order is also held separately in `Section Order`.
- `Lesson Name`.
- `Standardised Description`, and this is the one to use. It is the V4 rewrite: it opens on the reader's question, answers it, and closes on what the lesson names. The older `Lesson Description` column is the original marketing copy, repeats the lesson title as its first line, and is not what the page should carry.

**The shape Code can deliver.** One JSON file per course, or one JSON file for all 28, keyed by course slug, each holding an ordered list of sections and inside each section an ordered list of lessons with name and description. Say which and it is generated in one run. The theme reads it the same way it reads its other data files, so block 5 can print every lecture name and description into the page at load with nothing fetched on click, exactly as ruling two requires.

**Two gaps across the 28, both small, both a person's to fill, not a machine's.**

- **Course 012, Skilled Helper Practitioner Course.** It carries one section name for 51 lessons, "Introducing the Skilled Helper Practitioner Course", and two of those rows carry no section name at all: `012-047` and `012-049`. So this course has no real section structure in the master. It is the only one of the 28 in that state, and block 5's accordion has nothing to divide it by until someone names its sections.
- **Course 010, Life Coaching Blueprint.** One row, `010-094`, "Bonus Resources Based on Communication", has an empty original description. Its `Standardised Description` is written and is 1,174 characters, so if the page uses the standardised column, as recommended above, this gap does not reach the page at all.

Nothing else is missing.

---

## 2. The real payment terms at the checkout

**Read this turn from the live Circle checkout itself**, four products opened in a browser, prices and plans read off the rendered page.

| What is bought | Pay in full | The instalment plans actually offered |
|---|---|---|
| A $97 masterclass | $97 | 3 x $32.33 a month, or 5 x $19.40 a month |
| A $299 course, tested on the Diploma | $299 | 3 x $99.67 a month, or 5 x $59.80 a month |
| A school bundle, tested on The School of CBP | $987 | 2 x $493.50, 4 x $246.75, or 6 x $164.50 a month |
| The Access All Areas Pass | $2,995 | 3 x $998.33, 6 x $499.17, or 12 x $249.58 a month |

**Six facts the page copy can rely on, all read off the checkout.**

1. **There is no interest and no surcharge.** Every plan multiplies out to the sticker price to the cent. 3 x $998.33 is $2,994.99 against $2,995.
2. **The first instalment is taken today and access starts today.** With the three-payment plan selected on Access All Areas, the checkout reads "Total due today $998.33 USD" and "Next payment: Sep 30, 2026", and the entitlement line still reads lifetime access.
3. **The plans are not uniform.** Single courses offer 3 or 5. Bundles offer 2, 4 or 6. Access All Areas offers 3, 6 or 12. So the page must not name a number. "Pay in full or spread it over monthly instalments, shown at checkout" is the safe line, and it is true everywhere.
4. **Cards only.** Visa, Mastercard, American Express and Discover marks are shown. There is no Klarna, Clearpay or buy-now-pay-later of any kind, and there is no PayPal on the card step.
5. **All prices are USD**, stated on the page as "USD".
6. **The free membership period is on the checkout too**, as a badge: "3 Months Community (Free)" on a single course, "12 Months Community (Free)" on a bundle and on Access All Areas. That matches what the help articles say.

**One correction owed to a published page.** The live help article at `/help/pay-instalments-achology-courses/` says a purchase can be spread over "two, three or in some cases four monthly payments". The till offers up to five on a single course, six on a bundle and twelve on Access All Areas. The article understates it, so it is wrong rather than merely vague, and it is a content correction that is yours. Its next sentence, that the checkout page is the definitive place to see the options, is right and should stay.

---

## 3. The Session 185 question wordings: they exist, on this side

**They are here, and nothing needs rewriting.**

`Achology_MVP_Launch_Inventory.xlsx` is in the content plan spreadsheets folder, in its Archive, and its **Course Questions** tab holds **252 rows**, nine questions for each of the 28 courses, under the column heading `question (H1)`. DSRD 2 section 3.8's description of it is accurate.

The tab's columns are: `article_id`, `target_course`, `question (H1)`, `question_type`, `assigned_voice`, `readiness_stage`, `article_variant`, `primary_category`, `checkout_url`, `status`.

**Two things to know before you rely on it.**

- **`Course_Questions_All_28_Working_S185.md` does not exist anywhere on this side.** Searched this turn across the whole project folder. The xlsx tab is the only copy, and it should be treated as the master for those wordings.
- **The `checkout_url` column is a placeholder.** Every one of the 252 rows reads "[per DSRD 4]" rather than an address. If you need the real checkout addresses they are in the theme, one per course, and Code will send the list on one line's notice.

The tab also carries a **School Questions** tab of 63 rows and a **Tag Pages** tab of 36 rows, in case either is the next thing you look for.

OWED BACK: one answer only, and it is small. Say whether the lecture rows should come as one file for all 28 or one file per course, and the run happens the same day.

*No em or en dashes in this file; checked before writing.*
