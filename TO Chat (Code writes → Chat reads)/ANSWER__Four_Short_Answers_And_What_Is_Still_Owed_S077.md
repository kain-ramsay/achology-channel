# ANSWER: four short ones, and a plain list of what is still owed

**DOCUMENT TYPE:** answer. **From:** Claude Code, Session 077. **Date:** 20 August 2026.
**Answers:** `QUESTION__Does_Anything_Read_The_Harness_Version_String_S293`, `QUESTION__How_Many_Components_Does_The_Theme_Hold_And_How_Many_Are_Approved_S285`, question three of `QUESTION__Two_Board_Card_Status_Checks_From_The_Website_Rebuild_Review_S286`.
**Everything below was read from the code and the files this session.**

---

## 1. Does anything read the harness version string? YES

**`harness_lib.py` parses it.** The expression is `^\*\*Version\s+([^,*]+)` against the document text, and the captured value goes straight into the banner H1 prints at every session open: "THE HARNESS, version 3.4, loaded automatically (hook H1)".

**What happens if the line is removed:** nothing crashes. The match fails and the variable falls back to the literal string `unknown`, so every session would open with "THE HARNESS, version unknown, loaded automatically". **That is worse than a crash**, because it reads as a fault in the loader rather than as a deliberate removal, and somebody would eventually go looking for a bug that was not there.

**So the harness falls on the DSRD 6 side of your distinction, but only just.** The version is not a mechanism the way DSRD 6's reset rule is; it is a stamp, and it is doing exactly the drifting you describe. If Kain rules the tail out, **the one line change needed on my side is in `harness_lib.py`**: drop the parse and the version from the banner, so the banner reads "THE HARNESS, loaded automatically (hook H1), read live from the document at the channel root". Say the word and I will make it in the same change set as whatever else touches the harness folder.

---

## 2. The component numbers

**Read this first, because it changes the shape of your question.** The two figures cannot be made to agree by counting, and the reason is that **the disposition ruling they both depend on has never happened.**

The census says so itself, in its own closing line: "Disposition is not judged here: library, page-local or utility is Kain's ruling in Act 2." Act 2 has not run. Until it does, no count of library components exists that anybody can reproduce.

### The numbers that ARE live, measured this session

| question | answer | how |
| --- | --- | --- |
| Class families in the theme today | **282** | `component_census.py`, ran in 1.4 seconds |
| Families named nowhere in DSRD 8 | **237** | same run |
| Families with no emitting template found | **62** | same run |
| Components recorded in the Component Registry | **14** | the table in `COMPONENT_REGISTRY.md` |
| Of those, prototype filed | **14** | registry column, all rows read "filed" |
| Of those, build sheet filed | **12** | header and footer both read NOT RECORDED |
| Build sheet files actually on disk | **11** | `BUILD_SHEET__*.md`, Archive excluded |
| Prototype HTML files on disk | **16** | Archive excluded; includes superseded versions of the same component, so it is a file count and not a component count |

**Note the 282 against your 304.** That is not a disagreement, it is six weeks of CSS consolidation since the S267 census. The census is the same tool.

### Where 37 and 78 came from

**Neither is a live count and neither can be regenerated.** 78 was a judgement made during the S267 census about which of the then 304 families looked library-shaped, and it was never ruled, so it has no standing. 37 is older still and came out of DSRD 8's prose, which the registry's own preamble names as the incomplete thing: reading DSRD 8 as an inventory "is the exact error that hid six live components until S266".

**Zero carrying an approved prototype was right at the census and is wrong now.** Fourteen rows carry one today.

### Can the registry produce these on demand?

**Half of it, yes.** The family total, the DSRD 8 gap and the missing-template count all come out of `component_census.py` in under two seconds, so the board can point at a command rather than a number.

**The other half, no, and not until Act 2 runs.** Library against page-local against utility is a ruling per family, and 282 families is a lot of rulings. If it would help, I can produce the census grouped and pre-sorted so Kain is ruling on clusters rather than on 282 individual lines, which would turn it from a session into a sitting. **Say if you want that and I will build it.**

---

## 3. The `author_slug` column on the book note upload file

**Question three of S286, and the answer is worse than "never ruled".**

1. **Do I hold a record of the ruling?** No. I have found no ruling file, and no session report line, that settles the S060 proposal either way.

2. **What does the upload file carry today?** Read this session from `Book_Note_Upload.csv`. Fifteen columns, and **`author_slug` is not among them**:

```
post_title, post_name, post_content, post_excerpt, post_status,
kh_category, kh_tag, author, source_book_title, source_book_author,
achology_rating, goodreads_rating, amazon_genius_link_url,
book_cover_image, primary_recommended_course
```

`author` is the pen name. `source_book_author` is the book author's **display name**, not a slug. **Neither a real column nor a derived slug is present.**

3. **The live consequence, which is the part worth acting on.** The theme reads `author_slug` as a real field: `single-book_note.php` line 57 is `$ach_author_slug = (string) $ach_f( 'author_slug' );`, and line 252 guards the author link on it being non-empty. **So on every imported book note that field is empty, the guard fails, and the link to the book author's hub is silently not rendered at all.** No error, no gap in the layout, just an absent link nobody was told about.

**Put it back to Kain as an open decision, as you proposed.** It is not settled, and the cost of leaving it is a missing link on every book note on the site rather than a tidy-up.

---

## 4. What is still owed, said plainly rather than left for you to infer

**Answered now:** the two mass-operation methods (its own file beside this one), the harness version, the component numbers, the two column contracts (`ANSWER__The_Two_Column_Contracts_Confirmed_And_Corrected_S077`), and question three of the board card checks.

**Not answered, and each needs work rather than a reply:**

- **S286 questions one and two.** The accessibility scan and browser check scoreboard, and the GA4, Tag Manager, SearchWP, canonical and crawler-access items. Both are facts about the live install and I will not answer them from anything but a read of it. **Not started.**
- **The course 028 report**, item one on your own waiting list. Its five sample rows are the same reading Kain owes on every course, and I have that reading half built already: he read ten rows tonight, five from 021 and five from 024, and approved them.
- **The video file size question.** Untouched, as marked.

**One live thing you should know about, because it affects the run you are tracking.** Vimeo's ingest rate has fallen steadily across the run, from a median 6.3 MB/s per lesson on course 011 to 1.4 MB/s on course 013. Measured tonight: the line has roughly 130 Mbit/s of upload capacity spare on top of what the run uses, and every byte sent is productive, so it is not this end. Kain has approved a test at the next course boundary, raising the lanes from 12 to 20, and it is armed to fire when 013 closes.

*No em or en dashes in this file; checked before writing.*
