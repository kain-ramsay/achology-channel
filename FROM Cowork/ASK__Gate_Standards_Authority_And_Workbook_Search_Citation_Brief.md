# ASK: which content_gate_standards.json copy is authoritative, and does a workbook owe its own Search and Citation Brief

**DOCUMENT TYPE:** ASK, from Claude Cowork. **Date:** 7 September 2026.
**Surfaced while:** answering Kain's question on expanding each workbook's teaching section by 400 to 450 words.
**Read this cold.**

---

## What is true now, checked this turn

Two copies of `content_gate_standards.json` are both current-looking, in different folders, and materially different:

- `Educational Publishing System / Files for Chat from Code / content_gate_standards.json`, 24KB, last touched 1 September. This is the copy last session's workbook gate run used.
- `Achology Website Upgrade 2026 / 04. Content Production Factory + COWORK / content_gate_standards.json`, 42KB, last touched 6 September, sitting beside `content_gate.py` (77KB, touched today) and this project's own live harness documents (`000__COWORK_PRODUCTION_HARNESS.md`, `000__THE_PUBLISH_READY_PIPELINE.md`, `000__THE_SEARCH_AND_CITATION_BRIEF.md`) and every one of Cowork's own batch reports going back to August.

The second one is the live one. It sits in Cowork's own working folder, it is the newer and much larger file, and its own `_types_still_to_enter` list names only `buyer-intent-answer` and `help-answer` as not yet entered, confirming `workbook` is a finished, current entry there, not a stale placeholder.

Re-run against the real copy, `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` now reads:

```
CONTENT GATE  |  workbook  |  DRAFT__The_Karpman_Drama_Triangle_Workbook.md

  PASS  total body words                               1352 (standard 1100 to 1900)
  PASS  headed sections, counted not named             4 found (standard 4)
  PASS  paragraphs of 2 to 4 sentences                 all within
  ..    one-sentence paragraphs                        13 of 39, allowed (Kain, S299)
  PASS  no em or en dashes                             0 found
  PASS  banned brand words                             none
  PASS  machine-written tells                          none
  PASS  reading ease (Flesch, approximate)             61.5 (band 60 to 70)
  FAIL  required fields present (22)                   11 missing: landing_page_body, whats_inside, rm_focus_keyword,
                                                         rm_seo_title, rm_seo_description, demand_evidence, search_intent,
                                                         reviewed_by, update_cadence, query_variants, schema_type
  FAIL  every tag is one of the 36 locked slugs        1 outside the register: To be confirmed at commission
  FAIL  outcome or problem tags, 2 to 4                 0 found
  PASS  lead_tag is one of the record's own tags
  FAIL  author is a key the people registry holds       Base voice, no pen name; assigned at commission...
  FAIL  focus keyword set                               missing
  PASS  no process text in the body                     clean
  PASS  internal link present                           1 found
  FAIL  external link to the source present              0 found
  PASS  no paragraph over 120 words                     all within
  FAIL  stage 0 demand evidence recorded
  FAIL  landing page body present

  GATE: FAIL (8)
```

Every check on the drafted prose itself still passes clean: word count, section count, paragraph shape, no dashes, no banned words, no machine tells, reading ease. Nothing about the writing changed. What changed is the metadata bar underneath it: the live copy checks 22 required fields, not 17, and adds three checks last session's copy never ran at all: tags against the 36-slug locked register, 2 to 4 outcome or problem tags, and the author against a people registry of real keys. All eight fresh failures are the placeholder text this session deliberately left as "to be confirmed at commission," per the brief's own scope, now failing checks that did not exist in the copy I ran against. Nothing here says the drafted words are wrong.

The five new required fields (`search_intent`, `reviewed_by`, `update_cadence`, `query_variants`, `schema_type`) belong to a second, newer mechanism: the Search and Citation Brief, ruled S329 to S332, which `rank-math-90`'s own Part A step 1 says every content-type skill runs before drafting starts. Run cold against the draft:

```
PRE-DRAFT GATE: FAIL (9)
  FAIL  1. stage 0 demand evidence recorded
  FAIL  2. the three metadata fields present            missing: rm_focus_keyword, rm_seo_title, rm_seo_description
  FAIL  3. keyword claimed in the register
  PASS  4. no body yet                                  WARNING: 1352 words already written
  FAIL  5a. the Search and Citation Brief section is present   no such heading in the file
  FAIL  5e. search_intent / update_cadence / query_variants / reviewed_by / schema_type   all empty
```

This step was not run before drafting. It is not in the `workbook-creation` skill's own ordered steps (which route to `rank-math-90` for the keyword and the three Rank Math fields, but do not name the Search and Citation Brief), even though `rank-math-90` itself says the brief step is universal, and the standards file's own `_update_cadence_by_type` block names `workbook: annual`, meaning the type is meant to carry one.

## What this is, and is not

This is not a defect in the drafted Karpman workbook's words. Every quality check on the prose passed both times, against both copies. It is two things: last session's gate run was against a stale copy sitting in the wrong folder, so the "GATE: FAIL (5), every failure traces to two named causes" line in the delivered report undercounts the real gap; and there is a real, unresolved question of whether a workbook record is meant to carry its own Search and Citation Brief, separately from the landing page, which nothing in `workbook-creation`'s own steps currently sends a drafter to do.

## What is not this session's to decide

Whether the workbook type owes its own Search and Citation Brief, distinct from the landing page's fields, is a reading of `rank-math-90` against `workbook-creation` that the two skills do not currently agree on cleanly, and it is not this session's call to settle alone. Nor is which copy of `content_gate_standards.json` the Educational Publishing System side should be pointed at, or whether the stale EPS copy should be deleted, refreshed, or left as a dated snapshot on purpose.

---

OWED BACK: which copy of the standards file is authoritative going forward (this ASK treats the Content Production Factory + COWORK copy as live from here on, and will keep doing so unless corrected); and whether a workbook drafts its own Search and Citation Brief before the teaching is written, per `rank-math-90`, or is exempted the way the six landing-page fields are. To TO Cowork.

*No em or en dashes in this file; checked before writing.*
