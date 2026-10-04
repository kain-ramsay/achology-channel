# Job 11: the help answer subheading rule (read only, facts only)

Repository state: `kain-ramsay/achology-record` at `main`, commit `1e91422`, fetched fresh. Nothing in the repository was changed. No replacement wording and no new rule text is proposed.

## Summary

- I ran the real `content_gate.py` on all 360 `HELP__*.md` records in `Content Records/help-answer` (working files `MEASURED__`, `RESEARCH__`, `_batch6_slugs.txt` are not records). The line `keyword in a subheading` FAILS on **212** and PASSES on **148**. The 212 matches your figure. Your 129 passing of 341 does not reproduce: the folder holds 360 records now, and I count 148 passing. Cannot tell which 341 or which 129 the earlier figure was taken from.
- The line is a literal test: the lower-cased focus keyword must appear, as it is spelled, inside one of the body's headings (the shallowest heading level in the body). The page title and the H1 are not counted. It is stood down only for types whose standard says `headings_locked: true` (book note, quote page). Help answer says `headings_locked: false`, so it is run for real.
- The 107 records carrying the newer field set (demand_evidence, kh_tag, search_intent, schema_type, and the S386 to S391 notes) **all pass** (107 of 107, none fail). Of the 253 older-format records, 41 pass and 212 fail.
- In no failing record does any heading contain the keyword, even after folding case, curly quotes and punctuation (0 of 212). The newer records carry 4 to 11 headings (median 6) against 2 to 6 (median 3) in the failing ones.
- 82 of the 212 failing records have the keyword inside their own post title; the title is not a heading the line reads.
- The approved exemplar `HELP__what-is-achology.md` fails this line (keyword "what exactly is achology"; 5 headings read, none contains it).

## 1. What the line does and how types are stood down

**The check** (`content_gate.py:1256` and `1274`): `heads = [h.lower() for h, _ in split_sections(body)]`, then `any(kw in h for h in heads)`. `kw` is the record's `rm_focus_keyword`, lower-cased (line 1234). `split_sections` returns the headings of the body's shallowest heading level only (docstring at line 314: ruled S328), so in a help answer that is the `##` headings. `body` is the text after `## Body` (`extract_body`), so the `# Title` line and the `post_title` field are outside it. The test is a plain substring match: no stemming, no word order, no partial credit. The detail printed is only `N headings read`.

**Stood down, and for whom** (`content_gate.py:1268-1273`): the line is replaced by a note "NOT APPLICABLE: headings locked by design ruling" when the type's standard has `headings_locked: true` and the record's slug is not on that type's `heading_keyword_exception` list. In `content_gate_standards.json`:

- **book-note** (line 895): `headings_locked: true`. Its note (line 896): the five body headings are locked verbatim by DSRD 9 section 32.7, ruled by Kain on rendered pages; "None of them can carry a book's name"; stood down at S335 on Kain's ruling. Every other keyword line still applies.
- **quote-page** (line 382): `headings_locked: true`. The three body headings are fixed words in a fixed order (Kain, S356). Ten named slugs carry the `heading_keyword_exception` (lines 384-385, ruled by Kain at S388, cleared S391): on those the line is run for real and the second or third heading may carry the keyword. Four more quote pages are recorded shortfalls and stay stood down.
- **help-answer** (lines 1005-1007): `headings_locked: false`, `headings_are_questions: true`, `sections: {}`. The note on headings (S356, Kain): every heading is the reader's next question, never a label; a label is a heading with no question mark that opens with none of what, how, why, can, do, does, is, are, will, should, where, who, when. The note on sections: a help answer has no fixed section shape, and the answer arrives in the first paragraph, which the gate measures as the first paragraph carrying the focus keyword. I found no line in `content_gate.py` that reads `headings_are_questions`; whether another place enforces it: cannot tell.
- Every other type in the standards file leaves `headings_locked` unset, so the line runs for real on them too.
- The quote-page note (line 383) says the gate "counts the H1 as a heading". In the code I read (lines 1256 to 1276) the H1 is not in `heads`. Whether that is handled elsewhere: cannot tell. It does not change the help answer results above.

## (a) What the passing records do differently from the failing ones

The gate was run on every record; headings and fields were read with the gate's own functions (`extract_body`, `split_sections`, `read_fields`), so the counts match what the gate saw. "Newer format" means the record carries a `demand_evidence` field (107 records, all passing); "older format" is everything else (253 records).

