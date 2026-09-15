# ASK: 25 of the 42 Job 4 book notes fail on section headings, a category the UPDATE note did not mention

**Filed by Claude Cowork, Session 361. Date: 15 September 2026.**

## What I found

Running `content_gate.py` directly against each of the 42 draft (`post_status: draft`) book-note records, 25 of them fail on the locked section-heading check as well as the categories the UPDATE note listed. The gate's live standard (`content_gate_standards.json`, book-note type) requires these five headings verbatim, in order:

1. What this Book is Actually Saying
2. Where the Author is Coming From
3. What Could this Mean for Society?
4. What You Can Take From the Book
5. What are Your Next Learning Steps?

25 of the 42 carry a different, older set instead (for example "The Argument at the Heart of the Book", "The Background the Author Comes From", "Practical Applications Beyond the Book", "What this Might Possibly Mean for You", "What Your Next Learning Step Could Be"). The gate fails these outright: `section headings, verbatim and in order` plus one `unexpected section` line per heading.

The 25: a-treatise-of-human-nature, as-a-man-thinketh, atomic-habits-clear, best-self-be-you-only-better, boundaries-cloud, cognitive-behavior-therapy-second-edition, crucial-conversations-mcmillan, discipline-equals-freedom, emotional-intelligence-goleman, extreme-ownership-willink, feeling-good-burns, frames-of-mind, games-people-play, make-your-bed, the-history-of-philosophy, the-nicomachean-ethics, the-perennial-philosophy, the-philosophy-of-freedom, the-prince-machiavelli, the-selfish-gene, the-social-animal-aronson, the-tao-te-ching, thus-spoke-zarathustra, words-that-change-minds, words-that-work.

## What I have done

The other 17 of the 42 (headings already correct) are fixed and re-verified: paragraph rhythm and the "plainly" swap are done on all 17; I am now working through the remaining named categories on those 17 (tag count, reading ease, body word count, keyword placement, one external link) one file at a time, checked against the gate after each.

I have not touched the 25 heading-mismatched files. Renaming a locked heading is a bigger, more consequential edit than the mechanical fixes the UPDATE note described (it can mean the paragraph under the old heading no longer fits the new heading's stated scope, which is a content judgement, not a punctuation one), and the UPDATE note's count did not budget for it, so I am not guessing at it.

## The ask

Which of these does Kain want for the 25: (a) rename the five headings to the current locked wording and reflow the existing paragraphs under them as a mechanical relabel, checked by eye that nothing reads oddly against its new heading; or (b) something else, for instance a fuller rewrite if the old headings' scope has drifted too far from the new one to just relabel. I can do (a) on my own read of it, but it is a bigger commitment than the note described, so I am asking rather than assuming.

OWED BACK: a steer on (a) versus (b) versus something else for the 25, before I touch them. The other 17 continue in the meantime.
