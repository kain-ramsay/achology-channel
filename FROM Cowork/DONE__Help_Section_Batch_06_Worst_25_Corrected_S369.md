DONE, from Cowork to Claude Chat, Session 369. Continues `BRIEF__The_Help_Section_Reader_First_Correction_Pass_216_Answers_Worst_First_25_Per_Batch_S362.md` (still in TO Cowork, runs across sittings). Batch 6 of the 216-answer worst-first pass.

# Help Section Batch 6: 25 Worst-First Answers Corrected

Before drafting, read `RULING__Every_Article_Is_Written_For_A_Human_Reader_First_The_Gates_Are_The_Floor_S362.md` in full (found sitting in TO Cowork, unread by Cowork until this batch) and applied it throughout: write the piece a human would write, then check it against the gates, never the reverse. Also continued manually enforcing the S361 single-sentence-paragraph ban, since `content_gate.py` still excludes help-answer from any sentence-count check (confirmed by direct read of the gate script this session — the S361 brief asking Code to add that check is still sitting unactioned in FROM Cowork, which is expected; that is Code's queue, not a Cowork blocker).

## Method

Computed the worst-first order from `MEASURED__All_250_Help_Answers_S117.csv` filtered to the 216 in-scope rows (`paragraphs_over_cap > 0`), subtracted the 125 slugs already done across batches 1–5, leaving 91 remaining. Took the next 25, worst-first, as batch 6.

Read all 25 source records in full, then dispatched five parallel drafting passes (five records each), each carrying the full DSRD 2 section 2.24 standard, the S362 human-first ruling verbatim, the S361 single-sentence-paragraph ban verbatim (with the S358 fixed-structure exception), and a per-file list of the issues I'd already spotted on my own first read, with explicit instruction to verify the whole file fresh rather than just patch that list. Every pass found genuine additional violations my own first pass had missed, mostly single-sentence "hook" one-liners sitting right after a heading, and a few paragraphs that hit 3 sentences but still ran over the 60-word ceiling.

I then rebuilt all 25 corrected files myself from the returned drafts, ran an automated check across all of them (paragraph sentence/word count, single-sentence-paragraph detection, "plainly" search, em/en-dash search, UKRLP-closer byte match, word-count floor), fixed nothing further because nothing failed, and pushed all 25 to the live records. Nine flags came back from the automated check; all nine were false positives I'd anticipated: the historical `measured_at_S117` line correctly still says "plainly" where that was the original flaw (it is the baseline record and is never edited, only appended to), and colon-terminated list-header lines ("Start with the document that owns your question:") tripped the single-sentence detector even though they're structural list intros, not orphaned prose. That list-header question is flagged below for your ruling since it recurred across five separate files.

## The 25 corrected, worst-first, with final word counts

1. `is-achology-global-platform` — 414 words
2. `achology-trust-legal-policies-work-together` — 397 words
3. `share-my-achology-account-login` — 373 words
4. `how-long-achology-operating` — 411 words
5. `will-clients-take-achology-certificate-seriously` — 383 words
6. `downloading-achology-content` — 392 words
7. `become-a-master-achologist` — 405 words
8. `is-achology-a-university` — 384 words
9. `prior-qualifications-needed-achology` — 405 words
10. `achology-course-required-attend-workshops` — 460 words
11. `achology-uk-register-learning-providers` — 401 words
12. `does-achology-supervise-peer-coaching` — 403 words
13. `mentorship-sessions-recorded-achology` — 406 words
14. `dimap-course-upgrade` — 406 words
15. `is-achology-content-scientific-or-ideological` — 415 words
16. `adult-to-adult-learning-no-hand-holding` — 454 words
17. `many-times-coach-same-person-cips` — 464 words
18. `there-free-achology-membership-include` — 453 words
19. `standards-apply-trainee-achologists` — 453 words
20. `offer-free-coaching-someone-outside-achology` — 488 words
21. `achology-s-five-community-principles` — 482 words
22. `achology-knowledge-hub` — 564 words
23. `host-own-achology-event` — 335 words
24. `difference-membership-courses-achology` — 350 words
25. `become-an-achology-affiliate` — 354 words

All 25 sit between the 320-word floor and the 625-word target, all now measure 0 paragraphs over cap, 0 label headings and 0 remaining machine tells (each file carries a new `corrected_S369` line under its original `measured_at_S117` line recording this). Every file's Page fields table and UKRLP closer sentence were left byte-for-byte untouched, verified programmatically, not just by eye.

## What the correction actually found

Three recurring patterns across nearly every file in this batch, none of them visible in the S117 measurement:

**A short one-sentence "hook" standing alone right after a heading.** This was the single most common violation: a punchy line like "That difference is the entire point of the activity." or "This is worth understanding rather than resenting." sitting by itself as its own paragraph, immediately followed by the paragraph that actually explains it. Nineteen of the 25 files had at least one of these; several had three or four. Fixed by merging into the neighbouring paragraph where that kept it under the word cap, or by giving the line a genuine second sentence where merging would have pushed the neighbour over cap.

**Two broken headings that were duplicates of the page's own title, dropped into the middle of the body.** `is-achology-global-platform` had "Achology A Global Learning Platform: What Membership Means For You" as a mid-body H2; `how-long-achology-operating` had "How Long Has Achology Been Operating? Two Dates And Why They Differ"; `is-achology-a-university` had the exact title "Is Achology A University Or Degree Provider?" repeated as an H2. All three read like a leftover from however these were first generated. Replaced each with a genuine, distinct question matching its own content.

**Dense lists running as prose instead of as lists.** `become-a-master-achologist`'s Level 5 requirements and annual maintenance section, `host-own-achology-event`'s five event types, `become-an-achology-affiliate`'s three banned promotional tactics, and a few others were each a single long sentence naming four or more things, joined by semicolons. Converted each into a proper list; this is also what brought several of the worst word-count overruns back under the 60-word paragraph cap without cutting any content.

Two files (`achology-uk-register-learning-providers`, `dimap-course-upgrade`, `adult-to-adult-learning-no-hand-holding`, `standards-apply-trainee-achologists`, `will-clients-take-achology-certificate-seriously`) had the actual "plainly" instance the S117 measurement flagged, always removed rather than swapped to "simply", except where a direct replacement read naturally (one case, "told plainly" to "told directly").

## One convention decision I made across the batch, flagging for your ruling

Several files use a colon-terminated line to introduce a bulleted list, e.g. "Start with the document that owns your question:" followed immediately by the list. Read alone, that line is mechanically a single sentence. I treated it as exempt from the single-sentence-paragraph ban, the same way the Related Questions block is exempt, on the reasoning that it's a structural list header rather than an orphaned prose one-liner, and it matches how lists are introduced elsewhere across the site. This wasn't in my brief to the drafting passes as a rule, but every one of the five independently made the same call, and my own automated QA flagged all five instances so I could look at them by eye before deciding to let them stand. If you'd rather these read as full sentences ("Start with the document that owns your question. Money sits in..." etc. as prose, or a colon-free lead-in folded into the surrounding paragraph), that's a small rewrite across roughly eight lines total and I can turn it around quickly. Otherwise, worth writing into DSRD 2 section 2.24 as the settled reading, since it will keep recurring.

## Facts flagged, not fixed, per the brief's instruction

- `achology-knowledge-hub.md` and three other files in this batch reference "the Achology Eldership" or "the Eldership team" without ever explaining what it is. It isn't one of the eight recurring terms DSRD 2.24 names (CIPS, PALS, VALTS, CCaC, ALTs, DiMAP, SoMAP, UKRLP), so I left it unglossed rather than invent an explanation, but it recurs often enough across the help section that it may belong on that list.
- `dimap-course-upgrade.md` opens with the bare abbreviation "DiMAP" before its full name is spelled out two sentences later, mirroring the page's own H1 and title fields. Other files in this batch (e.g. the UKRLP page) lead with the full name first. Left as is since it matches the established title, but flagging the inconsistency in case you want one rule applied everywhere.
- `how-long-achology-operating.md` needed one sentence of new framing text to fix a single-sentence-paragraph violation around the two published student-count figures (56,701 and 145,112, both unchanged): "Numbers like that are easy to state and just as easy to inflate, which is why each one sits on the page of the course it belongs to." This is editorial connective tissue, not a new claim, but it's the one addition across the whole batch that wasn't already implied by the surrounding sentences, so flagging it for your eye rather than presenting it as invisible.

No prices, dates, figures, event types, credit counts, or CPD requirement numbers were changed anywhere in this batch. Every external link and every internal link target is unchanged from the source records.

## Definition of done

All 25 corrected files written to their live locations in `Content Records/help-answer/`, each carrying its `corrected_S369` measurement line. This report filed to FROM Cowork. 66 of 91 help answers remain after this batch. Carrying straight into batch 7 next, per the brief's "runs across sittings without stopping" instruction, unless redirected.
