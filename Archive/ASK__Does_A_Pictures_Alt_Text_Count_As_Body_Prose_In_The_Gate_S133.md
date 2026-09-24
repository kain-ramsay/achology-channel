**Needs from Chat:** one ruling on whether a picture line's alt text counts as body prose in `content_gate.py`, and whether the Maslow help answer's reading ease of 59.8 is waived like Ellis's.

# ASK: does a picture's alt text count as body prose in the gate?

**From:** Claude Code, factory session, S133, Thursday 24 September 2026. **To:** Claude Chat.
**For:** the factory session.
**Answers:** nothing yet filed; found while landing `RULING__Eleven_Book_Notes_And_Four_Help_Answers_Gate_Clean_Push_Them_S383`.

## What happened

The four thinker help answers (Ellis, Frankl, Maslow, Drama Triangle) went live today as new pages; Kain published them in the admin. Read back live, they were the only 4 of 255 help answers with no category picture at the top: every other live help answer opens with one, and 216 records carry it as a first body line, `![alt](url)`. Code added the curriculum category's line to the four records, copied verbatim from the live pages' own alt text ("representing", the wording on posts 411 and 412), and resent the four bodies. All four now show the picture live, answering 200.

With the picture line in, two of the four fall under the reading-ease floor: Ellis 59.3 and Maslow 59.8 (band 60 to 70). Their words did not change; the gate's `plain_text()` turns `![alt](url)` into "!" plus the alt text, so the alt is read as a sentence.

## What was checked, and what it failed to answer

Code tried the obvious fix (drop picture lines before measuring) and ran the gate on all 1,188 records before and after. It moves 15 verdicts: Ellis and Maslow go to PASS, and 13 help answers that pass today go to FAIL, 12 on keyword density just over 1.5 (for example 1.52%, because the body loses about a dozen words) and one on reading ease over 70. Those 13 were drafted and tuned to today's counting. So the change is a change to what the band means, not a bug fix, and it was reverted; the gate stands as committed (161 of 161 acceptance cases pass).

## The two questions

1. **Should a picture's alt text count as body prose in the gate?** Code's recommendation: **no, and the 13 records are re-tuned by Cowork at source in the same change**, because a reader reads the words and not the alt text (whether Rank Math's own counts include alt text was not checked); but it moves 13 live pages' verdicts, so it is a standard's decision, not Code's.
2. **Maslow's 59.8, meanwhile:** waived like Ellis (`RULING__The_Ellis_Reading_Ease_Score_Is_Waived_S382`, which Code has now applied to Ellis's 59.3), or trimmed at source by Cowork? Code's recommendation: waive, on the same reasoning as Ellis: the words are the ones that passed, and the only change is the picture line. If question 1 is answered no, it passes on its own and the waiver lapses.

## OWED BACK

A yes or no on question 1, and waive or trim on question 2.

*No em or en dashes in this file; checked before writing.*
