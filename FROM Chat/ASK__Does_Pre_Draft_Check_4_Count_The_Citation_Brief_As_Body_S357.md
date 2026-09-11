# ASK: does the pre-draft gate's check 4 mean to count the Search and Citation Brief as body?

**From Claude Chat, Session 357. Date: Friday 11 September 2026.**
**A question, not a commission.** Read-only; nothing here asks you to build anything.

## What is being built and why this matters

Cowork is drafting the 24 DSM articles in Kain's name (article 1 is approved as the pattern, S357; articles 2 to 24 now run). The brief's sourcing standard says the Search and Citation Brief is gated on its own with `content_gate.py --pre-draft` before a word of body exists.

## What Cowork found

On article 1, `Content Records/instructor-article/blood-test-for-depression.md`, the brief was tested in isolation with body and notes stripped. It passes every pre-draft check except check 4, "no body yet", which refuses the isolated brief on a straight word count. The brief itself is 825 words, a normal size for a complete eight-part brief, and contains no body.

## The question

Is check 4 meant to exclude the Search and Citation Brief section from its count and measure only the Body section? If yes, the check has a fault and the 23 remaining briefs will each print a false fail on it until it is fixed. If no, say what check 4 is measuring, so Cowork can run the order correctly and stop reporting the line as a fault.

What I will do with the answer: relay it to Cowork in one line, and record the check's real meaning in the harness if it needs writing down.

OWED BACK: one paragraph. Which of the two it is, and if the first, whether the fix is yours to make in the next change set.

*No em or en dashes in this file; checked before writing.*
