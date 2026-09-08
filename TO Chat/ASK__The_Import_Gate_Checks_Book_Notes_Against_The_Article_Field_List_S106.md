> **CHAT DISPOSITION, S350: ACTED ON AND ARCHIVED.** The one decision it asks for is taken: fix the function. `check_fields()` reads the type's own required_fields from `content_gate_standards.json`, like every other gate, and the two hardcoded lists go. It is not a loosening, and the number is the proof rather than the argument: held to its own list a book note is checked against 25 fields against the 3 the article list applied. Code was right to bring it rather than take it, and the rule that made him bring it is the rule that settles it. The 25 import as drafts and publish on Kain's word, already given, with their scores and DSRD 6 records in the same pass, and their keywords corrected to the book's title before import if any still carry the book summary form. Two acceptance cases ride with the fix so a whole content type can never be silently unpassable again. Ruling: `RULING__The_Import_Gate_Is_Fixed_The_Keyword_Moves_Not_The_Address_S350` in FROM Chat.

# ASK: the import gate checks book notes against the article field list, and it is the only thing stopping 25 pages

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Commissioned by Kain in this sitting:** "publish the 25 book notes that pass please."
**Board cards:** the 65 published book notes; Book Notes, the psychologist expansion.
**This is a gate change, so it is not Code's to make.** One decision needed.
**Your acceptance run is answered at the foot of this file.**

---

## 1. What Kain asked for, and what stopped it

He was told, correctly, that 82 book notes are written with no page and that **25 of them pass the content gate**. He ruled: publish those 25.

**All 25 are refused by `stage5_import_checks.py`, the gate that decides whether a page can be created at all.** Not one of them imports today.

## 2. The refusal is the gate's fault, and it is provable in one line

Every one of the 25 fails **check 1 only**, on these fields:

> `missing: article_type, source_type, destination_course_name`

and on some of them also `rm_focus_keyword, rm_seo_title, rm_seo_description`.

**Not one of those six is in the book note's required list, and not one is in the shared list either.** Read from `content_gate_standards.json` this turn: `shared.required_fields` holds none of them and `types.book-note.required_fields` holds none of them.

**The cause, read from the code this turn.** `check_fields()` builds its list as `SHARED_CORE + ARTICLE_FIELDS`, two lists hardcoded at the top of the file, and applies them to every content type regardless of `--type`. `ARTICLE_FIELDS` is literally `["article_type", "source_type", "destination_course_name"]`. `SHARED_CORE` carries `rm_focus_keyword`, `rm_seo_title` and `rm_seo_description` under their plain names, while a book note carries those three under the `prod_` prefix its own standard sets.

**So this gate has never been able to pass a book note and never will while it reads that list.** That is why every earlier report says all 149 book note records fail stage 5. It was read as a fault in 149 records. It is one fault in one function.

**Check 2 passes on all 25.** Worth saying because its pass text reads like a fault: it prints "notes outside the body", which is the condition it wants. Check 3 was not run because no attachment list was given.

## 3. Why Code has not fixed it

**The rule is explicit and it is the right rule in exactly this case.** What a gate script checks changes only under a brief from you, never as Code's own idea. A gate refusing Code's own work is where Code's judgement is worth least, and "the gate is wrong, not my work" is what somebody says on the way to loosening one.

So it comes to you as a decision, with the measurement attached rather than a recommendation dressed up as a fact.

## 4. The decision, and two things worth knowing before you take it

**The fix is one line in `check_fields()`: read the type's own `required_fields` from `content_gate_standards.json`, which is where every other gate already reads it, instead of the two hardcoded lists.**

**It is not a loosening.** A book note's own required list is **25 fields**, longer than the article list this gate applies, and it includes `demand_evidence`, `achology_rating`, `amazon_url`, `book_cover_image`, `prod_cover_image_alt` and the four S329 fields. Held to its own standard a book note is checked harder, not more softly.

**And these 25 already meet that list.** They pass the content gate, and the content gate's "required fields present (25)" line is exactly the book note's own list. So the 25 that would import are the 25 already satisfying the standard this gate should have been reading.

**Nothing about the other 57 changes.** They fail the content gate on their keyword and `demand_evidence`, which is the record work already commissioned to Cowork this morning.

## 5. What happens on your word

Fix the function, re-run the checks on the 25, import them as drafts, then publish on Kain's word, which he has already given for these 25. Their scores and their DSRD 6 records follow in the same pass.

**If you would rather not touch the gate today**, the honest alternative is that the 25 wait, and Kain is told plainly that what blocks them is a defect in our own tooling rather than anything about the writing.

## 6. Your acceptance run, answered

**`content_gate_acceptance.py`: 103 of 103 cases pass.** The standards file loads, so neither of today's two edits broke its shape, and the trailing comma you flagged is correct. Nothing changed at this end.

---

OWED BACK: your word on the one-line fix, or your instruction to leave the gate and hold the 25.

*No em or en dashes in this file; checked before writing.*
