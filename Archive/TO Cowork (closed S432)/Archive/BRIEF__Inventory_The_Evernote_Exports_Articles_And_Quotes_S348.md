# BRIEF: inventory the Evernote exports, so we know what is left to salvage

**DOCUMENT TYPE:** brief, from Claude Chat, Session 348. **Date:** Monday 7 September 2026.
**Approved by Kain** in the S348 sitting.
**Governed by** `000__COWORK_PRODUCTION_HARNESS.md` at the root of this folder, as every Cowork job is.
**Job type:** measurement. Nothing is drafted, corrected, or gated in this job.

---

## 1. Why this job exists, in plain words

A month ago Kain exported everything from his old Evernote account. It sits in the `Evernote Folder (Exports + Images)` folder here: seven notebooks of old articles and two notebooks of quotes. Nine files, 432 megabytes, mostly pictures.

Kain wants to know two things before he can close Evernote for good:

1. **Are there any old articles in those seven notebooks that have not already been rescued**, and could still be rewritten to the current standard?
2. **How many quotes are in the two quote notebooks, from which people and on which topics**, so the quote pages can be planned as a batch job rather than guessed at.

Chat cannot read these files: they are too large for a chat window and the copy tool is not available. So the answer is a script, and you run it.

## 2. What you do

**Step 1.** Open a terminal in this folder, the Content Production Factory, and run:

```
python3 evernote_inventory.py
```

It reads the nine exports one note at a time, never loading a whole file. It reads nothing else except three things it lines the notes up against: every record in `Content Records`, the old site's page list at `05. Spreadsheets | Data | CSV Files / Search Console + Live Site Exports / live-site-urls.csv`, and the master workbook `Achology Master Books and Quotes.xlsx` in `Content Plan Spreadsheets / Working`.

**It writes only into one new folder** beside itself, `Evernote Salvage Inventory S348`, three files: the articles inventory, the quotes inventory, and a summary. It prints the summary to the terminal as it finishes.

**Step 2.** If the summary line says the master workbook was **NOT checked**, install the one library it needs and run again:

```
python3 -m pip install openpyxl
python3 evernote_inventory.py
```

If that install is refused on Kain's Mac, leave it and say so in your DONE file; the workbook column is the least important of the three checks.

**Step 3.** Read the articles inventory. For every row whose verdict begins **candidate**, open the note's title and word count and add one column of your own judgement, `cowork_view`, with one of three values: `worth rewriting`, `not worth it`, or `already covered under another title`. That last one matters: the script matches titles exactly, so a note titled one way and rescued under a different title will show as a candidate when it is not. Your eye catches what the script cannot. **Do not rewrite anything.** A view, not a draft.

**Step 4.** Read the quotes summary. Note the distinct people count and the distinct topics count. Skim the quotes inventory and say in your DONE file whether the quote extraction looks right: are the rows real quotes, or has the script picked up headings and stray lines. If it is picking up rubbish, say what the rubbish looks like so Chat can tighten the script. **Do not verify any quote in this job.** Verification is the next job, and it is a big one.

## 3. What comes back

One DONE file in FROM Cowork, named `DONE__Evernote_Inventory_Complete_S348.md`, carrying:

1. The summary, pasted whole.
2. The count of article candidates, split by your three views.
3. Your one-paragraph read on the quotes: how many, how clean the extraction is, and anything that surprised you.
4. Any error the script threw, pasted whole. If it fails, do not patch it: paste the error and stop.

The three inventory files stay in their folder. Chat reads them from there.

## 4. What you must not do

- Do not write to the Evernote folder. It is read-only by its own README.
- Do not write to `Content Records`. Nothing here is a record.
- Do not draft, correct, or gate any article or quote. This job counts; the next job produces.
- Do not edit the script. If it is wrong, say so and Chat fixes it.

## 5. What happens after this

Chat reads the inventory with Kain. He rules how many quotes run and in what order. Then the quote job is briefed as a proper commission: verify each quote against a source, correct what can be corrected, drop what cannot, and write its accompanying page under the `quote-page` skill and the `rank-math-90` route, in batches. The salvageable articles, if any, go the same road as the 117 rescued ones already did.

When both are done, Kain deletes the Evernote files and closes the account. This inventory is the first step of the last salvage job on the plan.

---

*No em or en dashes in this file; checked before writing.*
