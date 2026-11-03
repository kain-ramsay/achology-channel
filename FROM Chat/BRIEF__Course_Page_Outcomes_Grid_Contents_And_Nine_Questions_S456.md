> CODE DISPOSITION, S457 (factory, walk against the build site): WAITS ON a theme session: released by Chat at S457; the question selector needs a Penpot design Kain has signed, the short answers come from Chat, and the outcomes file is still unsigned
> CODE DISPOSITION, S208: WAITS ON Chat releasing it (its HELD line below); read in full by the course page design session, whose block 2 (Kain's pick 74, pattern 18, outcome tiles three across) takes the nine-box grid when it is released.
**RELEASED, Session 457, 3 November 2026.** Kain: "Yes, release it". Decisions 3 to 8 are settled by his S457 rulings on the idea pages plan: there is no separate lesson page type, the course contents carry no per-lesson links for now, and the idea pages and lesson articles come after launch. **All 28 courses' lesson paragraphs are signed** (002 to 006 one at a time, 007 to 028 as one set, "Yes, sign them all"), so print every course. The 004 preview changed: 004-001 no longer names a Facebook group.

**For Code (theme session). What this needs from you:** three changes to the course page template, each shown to Kain as four rendered options in the Change Viewer where it is visual, then one DONE naming the theme version.

# BRIEF: the course page outcomes grid, the course contents and the nine questions (Chat, Session 456, 3 November 2026)

**Why.** Kain ruled at S454 that the course page shows its learning outcomes as a grid, and that the nine questions for each course become one shared set on all 28 pages. At S456 he ruled the set at nine, word for word below ("Okay, so let's just go with 9 questions. Let's just go for 9."), and ruled that the set must fit every course, because "some of the courses aren't psychology courses". The governing record is the signed course page spec, `000__SIGNED_SPEC__Course_Page_Diploma_S333.md`, section 3c, which carries his rulings word for word.

**Kain's words:** "Yes, release it" (S457), after "Yes, sign them all" on the lesson paragraphs.

**Superseded inside this brief, read first.** Section 1's nine-box grid is replaced by Kain's "Map as the Floor" outcome cards, which the course page design session has already built. Spec 3c item 5 governs them, with the S457 rules: Mulish 16/1.5, four lines at most, and no fixed height. Do not rebuild them from section 1. The "four rendered options in the Change Viewer" lines are also replaced by Kain's Penpot ruling of 3 November 2026. The course contents look is already signed in its preview. The question selector still needs its look designed in Penpot and signed before it is built.

## 1. The outcomes grid (inside block 2, What You Will Learn)

- **The rule (Kain, S454, spec 3c item 5).** Eighteen outcomes for each course. Nine show at first, in a grid of boxes. Each box carries the outcome and its section ("Section 3"). Clicking a box swaps it for the next outcome not yet shown, and after all eighteen have shown the order starts again.
- **The data.** `Course Page Copy/000__COPY__Course_Learning_Outcomes_S454.md`, beside the spec. Each outcome is a numbered line with its section after it in bold; the italic line beneath it (lesson number and name) is for checking only and never reaches the page. Outcomes 1 to 9 are the first nine on show, 10 to 18 the reserve. **That file is a first version, not signed.** Build the grid and its data file now; the words go live only when Chat writes that the file is signed. Course 011 has sixteen outcomes, not eighteen; the grid must work with any count from nine up.
- **Behaviour.** All eighteen are in the delivered HTML, so a reader with no script and a search engine both see every outcome; the swap only changes which nine are visible. The click works from the keyboard, and a screen reader is told the box has changed.
- **Visual.** The box, the grid at each width and the swap are Kain's: four rendered options on the Diploma page, one a reading he did not name, your recommendation named (Harness Rule 7).

## 2. The course contents (block 3)

- **Each lesson shows its name, and under it its guiding question** (the first paragraph of its Standardised Description, as `achology_course_lesson_summary()` already returns).
- **Clicking a lesson opens one paragraph of 60 to 80 words saying what the lesson teaches** (Kain, S456: "we need a paragraph for each ... a block that allows the website visitor to navigate through exploring exactly what is taught in every lecture of the course"; course 001 signed: "totally user friendly ... exactly what I was looking for"). The paragraph replaces the rest of the Standardised Description on the page; the description itself is not printed.
- **Where the paragraphs come from.** One copy file per course in the Course Page folder's `Course Page Copy`, `000__COPY__Course_Lesson_Paragraphs_{NNN}_S456.md`, each paragraph under a bold line that starts with its lesson key (`**001-006 ...**`). Build one theme data file from them (a `paragraph` field per lesson, keyed by lesson key, beside or inside `data/lectures/{slug}.json`), with a build step so a re-signed copy file can be rebuilt without hand edits. Print only courses whose copy file says signed; a course not yet signed shows the name and question with no paragraph.
- **The look Kain signed** is in `Course Contents Previews S456/000__PREVIEW__Course_Contents_001_S456.html`: sections fold as option 1, each lesson is one button carrying its name, a plus mark and its question, and the paragraph opens beneath it. Every paragraph is in the delivered HTML and hidden visually only, so the spec's line "Every lesson name and description is in the delivered page and hidden visually only" is met; nothing loads on click. The button states `aria-expanded` and controls its paragraph.
- **No lesson links out.** The course page reaches the lesson articles only through its one line to its home hub (DSRD 1 section 6, link line 5). This is decision 6.
- Courses 012 and 027 keep their named cases (no section structure; one section).

## 3. The nine questions (block 10, Questions People Ask Before They Enrol)

- **Replace `achology_course_questions()`** and its per-course nine with one shared list, the same on all 28 pages, in this order, with these anchor ids:

| # | Question | Anchor | Read the full answer goes to |
|---|---|---|---|
| 1 | Is this the right course for me to start with? | `q-start` | /help/getting-started/first-course-complete-beginner/ |
| 2 | Will I learn practical skills, or mostly theory? | `q-practical` | /help/achology-basics-and-identity/achology-teaching-philosophy/ |
| 3 | Should I buy this course alone or the whole school? | `q-school` | /help/curriculum-and-subjects/which-courses-included-each-school-bundle/ |
| 4 | How many hours a week will the course take? | `q-hours` | /help/learning-experience/how-long-achology-courses-take-timelines/ |
| 5 | How long do I have to finish the course? | `q-time` | /help/pricing-and-payments/achology-lifetime-access-explained/ |
| 6 | Will I get to practise what I learn with other people? | `q-practise` | /help/events-and-mentorship/achology-live-events-types/ |
| 7 | What happens when my included membership ends? | `q-membership` | /help/membership-and-access/course-included-free-membership-happens-when/ |
| 8 | Can I pay for the course in monthly instalments? | `q-instalments` | /help/pricing-and-payments/pay-instalments-achology-courses/ |
| 9 | What if the course turns out not to be for me? | `q-refund` | /help/refunds-and-billing/does-achology-offer-a-money-back-guarantee/ |

  Every address above is the one its Help record carries in Content Records; check each against the install before it is printed.

- **The short answer is no longer found by matching the question to a Help answer's title.** The nine questions are worded differently from the Help answers they point to, on purpose, so no two pages share a title. Each question carries its own short answer (one to three paragraphs, written by Chat's delivery session after this brief is released) and the fixed address above. Read the short answers from one theme data file, one row per anchor, so Kain and Karen can edit them; Chat sends that file's words when they are signed. Until then each question renders with no panel, as today.
- **The link line stays** *Read the full answer*, to the address in the table, opening in the same tab (Kain, S456: "Yes, link them").
- **No question names Achology, a person or a certificate (Kain, S456).** The questions never name a course either. A short answer may need the course's own price or name; if Chat's answers use a slot, it is written `{course_name}` or `{course_price}` and filled from `courses-setup.php`, never typed.
- **Visual.** The question selector at nine (the About page's selector, or a plain accordion) is still Kain's open ruling from spec section 6: four rendered options, your recommendation named.
- **Markup.** Whether the nine carry FAQ markup is yours under DSRD 3 section 5; say which in the DONE.

## What Chat checks afterwards

On the build site, on the Diploma and on course 027: all eighteen outcomes in the page source and nine on show; every signed course's lesson paragraphs in the source, each opening on click under its name and question; no lesson link; the nine questions in order with their anchors; every "Read the full answer" address opening a signed page.

OWED BACK: one DONE naming the theme version, the option Kain chose for each visual, and the three checks above as you ran them.

*No em or en dashes in this file; checked before writing.*
