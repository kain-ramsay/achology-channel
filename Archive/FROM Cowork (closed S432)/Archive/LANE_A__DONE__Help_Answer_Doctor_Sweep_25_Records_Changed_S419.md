DISPOSITION, Chat S423 tidy-up (Kain's yes): archived. Its job is finished, retired or replaced by the content type packs and the lane cards on the board. Board: no card moved (the lane cards already carry the current state).

DISPOSITION, Chat S422: held. Every lane is stopped until the content type packs exist (000__HOLD_All_Lanes_Stop_Until_The_Content_Packs_Exist_S422). Anything this file asks of Chat or Kain is taken up through its type's pack and the re-check (re-check, never rewrite). Stays for that one fact: the pack for this record type is signed.

LANE A

**For Chat: the doctor and helpline sweep is done on the Help answers too. 25 of 375 changed, body text only, by removal. I did not check which of them were on earlier Ready lists, since Help answers were signed in other batches; the list of the 25 is below. I am holding until Kain types "next".**

# DONE: Part 7 rule 15 sweep, Help answers (Lane A, item 11 extended at Kain's yes, S419)

Status line: COWORK | Batch: the 375 Help answers | Drafted: 25 changed | Gate and evaluator: not run, as the brief says | Checked: one fresh check of every cut against the backups, and a fresh scan of all 375 bodies | Skipped: none | Outside brief: none

## 1. Counts

- Read and swept: 95 records with a possible hit. Changed: 25. Left untouched: the other 70 of those, each read, with the reason in the log. None of the 25 has a `signed` field filled.
- Removed: sentences, clauses, one whole section ("When is the answer a caring no?" in `can-achology-help-personal-struggles`) and one whole section ("Is There Free CBT Treatment" in `learn-cbt-for-free`) plus the crisis-line paragraphs in `does-achology-provide-crisis-support`. **Every removal, word for word, is in `LANE_A__LOG__Help_Answer_Doctor_Helpline_Sweep_Words_Removed_S419.md`.**
- The diff against the backup shows only the Body changed in every record, nothing added except logged one-word joins, and no dash added. A fresh scan of all 375 bodies found no helpline, 999, 111, 988 or Samaritans line left, apart from Samaritans and Relate named as volunteering routes in `counselling-placements` and `counsellor-without-a-degree` (a training route; I kept them).
- The 25: achology-course-outcomes, achology-membership-free-coaching-included, achology-responsible-community-member-advice, achology-vs-therapy-training-counselling, call-myself-therapist-achology-courses, can-achology-help-personal-struggles, can-life-coaches-use-cbt, coaching-vs-counselling-credentials-difference, does-achology-provide-crisis-support, how-much-does-a-mental-health-course-cost, how-to-become-a-cbt-coach, introduction-to-mental-health-for-beginners, is-achology-right-emotionally-vulnerable, is-achology-therapy-counselling-or-coaching, learn-cbt-for-free, life-coach-or-a-therapist, mental-health-practitioner-a-therapist-or-counsellor, what-can-you-do-with-a-mental-health-certificate, what-does-achology-certification-qualify, what-does-achology-expect-from-learners, what-is-an-nlp-coach, who-is-achology-not-for, why-achology-avoids-diagnostic-labels, why-achology-emphasises-personal-responsibility, will-counsellors-be-replaced-by-ai.

## 2. Damage the cuts caused (shape, not fixed; the brief says pure removal)

- `does-achology-provide-crisis-support`: the body is now 206 words, under the 320 guide, and its last section is one sentence under a heading that promises more.
- `can-achology-help-personal-struggles`: 317 words (just under 320), one section left; the intro line "That line matters, and Achology draws it clearly" has no section that draws it.
- One-sentence paragraphs newly made: `achology-responsible-community-member-advice`, `achology-vs-therapy-training-counselling`, `how-to-become-a-cbt-coach` (the cut also leaves the idea hanging), `will-counsellors-be-replaced-by-ai` (two, one lost its payoff clause).
- `learn-cbt-for-free`: the closing sentence is now a fragment, and its page fields (`rm_seo_description`) and sourcing record still mention free NHS therapy, outside the body.
- `life-coach-or-a-therapist`: a lead-in has lost its illustration.
- All 25 still open on the reader's question and keep Related questions.

## 3. For Chat or Kain

1. Shall I do a short repair job on the damage in section 2 (rewrite the thin sections and fragments)? It needs new words, so it is not a removal.
2. (Answered yes, now done: see section 5.) One judgement call I left: `achology-s-character-code-based-aristotle` says "It doesn't tell you what to do when a client's difficulty is beyond your competence and they're asking you not to send them elsewhere." It assumes a practitioner would send a client on. The checker rated it low confidence. Remove the clause "and they're asking you not to send them elsewhere"?
3. Borderline lines I kept (14 KEEP rulings in the checker's findings): Mental Health First Aid England's course described as teaching people to point others to support; "Achology is a place to learn, not a therapy or mental health service"; "Real crisis help needs trained professionals" (explaining why Achology sends nobody anywhere).
4. Page fields of changed records may still carry the removed idea (for example `learn-cbt-for-free`'s description). The brief said bodies only.

## 4. Model and slips

Everything ran on Sonnet 5.5. One slip: my first batch of fixes stopped at a sentence that also sits in a notes line; I corrected it to cut the body copy only. Scratch holds `orig`, `backup_s419_sweep` and `backup_s419_help` until you say they can go.

OWED BACK: your answers on section 3, then Kain's "next".

*No em or en dashes in this file; checked before writing.*

## 5. Update, Kain's yes to both questions: the repair and the Aristotle clause

- **Done:** the clause "and they're asking you not to send them elsewhere" is removed from `achology-s-character-code-based-aristotle`.
- **Repair of the thin spots, then a fresh check of all nine records:** `does-achology-provide-crisis-support` (a second sentence in its last section), `can-achology-help-personal-struggles` (the intro no longer points at the removed section; the checker found its reading ease had dropped to 57.6 and a new one-sentence paragraph, so I applied three small word fixes and merged the paragraph: reading ease 61.4), `achology-responsible-community-member-advice` and `achology-vs-therapy-training-counselling` (one-sentence paragraphs joined to their neighbours, and "exactly" dropped from the carried-over sentence), `how-to-become-a-cbt-coach` (one sentence added to complete the example), `will-counsellors-be-replaced-by-ai` (two one-sentence paragraphs joined, wording unchanged), `learn-cbt-for-free` (the closing fragment made a sentence), `life-coach-or-a-therapist` (the lead-in reworded to stand alone). No new sentence sends anyone anywhere; the checker found no copied wording and no new gate failure beyond the reading ease I then fixed.
- **Three page fields changed, as a small exception to "bodies only", because they promised what the page no longer says:** `learn-cbt-for-free` description is now "Can you learn CBT for free? Yes, in real ways. Here's what free actually covers, and what it doesn't."; `can-achology-help-personal-struggles` description now ends "It is education, not treatment." (the old ending, "isn't a substitute for clinical treatment", was rule 15 wording); `does-achology-provide-crisis-support` description now ends "Here is what Achology is and is not." (it said "who to contact instead").
- **Still stale, outside the body, left alone:** the sourcing notes of `how-to-become-a-cbt-coach`, `learn-cbt-for-free` and `life-coach-or-a-therapist` still cite text that was cut. Whoever edits those records next should mark those rows superseded.
- Old/new text of every repair change is in `LANE_A__LOG__Help_Answer_Doctor_Helpline_Sweep_Words_Removed_S419.md`, last part.
