# DO THIS: four things I need from you before the 49 can import

**From:** Claude Code · **Date:** 2026-07-27
Your last note answered who strips the file (me, understood, authorised). It
did not answer the request I filed after it. These four are what I need. Kain
wants the 49 imported next session with no further delay, so please answer all
four in one reply.

---

## 1. Fix two broken internal links. This is a content fix, so it is yours.

Your gate did not catch this. **Two of the 49 link to the two Professional
Directory articles you are removing.** Strip those rows and these links land on
a 404.

I checked all 78 distinct `/help/` targets across the 49 against the 200 live
articles plus the 49 themselves. 76 resolve. These two do not:

- `achology-professional-directory-get-listed`
- `would-removed-achology-professional-directory`

Both sit in the `related_questions_urls` column:

| Row | Slug | Dead target |
|---|---|---|
| `GAP-005` | `have-each-year-keep-master-achologist` | `achology-professional-directory-get-listed` |
| `GAP-015` | `have-retake-code-ethics-training-every` | both |

**What I need:** either the replacement related-question URLs for those two
rows, or your instruction to drop those entries. Give me the exact replacement
text and I will apply it as part of the mechanical transform. I am not choosing
replacement articles myself, because which question a reader should be sent to
next is editorial, not mechanical.

## 2. Publish dates: CSV dates, or import date?

Do the 49 import with the `date_published` / `date_modified` values in the CSV,
or stamped with the import date? The 200 carry their own dates. I will not
guess at the freshness signal you intend. **One line: "use the CSV dates" or
"stamp them today".**

## 3. Confirm the `url` column is reference-only.

It carries the build domain (`https://achologytest.com/help/...`). Confirm it
is not mapped into any WordPress or Rank Math field, so the test domain cannot
travel into production at cutover. **One line: "reference only, do not import"
or tell me where it goes.**

## 4. Audio: two confirmations.

- **Which column do I voice?** Your note said `answer_text_full`. Confirm, because
  voicing the wrong column wastes the entire run.
- **New pronunciation cases?** The engine is fed "Ackology" so it says Achology
  correctly. If the 49 introduce any new proper nouns, acronyms, names or
  initialisms a voice engine will mangle (SOMAP, CCAC, CIPS, PALS, VALTS and
  DiMAP all appear in the slugs), **list them with the pronunciation you want**
  and I will add them to the substitution set before the run rather than after
  Kain hears it.

---

## What happens once you answer

I strip the file as you authorised: drop `GAP-018` and `GAP-019`, drop the five
working columns, add the byte-order mark, apply your fix from §1. I post the
resulting header row and row count here for the record, then import via the
saved WP All Import template that brought the 200 in, matching categories on
`category_slug`. Then the count checks (49 new, 249 total), end-to-end spot
checks including a certificate-category row, and a report back. Audio is a
separate pass afterwards, never in the same run.

Everything else is already settled and needs nothing from you: the import
route, the field mapping, the categories (all nine exist live, including the
renamed one), and the audio wiring (the theme finds `{slug}.mp3` by convention,
so no CSV column and no theme change is needed).

**Blocked on §1 and §2 only.** §3 and §4 I need before I finish, but they will
not stop me starting.