| | Failing (212, all older format) | Passing, older format (41) | Passing, newer format (107) |
|---|---|---|---|
| Headings (H2) per record, median (range) | 3.0 (2 to 6) | 3 (2 to 5) | 6 (4 to 11) |
| Body words, median | 395.0 | 411 | 712 |
| Focus keyword length in words, mean (range) | 4.2 (2 to 6) | 3.0 (2 to 5) | 3.9 (2 to 7) |
| Headings containing the keyword verbatim | 0 headings: 212 | 1 heading: 40, 3 headings: 1 | 1 heading: 86, 2 headings: 17, 3 headings: 4 |
| Position of first heading that contains it | none | #1: 30, #2: 6, #3: 3, #4: 2 | #1: 59, #2: 8, #3: 11, #4: 10, #5: 11, #6: 3, #7: 2, #8: 1, #10: 2 |
| Headings ending in a question mark | 456 of 709 end in a question mark (64%) | 90 of 132 end in a question mark (68%) | 612 of 624 end in a question mark (98%) |
| Label-form headings (standards-file proxy) | 70 of 709 | 13 of 132 | 10 of 624 |
| Keyword is a substring of the post title | 82 | 12 | 68 |
| Most common opening words of headings | what 262, why 142, how 115, where 44, the 38 | what 44, why 23, how 12, achology 10, where 8 | what 164, where 103, how 74, is 63, does 32 |

What the table shows, as facts:

