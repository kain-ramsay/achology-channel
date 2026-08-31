> **CHAT DISPOSITION, S322: read in full, acted on, archived.** Its OWED BACK line says nothing. The Book Notes card carries the superseding fact and the earlier report's disposition line was corrected in the same turn. **Two things are named for Kain rather than actioned here:** the three 500px covers, which are the whole hand-work list, and orphan attachment 34148, which Code will not delete and Kain can. The cover sourcing commissioned to Cowork under the S306 note is closed, not deferred.

# REPORT: all 680 book covers are sourced, and all 65 live pages render one

**From:** Claude Code, Session 089. **Date:** 31 August 2026.
**Ruled by:** Kain, in the sitting: "go through that exact same process and get all of these book covers that we need... I don't want this deferred."
**Supersedes section 1 of** `REPORT__The_Book_Covers_Are_Machinery_And_A_Sourcing_Gap_S089`, filed earlier the same session, which said no code change could fill the 64 dark pages and that the artwork had to be sourced by a human. **That was wrong, and how it was wrong is section 1.**
**Board card:** Book Notes. **Shipped:** theme v0.119.1, deployed and proved.

---

## 1. The correction I owe first

Earlier this session I reported that the 64 dark book note pages had no artwork anywhere, that no code change filled them, and that the job belonged to Cowork under the S306 note.

**The artwork gap was real. The conclusion was not.** The covers did not exist on disk, and I treated "not on disk" as "has to be found by a person". This project had already built a machine that finds them, ran it twice, and got 599 of 620 covers out of it. I did not check whether that machine existed before saying the job needed a human, and Kain had to tell me it did.

**And it was not in the theme, which is why it had to be asked for.** The S049 and S053 script was written in a scratchpad and never committed. The channel Archive holds the record describing the method; nothing on disk could run it. The only surviving copy was inside old session transcripts, and it was recovered from there this session.

**It is `tools/book_cover_source.py` now**, under version control, for that reason and no other.

## 2. The ladder, read from the record rather than recalled

From `DELIVERY__The_Second_Cover_Pass_S053` and `RECORD__ISBN_And_Cover_Run_S049`, both in the channel Archive, with what each source actually delivered on 620 real books:

1. **Apple Books, the public iTunes Search API.** The backbone. No key, no account, no cost. The API advertises a 100px thumbnail as `artworkUrl100`, and the size in that address is a request rather than a ceiling: rewriting it to `2000x2000bb` returns the original artwork. That one line is why S049 ended with 44 low resolution rows, because it took the address as given.
2. **Archive.org**, reached through Open Library's record of the scan. The largest files in the set, up to 4448px.
3. **Open Library by cover id.**
4. **Google Books.** Recorded as untested rather than failed at S053, because the keyless endpoint answered 429 throughout. Retried here.
5. **Amazon by ISBN**, last, and it supplied one file in the whole of S053.

**The rule that does not move:** every candidate is checked back against the expected title and author before its file is kept, the whole result list is read rather than the first answer, derivative works are filtered, and nothing is upscaled. A wrong cover is worse than no cover.

**Two things added this session.** Apple's audiobook catalogue as well as its ebook one, because an older title never issued as an ebook still has cover art on an audiobook edition. And an `--upgrade` mode, so a cover that is present but under the 900px bar can be refetched, which is Kain's S252 ruling working: "no low_res flag, get proper pictures for all of them."

## 3. The result, read off the disk rather than off the run

| | |
|---|---|
| master rows | 680 |
| rows holding a cover file that opens | **680** |
| at 900px or better | **677** |
| under the bar | 3 |
| median long edge | 2000px |
| largest | 4448px |
| rows with no file | **0** |

Eighty covers were sourced this session. Nothing was found for none of them.

**The three under the bar**, at 500px each, correct books at too small a size: `the-feeling-good-handbook`, `a-guide-to-rational-living`, `the-psychology-of-self-esteem`. Every source on the ladder was walked for each; Apple, Archive.org and Google hold no matching edition, and the check correctly refused the near misses it was offered. They are the hand-work list and they are three rows, against 64 at the start of the day.

`cover_status` in the master is rewritten from the disk rather than from anyone's belief about it, which is the direction it has been wrong before: the S306 note records it marking 16 rows `ok` when no file existed for any of the 16. It now reads 677 `ok` and 3 `low_res`. The superseded workbook is archived as `Book_Note_Master__superseded_S089_pre_cover_status.xlsx`.

## 4. The fault that every count in this run missed

**64 uploaded, 64 attached, 65 read back carrying an attachment id. Every number correct, and all 65 pages were rendering a broken image.**

An ACF field is **two** meta rows, not one: the value, and `_book_cover_image` holding the field's key. `get_field()` reads the key to learn what kind of field it is looking at. `wp post meta update` writes one row, so ACF had no way to know the value was an image id, handed the template the raw integer, and the page emitted `<img src="34124">`. A browser reads that as an IP address and asks `http://0.0.133.76/` for a book cover.

**Nothing in the run could see it.** Only `naturalWidth` on the rendered page, which is zero on an image the browser failed to fetch. It was found by reading the page rather than by reading the code, which is the S088 lesson arriving again in different clothes.

Fixed in three places: both meta rows are written together by the tool and by the importer; the template resolves a bare attachment id rather than printing it, as a second line of defence; and the media library index reads a source-filename stamp, because WordPress renames a file on collision and an index keyed on the stored name uploaded one cover twice.

**Read back on every published page: 65 of 65 covers load.** The three shortest are the three named above.

**One orphan attachment is left in the media library**, id 34148, the duplicate that fault created. It is not deleted, because deleting is not mine to do; it is named so it can be.

OWED BACK: nothing. The Cowork cover sourcing named in the earlier report is no longer owed, and the sourcing line on the Book Notes card can close.

*No em or en dashes in this file; checked before writing.*
