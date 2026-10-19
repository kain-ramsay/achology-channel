# ASK: content_gate.py does not implement the S357 paragraph floor ruling; this session enforced the old rule by hand instead

**From:** Claude Cowork, the session following S360. **Date:** Monday 14 September 2026. **Session type:** content batch (course 001 quote pages).
**Under:** standing rule 17, Ask-Code Protocol: this is a fact about how a build behaves that only Code's file holds.
**Reads with:** `content_gate_standards.json` and `content_gate.py`, both in the Content Production Factory folder.

---

## What happened, plainly

Kain gave a new standing instruction this session, for all new quote-page drafting from now on: the paragraph floor ruling. Every paragraph is at least three sentences or at least fifty words, whichever it reaches first; one short paragraph is allowed per section, never two.

`content_gate_standards.json`'s shared block already carries this, word for word in its keys: `paragraph_sentences: [3, 4]`, `paragraph_floor_words: 50`, `single_sentence_paragraph: "once_per_section"`, `short_paragraph_allowance_per_section: 1`.

**`content_gate.py` does not read most of this.** Its paragraph-rhythm check is:

```python
pmin, pmax = std["paragraph_sentences"]
single_ok = std.get("single_sentence_paragraph") == "allowed"
...
if n < pmin or n > pmax:
    bad.append("p%d=%d" % (i, n))
```

`single_ok` tests for the literal string `"allowed"`, which the standard no longer sets; it sets `"once_per_section"`, so `single_ok` is always false. `paragraph_floor_words` and `short_paragraph_allowance_per_section` are never read anywhere in the file (confirmed by `grep -n "floor_words\|short_paragraph_allowance" content_gate.py`, no matches). So the deployed gate still enforces the older rule it printed before S357: every paragraph must run three to four sentences, no exceptions, with no word-count alternative and no per-section allowance for one short paragraph.

## What this meant for tonight's batch

Two quote pages were drafted and shipped this session under the new ruling: CQ001-052-1 and CQ001-056-1. Both times, the actual gate enforced the old strict rule, not the one Kain ruled. Paragraphs were rewritten by hand to land at exactly three to four sentences each, including splitting semicolon-joined clauses purely to satisfy the count, rather than being allowed to stand as a shorter, fifty-plus-word paragraph where that read better. Both pages pass gate. Neither got the benefit of the ruling as Kain actually stated it. This is not a one-off; it recurred identically on both records.

## The one question

Does Kain want `content_gate.py`'s paragraph-rhythm check patched to actually implement the standard already sitting in the JSON (word-count floor as an alternative pass condition, one short paragraph per section allowed), so the next fourteen or so quote pages in this batch get the real ruling rather than a stricter stand-in? Or is the strict three-to-four-sentence rule fine as the practical standard for now, leaving the fuller allowance unused in the JSON until some other session gets to it?

**Cowork's recommendation:** patch it. The JSON was written to carry Kain's ruling, the code was not updated to match, and the two now disagree; that is exactly the kind of drift the project's own harness system exists to catch before it repeats across a whole batch. Nothing here is blocked either way. The batch continues under the strict interpretation regardless of the answer, since it produces a page that passes gate; this is filed so the gap is fixed once rather than rediscovered lecture by lecture.

---

OWED BACK: Kain's ruling on whether to patch `content_gate.py`'s paragraph-rhythm check to implement the floor-words and once-per-section allowance, or leave the strict three-to-four-sentence rule as the practical standard for now. To FROM Cowork.

No em or en dashes in this file; checked before writing.
