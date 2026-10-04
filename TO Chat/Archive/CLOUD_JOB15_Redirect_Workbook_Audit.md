# Job 15: redirect workbook audit

**Result: the audit could not be run, because `Redirect_Master.xlsx` is not in this repository or on this machine. There are no counts and no worst-thirty list in this report, and none were invented.** What is here instead is the evidence that the file is absent, and a script that runs the whole audit as soon as the file is supplied.

## Why the file is not here

Checked on a fresh fetch of `main` (`322fd2f7`):

1. **The folder is not whitelisted.** The `.gitignore` allows only two folders under `05. Spreadsheets | Data | CSV Files/`: `Course + Lesson Data | MASTER/` and `Notion Done Card Backup S092/`. The `Redirect Map/Master File` folder the brief names is not among them.
2. **Workbooks are ignored by name.** `.gitignore` line 147 is `*.xlsx`.
3. **Not in any commit.** `git log --all` and a search of every path in every commit find no `.xlsx`, and no file named `Redirect_Master`. The only Redirect-named files in history are four small Markdown notes (S051, S273 and a question about a live-site URL export).
4. **Not on disk.** A search of the whole container for `*.xlsx` and `*Redirect*Master*` finds nothing. The only remote branch of the record repo is `main`.
5. **Not in the theme repo.** It holds two Python scripts about redirects (`redirect_chain_register.py`, `redirect_one_hop.py`) and no workbook.
6. **DSRD 1 §11.4 confirms where the file lives** (the Redirect Map | Master File folder inside the spreadsheets folder, "Courses + commerce" tab), so the path in the brief is right; it is just on a machine this session cannot reach.

I did not look in `achology-channel` or `achology-component-prototypes`: they are outside what this job was scoped to, and DSRD 1 puts the file in the record's spreadsheets folder.

## What is needed

Either of these:
- put `Redirect_Master.xlsx` somewhere this session can read (a branch of a repo it can see), or
- add `!/Claude Code (Projects)/0001. Achology Website Upgrade 2026/05. Spreadsheets | Data | CSV Files/Redirect Map/` and a `!*.xlsx` exception for that folder to `.gitignore`. That is a change to a rule I was told not to touch, so I have not made it.

## The script, and how far it was tested

`cloud-reports/job15-redirect-workbook-audit.py` (read-only: opens the workbook with `read_only=True` and never saves).

```
python3 job15-redirect-workbook-audit.py <Redirect_Master.xlsx> <record repo root> [<theme repo root>]
```

For every tab with a source column and a destination column (found by header words such as Old, Current, Source, From, and New, Destination, To, Target), it groups rows as:

| Group | Meaning |
|---|---|
| self | source equals destination after normalising |
| blank | destination empty |
| malformed | not a site path or http(s) address, contains whitespace or a doubled slash |
| duplicate | the same source on more than one row anywhere in the workbook |
| loop | following destination to source returns to an address already visited |
| chain | the destination is itself a source (more than one hop), not a loop |
| unknown | the destination matches no `address` field in any Content Record and no `home_url('/…')` address in the theme: **"cannot tell if the page exists"** |

It prints the per-tab counts as a table and the worst thirty rows (loops and self-pointers weigh most, then malformed and blank, then chains and duplicates, then unknown), each with its tab and row number as Excel shows it.

**Tested only on a made-up eleven-row sheet** containing one of each fault: every group fired on the right row. It has never seen the real workbook, so these are untested against the real file:
- the header words may not match the real column names (a tab with no match is listed, not silently skipped);
- the real file may hold several redirects per row or merged cells;
- the "unknown" group will be large, because the known-address list is only the Content Record `address` fields plus the theme's literal `home_url()` addresses. Pages like `/academy/` that the theme builds another way are not in it, and a large "unknown" count will mostly mean "this list is incomplete", not "these pages are missing".

`openpyxl` was not installed here and was installed with pip to run the test.

## What was changed

Two new files in `cloud-reports/`. No existing file changed.


## Run by Code on the Mac (S145), because the workbook is not in the repository

Command: the cloud script with the workbook, the record root and the theme root. Output:

| Tab | Rows | self | blank | malformed | duplicate | loop | chain | unknown |
|---|---|---|---|---|---|---|---|---|
| Core pages | 27 | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| Courses + commerce | 38 | 0 | 0 | 0 | 0 | 0 | 0 | 37 |
| Schools | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Articles | 157 | 0 | 0 | 0 | 0 | 0 | 0 | 63 |
| Quotes | 1123 | 0 | 0 | 0 | 0 | 0 | 0 | 1123 |
| Quote authors | 506 | 0 | 0 | 0 | 0 | 0 | 0 | 506 |
| Help articles | 213 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Help categories | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| KH categories | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| Book notes | 81 | 0 | 0 | 0 | 0 | 0 | 0 | 55 |
| Videos | 205 | 0 | 0 | 0 | 0 | 0 | 0 | 28 |
| Jobs | 27 | 0 | 0 | 0 | 0 | 0 | 0 | 27 |
| Old tags | 127 | 0 | 0 | 0 | 0 | 0 | 0 | 127 |
| Pen-name authors | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Miscellaneous | 45 | 0 | 1 | 0 | 0 | 0 | 0 | 36 |

Tabs with no source and destination column: Read Me, Summary

