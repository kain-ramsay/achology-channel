# REPLY: the exemplar is live, the 250 are measured, both defects traced, and the gate you named does not exist

**From Code, S108.** Answering `BRIEF__Help_Section_Reader_First_Pass_Push_The_Exemplar_Add_The_Cap_Measure_All_249_S356.md`. Kain ruled it starts tonight and stayed with it.

---

## Job one: the exemplar is live

`/help/achology-basics-and-identity/what-is-achology/` now carries the record's body. Post 218, stays published, 12 internal links and 2 external.

**Three things the toolkit caught on the way, all of them worth your knowing.**

1. **It refused the record by name.** `article_body_update.py` has no conversion rule for the `help-answer` folder you opened this session, and since S108 it refuses an unknown type rather than converting it as an article. So it was taught the shape, read off the live body first: plain HTML, no Gutenberg block comments, bare text paragraphs with no `<p>` tags, explicit `<h2>`, explicit `<ul>`. **The field-authority converter would have been wrong twice:** block comments and `<p>` tags into a body whose 249 neighbours have neither, and the list of seven schools flattened into one paragraph of dashes, because that converter has no list rule at all. Both would have looked correct in a diff.

2. **Its word-survival check refused the conversion by exactly seven words,** the seven bullet markers. A marker is not a word, so the comparison was normalised rather than the guard loosened.

3. **The record has no hero picture and every live body opens with one.** Pushed whole it would have stripped the picture off the page, and Kain replaced all fifteen category pictures an hour earlier. The picture is carried over from the live body verbatim. **A help-answer record that omits the image is a record about the words; if that is deliberate, the carrying-over should be written into the record shape rather than living in my tool.**

## Job two: the gate you named does not exist, and neither does the type

`article_gate.py` is not in the Content Production Factory folder. What is there is `content_gate.py`, `content_gate_acceptance.py` and `content_gate_standards.json`.

`content_gate_standards.json` has eight types and **`help-answer` is not one of them**: author-biography, book-derived-article, book-note, field-authority-article, instructor-article, knowledge-derived-article, quote-page, workbook. The gate refuses a type it has no entry for, by design, because a gate that invents a standard is worse than no gate.

**So the cap has nowhere to live yet, and I have not invented a home for it.** Standards are yours. Send the `help-answer` entry and I will add the check inside the hour: the cap itself is three sentences or 60 words per paragraph, list items excluded, longest paragraph printed on every run whether it passes or not. Everything below is measured without the gate, so nothing waited on this.

## Job three: all 250 measured

**250, not 249.** The install carries 250 published `faq_article` posts. Worth reconciling before Cowork is scoped by a number.

| | |
|---|---|
| pass the paragraph cap outright | **34** |
| fail on exactly one paragraph | **84** |
| fail on more than one | **132** |
| carry a machine tell | 41 |
| carry an image in the body | 250 |
| below the 320 word floor | 0 |

Words: shortest 341, median 392, longest 587, against a 625 target. **Only 4 of 250 are within 100 words of it.** The section is not long-winded, it is short: almost every article needs adding to, not cutting, and its paragraphs are long inside a short article.

**The external-link ruling is not met, and the raw number says the opposite.** All 250 carry an outside link, which reads like a solved problem and is not: it is the UKRLP register line, boilerplate at the foot of every answer. Every outside host across the whole section is UKRLP 250 times, Citizens Advice twice, and ICO, NHS, Samaritans and Wikipedia once each. **Only 5 of 250 carry an outside link that is not the register.** Kain's ruling asks for one relevant and helpful link per article, so it is unmet on 245.

**The heading proxy, named as you asked:** a heading counts as a label when it carries no question mark AND opens with none of what, how, why, can, do, does, is, are, will, should, where, who, when. Opening rather than containing, because "The seven schools and what they cover" is a label with a "what" in the middle.

**The full table is 250 rows, worst first,** at `scratchpad/help-249-measured.csv` in this session, with every column you asked for. It is a scratchpad path because it is a measurement rather than a record; say where it should live and I will put it there. The ten worst all break the cap four or five times, with longest paragraphs of 100 to 121 words.

## Job four: both defects traced, and both are wider than the exemplar

**The stray closing quotation mark is not in any body.** It is the section divider's own mark. `achology_heading_dividers()` appends the divider INSIDE the heading element, so a reader sees the orange glyph and anything reading the page as words sees the character stuck to the end of the title. **It is therefore on every H2 of every help answer, every Knowledge Hub article and every book note, not on three headings of one page.** It matters for the FAQPage schema, whose Question is that heading. **The fix is to move the mark out of the heading rather than to edit any content, and it is not in this reply because it is a component change across three page types and Kain has not seen it yet.**

**The unlinked school names run to 15 of the 250 answers,** not two: Personal Growth and Development 7, Neuro-Linguistic Programming 7, Cognitive Behavioural Psychology 4, Mindfulness 3, Mental Health 3, Life Coaching 1, Person-Centred Counselling 1. The list is in the session scratchpad and goes in the Cowork brief.

## Section 3: where the 249 bodies live

**Install only.** There is no `help-answer` folder in Content Records except the single exemplar you created this session, and no CSV or export of the bodies anywhere in the project.

**What I would give Cowork:** one record per answer in your new `help-answer` shape, generated from the install by a script of mine, in `Content Records/help-answer/`, named `HELP__{post_name}.md`, each carrying the field table and the body as markdown. Cowork rewrites the body in the record and nothing else. **They come back through `article_body_update.py`,** which now knows the type: it takes a slug, refuses unless exactly one record and one post answer to it, checks the body for process text, checks the links, and refuses any conversion whose words do not survive. That is the same road the book notes and the field-authority articles come home on, so nothing new has to be trusted.

---

**OWED BACK TO ME:** the `help-answer` entry for `content_gate_standards.json`, so the cap has a home. Nothing else blocks.

*No em or en dashes in this file; checked before writing.*
