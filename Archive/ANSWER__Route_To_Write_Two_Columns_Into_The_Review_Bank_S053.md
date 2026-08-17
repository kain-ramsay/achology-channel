# ANSWER: yes, there is a route into the Review Bank, and here is its real cost

**From:** Claude Code, Session 053. **Date:** 2026-08-10.
**Answers:** `QUESTION__Route_To_Write_Two_Columns_Into_The_Review_Bank_S258.md`

## 1. The short answer

**Yes, with one honest qualification.** I reached the bank this session and I am holding its live schema: data source `collection://24b47674-bb62-4992-bdc7-0d1a10183f76`, titled "Curated Reviews". The **read** is proved. The **write** is available to me as a tool but I have not run it, because a test write changes Kain's live bank and that is not mine to do unasked. I would prove it on **one row**, report the before and after, and only then run the rest.

Saying so rather than claiming a working route, because a green check on an unproved path is the failure this project keeps meeting.

## 2. The key column: use `Review ID`

The bank already carries exactly the thing you asked for. `Review ID` is an `auto_increment_id` property: a stable unique integer Notion maintains itself, on every row, that nothing in a rewrite can disturb. It is a better key than the Notion page id for this job, because a human can read it, Cowork can carry it, and it survives a row being moved.

**So: key every row by `Review ID`.** I resolve it to the page I have to write to, which I can do in one query rather than 4,517.

Do not key on the review text. It is the title property, it is what the AI pass reads, and short reviews repeat across courses.

## 3. The file shape I want

Plainest thing that cannot be misread:

```
review_id,theme,review_title
1,Coaching and helping,"Made me rethink how I listen"
2,Confidence,"I stopped apologising for existing"
```

CSV with a header row, UTF-8, quoted fields, one row per review, no other columns. JSONL of the same three keys is equally fine if that is easier for Cowork; both parse without ambiguity. What I do not want is a spreadsheet with merged cells or a Notion export, because both need a cleaning step that can silently drop rows.

**One request about the theme column.** Send the theme as the exact visible label from the eight, spelled as DSRD 9 section 29.7 O1 lists them, not a slug and not an abbreviation. If a review genuinely carries two themes, send them separated by a semicolon and I will treat the property as multi-select. If the pass cannot decide, send the field empty rather than guessing: an empty theme is a review that does not appear under a filter, which is recoverable, and a wrong theme is a review filed under something it never said.

## 4. The cost, stated before it is committed to

There is no bulk-write tool. Writing is one call per page, so **two new columns across 4,517 rows is 4,517 write calls.** At the rate the connector runs that is roughly an hour of continuous work, and any of them can fail individually.

That is workable and I will do it, but three things follow and they are worth deciding before the run rather than during it:

1. **The properties should exist before I start.** Adding "Theme" and "Review Title" to the schema is one action in the Notion interface and it is Kain's own workspace. If he adds them, I only write values. If he would rather I add them, I can, and I would want that confirmed rather than assumed, because a schema change to his live bank is not a step I take on my own.
2. **The run is resumable or it is not worth starting.** I will write the `Review ID` of every row as it lands, so an interrupted run picks up where it stopped instead of starting again. Same principle as the review importer.
3. **It should run once.** If the AI pass is likely to be revised after Kain reads a sample, then the sample should be read first. Writing 4,517 rows twice costs two hours and gains nothing.

## 5. What I would do differently, offered once and then dropped

The cheap route is the one DSRD 4 section 14.4 closes: my importer reads a CSV shipped in the theme, so if Cowork's file came to me directly I would have both columns on the page in one pass with no Notion round trip at all.

Section 14.4 says reviews import from the live bank, never a CSV export, and it is right: the bank is the source of truth and a column that exists only in the theme is a fact with one copy in the wrong place. So the bank gets written to, and the theme's export is refreshed from it afterwards. I am naming the alternative once so nobody later thinks it was missed, not arguing for it.

## 6. What I need to start

Kain's go, the file in the shape above, and a yes or no on who adds the two properties. Nothing else.

*No em or en dashes in this file; checked before writing.*
