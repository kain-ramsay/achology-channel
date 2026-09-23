> DISPOSITION, Chat S370: STAYS. Waits on Code: the help-answer single-sentence check in `content_gate.py`, and the re-measurement counts. One fact closes it, Code's confirmation that the check is live and the counts are filed.

> **CHAT DISPOSITION, S382: ACTED ON, archived.** Code confirmed the check is live (`SHIP__Inbox_Work_Part_2_S131.md`, job 1: acceptance 137 of 137, then corrected to 149 of 149 once list items stopped being miscounted as lone-sentence paragraphs) and filed the re-measurement counts (246 records read, corrected count 46 of 279 carrying at least one one-sentence paragraph). The waiting fact has landed. No further action; counts sit in the SHIP file for reference.

BRIEF, from Cowork, S361

TO: Code

Kain's ruling this session, verbatim: "Placing one abrupt sentence as a paragraph is not acceptable anywhere on the site Claude. Period. Write to human beings, and never to appease a machine." This supersedes the old S299 rhythm-device allowance and its S357 ration of one short paragraph per section, on every content type, no exception standing.

DSRD 2 (section 2.24 item 2, and the paragraph floor passage in section 3.0) is updated to record this. content_gate_standards.json is updated: the shared short_paragraph_allowance_per_section is now 0, which fails the existing once_per_section logic in content_gate.py on the FIRST short paragraph in a section rather than the second. That half needs no code change; the existing mechanism already handles a zero allowance correctly.

The one half that does need a code change: the help-answer type. content_gate.py's ctype == "help-answer" branch is hard-excluded from the paragraph-rhythm check entirely and only tests paragraph_words_max / paragraph_sentences_max (the S356 ceiling). That ceiling check does not fail a paragraph for being exactly one sentence, so a help answer can still pass gate-clean with single-sentence paragraphs throughout. Please add a single-sentence check to that branch: any paragraph in a help-answer body with exactly one sentence is now a fail, same as everywhere else, alongside the existing ceiling check (unchanged).

Once that's in, please re-run the gate across: the 250 live help articles, and the 25 batch-one records Cowork is holding in Content Records/help-answer/ (5 of which are already rewritten clean by hand; the other 20 are the old mechanically-split drafts and will very likely fail this new line). Report counts, worst first, the same shape as the S357 re-measurement this session.

This also functions as the retroactive audit Kain's ruling implies: once the shared gate's zero-allowance and the help-answer single-sentence check are both live, re-running the existing gate across the already-published quote pages, book notes and instructor articles that relied on the old one-per-section allowance will surface every breach automatically. No separate audit tool is needed; the existing measurement pass does this by design once the JSON and code agree.

OWED BACK: the help-answer code change, and the re-measurement counts (live 250 + the 25 batch-one records), worst first.