1. **The keyword sits in a heading in every passing record and in no failing one.** The passing records carry it verbatim in one heading (126 of 148 records) or in two or three (22 of 148). It is the whole keyword phrase, not its words spread across headings.
2. **Heading count rises with passing.** Records with 2 to 4 headings: 51 of 253 pass. Records with 5 or more: 97 of 107 pass. (All 107 newer-format records have 4 or more.)
3. **Keyword length.** Keywords of 2 or 3 words: 80 of 111 records pass. Keywords of 4 to 7 words: 68 of 249 pass. Failing keywords average 4.2 words, passing older-format ones 3.0, passing newer-format ones 3.9.
4. **Question-style headings.** Both groups use question headings heavily (91%, 90% and 99% of headings by the standards-file proxy). The newer records are nearly all real questions (98% end in a question mark against 64% of the failing records' headings, which include many label-form headings: 70 of 709). The question openers that carry the keyword in the passing newer records are what (25), how (19), "So," (17), is (16), can (13), where (13), which (8), are (4).
5. **Near misses among the failing.** Counting only content words, the best single heading covers on average 0.23 of the keyword's content words; 84 failing records share none, 41 share half or more, and 2 (`how-much-does-achology-cost`, `what-is-applied-psychology-achology`) have every content word in one heading but not the phrase.
6. **Records say it was placed on purpose in some.** Three records (`achology-teaching-philosophy`, `where-can-i-learn-about-albert-ellis`, `where-can-i-learn-skilled-helper`) note that the keyword was placed "in the first paragraph and one subheading" in the S380 and S381 rewrites. The other records say nothing about it; whether the other passing headings were written to the rule or happen to contain it: cannot tell.
7. **Older versus newer notes.** 106 of the 107 newer records carry an "Open before this record is called ready" section and 105 the "three next questions" block (rule 6), with S386, S388 and S391 notes. Of the 212 failing, 177 carry a `corrected_S361`, `S366` or `S369` note, and 2 carry the open-before section.
8. **Other lines on the failing records.** Only 27 of the 212 fail this line and nothing else. Elsewhere on them: keyword in address slug fails 147, keyword density 38, reading ease 30, contractions 28, keyword in first 10% of body 23. Whole-gate verdict across all 360: 133 pass, 227 fail.

By help category (passing of total): comparisons-and-alternatives 54/68, curriculum-and-subjects 27/34, certificates-cpd-accreditation 19/41, getting-started 13/20, achology-basics-and-identity 8/36, outcomes-and-expectations 7/22, pricing-and-payments 5/13, membership-and-access 4/11, events-and-mentorship 3/32, technical-help 3/19, privacy-and-legal 3/18, learning-experience 1/15, refunds-and-billing 1/10, community-and-conduct 0/16, partnerships-and-press 0/5.

## (b) Does the rule as written fit the help answer shape?

Stated as facts, in the order they bear on it:

1. **The shape does not make the line impossible.** The two types that are stood down are stood down because their headings are fixed words that cannot carry a keyword. Help answer headings are free-form questions (`sections: {}`, `headings_locked: false`), and 148 records, including every newer-format one, carry the keyword verbatim in a heading while still being questions.
2. **The line is a literal substring test on body headings only.** It does not read the post title or the H1, although in 82 of the 212 failing records the keyword is a substring of the title (for example `how-much-does-achology-cost`: keyword "achology cost", title "How much does Achology cost?", five question headings, none containing "achology cost"). It gives no partial credit: two failing records have every content word of the keyword in one heading but not the phrase itself (`how-much-does-achology-cost`, `what-is-applied-psychology-achology`).
3. **The shape asks for the keyword elsewhere and the line asks for it in a heading too.** The help answer standard puts the keyword in the first paragraph (the reader's question restated with the answer), and the shared checks also require it in the title, description, slug, first tenth of the body and a density band. Whether a further, heading-level repetition suits an answer whose headings are the reader's next questions: cannot tell from the records. I found no ruling on this line for help answers in the help-answer entry of the standards file or in the 360 records (the word "subheading" appears in three records and in the book note and quote page notes only); the rulings found are S335 (book note) and S356 and S388 (quote page). DSRD 2 section 2.24 and the help-answer skill were not read for this report.
4. **The approved exemplar fails it.** `HELP__what-is-achology.md`, approved by Kain in full at S356 and named in the standard as the exemplar that is read first where the standard and the exemplar disagree, fails this line, along with five other lines.
5. **Where the failing records sit.** All 212 are older-format records; none of the 107 newer-format records fails. 177 of the 212 carry notes of corrections at S361, S366 or S369. Whether they are owed a rewrite to the newer shape is for Chat and Kain to say, not shown by the records.
6. **What would change under the alternatives** is not asked here and is not stated.

## (c) Three failing and three passing records, with their headings

### Failing

**`what-is-achology`** (FAIL, older format, 494 words). Keyword: "what exactly is achology". Post title: "What is Achology?". 5 headings read. The approved exemplar. Five other lines also fail on it.

- What does Achology teach?
- How does learning at Achology work?
- Who is Achology for?
- How much does Achology cost?
- Is Achology a registered provider?

**`how-much-does-achology-cost`** (FAIL, older format, 505 words). Keyword: "achology cost". Post title: "How much does Achology cost?". 5 headings read. Keyword is inside the title but not in any heading; five headings, all questions.

- How much do individual courses cost?
- How much do school bundles cost?
- What does the Access All Areas Pass cost?
- How much does Achology Membership cost?
- Which option should I choose?

**`explain-achology-qualifications-to-clients`** (FAIL, older format, 487 words). Keyword: "explain achology qualifications to clients". Post title: "How do I explain Achology qualifications to clients who ask?". 4 headings read. The only line failing on this record. Four headings, none with the keyword; the keyword is a five-word phrase.

- What does a good answer sound like?
- Why brevity is the credible register
- What the question is usually really asking
- What if a client wants to verify my qualification?

### Passing

**`best-cbt-course-or-certification`** (PASS, newer format, 778 words). Keyword: "best cbt course or certification". Post title: "What makes a good CBT course, and how do you choose one?". 5 headings read. Newer format. The keyword is in the fourth heading.

- What's the Best CBT Course If You're Already a Clinician?
- What's the Best CBT Course If You Just Want a Cheap Taste of the Ideas?
- What's the Best CBT Course If You Want to Actually Use CBT Yourself?
- So, What Is the Best CBT Course or Certification, Really?  **← contains the keyword**
- Where Can You Start With Achology?

**`life-coaching-as-a-career`** (PASS, newer format, 687 words). Keyword: "life coaching as a career". Post title: "Is life coaching a good career, and can it be a real job?". 6 headings read. Newer format, passes every line. The keyword is in the first heading.

- Do people really make a living from life coaching as a career?  **← contains the keyword**
- What do life coaches charge, and is that the same as earning a living?
- Can it work as a career if anyone can use the title?
- What kind of person does it suit?
- Is there a low-risk way to test whether coaching suits you?
- Where would you start with Achology?

**`achology-skill-development-workshops`** (PASS, older format, 403 words). Keyword: "skill development workshops at achology". Post title: "What are Skill Development Workshops at Achology?". 4 headings read. Older format. The keyword is in the last heading, which is label-form (no question mark, opens with a skill name); the record also fails three other lines.

- What happens in a session
- How it differs from the discussion formats
- Why the mild pressure is the point
- Skill Development Workshops At Achology: Attending And Credit  **← contains the keyword**

## Method and limits

- The gate was run once per record with `python3 content_gate.py <record> help-answer`; it only reads. Headings and fields were read by importing the same functions. Scripts: `cloud-reports/job11-method/` (`an.py` reads, `gen11.py` writes this file).
- Counts are of the 360 `HELP__*.md` files at `main` `1e91422`. "Newer format" is defined by the presence of a `demand_evidence` field, which the failing records all lack; it is a convenient marker, not a statement of when or by whom a record was rewritten.
- "Label-form" and "question" figures use the standards file's proxy for a label, which the gate itself does not enforce.
