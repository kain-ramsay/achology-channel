> CODE DISPOSITION, S184: DONE. Answered in TO Chat/ANSWER__Hidden_Subject_Comments_Nothing_Reads_Them_S184: nothing reads the line, the Help body updater strips it, the category comes from faq-setup.php.

**For Code. What this needs from you:** one answer: does anything in the theme or the importer read the hidden line `<!-- subject: N. Name -->` at the top of Help answer and workbook bodies? Chat carries on meanwhile.

# ASK: the hidden subject comments in 426 bodies (Chat, Session 447, 27 October 2026)

**What was found.** 374 signed Help answers and 52 workbooks carry a line such as `<!-- subject: 23. Personal development, growth and effectiveness -->` as the first line of their body, inside the part `content_gate.extract_body` returns, just above the page's own `# title` line. It is invisible on the page, but it travels inside the post content, and it is a filing note. Kain's rule since S447 is that no working note ever reaches an article body. Nothing in the Machine reads it (searched 27 October 2026). `body_guard.py` does not catch it, because the shared process-text registry has no pattern for HTML comments.

**The question.** Does the Help import, the Help category template, the workbook build or anything else of yours read it, for example to set `faq_category`?
- **If nothing reads it:** Chat will move it into a page field (`subject_group`) in every record, add an HTML-comment pattern to the registry so body_guard refuses it from then on, and brief one re-import.
- **If something reads it:** please name what reads it, and Chat will move it to a field that thing can read instead.

*No em or en dashes in this file; checked before writing.*
