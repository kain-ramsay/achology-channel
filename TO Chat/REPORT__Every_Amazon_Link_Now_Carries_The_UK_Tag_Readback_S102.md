# REPORT: every Amazon link in the book note data now carries the UK tag, and the test page reads it back

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** the OWED BACK line of `RULING__Install_OneLink_And_Tag_Every_Book_Link_S309.md`, as corrected by Chat at S338 (no script exists to install; steps 2 to 4 stand).
**Board card:** Plugins and Site Configuration; Book Notes.

## What was done, step 2 of the ruling

`?tag=kainramsay01-21` appended to every Amazon address in the book note data, at source, none of which carried any tag before (counted this turn before the change):

| Where | Addresses found | Tagged |
|---|---|---|
| The Book Note master, its `amazon_url` column | 637 of 680 rows carry one | 637 |
| The book note records in Content Records, their `amazon_url` field | 103 | 103 |
| The install, the `amazon_url` meta on book note posts | 59 rows | 58 |

The one install row not tagged belongs to a post revision, not a page (`post_type` revision, an old saved copy of a live note), and WP-CLI refuses to write meta onto a revision. Nothing public reads it. Every published book note's own row is tagged.

The master was backed up first under a name that is never reused (`Book_Note_Master__pre_S102_onelink_tag_2026-09-05_1.xlsx` in its Archive folder). `amazon_genius_link_url` was not touched, in either the master or the records; an address already carrying a tag would have been left alone, and none was.

## Step 3, the readback

`/learn/psychology/book-notes/mans-search-for-meaning/`, cache purged, fetched fresh this turn: the page carries one Amazon link, the hero's `Get this book at Amazon` button, and its address now reads `https://www.amazon.com/dp/0807067997?tag=kainramsay01-21`. Before the change the same link had no tag (fetched and kept for comparison). There is no second button on this page: the travelling shelf that carried one was retired at S085, so "both buttons" in the ruling's step 3 is one button on the page as built.

No script is in the external script list, correctly: Chat's S338 correction retired step 1 with the thing it would have installed.

## What is Kain's, step 4

The UK click test in Safari: open that page, click the Amazon button, land on amazon.co.uk with the tag in the address; the click shows in the Associates report within a day. Nobody buys through it. Genius Link stays until that passes and Kain says so, exactly as the ruling leaves it.

## One thing this unblocks

Instructor article I18's external link (item 2 of the S099 blocked list) can now be a plain tagged Amazon address, as Chat's correction said. The record's body is Cowork's or Chat's to carry it; the import route for the three held articles is Code's and is being run this session.

OWED BACK: nothing from Code. Kain's click test, then Karen cancels Genius Link on his word.

*No em or en dashes in this file; checked before writing.*
