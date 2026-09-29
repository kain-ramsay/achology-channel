**Needs from Cowork:** the 51 author biographies get their missing demand evidence, and the ones that fail keyword density get fixed. This is FIRST in your tray, ahead of the question programme. About 51 AnswerSocrates requests; do not go over.

# BRIEF: demand evidence on the 51 author biographies

**From:** Claude Chat, S389, Tuesday 29 September 2026. **To:** Claude Cowork.
**Why this exists.** Your 641 DONE file reported that all 51 author biographies still fail one line, the missing `demand_evidence` field, and 18 also fail keyword density. You rightly left them: the evidence needs a real demand lookup, and the call on record-field faults was Chat's. Chat's call is: do it, and do it now, because the AnswerSocrates month ends 17 October 2026 and 185 requests are left.

## The method, one request per biography

1. **The keyword is already set.** Use each record's own `rm_focus_keyword` (for example `abraham maslow`, `a. c. grayling`). Do not change any keyword, title or address.
2. **One `get_keywords` call per biography**, query = that keyword, country US, language en. That is one request each, 51 in total. Do not use `get_trends` (it is bulky and adds nothing here). If a call fails, retry it once; if it fails again, skip that record and name it in your report.
3. **Read the result honestly.** Record: whether the exact phrase appears in the results, how many keywords came back in total, and two or three real phrases from the results that show why someone searches for this person (for example "who was ...", "... biography", "... quotes", "... theory").
4. **Write one row into the record's Page fields table**, named `demand_evidence`, placed directly after `rm_seo_description`. One paragraph, in this form:
   `AnswerSocrates, US, run by Cowork [date] for "[keyword]": [N] keywords returned; the exact phrase [appears / does not appear]; phrases include "[phrase]", "[phrase]" and "[phrase]". Checked against KEYWORD_REGISTER.csv the same day: [free / already claimed by ...].`
5. **If the demand is thin or the results are mostly noise** (as with a journal named after the person, or a name shared with someone else), say so in the same paragraph in plain words, exactly as you did for H29. Never invent a phrase and never round a number up. `kain-ramsay` is the likely thin one: report what comes back.
6. **Do not change the body** for this step. The only edit is the one new row.

## Then the density fix (only the records that still fail it)

After step 4, run `content_gate.py` on each record. For any that still fail keyword density (18 did in your report), add real mentions of the person's name where a sentence naturally wants one, until the gate passes. Rules: no filler sentence, no repeating a phrase near-verbatim across records, nothing that reads as machine-written, and every fact stays as it is. If a record cannot pass density without a forced sentence, leave it failing and name it in your report for a decision; do not pad.

## Stop conditions

- If AnswerSocrates returns an error on three different records in a row, stop and report; do not spend requests retrying.
- If `get_usage` shows fewer than 20 requests left at any point, stop and report.
- Do not start the question programme until this brief is done or stopped.

## What to send back

One DONE file in FROM Cowork: a table of the 51 records with the exact phrase found (yes or no), total keywords returned, the register check, and the gate result before and after; the list of any records skipped or left failing; and `get_usage` at the end. Also put a line at the top telling Chat which records are ready for Code to push.

*No em or en dashes in this file; checked before writing.*
