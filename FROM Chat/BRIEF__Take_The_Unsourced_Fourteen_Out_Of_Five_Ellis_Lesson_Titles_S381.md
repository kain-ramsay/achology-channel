> **CODE DISPOSITION, S132: DONE, cancelled by Kain.** Asked directly, he said "No - just leave them as they are and drop this, permanenelty." Nothing renamed; `RULING__Kain_Drops_The_Ellis_Lesson_Rename_Permanently_S132.md` in TO Chat.

> **CODE DISPOSITION, S131: WAITS ON Kain saying yes to Code directly.** Renaming five live lessons in Circle changes what students see on another platform, so Code asks Kain in its own session before touching it; asked at this session's next message.

# BRIEF: take the unsourced "fourteen" out of five lesson titles in Circle

**Needs from Code:** rename five lessons through the Circle admin API, read each back, report.

**From:** Claude Chat, S381, Wednesday 23 September 2026. **To:** Claude Code.
**Approved by Kain, S381:** "yes" to taking the number out; asked whether his list of fourteen came from a source, "no".
**Why:** Ellis's own published lists of irrational beliefs ran to ten, eleven or twelve. No source gives fourteen, so a reader who knows his work would find the titles wrong. The rest of each title stays exactly as it is.

| Lesson key | Course | Title now | Title to set |
|---|---|---|---|
| 001-041 | DiMAP | Albert Ellis' Fourteen Completely Irrational Beliefs (Part 1) | Albert Ellis' Irrational Beliefs (Part 1) |
| 001-042 | DiMAP | Albert Ellis' Fourteen Completely Irrational Beliefs (Part 2) | Albert Ellis' Irrational Beliefs (Part 2) |
| 007-013 | CBT Practitioner | Exploring Albert Ellis' 14 Self-Sabotaging Beliefs (Part 1) | Exploring Albert Ellis' Self-Sabotaging Beliefs (Part 1) |
| 007-014 | CBT Practitioner | Exploring Albert Ellis' 14 Self-Sabotaging Beliefs (Part 2) | Exploring Albert Ellis' Self-Sabotaging Beliefs (Part 2) |
| 020-024 | Authentic Confidence Masterclass | Albert Ellis' Fourteen Insidious Perspectives for Life | Albert Ellis' Insidious Perspectives for Life |

1. Rename each lesson's title only, through the Circle admin API (the circle-api-reference skill holds the route). Nothing else on the lesson changes.
2. Read each back from Circle.
3. Update the five `lesson_name` values in `LESSON_INDEX__Twenty_Eight_Courses_S351.csv` to match. (Chat already took "fourteen" out of the two matching `standardised_question` values for 007-013 and 007-014.)
4. Any other place the site shows these titles (course page curricula, the Video Library, Knowledge Hub records naming the lessons): list where, and fix what reads from your data.

If the API cannot rename a lesson title, stop and say so; Kain then does the five by hand.

## OWED BACK

The five read-backs and the list from step 4.

*No em or en dashes in this file; checked before writing.*
