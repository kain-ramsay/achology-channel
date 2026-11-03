**HELD. Do not run.** Chat releases this brief by replacing this line once Kain has answered the nine decisions on `000__DECISIONS__Buyer_Questions_And_Lecture_Pages_S456.html` (the Course Page design folder). Until then it is a draft, written against Chat's recommendations.

**For Code (theme session). What this needs from you:** three changes to the course page template, each shown to Kain as four rendered options in the Change Viewer where it is visual, then one DONE naming the theme version.

# BRIEF: the course page outcomes grid, the course contents and the twelve questions (Chat, Session 456, 3 November 2026)

**Why.** Kain ruled at S454 that the course page shows its learning outcomes as a grid, and that the nine questions for each course become one shared set of twelve on all 28 pages. Session 456 brought him the twelve and the course contents decision on one page. The governing record is the signed course page spec, `000__SIGNED_SPEC__Course_Page_Diploma_S333.md`, section 3c, which carries his rulings word for word.

**Kain's words:** to be written here when he answers.

## 1. The outcomes grid (inside block 2, What You Will Learn)

- **The rule (Kain, S454, spec 3c item 5).** Eighteen outcomes for each course. Nine show at first, in a grid of boxes. Each box carries the outcome and its section ("Section 3"). Clicking a box swaps it for the next outcome not yet shown, and after all eighteen have shown the order starts again.
- **The data.** `Course Page Copy/000__COPY__Course_Learning_Outcomes_S454.md`, beside the spec. Each outcome is a numbered line with its section after it in bold; the italic line beneath it (lesson number and name) is for checking only and never reaches the page. Outcomes 1 to 9 are the first nine on show, 10 to 18 the reserve. **That file is a first version, not signed.** Build the grid and its data file now; the words go live only when Chat writes that the file is signed. Course 011 has sixteen outcomes, not eighteen; the grid must work with any count from nine up.
- **Behaviour.** All eighteen are in the delivered HTML, so a reader with no script and a search engine both see every outcome; the swap only changes which nine are visible. The click works from the keyboard, and a screen reader is told the box has changed.
- **Visual.** The box, the grid at each width and the swap are Kain's: four rendered options on the Diploma page, one a reading he did not name, your recommendation named (Harness Rule 7).

## 2. The course contents (block 3)

- **Each lesson shows its name, and under it its guiding question** (the first paragraph of its description, as `achology_course_lesson_summary()` already returns). This is decision 9.
- **The rest of the description is put into the delivered page, out of sight until the lesson is opened.** Today only the first paragraph is printed, so the spec's own line, "Every lesson name and description is in the delivered page and hidden visually only", is not yet met. Nothing loads on click.
- **No lesson links out.** The course page reaches the lesson articles only through its one line to its home hub (DSRD 1 section 6, link line 5). This is decision 6.
- Courses 012 and 027 keep their named cases (no section structure; one section).

## 3. The twelve questions (block 10, Questions People Ask Before They Enrol)

- **Replace `achology_course_questions()`** and its per-course nine with one shared list, the same on all 28 pages, in this order, with these anchor ids:

| # | Question | Anchor | Read the full answer goes to |
|---|---|---|---|
| 1 | Is Achology recognised, and who accredits its courses? | `q-recognised` | /help/outcomes-and-expectations/will-employers-recognise-achology-certificate/ |
| 2 | What does it mean to be Achology certified? | `q-certified` | /help/certificates-cpd-accreditation/difference-between-certificate-completion-certificate-achievement/ |
| 3 | Can I work with clients after an Achology course? | `q-clients` | /help/outcomes-and-expectations/call-myself-certified-achology-credentials/ |
| 4 | What do Achology reviews from past learners say? | `q-reviews` | /reviews/ |
| 5 | How much does an Achology course cost, and what's included? | `q-cost` | /help/pricing-and-payments/achology-pricing-versus-udemy-universities/ |
| 6 | Can I pay for an Achology course in monthly instalments? | `q-instalments` | /help/pricing-and-payments/pay-instalments-achology-courses/ |
| 7 | Can I get a refund if an Achology course isn't for me? | `q-refund` | /help/refunds-and-billing/does-achology-offer-a-money-back-guarantee/ |
| 8 | How long do I have to finish an Achology online course? | `q-time` | /help/pricing-and-payments/achology-lifetime-access-explained/ |
| 9 | Can I start an Achology course with no experience? | `q-experience` | /help/learning-experience/achology-course-prerequisites-requirements/ |
| 10 | What support do I get from Achology while I study? | `q-support` | /help/events-and-mentorship/mentoring-opportunities-achology-membership/ |
| 11 | Are Achology courses the same as Kain Ramsay's on Udemy? | `q-udemy` | /help/comparisons-and-alternatives/kain-ramsay-udemy-vs-achology-courses/ |
| 12 | Is online certification as valuable as in-person training? | `q-online` | /help/comparisons-and-alternatives/are-psychology-certificates-worth-it/ |

  Every address above is the one its Help record carries in Content Records; check each against the install before it is printed.

- **The short answer is no longer found by matching the question to a Help answer's title.** The twelve questions are worded differently from the Help answers they point to, on purpose, so no two pages share a title. Each question carries its own short answer (one to three paragraphs, written by Chat's delivery session after this brief is released) and the fixed address above. Read the short answers from one theme data file, one row per anchor, so Kain and Karen can edit them; Chat sends that file's words when they are signed. Until then each question renders with no panel, as today.
- **The link line stays** *Read the full answer*, to the address in the table, opening in the same tab.
- **Course name in an answer.** The questions never name a course. A short answer may need the course's own price or name; if Chat's answers use a slot, it is written `{course_name}` or `{course_price}` and filled from `courses-setup.php`, never typed.
- **Visual.** The question selector at twelve (the About page's selector, or a plain accordion) is still Kain's open ruling from spec section 6: four rendered options, your recommendation named.
- **Markup.** Whether the twelve carry FAQ markup is yours under DSRD 3 section 5; say which in the DONE.

## What Chat checks afterwards

On the build site, on the Diploma and on course 027: all eighteen outcomes in the page source and nine on show; every lesson's full description in the source and only its question on show; no lesson link; the twelve questions in order with their anchors; every "Read the full answer" address opening a signed page.

OWED BACK: one DONE naming the theme version, the option Kain chose for each visual, and the three checks above as you ran them.

*No em or en dashes in this file; checked before writing.*
