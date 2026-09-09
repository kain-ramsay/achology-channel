# BRIEF: the help section's reader-first pass. Push the exemplar, add the paragraph cap to the gate, measure all 249, fix two defects, and answer one question

**DOCUMENT TYPE:** brief, from Claude Chat, Session 356. **Date:** Wednesday 9 September 2026.
**Authority:** Kain, live in the S356 sitting. He read the live section, ruled that many of the 249 help articles read as machine-drafted, rewrote one with Chat as the exemplar and approved it in full, and approved the four-step process below. The standard is written into DSRD 2 section 2.24 (the reader-first shape) and the help-answer skill, rule 6, this session.
**Board card:** 250 help articles (3ab4da19af35819abb3fe712ae00438a).
**Read this cold.**

---

## 1. The standard, in one paragraph

A help article is finished when a first-time visitor leaves with fewer questions than they arrived with. The shape that makes it true: the answer in the first paragraph; no paragraph longer than three sentences or 60 words; every heading the reader's next question, never a label; a list where an answer has more than three parts; every unfamiliar term explained in one plain sentence where it first appears; written to "you", warmly, still institutional (no author, no first person). Facts stay on the page that owns them. The exemplar is `Content Records/help-answer/HELP__what-is-achology.md` (a new folder, opened this session; the record shape is in the file).

## 2. Four things asked of you, in this order

**One: push the exemplar to its live page.** `/help/achology-basics-and-identity/what-is-achology/`. The body in the record replaces the live body whole; the title, address, category, SEO title and description do not change. Run your gate on it before it goes; if a line fails, say which rather than editing the words, since Kain approved them.

**Two: add the paragraph cap to the help section's gate.** `article_gate.py` gains one check on the help-answer type: any paragraph over three sentences or over 60 words fails. List items are not paragraphs. Print the longest paragraph's words and sentence count on every run, the way `content_gate.py` prints paragraph words, so the number is visible even when it passes.

**Three: measure before anyone rewrites.** Run the gate with the new cap, plus the machine-tell list from `content_gate_standards.json` (`machine_tells_always`, which now carries "plainly"), across all 249 live help bodies as they are on the install today. Report one row per article: address, word count and its distance to 625, external links present (count), image in the body (yes or no), longest paragraph (words and sentences), number of paragraphs over the cap, headings that are labels rather than questions (a heading with no question mark and no "how" or "what" or "can" or "do" in it is a fair first proxy; name the proxy you use), machine tells found. Sort worst first. Give the counts at the top: how many pass the cap outright, how many fail on one paragraph, how many fail on more, how many already carry an external link. That list is what Cowork's correction pass is scoped to, so the section pays for the rewrites it needs and not for 249.

**Two rulings from the same sitting that change what the pass produces, so the measurement should show them:** Kain ruled 625 words as the target for every article the pass touches, with 320 staying the floor and nothing padded, and one relevant and helpful external link in every article. The S097 line that a help answer carries no external links by design is superseded. The exemplar carries two (the UKRLP register and a definition).

**Four: two defects on the live exemplar page, found by Chat on fetch today.** All three of its H2s end in a stray closing quotation mark ("What Achology teaches\u201d"). Find whether the body carries it or the render adds it, and whether any other help page shows the same. Two of the seven schools in it were named without a link (Mental Health; Personal Growth and Development); the exemplar body fixes that page, but check whether other help pages carry unlinked school names, since the linking rule (DSRD 1 section 6.4) is section-wide.

## 3. One question, read-only

**Where do the 249 help bodies live for editing?** Chat needs to know whether they exist as records on disk that Cowork can rewrite (a folder, a CSV, an export), or only on the install. This decides how the Cowork correction pass is fed. Name the path, or say "install only", in one line. If it is install only, say what export you would give Cowork and how the corrected bodies come back to you.

## 4. What comes back

One REPLY in TO Chat: the exemplar pushed (or the failing gate line), the cap in the gate, the 249-row measurement with its counts at the top, the two defects' cause and spread, and the one-line answer to section 3. The Cowork brief is written by Chat from your measurement and does not exist until it lands.

---

OWED BACK: that one REPLY. Nothing else.

*No em or en dashes in this file; checked before writing.*
