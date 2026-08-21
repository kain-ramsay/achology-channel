# RULING: name the named guest, and never let a banned word rewrite a proper noun

**DOCUMENT TYPE:** ruling, given by Kain directly in the Code S078 sitting. **Filed:** 21 August 2026, same session, per Harness Rule 14.
**Owning document:** `The_Standardisation_Rule_Set.md` V4, rule 3 (the teacher is never named) and the Tier 1 banned list.
**Board card:** the video upgrade run, standardised descriptions.

---

## What Kain said

Asked to settle two questions that arose while writing the V4 descriptions for courses 016 to 020, his answer was:

> "yes to naming her properly, and yes to overriding the ban for genuine framework names, since a banned-word list should never rewrite somebody's name or a published model's title!"

Both halves are acted on and already in the master spreadsheets. This file is the record so V4 can be corrected at source.

## Question one: the named guest in a demonstration lesson

**V4 rule 3 carried an unresolved line, and it was flagged in the document itself** as the one line not ruled by Kain directly: "Where a lesson has a named guest, interviewee or case subject, that person is named in full, because they are part of what the lesson covers rather than the person delivering it."

**The row it bit on.** Course 018 carries fourteen lessons that are recorded conversations or live demonstrations, in which Karen A. Ramsay is the person being coached, questioned or interviewed. The source text for those rows reads, in several cases, "Kain and Karen" or "Kain guides Karen". Naming her that way names the teacher by implication, which rule 3 forbids absolutely. Writing round it left fourteen rows describing an unattributed conversation.

**Kain's ruling settles it: she is named properly.** The rows now name **Karen A. Ramsay** at first mention and describe her part directly, while the teacher stays unnamed, generally by putting the sentence in the passive. So "Karen A. Ramsay is guided through the examination of a negative pattern of thinking", never "Kain guides Karen".

**The canonical name was read, not guessed.** It comes from the theme's own Our People data at `people-setup.php`, row `karen-ramsay`: `'name' => 'Karen A. Ramsay'`, `'role' => 'Chief Executive Officer at Achology'`. That record is the approved artefact from the Our People build at S076.

**The fourteen rows:** 018-012, 018-032, 018-038, 018-041, 018-047, 018-051, 018-052, 018-053, 018-059, 018-060, 018-061, 018-112, 018-122, 018-126.

**What V4 needs:** rule 3's flagged line is now ruled and the flag comes off. Worth adding the mechanism explicitly, because it is the part that makes the rule workable: where the guest and the teacher appear together in the source, the sentence is rewritten so the guest is the subject and the teacher disappears rather than being referred to obliquely.

## Question two: a proper noun that contains a banned word

**The conflict.** Tier 1 bans "empower" and "empowerment" as marketing vocabulary, with no exception. Two lessons teach a published model whose actual title is **The Empowerment Dynamic**: 018-096 and 020-032. The mechanical gate refused to write either row, so the model could not be named at all.

**This is a genuine collision between two V4 rules**, not a drafting problem. "What is never touched" says: "Facts, names, numbers and claims of substance. If the source names a framework, a person, a model or a count, it survives exactly." Tier 1 says the banned words never appear. Both cannot hold.

**Kain's ruling resolves it in favour of the name.** A banned-word list exists to stop marketing language being manufactured; it was never meant to rewrite the real title of a published model or anybody's name.

**How it was built, so the exception cannot widen quietly.** `apply.py` now carries a `PROPER_NOUNS` list holding the exact string. The banned sweeps read a copy of the text with those strings masked out; the title-repeat check still reads the unmasked text, because a title repeat is a fault whatever words the title contains. The narrowness was proved rather than asserted: a bare "empower" outside the proper noun still fails the gate, and naming the teacher still fails it.

**What V4 needs:** a stated precedence between "what is never touched" and Tier 1, so the next collision does not stop a run. Suggested wording, for Chat to take or improve: *a proper noun survives exactly, and Tier 1 does not apply inside it; Tier 1 applies to every other use of the word in the same description.*

## Where this leaves the descriptions

All 2,146 rows now stand at V4 shape. The two deliberate holds are unchanged: 010-094, whose source is the only blank in the set, and 014-141, which waits on a course 014 transcript that does not yet exist.

*No em or en dashes in this file; checked before writing.*
