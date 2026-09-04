# 220 help answers: keyword fixed, GATE not run (no local script for this type) — CSV ready for import

`CORRECTED__220_Help_Answers_S338.csv`, sibling to this file, 220 rows: id, slug, post_title, old_keyword, new_keyword, new_seo_title, new_seo_description, new_body_html.

**Root cause confirmed.** All 220 were drafted with the Rank Math focus keyword set to the entire question (median 9 words, max 14). Only 5 of 220 already had a keyword short enough to fit an SEO title window. This is the exact defect rank-math-90's S337 correction describes; it just hadn't reached the 220 before now.

**What was done.** Ten parallel drafting passes (22 rows each), each picking a short, natural 2-6 word phrase from the real question (not a mechanical stopword strip), rewriting the SEO title and description around it, and lightly editing the body: keyword verbatim in the opening sentence, density tuned to 1.0-1.5%, no paragraph over 120 words, no em/en dashes, no first-person narration, "member of Achology" preserved, all existing links and HTML left untouched.

**Independently re-verified, not trusted on the drafting passes' own report.** Ran my own mechanical check against all 220 rows (title/description window and length, keyword verbatim in first 10% of body, density band, paragraph length, dashes, "Achology member" phrasing, first-person). First pass found 17 rows over the 120-word paragraph line and found 2 rows under the density band; the paragraph flags turned out to be a bug in my own checker (it was measuring `<ul><li>` list content as one block, not real prose paragraphs) rather than real defects, corrected and re-run. The two real density misses (rows 323, 326) were fixed directly. Final result: all 220 rows clean against every check above.

**One honest gap, not closed here.** There is no content_gate.py entry for the help-answer type (content_gate_standards.json lists it "NOT entered"), and this type's real gate is `article_gate.py`, which runs on Code's side at import. So this batch was verified against the documented rank-math-90 and help-answer criteria by a script I wrote myself, not against an executable gate Cowork owns for this type. Final say on whether these 220 actually clear Rank Math 90+ is Code's, read off the install after import, same as the established Part A / Part B split.

**Nothing here changes the article's facts, claims, or links.** Every edit was keyword placement and paragraph mechanics only.

Ready for the two-importer route once that lands, or whatever update mechanism you use for editing content on live posts that already exist (these are edits to live pages, not new imports).
