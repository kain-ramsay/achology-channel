# REPORT: the review normalisation dry run

**From:** Claude Code, Session 054. **Date:** 2026-08-11.
**Answers:** `COMMISSION__Review_Normalisation_Dry_Run_S262.md` in full.
**Nothing was applied.** No review text changed in any store. The script computes and reports; it has no write path.
**Source:** all 4,517 `review_text` values read from the live WordPress database this session, not from a CSV and not from the Notion bank.

## The headline

**897 reviews would change. 3,038 are already correct. 582 are flagged and stay untouched until Kain rules on them.**

That is 20 percent of the archive receiving a change, and four fifths of those changes are a single full stop at the end.

| | Count |
|---|---|
| Reviews read | 4,517 |
| Flagged, excluded from every count below | 582 |
| The confident pool | 3,935 |
| **Changed by at least one rule** | **897** |
| ... a sentence-initial capital only | 229 |
| ... a terminal full stop only | 575 |
| ... both | 93 |
| Already correct, untouched | 3,038 |

## The dry run found two defects in its own rules, and this is the useful part

The first run reported 1,035 changes. It was wrong, and the twenty samples are what caught it. Both faults were the script reading a reviewer's own punctuation as missing punctuation:

**1. It put the full stop inside emoticons and brackets.** A review ending "I have become a huge fan of you:)" came back as "of you:.)", and "( btw it's Thanksgiving 2023 )" came back as "2023 .)". The rule stripped closing brackets before testing the last character, so it walked past the smiley and inserted a stop behind it. Now: closing quotes are stripped, brackets never are, and a review ending in an emoticon or a bracket is flagged. **93 reviews.**

**2. It put a full stop after people's names.** Reviews closing "Thanks a lot Again, / Madhan" and "Much appreciated! / Karin" came back as "Madhan." and "Karin.". Adding a full stop to somebody's signature is an edit to their words, not typography. Now flagged. **62 reviews.**

Both were inside the amendment's letter and outside its purpose. **The apply pass must not run against the first version of these rules**, and the numbers Kain rules on are the corrected ones above.

## The flag list, with reasons

582 reviews, each excluded from the counts and untouched. A review can carry more than one reason.

| Reason | Count | Why it is not mechanical |
|---|---|---|
| Written entirely in lower case | 159 | Capitalising every sentence rewrites the register the reviewer chose. |
| Contains an all-capitals word | 140 | It may be an acronym the reviewer meant, or emphasis. The amendment protects acronyms explicitly. |
| Ends in an emoticon | 78 | Where the stop belongs, if anywhere, is a reading. |
| Sentence boundary ambiguous: a full stop with no space after it | 68 | "life.I have" could be one boundary or a typo inside one sentence. Splitting is a guess. |
| Ends in what reads as a name or sign-off | 62 | See defect 2. |
| Ends in an ellipsis | 43 | The reviewer chose to trail off. |
| Contains emoji | 28 | The same reading problem as an emoticon, at any position. |
| Contains a score such as 10/10 | 18 | A score is a deliberate fragment. |
| Ends inside a bracket | 15 | See defect 1. |
| Written mostly in capitals | 15 | Shouting is the reviewer's choice, not a defect. |

## The paragraph facts, which were the second half of the ask

Measured across all 4,517, the flagged ones included.

| How breaks are stored | Reviews |
|---|---|
| **No break of any kind: one unbroken run of text** | **3,895** |
| Newline characters | 622 |
| Of those, a blank line, meaning a true paragraph gap | 250 |
| HTML markup (`<br>`, `<p>`) | 0 |
| Carriage returns | 0 |

**What this means for Kain's subtle spacing, in plain terms.** Breaks are stored as plain newline characters and nothing else. **86 percent of reviews have no break at all**, so for those, paragraph spacing is a setting with nothing to act on. For the 622 that do, the spacing itself is **purely a stylesheet value**: the card needs `white-space: pre-line` or equivalent so the stored newlines render at all, and then the gap is one number. **No break was inserted and none should be**, exactly as the commission says.

