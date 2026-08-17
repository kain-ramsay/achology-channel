# REPORT: the block heading standard is in the gate, and here is the sweep

**From:** Claude Code, Session 054. **Date:** 2026-08-11. **Theme:** v0.60.10, deployed.
**Answers:** DSRD 7 section 3.3's enforcement paragraph: "Code builds the four mechanically checkable rules (length, sentence count, mid-sentence capitalisation, first-word voice test) into the page gate, then sweeps the existing lines; failures come back through Chat for rewrites Kain approves."

## 1. The ruled rewrite is applied

The testimonials watch line now reads, on both pages that carry it: **"Watch testimonials from our past and present students on their learning experience with Achology."** Sentence case, and the doubled word gone; it read "testimonials videos". Live at v0.60.8.

## 2. The checker is check 15, and two of the five rules are reported rather than failed

Built into `page_gate.py`. The four mechanical rules fail: 12 to 25 words, one or two sentences, sentence case, and the voice test. Two things are surfaced and never failed, because both turn on a reading rather than a measurement:

- **A heading with no supporting line.** Rule 1 allows it where the line would restate the heading or the block lists self-describing items, which is a judgement.
- **An imperative opener.** Rule 4 allows it where the block's job is to direct an action, which is also a judgement.

The seven policy pages are a named carve-out and report as one, per the section's own words.

## 3. The first run was wrong, and what it was wrong about matters

**The first version reported 40 failures and most of them were not failures.** It was reading the opening paragraph of the manifesto, the code of ethics, the founders' letter and every help article as an over-long supporting line. Had that list travelled, Chat would have been asked to cut forty paragraphs of real writing down to 25 words.

Two narrowings, both structural rather than guessed:

1. **A heading followed by more than one paragraph introduces long-form writing**, not a supporting line. A supporting line is one paragraph; that is what it is.
2. **A heading inside a prose host is a section heading**, which this standard does not reach. Needed as well as the first test, because an article section can be a single paragraph and still be prose: "Why Self-Awareness Matters" is one 45-word paragraph, and cutting it to 25 words would be editing the article.

Both exclusions are **counted and printed** rather than dropped, so a page cannot read as clean on ground the checker never looked at.

**This is a real gap in section 3.3 and it is Chat's to close, not mine.** The section says "every content block heading" and never draws the line between a block heading and a section heading inside a piece of writing. I have drawn it structurally so the checker could run at all, and it should be written into the section in words, so the next person does not have to infer it from a regular expression.

## 4. The sweep: 12 distinct failures across 9 pages

Every one is a genuine block heading with a genuine supporting line. Copy is Chat's under Rule 8, so these come back as rewrites, not as fixes I have made.

| Page | Heading | What fails |
|---|---|---|
| `/about/` | Achology: What It Is, and Who It's For | 49 words, and 3 sentences |
| `/about/` | The Achology Story | 34 words |
| `/about/` | Five Aspects of the Achology Experience | mid-sentence capitals: Learning, Experience |
| `/about/`, `/reviews/`, `/testimonials/`, `/about/founders-letter/` | Do you have questions about studying with Achology? | 38 words. **One line, four pages**: it is the shared enquiries panel, so one rewrite fixes all four |
| `/reviews/`, `/testimonials/` | A Global Learning Movement | 8 words, and mid-sentence capitals: Students, Span, Entire, Globe |
| `/about/code-of-ethics/` | Code of Ethics Bi-Annual Training | 39 words, and mid-sentence capital: Master |
| `/learn/psychology/` | Quotes (0) | 11 words |
| `/about/instructors/kain-ramsay/` | Kain's Writing and Articles | 8 words |
| a help article | Still Have Some Unanswered Questions? | 10 words |

**And one collision that is not a failure to be rewritten. It is two of Kain's own rulings disagreeing.**

"A Global Learning Movement" and its line "At Achology, Our Students Span the Entire Globe" are **Kain's own words, given in session and ruled at S053**. They are recorded as RULED in the global impact build sheet filed this session. The heading standard was ruled at S263, and his line breaks two of its rules: 8 words against a floor of 12, and title case against a sentence-case rule.

I have not touched it. **A later general rule does not quietly overwrite an earlier specific ruling on his own wording**, and which one gives way is his to say. It is the only item on this list where the answer might be "the standard yields" rather than "the line changes".

## 5. Pages that pass clean

`/about/instructors/`, `/policies/`, `/help/`, a help category page and the article page all pass with zero failures once the prose exclusion is right.

## 6. What I need back

1. **Rewrites for the 12**, from Chat, for Kain's approval. The enquiries panel line is the highest value: one rewrite, four pages.
2. **Kain's word on the global impact band line**, which is the collision in section 4.
3. **Section 3.3 amended** to say in words where a block heading ends and a section heading inside writing begins, so the boundary lives in the standard rather than only in my checker.

*No em or en dashes in this file; checked before writing.*
