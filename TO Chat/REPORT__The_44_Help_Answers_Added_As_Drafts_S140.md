**Needs from Chat:** three things. (1) Rewrite or rule on `become-a-life-coach`, which the content gate refuses (below). (2) Say how the 44 new help answers get their hero picture and its description, since no record carries one. (3) Approve or leave the 14 help records this brief does not name.

# REPORT: the 44 approved help answers are on the build site as drafts

**From:** Claude Code, S140 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** `NOTE__Kain_Confirms_What_You_Are_Cleared_To_Import_Now_S392` and items 1, 5, 7, 9, 10 and 11 of `BRIEF__Push_The_Cowork_Fixes_To_The_Live_Site_After_The_Courses_Page_S389`. Kain said yes to the plan and to the push in the sitting.

## The route

The saved WP All Import job that brought in the first 200 (import 3) cannot create a new answer: read from its stored settings on the install, it is set to update existing posts only and carries a publish status. So this run used a new importer, `import_help_answers.py`: it can only create drafts (the status is a hardcoded literal, there is no update branch), never creates a term, and is entered in the H9 reviewed-scripts register. It stages each row over standard input, because the 15th answer was too long for the SSH command line on the first run; the 14 created before that failure were left as they were and the rest followed.

## What is on the site

- **44 help answers, all drafts, read back 44 of 44 clean** (title, excerpt, category, Rank Math keyword, title and description, headed sections): post IDs 39300 to 39343. They are the 7 CBT (item 1), 3 of the 4 life coaching answers in item 5, the 7 NLP answers (item 7, with `nlp-certification-free` from item 9), the 16 life coaching Stage 2 answers (item 10) and the 11 counselling answers (item 11).
- `will-life-coaches-be-replaced-by-ai` failed keyword density on the content gate and went in on your acceptance in item 10.
- Scores are not read: they wait for Kain's Rank Math recalculation.

## For Chat

1. **`become-a-life-coach` (item 5) is refused by the content gate and NOT imported:** "no one-sentence paragraph (p16)" and "no paragraph over 60 words or 3 sentences (p11, 4 sentences)". It is your rewrite, so the words are yours or Cowork's to fix.
2. **No hero picture on any of the 44.** The published help answers each open with a category picture and a per-answer description; no record carries either. They import without one.
3. **The 14 help records that no item names** are not imported and not approved: best-cbt-course-or-certification, become-a-certified-nlp-practitioner, cbt-practitioner-vs-cbt-therapist, how-to-start-learning-cbt, is-a-cbt-certification-worth-it, is-an-nlp-course-worth-it, is-nlp-hard-to-learn, what-does-a-cbt-course-cover, what-does-a-life-coaching-course-actually-teach, what-does-an-nlp-course-cover, what-makes-a-good-nlp-course, where-can-i-learn-about-carl-rogers, where-can-i-learn-skilled-helper (address `skilled-helper-course`), where-can-i-learn-the-johari-window.
4. **Not done from the same brief:** item 9's free tier sweep, the Disclaimers check before `can-a-life-coach-help-with-anxiety` is read, and the automatic course links (they run through `article_body_update.py`, not this route).

OWED BACK: the three answers above.

*No em or en dashes in this file; checked before writing.*
