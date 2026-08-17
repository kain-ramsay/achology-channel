# RECORD: the Founders' Letter metadata, three of four set. The fourth is a question.

**From:** Claude Code, S048. **Date:** 2026-08-06. **Theme:** v0.38.56, live.
**Page:** https://achologytest.com/about/founders-letter/ (post ID 10887)
**Answers:** `ANSWER__Founders_Letter_Metadata_S245.md`. **Not yet closable:** the title.

## The answer told me to check the page before setting anything. It was right to.

> "So the page is no longer bare: verify what is present on the rendered page before setting anything, rather than assuming the gap still shows."

What was actually there, read from the database this session rather than assumed:

| Field | State found | Matched the answer's assumption? |
|---|---|---|
| `rank_math_focus_keyword` | `Founders' Letter,Achology founders,founders,Letter,Achology` | No. A five-item list, not the single approved keyword. |
| `rank_math_description` | the older string | Yes, as expected, and replaced. |
| `rank_math_title` | `Achology Founders' Letter: Why Kain and Karen Built Achology` | **No.** See the question below. |
| hero image alt | `Kain and Karen Ramsay, founding partners of Achology.com` | Yes, as expected, and replaced. |

## What is set now, read back off the rendered page

**Focus keyword** (database, confirmed by reading it back):

```
founders letter
```

**Description** (rendered page):

> "Kain and Karen Ramsay's founders letter: why they created Achology in 2017, what it taught them, and what comes next. In their own words."

**Hero image alt** (rendered page):

> "Kain and Karen Ramsay, the authors of Achology's founders letter"

All three are the approved strings, character for character.

**One detail worth recording, because getting it wrong would have been
invisible.** The approved alt carries a **straight** apostrophe. The theme's
habit everywhere else is `&rsquo;`, and following that habit would have quietly
changed an approved character into a different one. I checked the source file
for which character it actually contains before writing it. Rule 8 places
approved copy exactly as written, and punctuation is part of that.

## Rank Math score

`rank_math_seo_score` currently reads **81**, which clears the 80 bar the answer
was aiming at.

**Read that number with one caveat.** Rank Math recalculates the score when a
post is saved in the editor, not when post meta is written underneath it. The
81 may therefore predate the keyword and description I just set. It is the
stored value, honestly reported, not a measurement of the strings now live.
Anyone opening the page in wp-admin will trigger a real recalculation.

## Not touched, and why

`page-about.php` carries the **same image with the old alt still on it**. That is
a different page, so Rule 3 keeps it out of this change set. It needs the same
correction, and it belongs either to `BRIEF__About_Testimonials_Sweep_S245.md`
or to About's turn in the walk, whichever reaches it first. Recorded here so it
cannot fall between the two.

## The item that cannot close: the title

Filed separately as
`QUESTION__Founders_Letter_Title_Does_Not_Match_The_Approved_String_S048.md`,
and **marked waiting on ruling** per Rule 5. In short: the answer says the
approved title "stands as already set, no change", and it does not stand. The
live title is a different string. I have not changed it, because it is content
and because the answer itself records that Kain set the title himself, which
would make the live value his and later than the approved one.

`ANSWER__Founders_Letter_Metadata_S245.md` therefore **stays live in FROM Chat**
rather than being archived: three of its four acceptance items are done, and
the fourth is waiting on that ruling.

*No em or en dashes in this file; checked before writing.*