One thing for Kain's eye rather than mine: those 622 reviews currently render as one unbroken block, because nothing in the card honours the newlines the reviewers typed. So the change is not "add spacing", it is "start showing the breaks that are already in the data, and space them". That is a visible change to a page he approved.

## Twenty before-and-after pairs

Windowed on the change, because a full stop at the end is invisible in a window on the opening.

| id | caps | stop | The change |
|---|---|---|---|
| 28978 | 1 | 0 | `this has been the best course` becomes `This has been the best course` |
| 29044 | 1 | 0 | `very innovative course.` becomes `Very innovative course.` |
| 29059 | 2 | 0 | `been enrolled to this course` becomes `Been enrolled to this course` |
| 29075 | 1 | 0 | `halfway though the course` becomes `Halfway though the course` |
| 29045 | 1 | 0 | after a line break, `i was briefed about` becomes `I was briefed about` |
| 28991 | 0 | 1 | `...make this course feel more interactive` gains a full stop |
| 28994 | 0 | 1 | `The thinking is really insightful though` gains a full stop |
| 29019 | 0 | 1 | `...heard 80% of this information before` gains a full stop |
| 29037 | 0 | 1 | `...psychology of the human behaviour` gains a full stop |
| 29065 | 0 | 1 | `...from their very own acquired philosophy` gains a full stop |
| 29071 | 0 | 1 | `Thank you so much for such a well tailored course` gains a full stop |
| 29082 | 0 | 1 | `But only half way being forced to rate` gains a full stop |
| 29127 | 0 | 1 | `...is giving me a sense of purpose` gains a full stop |
| 29147 | 0 | 1 | `...making myself wise with each new learning` gains a full stop |
| 29149 | 0 | 1 | `...practice of modern applied psychology` gains a full stop |
| 28988 | 2 | 1 | two opening capitals and a closing stop, placed inside the reviewer's own quote mark |
| 29003 | 2 | 1 | `it is very unfortunate` becomes `It is very unfortunate`, plus a closing stop |
| 29011 | 2 | 1 | `kept me engaged` becomes `Kept me engaged`, plus a closing stop |
| 29141 | 1 | 1 | `it is completely changing my world view` becomes `It is...`, plus a closing stop |
| 29148 | 2 | 1 | `when i checked the FB community` becomes `When i checked the FB community` |

**29045 and 29148 are the pair worth reading twice.** Both show the rule doing what it should and no more: the sentence start is raised, and the reviewer's own lower-case `i` in the middle of their sentence is left exactly as they typed it.

## Where the apply pass would run, and how it would be reversed

**WordPress only, and nothing else.** The 4,517 live in `qbk_postmeta` under `review_text` on the `review` post type. The Notion bank was the import source at S053, not a live dependency, and the Reviews page reads WordPress. Normalising the bank as well would create a second, differently-edited copy of every review that nothing reads and that would drift from the live one the first time Kain edits a review in WordPress. One store, and it is WordPress.

**Reversal is one query, and it is set up before the first change, not after.** Before any update, the pass writes each review's untouched text to a sibling meta key `review_text_raw` on the same post. Restoring the whole archive, or one review, is then a single copy back. On top of that, a full `qbk_postmeta` dump is taken and kept before the run starts, so a failure part-way through still has a complete floor under it. Both are in place before the first write or the pass does not start.

## What I need back

**One ruling from Kain, and two things that are his rather than mine.**

1. **Does the apply pass go ahead on the 897, with the 582 flagged reviews left exactly as they are?** That is the yes or no.
2. **The 159 written entirely in lower case are the largest flag group and the most interesting one.** They are not typos; they are a register. My read, offered rather than applied: leave them. Capitalising them is the one part of this amendment that would make the archive read less like real people.
3. **The paragraph spacing needs his eye**, because for 622 reviews it changes what the card shows, not only how far apart it shows it.

*No em or en dashes in this file; checked before writing.*
