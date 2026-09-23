> **CHAT DISPOSITION, S380: ACTED ON AND ARCHIVED.** Kain approved extending the checks; `BRIEF__Widen_The_Voice_Checks_To_Catch_About_A_Piece_Of_Writing_S380.md` in FROM Chat. No board card moved.

# ANSWER: which article types the voice checks cover, and what they look for

**From:** Claude Code, S131 (factory session), Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** `ASK__Does_The_Self_Description_Check_Run_On_Every_Article_Type_S380.md` (head-lined DONE). Read from `content_gate.py` this session; nothing changed.

## 1. Which types `voice_checks()` runs on

`VOICE_TYPES` in `content_gate.py`: instructor-article, instructor-article-nlp-frame-s363, knowledge-derived-article, field-authority-article, book-derived-article, hub-question-article, hub-guide.

| type | covered |
|---|---|
| field-authority article | yes |
| book-derived article | yes |
| knowledge-derived article | yes |
| instructor article | yes (both keys) |
| quote page | no |
| help answer | no |
| author biography | no |
| book note | no |
| workbook | no |
| workbook landing page | no (the gate has no entry for this type at all) |

## 2. Fail or count on a published record

Two of the seven lines are counted, not failed, on a published record: "no paragraph describing the article" and "opens speaking to the reader". Decided in code: the record's `post_status` reads `publish` and it does not carry `voice_standard: s130`. Anything unpublished, or published and marked `voice_standard: s130`, fails them. The other five lines always fail: the three source-person lines, "first heading does not repeat the title" (counted only on hub-question-article, per Chat S379), and "meta description opens on the answer". No record carries `voice_standard: s130` today, so all published records of the covered types are counted on those two lines, the 38 rewrites included; Code ran those 38 strict by reading them as unpublished.

## 3. What the lines look for

- **Self-description** ("no paragraph describing the article"): any body paragraph matching `This piece`, `This article`, `In this piece`, `In this article`, `It then moves / turns / looks`, or `It closes with`. Case-sensitive on the capital T and I. It does not catch "this post", "What follows", "By the end", "Along the way", or lower-case "this piece" mid-sentence (Code's S131 search found live cases of each).
- **Source person narrated**: `{full name or first name},? {verb}` anywhere in the body, not only the opening, with the verbs writes, wrote, notes, noted, adds, added, says, said, explains, explained, argues, argued, describes, described, recalls, recalled, observes, observed, puts it, points out, tells. So "Kain says" and "Kain explains" are caught anywhere. **But it runs only where `reviewed_by` names a person in the theme's people list who is not the byline.** On a record Kain signs himself, or with no such reviewer, none of the three person lines run. "he writes" and "she writes" are never caught, since no name is in them.
- **Source person named at most once**, and **no reference to the source post** (`Kain's post / blog post / blog / article / writing`), under the same condition.

## 4. What covering more would take (estimate only)

- **Adding a type to `VOICE_TYPES`** is one line per type, plus its acceptance cases. The opening line ("speaks to the reader") would then apply too, which may not suit every type: a quote page opens on its quote, a help answer on the reader's own question, which already passes. Chat to say which lines each new type takes; about an hour of Code's time with cases for five types.
- **Widening the self-description phrases** to the S379 list (this post, What follows, It closes with, By the end, Along the way, lower-case forms) is a change to one pattern plus cases; "By the end" and "Along the way" are ordinary English and would flag correct sentences (the S131 search shows several), so they are better left to the reader's eye than to a fail.
- **Catching narration without a reviewer** (a writer reporting what someone else wrote on a record with no `reviewed_by`, or "he writes") needs the names to come from somewhere else, for example a `source_person` field on the record if Chat adds one. Without a named person the check can only match pronoun forms, which would fail every book note and many honest sentences.
- Book notes carved out as Chat proposes: they are not in `VOICE_TYPES` now and nothing above adds them.

## OWED BACK

Nothing.

*No em or en dashes in this file; checked before writing.*
