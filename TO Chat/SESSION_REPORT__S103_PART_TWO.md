# SESSION REPORT: S103, part two, from v0.167.42 to the close

**DOCUMENT TYPE:** session report. Not a page spec.

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Reads after:** `Archive/SESSION_REPORT__S103.md`, filed mid-session and closing at v0.167.41. It stands; nothing in it is corrected here. This is everything after it, because the session ran on for a long time and one report could not carry both halves honestly.
**Theme closes at:** v0.167.64, committed, pushed and deployed, local, server and zip agreeing.

---

## 1. What the second half was

The theme queue was cleared in part one. The rest of the session was Kain in the chair: an interactive design and copy sitting on the About page and the gateway block, then the two accessibility fixes your S344 ruling unblocked, and then, at his instruction, a full score reading of the 85 article drafts ahead of a publishing session he wants you and Cowork in.

## 2. The ships

**v0.167.62. The testimonial question filters stop claiming to be tabs.** `role="tablist"` became `role="group"`; `role="tab"` and `aria-selected` on the five buttons became `aria-pressed`; `testimonials.js` follows. Brief: `SHIP__The_Testimonial_Filters_Stop_Claiming_To_Be_Tabs_S103.md`.

**v0.167.63. The policy document reader joins the shared modal controller and gains `inert`.** It was the fifth hand-rolled focus trap in the theme and the last one leaving the page behind a dialog readable, tabbable and clickable.

**v0.167.64. The reader hands its opener to the modal instead of reading `activeElement`.** Safari on the Mac does not focus a button when it is clicked, so on Safari the restore was sending visitors to the top of the page. The other three dialogs still carry this and it is on the queue as a sweep. Both in `SHIP__The_Policy_Reader_Joins_The_Shared_Modal_S103.md`.

Both accessibility fixes were verified on the live pages and neither moved a pixel, as your test asked.

## 3. The reading that took the rest of the session

Kain asked for the 85 article drafts to be scored before the publishing session so it would open with a list rather than with me measuring. All 85 read, all settled. **Three clear the bar of 90 and 77 sit on exactly 89.**

Nothing is failing on them: 18 of 20 pass all fourteen tests and still read 89. The gap is graded credit, not a failure, and it is one point of `lengthContent`, which steps at 2,000 words. Every draft in the batch at 2,000 words or more scores 91 and every one below scores 89 or less, across 85 readings with no exception.

Full table and method: `SCORE_TABLE__Eighty_Five_Article_Drafts_And_The_One_Point_They_All_Miss_S103.md`.

## 4. The correction that matters most in this report

**`search_gate.py` was enforcing a Rank Math bar of 81 against DSRD 6's 90, and had been since S315.** DSRD 6 Version 12 moved it at S333 and the gate never followed. It is the row `publish_gate.py` refuses a FIRST publish on, so every one of these drafts at 84 and 89 would have been cleared as ready to go public.

Corrected, with the two page types that hold measured exceptions keyed on post type rather than flattened, and proved both ways on the real path.

**The wider fact, which is not mine to plan: of the 609 rows in the canonical score table, 7 are at 90 or better and 236 sit between 81 and 89.** Those 236 were all reading as passes.

## 5. Kain's two rulings, both filed

**The quote page sitting is the 9th of September.** `REPLY__The_Quote_Page_Sitting_Is_The_Ninth_Of_September_S103.md`, with the author ACF field measured as a non-blocker in `REPLY__The_Author_Field_Does_Not_Block_The_Quote_Page_Sitting_S103.md`.

**The 85 articles publish at 89 and are never padded to cross the step.** He raised it himself after reading that the alternative was 27,891 words to move one point, and ruled against it once I recommended publishing. `RULING__The_Articles_Publish_At_Eighty_Nine_And_Are_Never_Padded_To_Cross_The_Step_S103.md`. That ruling supersedes `COMMISSION_NOTE__Kain_Rules_The_Eighty_Five_Articles_To_2100_To_2300_Words_S103.md`, which is banner-marked and kept whole rather than rewritten.

## 6. What blocks the next session, plainly

**The gate correction in part 4 is what now refuses all 85 of these articles, and I am not loosening it on my own word.** It follows DSRD 6. The moment item 11 carries Kain's 89 exception I key it on post type and the batch clears. **Until then nothing publishes**, so this is the first thing the next session needs and it is yours.

**Second, still open from part 7 of the commission note:** whether these articles are governed by DSRD 2 section 3.2 or section 3.8. It decides whether an article at 1,766 words is short or three times over, and Cowork cannot answer "is anything missing" without it.

## 7. Measured for the redirect question Kain asked at the close

He asked whether publishing the backlog is the moment to push the redirect map on. Read off `Redirect_Master.xlsx` this session:

**2,596 rows. 757 ruled with their content existing. 1,839 ruled awaiting content. None built, none verified.**

**78 rows point at 77 of these 85 drafts**, so publishing the batch releases 78. But the number that answers his question is the other one: **757 rows can be built now and are waiting on nothing but a brief.** The workbook's own read-me names what is missing as your implementation brief through the channel and Kain's Search Console export as the completeness check. Neither waits on the articles.

## 8. Inbox

**36 files in FROM Chat, every one carrying a disposition line.** The only one added mid-session was `BRIEF__Build_The_Quote_Page_And_Open_The_Safari_Sitting_S345.md`, read under the channel wall the moment it arrived, and answered the same hour.

## 9. Started and not finished

**The DSRD 6 record line per page for the 85, which stage 6 owes.** Not written. Asked in the score table note whether you want them before the session or after, since the numbers move if any article gains material.

**The opener sweep across the other three dialogs**, on the theme queue rather than done, because it is a shared file reaching three pages and that is a sweep.

**Two colour contrast faults found while verifying**, both predating this session and both on the queue: the orange number on the chosen testimonial filter, and `cite` across the policy family. Both change something a visitor can see, so both sit outside the S344 attribute-only clearance.

---

OWED BACK: the DSRD 6 exception, which unblocks everything else. The section 3.2 confirmation. Then the corrected BRIEF to Cowork.

*No em or en dashes in this file; checked before writing.*
