# BRIEF: the pre-draft gate, a gate type for the two new content types, and the stale density note

**From:** Claude Chat, Session 327. **Date:** 1 September 2026.
**Authority:** Kain, in session, on Chat's recommendation: "Yes, that sounds good, please go ahead."
**Filed under:** an approved brief. Build all three parts; report through TO Chat with the acceptance printout. This is a factory-tooling brief, not a page, so no PAGE GATE line applies.

---

## Context, so this file stands alone

The order our standard sets for every Knowledge Hub piece is metadata first, copy second: `rank-math-90` Part A steps 1 to 3 prove the question, claim the keyword in `KEYWORD_REGISTER.csv`, and set `rm_focus_keyword`, `rm_seo_title` and `rm_seo_description` in the record before a body exists. Since S315 the content gate refuses a record missing those fields and `demand_evidence`. That check runs at the end of drafting, when a body already exists. Nothing structural prevents the body being written first; the failure is caught afterwards, when the fix is a rewrite. Kain asked today what actually enforces the order and ruled that a machine check should run before drafting, the way the inbox wall checks a disposition line before a close.

## Part 1: the pre-draft gate

Extend `content_gate.py` with a mode that checks a record before any body exists. Suggested invocation, yours to shape: `python3 content_gate.py --pre-draft [record-file] [article-type]`.

It passes only when all four hold, and reports each line:

1. `demand_evidence` is present and non-empty.
2. `rm_focus_keyword`, `rm_seo_title` and `rm_seo_description` are present, and the three field-level rules `rank-math-90` step 3 states hold: keyword inside the SEO title's first 50 characters, title under 60; keyword inside the description's first 120 characters, description under 155; the address slug carries the keyword.
3. The keyword has a row in `KEYWORD_REGISTER.csv`, and that row's `record_slug` and `address` match the record. A missing row fails; a mismatched row fails and names both values. This is the check that catches a stale register before it is found at import.
4. The record has no body yet, or the body is empty. A pre-draft check on a record that already carries a body passes with a warning line saying so, because the check is still worth running but the order has already been lost.

It runs nothing else: none of the body checks, sections, density or links. A mode that reports on absent things must not fail on their absence.

**Exception, by ruling (S327):** for `article_type: video-derived` records, the knowledge-derived article, the pre-draft gate is run after the draft and before the finish, because that type fixes its teaching first and takes its title and keyword afterwards (DSRD 2 section 3.5; the Educational Publishing System PRD guardrail 3). Check 4 therefore passes silently for that type when a body is present. Read the type from the record; do not special-case by filename.

## Part 2: gate entries for the two new content types

`content_gate_standards.json` has no type for either of these. Add both, reading the standards from their owning sections this turn rather than from this brief:

- **The knowledge-derived article**, key `knowledge-derived-article`, record `article_type: video-derived`. Shape and bands from DSRD 2 section 3.5, written out today: eight parts, around 1,500 words graded to the teaching, the illustration section optional. Required fields as the instructor-article type plus `source_video_id`. The two S327 checks worth a line each: the focus keyword appears in the first paragraph, and a `source_line` or closing italic paragraph is present.
- **The workbook landing page body.** It travels in the workbook record's `landing_page_body` field, so add checks to the existing `workbook` type rather than a new type: the body is 750 to 900 words with no tolerance, per Kain's S323 ruling recorded at DSRD 2 section 1.7 and written as a template at section 3.4.2 today; two H2s present; the workbook page's `rm_focus_keyword` differs from the companion article's and appears in the register on no other row; the page title is not the companion article's title. The article's title and keyword come from `related_article_slugs` via the register.

Where a value in this brief and the DSRD 2 section disagree, the section wins and you tell me.

## Part 3: the stale density note

`content_gate_standards.json`'s `_seo_finish_source` note still says the density band spans 1.5 to 1.8 and 1 to 1.5 "until Code re-measures". You re-measured at S318 and DSRD 6 section 5 item 11 was corrected to 1.0 to 1.5. Correct the note to the settled band and the settled source. Read the enforced band in the code while you are there and confirm it is 1.0 to 1.5.

## Acceptance

The pattern every gate in this system is proved by: show it refusing. For Part 1, one printout of a record with no register row failing check 3, one of a record with a mismatched address failing check 3 naming both values, one of a clean record passing all four, and one of a `video-derived` record with a body passing check 4 silently. For Part 2, one printout of each new type failing on a real fault and passing on the exhibit: exhibit 02 for the article, exhibit 04's body for the landing page, both in the Educational Publishing System's worked example folder. For Part 3, the corrected note quoted.

## What is asked of Code

1. Build the three parts and report the acceptance printouts to TO Chat.
2. Name the invocation you chose for the pre-draft mode, so the Cowork harness and the Educational Publishing System PRD can carry it verbatim.

OWED BACK: items 1 and 2. Not blocking: Cowork's redraft of the eighteen instructor articles starts on the existing gate today, and the pre-draft mode is retro-run on those eighteen records when it lands.

*No em or en dashes in this file; checked before writing.*
