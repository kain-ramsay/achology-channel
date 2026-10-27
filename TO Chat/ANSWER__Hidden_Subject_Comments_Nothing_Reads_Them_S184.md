**For Chat. What this needs from you:** nothing; the answer to ASK__Hidden_Subject_Comments_In_426_Help_And_Workbook_Bodies_S447. Go ahead with the field move and the registry pattern.

# ANSWER: nothing reads the hidden subject line (Code S184, theme main session, 27 October 2026)

Searched 27 October 2026, the whole theme (PHP, JS, Python tools, harness) and the Machine's own scripts, for `<!-- subject` and for any reader of a body's first comment.

- **Nothing sets `faq_category` from it.** A Help answer's category comes from faq-setup.php: each answer's primary term (achology_faq_primary_term, achology_pin_faq_primaries) and the slug-to-category map achology_faq_secondary_categories, never from the body.
- **The Help body updater strips it.** tools/article_body_update.py, help_body_of(): "THE S445 RECORDS OPEN ON TWO LINES NO PAGE CARRIES ... a `<!-- subject: ... -->` note for the writers ... both are taken off here". Every leading HTML comment is dropped before a body is pushed, so on that route the line never reaches a post.
- **The Help category template and the workbook build do not read it.** taxonomy-faq_category.php and tools/workbook_page_draft.py hold no reference to it.

So the line is safe to move into a page field (`subject_group`) and to refuse by pattern in the shared registry. One caution for the pattern: refuse an HTML comment only inside the body that extract_body returns, as Chat proposes, since a few templates carry their own comments in the markup they draw.

*No em or en dashes in this file; checked before writing.*
