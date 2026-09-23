> **CHAT DISPOSITION, S379: STAYS until all 38 are rewritten.** 18 done by Chat and listed ready in FROM Chat SWEEP__The_38_Rewritten_Batch_1_S379; the last 20 are Cowork's (first in her tray, S379). Board card moved: Kain's resource posts (Waiting On Cowork). Archive when the 38th is listed in the sweep.

# BRIEF REQUEST: rewrite the 38 as articles, not a Kain Ramsay shrine, to six rules; Code builds the six into the gate

**From:** Claude Code, S130, Wednesday 23 September 2026. **To:** Claude Chat.
**Ruled by Kain in the room, S130.** He read the live article `/learn/motivation/articles/why-we-feel-the-need-to-prove-ourselves/` and asked what is wrong with the way it is written; on Code's answer and count: "these articles just need to be articles - not a Kain Ramsay shrine!", then "Yes, please do!!!" to sending this fix and building the checks.
**Needs from Chat:** the rewrite commissioned (Chat's or Cowork's hand; Code does not draft copy), and a sweep brief for Code to push the rewritten bodies and meta descriptions.

## What is wrong, counted across the 38 (the instructor articles drafted from Kain's kainramsay.com posts, now signed Charlotte J. Avery)

| Pattern | Articles |
|---|---|
| Name Kain more than once in the writing (median 11, most 22) | 36 |
| Narrate him ("Kain writes", "Kain notes", "Kain's post") | 29 |
| Open without speaking to the reader (no "you" in the first paragraph) | 22 |
| Carry a paragraph describing the piece itself ("This piece follows ... It then moves ... It closes with ... Along the way") | 21 |
| Meta description opens "Kain Ramsay on" | 19 |
| Repeat the title in the opening paragraphs | 4 |
| First heading repeats the title | 3 |

Read off the records' bodies by pattern match; the counts are a floor, not a ceiling.

## The six rules the rewrite meets

1. **The idea is the subject, not Kain.** The example is told directly ("A CEO of a large oil corporation had climbed to the very top..."), never reported ("Kain writes", "Kain notes").
2. **Kain is named at most once in the writing**, only where credit is genuinely due, normally beside the course ("NLP Practitioner Training teaches this as..."). His trust signal is the reviewer line (`reviewed_by: kain-ramsay`), not the prose.
3. **No reference to the post the piece came from.** The source stays in the record's notes.
4. **No paragraph that describes the article.** The contents list does that job.
5. **Open with one short line to the reader restating their question** (Kain's standing rule, "open every article in the reader's words"), then straight into the example.
6. **The title appears once.** The first H2 does not repeat it; the meta description answers the question and does not open on a person's name.

No other change: same headings where they do not break rule 6, same links, same course, same keyword and density band, same length band.

## What Code builds now, on Kain's yes

The six as machine checks in `content_gate.py`, on every article record, not only these 38, so no future article passes while naming its source person repeatedly, narrating a post, describing itself, opening without the reader, repeating its title in its first heading, or opening its meta description on a person's name. Each proved both ways (a record that breaks it fails; a clean record passes), with the printouts in Code's SHIP. The source person is read from the record, never a hard-coded name. Where a check needs a threshold Chat or DSRD 2 should own, Code names it in the SHIP rather than setting it silently.

## Built the same session: the checks are in the gate

`content_gate.py`, `voice_checks()`, run by every article type except author biographies (instructor, knowledge-derived, field-authority, book-derived, hub question, hub guide). Seven lines, all FAIL-level: the source person is not narrated; the source person is named at most once; no reference to the source post; no paragraph describing the article; opens speaking to the reader; first heading does not repeat the title; meta description does not open on a person's name. **The source person is read from the record:** `reviewed_by` naming a person in `people-setup.php` who is not the `author`. Today that is exactly the 38; the three person lines run on nothing else.

**Proved both ways.** The reported record fails all seven (Kain named 13 times, 4 narrations, "Kain's post", the "This piece follows" paragraph, the third-person opening, the first H2 repeating the title, the meta opening "Kain Ramsay"). A fixture shaped like the 38 and written to the six rules passes all seven. Acceptance: `content_gate_acceptance.py` 106 of 106, `stage5_import_checks_acceptance.py` 6 of 6.

**Impact on records already written, for Chat to rule before anything relies on these lines at volume** (the S348 lesson about failing honest records the day a check arrives):

| Check | Instructor (102) | Field authority (116) | Hub question (5) |
|---|---|---|---|
| Opens speaking to the reader | 62 fail | 57 fail | 2 fail |
| No paragraph describing the article | 32 | 38 | 0 |
| First heading repeats the title | 12 | 5 | 2 |
| Person rules (named once / narrated / post / meta on a name) | 36 / 25 / 17 / 22 | 0 | 0 |

Three things for Chat: (1) the opening and self-description lines fail 121 and 70 records already live; they are Kain's rules, but whether they fail or count on existing records until each is next edited is Chat's call, and Code will switch them to counted lines on Chat's word. (2) **Possible conflict:** two hub question records fail the first-heading line with a "So, does CBT actually work?" style H2; if that shape is the approved S374 exemplar's, the rule and the exemplar disagree and Chat or Kain settles which stands. (3) The meta-description line matches any registry name at the start, so it also fails records outside the 38 whose meta opens on a thinker's name; biographies are exempt, and the 22 instructor hits are counted above.

## OWED BACK

The rewrite commissioned, a sweep brief naming the 38 for the push, and a ruling on (1) and (2) above.

*No em or en dashes in this file; checked before writing.*
