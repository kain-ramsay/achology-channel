BRIEF, from Claude Chat to Cowork, Session 369, Thursday 17 September 2026. Written on Kain's yes in session: the programme now follows the vault method, and the full-name searches go to Cowork next.

# Full-Name Searches For NLP And CBT, And The CBT Subject Questions Put Back

## Order of work for Cowork

**Do this brief first, then carry on with the help-answer pass** (the 91 remaining, under its own brief in this tray). **Do not start any other search family.** The next family waits for Chat's brief, because the method changed at S369 and the old brief's cutting rules no longer fit.

## Why the method changed (read first, it is short)

The plan file `PLAN__The_Question_Authority_Programme_S367.md` (Launch Content Planning folder) was rewritten at S369 to follow the vault method `Deriving A Content Set From The Demand Grid`. Read its sections 2 and 4. Two changes matter for you:

1. **Every subject is searched under its full names, not only its short form.** The tool returns only phrases containing the words typed, so "cbt" and "nlp" miss everyone who types the name out.
2. **Questions about the subject itself are now kept**, not cut. Under the S368 brief you cut people asking whether CBT works, how it helps, or what it is. Those are now wanted: they are subject questions, and they become Knowledge Hub articles.

## Step 1. The subject questions put back (no requests spent)

From your eight raw CBT files already in Demand Exports, write one new file: `AnswerSocrates__SUBJECT__cbt__US.csv`, same five columns as the other files, seed set to the seed each phrase came from. Put in it every phrase you cut under your "clinical treatment seeking" reason that is a **question or statement about CBT itself**: what it is, whether it works, how it works, what it helps with, whether it is evidence based, how long it takes, CBT versus other therapies, CBT worksheets and techniques. Keep out only phrases where the person is plainly looking for a therapist to book (near me, find a, book, cost of a session, insurance). Do not touch the eight existing sorted files.

## Step 2. The full-name searches, 8 requests, no more

Call `get_usage` first and note the number (it should read 16). Then one `get_keywords` call per seed:

| Seed | Country |
|---|---|
| neuro linguistic programming | US |
| neurolinguistic programming | US |
| nuero linguistic programming | US |
| cognitive behavioral therapy | US |
| cognitive behavioral psychology | US |
| cognative behavioral therapy | US |
| cognitive behavioural therapy | GB |
| cognitive behaviour therapy | GB |

If a misspelling (nuero, cognative) returns nothing, write that in the report and move on; it still counts as a request.

## Step 3. Cut and save each list before the next search

Same file format and naming as before, with the seed hyphenated: `AnswerSocrates__BUYING__{seed}__{country}.csv` and `AnswerSocrates__RAW__{seed}__{country}.json`. Keep every phrase a person choosing a course would type, **and every question or statement about the subject itself** (Step 1's rule). Cut: other meanings of the words; place names (keep near me, online, usa, uk); other languages; a person plainly looking to book a therapist; routes for people already holding a clinical licence. Keep every question even when an earlier file holds it. A plain non-question phrase already held in an earlier file of the same subject need not be written again. Rival names and accrediting bodies are kept.

## Step 4. Stop and report

One DONE file into FROM Cowork: requests before and after; each file with raw, kept and cut counts; how many phrases Step 1 put back; any misspelling that returned nothing; what you noticed that the short-form searches did not show. Then carry on with the help-answer pass.

## Definition of done

The SUBJECT file written; eight searches run (sorted and raw files saved), no more than 8 new requests; the DONE report filed.

*No em or en dashes in this file; checked before writing.*