| Tab | Row | Source | Destination | Groups |
|---|---|---|---|---|
| Miscellaneous | 11 | /publications/fdsfds/ | None | blank |
| Articles | 3 | /psychology/30-abraham-maslow-quotes/ | /learn/psychology/articles/30-abraham-maslow-quotes/ | unknown |
| Articles | 10 | /psychology/martin-seligman-and-his-contributions-to-positive-psychology/ | /learn/psychology/articles/martin-seligman-and-his-contributions-to-positive-psychology/ | unknown |
| Articles | 11 | /wisdom-for-life/how-the-eisenhower-decision-making-matrix-can-help-you-make-wise-decisions/ | /learn/wisdom-for-life/articles/how-the-eisenhower-decision-making-matrix-can-help-you-make-wise-decisions/ | unknown |
| Articles | 15 | /wisdom-for-life/upgrade-your-communication-skills/ | /learn/wisdom-for-life/articles/upgrade-your-communication-skills/ | unknown |
| Articles | 19 | /psychology/the-lasting-impact-of-william-james-his-contributions-to-the-field-of-psychology/ | /learn/psychology/articles/the-lasting-impact-of-william-james-his-contributions-to-the-field-of-psychology/ | unknown |
| Articles | 24 | /wisdom-for-life/the-power-of-listening-skills/ | /learn/wisdom-for-life/articles/the-power-of-listening-skills/ | unknown |
| Articles | 29 | /psychology/rosalynn-carter-breaking-mental-health-stigma/ | /learn/psychology/articles/rosalynn-carter-breaking-mental-health-stigma/ | unknown |
| Articles | 31 | /psychology/jean-piaget-quotes-on-human-development/ | /learn/psychology/articles/jean-piaget-quotes-on-human-development/ | unknown |
| Articles | 33 | /psychology/27-albert-bandura-quotes/ | /learn/psychology/articles/27-albert-bandura-quotes/ | unknown |
| Articles | 35 | /psychology/steven-pinker-quotes/ | /learn/psychology/articles/steven-pinker-quotes/ | unknown |
| Articles | 37 | /personal-growth/understanding-your-core-values/ | /learn/personal-growth/articles/understanding-your-core-values/ | unknown |
| Articles | 40 | /psychology/burrhus-frederic-skinner-quotes/ | /learn/psychology/articles/burrhus-frederic-skinner-quotes/ | unknown |
| Articles | 41 | /psychology/21-timeless-stanley-milgram-quotes/ | /learn/psychology/articles/21-timeless-stanley-milgram-quotes/ | unknown |
| Articles | 42 | /psychology/viktor-frankl-a-life-defined-by-hardship-purpose-and-meaning/ | /learn/psychology/articles/viktor-frankl-a-life-defined-by-hardship-purpose-and-meaning/ | unknown |
| Articles | 43 | /psychology/the-life-and-works-of-carl-jung/ | /learn/psychology/articles/the-life-and-works-of-carl-jung/ | unknown |
| Articles | 48 | /psychology/sigmund-freud-a-journey-through-his-life/ | /learn/psychology/articles/sigmund-freud-a-journey-through-his-life/ | unknown |
| Articles | 49 | /motivation/the-power-of-useful-thinking-how-to-change-your-mindset/ | /learn/motivation/articles/the-power-of-useful-thinking-how-to-change-your-mindset/ | unknown |
| Articles | 50 | /motivation/timeless-pearls-of-wisdom-for-instant-inspiration-and-personal-growth/ | /learn/motivation/articles/timeless-pearls-of-wisdom-for-instant-inspiration-and-personal-growth/ | unknown |
| Articles | 51 | /motivation/the-importance-of-self-awareness-and-make-better-choices/ | /learn/motivation/articles/the-importance-of-self-awareness-and-make-better-choices/ | unknown |
| Articles | 55 | /psychology/from-roots-to-revolution-a-brief-history-of-psychologys-evolution/ | /learn/psychology/articles/from-roots-to-revolution-a-brief-history-of-psychologys-evolution/ | unknown |
| Articles | 56 | /psychology/psychology-and-philosophy-how-philosophy-can-help-us-understand-our-psychology/ | /learn/psychology/articles/psychology-and-philosophy-how-philosophy-can-help-us-understand-our-psychology/ | unknown |
| Articles | 59 | /motivation/george-michaels-faith-discover-timeless-messages-within/ | /learn/motivation/articles/george-michaels-faith-discover-timeless-messages-within/ | unknown |
| Articles | 60 | /personal-growth/embracing-your-innermost-values-a-guide-to-living-authentically/ | /learn/personal-growth/articles/embracing-your-innermost-values-a-guide-to-living-authentically/ | unknown |
| Articles | 62 | /personal-growth/qualities-of-a-true-leader-insights-from-historys-finest-leaders/ | /learn/personal-growth/articles/qualities-of-a-true-leader-insights-from-historys-finest-leaders/ | unknown |
| Articles | 64 | /personal-growth/essential-productivity-insights-and-strategies/ | /learn/personal-growth/articles/essential-productivity-insights-and-strategies/ | unknown |
| Articles | 65 | /psychology/21-quotes-by-abraham-maslow/ | /learn/psychology/articles/21-quotes-by-abraham-maslow/ | unknown |
| Articles | 69 | /wisdom-for-life/wisdom-for-lasting-change-and-motivation/ | /learn/wisdom-for-life/articles/wisdom-for-lasting-change-and-motivation/ | unknown |
| Articles | 75 | /personal-growth/beyond-the-drama-triangle-10-lessons-from-daniel-yeagers-book/ | /learn/personal-growth/articles/beyond-the-drama-triangle-10-lessons-from-daniel-yeagers-book/ | unknown |
| Articles | 77 | /personal-growth/15-productivity-quotes-to-stand-the-test-of-time/ | /learn/personal-growth/articles/15-productivity-quotes-to-stand-the-test-of-time/ | unknown |
