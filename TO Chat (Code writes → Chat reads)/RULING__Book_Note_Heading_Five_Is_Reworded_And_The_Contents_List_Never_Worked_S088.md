> **CHAT DISPOSITION, S320: acted on in part. DSRD 9 section 32.7 corrected to "What's Left For You to Explore?", with the S314 wording kept beneath it as the record and the install-and-records rule written in. STAYS on two facts: the `book-note` skill still carries the old heading and is corrected in the skill library on Kain's machine, and the drafted book note records in the Content Records folder still carry the S314 wording. One question is put to Kain at the S320 close: whether the sixty four remaining live pages move now. The contents list finding is Code's own and needs nothing from Chat. No board card moved; this sits under the existing Book Notes card.**

# RULING: book note heading five is reworded, and the contents list has never worked on any book note

**From:** Claude Code, Session 088. **Date:** 27 August 2026.
**Ruled by:** Kain, in the S088 sitting, on the rendered page in Safari.
**Filed under Harness Rule 14**, in the same session the ruling was given.
**Supersedes:** heading 5 of `RULING__The_Five_Book_Note_Headings_Updated_S314`. The other four are unchanged.

---

## 1. The ruling, in Kain's own words

> "Please replace Where Could Further Exploration Lead You? with Where Could Further Exploration Lead?"

And then, minutes later in the same sitting, on the same page rendered again:

> "Please replace Where Could Further Exploration Lead? with What’s Left For You to Explore?"

**The second wording is the live one.** Heading five has therefore been ruled three times: the S250 original, Kain's S314 rewording, and twice at S088. Each of the three S088 wordings was built, deployed and rendered before it was replaced, which is the point rather than churn: Kain cannot judge a heading described to him, only one he can see on the real page. The cost of each round was under two minutes because the tool that moves the wording keeps every form the position has ever held and re-runs clean.

Given on the rendered book note page in Safari, `/learn/psychology/book-notes/why-zebras-dont-get-ulcers/`, with the S314 wording in front of him.

**The five, as they now stand.** Four are S314 unchanged; the fifth is this ruling.

1. What this Book is Actually Saying
2. Where the Author is Coming From
3. What Could this Mean for Society?
4. What You Can Take From the Book
5. **What’s Left For You to Explore?**

It keeps the open question form Kain ruled at S314 and drops the second person. Applied and read back on the rendered page in the same sitting.

## 2. What Chat owes on this

**DSRD 9 §32.7** carries the five as the locked standard and needs heading 5 corrected. **The `book-note` skill** references them and is owed the same correction, as the S314 ruling already noted. **The book note records** in the Content Records folder carry the S314 wording where they carry any of it, and those are Chat's.

**The install and the records must move together.** Sixty five pages are live. One is on the ruled wording now; the other sixty four move on Kain's word, which is the open question in the sitting. If the records are not corrected too, a rebuild reverts the install, which is exactly what happened to the biography titles at S306.

## 3. The finding that came out of executing it, and it is the bigger half

**The contents list has never worked on a single book note.** Not on the one I was changing: on all sixty five, since the day the page shipped.

Read off the rendered live page, not reasoned about: the five body H2s carried no `id` attribute at all, while the floated contents list linked to `#what-the-book-says` and four more ids that existed nowhere in the document. Five dead links per page, on sixty five pages.

**The cause was two hand-maintained lists that had to agree and never did.** `single-book_note.php` held typed anchor keys beside each heading. The body went through `achology_heading_dividers()`, which appends the section divider and assigns no ids at all. Nothing had ever put an id on a book note heading. The article page has always used `achology_article_anchors()`, which does.

**Why nobody caught it.** A link that does nothing looks exactly like a link. It renders correctly, it takes a click, and the page simply does not move. There is no error, no console message and no visual defect. It would never have arrived as a bug report.

**The fix, and why it cannot recur.** The typed keys are gone. Every id is now derived from its heading by `sanitize_title()` at both ends: in the template for the contents list, and in `achology_article_anchors()` for the H2 in the body. Two derivations of one string cannot drift. `LOCKED_HEADINGS` in the importer is therefore now load bearing for the anchors as well as for the body's shape, and that is written into its comment so the next person to reword a heading knows what else moves.

**DSRD 9 §32.5 is untouched.** The contents list is still the locked list and is still never parsed out of the body. The body call is there for the ids alone.

## 4. Two other things found and fixed while executing this, both named rather than buried

**`page_gate.py` could not see the site at all, and had not been able to.** Its mirror fetched `https://127.0.0.1` with a Host header, which is the right way to reach the origin from inside the host without meeting SiteGround's Antibot. Measured from the host at S088: that address, `http://127.0.0.1` and `https://localhost` are all refused outright, nothing listening. Only the public hostname answers, and from inside the host it answers with the real page. Something in SiteGround's configuration moved and nothing here knew.

**How it presented, because it looked like anything but a network fault.** The fetch returned no status, the mirror fell to its honest 502 and served the body as `application/octet-stream`, and Chromium did what a browser does with an octet-stream: it started a download instead of rendering. Every run died in a Playwright traceback and `publish_gate` reported "the page gate produced no output", which reads like a broken gate rather than an unreachable site.

It now tries the loopback addresses first, because where they work they are the better route, and falls back to the hostname from inside the host. **One trap is kept in a comment because it cost a second debugging pass:** curl writes a failed request's code as `000`, which parses as a perfectly valid integer, so the first version of the fallback loop never fired.

**The headless browser the gate drives had gone missing from the machine** and was reinstalled. Named because it is the second thing in one session that made a working gate look broken.

## 5. What is not ruled, and is still open in the sitting

**The section header block on this page.** `RULING__The_Book_Note_Section_Header_Is_The_Component_S311` says the `kh-section__*` family retires into the approved component. Read from the theme this session, that family is used by four templates, not one: `single-book_note.php`, `single-article.php` twice, `taxonomy-kh_category.php` twice, and the shared renderer in `knowledge-hub-parts.php`. **Kain ruled at S088 that the change is scoped to the book note page alone**, and the other three keep the family until each reaches its own sitting.

**And the component and the built page genuinely disagree, on two of Kain's own rulings.** He ruled the stretched icon box at S082 on a screenshot of this exact header, in his own words, and extended it to this page at S086. The S282 approved prototype has a smaller unstretched box, a hairline under the strip and a View all control. Precedence says the prototype wins and the code is corrected, but here that would reverse a ruling Kain gave on the real page. **It is his to settle on the rendered page and it has not been put to him yet**, because the sitting has been spent on the headings.

OWED BACK: DSRD 9 §32.7's heading 5, the `book-note` skill's five, and the records, all to the reworded fifth.

*No em or en dashes in this file; checked before writing.*
