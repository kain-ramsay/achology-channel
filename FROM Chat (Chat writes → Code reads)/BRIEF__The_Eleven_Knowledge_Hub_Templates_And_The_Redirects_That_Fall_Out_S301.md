# BRIEF: the Knowledge Hub page templates, all eleven, and the redirects that fall out of them

**From:** Claude Chat, S301 close
**To:** Claude Code
**Status:** Approved by Kain in session, S301. This governs the next run of work on both sides.

---

## The task, in Kain's own framing

**Every Knowledge Hub page template, taken one at a time, in order, until all eleven are confirmed. Nothing digresses until they are done.**

This includes pages that already exist. The book note page is built and live on the test site; it gets the same treatment. The article page has a spec; it gets the same treatment. **Nothing is exempt because someone already looked at it once.**

## What "confirmed" means

Four things, in this order, on every page:

1. **Verify.** What does the theme actually hold for this page today? Read from the code, never from memory or from a spec. Name the template file, or say plainly that none exists.
2. **Analyse objectively.** Against DSRD 2 (what the page holds) and DSRD 9 (how it is laid out). Report every gap and every disagreement, including where the built page is right and the specification is wrong.
3. **Amend.** Fix what is wrong or missing.
4. **Kain signs it by eye** on the real rendered page in Safari, on his Mac, his iPad and his phone.

A page is confirmed only when Kain has looked at the real thing and approved it.

## Why the order runs this way

**A column exists only because a template reads it.** The project has been running that backwards, which is how fifty quote pages came to be written with no route to the site.

So: **no CSV contract for any content type is written until its page is confirmed.** Once it is confirmed, you read the built template back and the column list falls out of it as a read rather than a guess. That is your own recommendation from `ANSWER__The_Quote_Template_Does_Not_Exist_And_What_That_Changes_S079`, and it is now the standing order.

## The eleven

The list is the one on the Notion card `Knowledge Hub Page Designs: all eleven, one per session, in order`. Article, quote, workbook, list pages, category pages, hub front page, author pages, tag pages, book note, search results, and the all-authors-and-all-tags index pair.

That card holds the current state of each line and is the authority on what is left. Order within the eleven is Kain's to set as we go.

---

## The redirects, and this is the part that changes how you work

**Ruled by Kain, S301: the redirect map is built per page type, inside this task. It is not a separate sweep at the end.**

**Why it matters, stated plainly so nobody treats it as admin.** Achology.com carries years of Google ranking on its current addresses. Every indexed address is an asset. An address that 404s after cutover loses its ranking, its traffic, and the sales that came through it. It also breaks inbound links from other sites, the internal links inside the 249 help articles, links in old emails, and readers' bookmarks. And it is one shot: get it wrong on cutover day and the recovery runs for months.

**Why per page type rather than one sweep at the end.** A new address only exists once its page template is confirmed. Doing it at the end lands a few thousand decisions in one sitting, cold, under launch pressure. Doing it per type keeps each batch small, in context, and decided by the person who just confirmed the page.

### The method, per page type

1. **The old addresses come from the Google Search Console export, never from guessing.**

   **The export already exists and is on disk.** Karen pulled it on 18 August 2026. It lives in the `Search Console + Live Site Exports` folder inside the `05. Spreadsheets | Data | CSV Files` folder. Read that folder's own `000__WHAT_IS_IN_HERE.md` before using anything in it; it explains what each file is and what each one does not contain.

   Three things worth knowing before you start, taken from that README rather than assumed:

   - The **Performance** export's `Pages.csv` is the priority file: every page with clicks, impressions, click-through rate and average position. **Google caps that download at 1,000 rows**, so it is the top 1,000 pages by traffic, not the whole site.
   - **`live-site-urls.csv`** is the fuller address list. Performance does not replace it; it says which of those addresses actually matter.
   - The **Coverage** export **carries no addresses at all**, only counts. Do not go looking for a list in it. What it does tell us: **134 addresses on the live site already return 404 today**, and 96 already redirect.
2. As each page type is confirmed, take the old addresses that map to that type.
3. Write one row per old address: **old address, new address, reason.**
4. **One home: DSRD 1 section 11.** Never mirrored.
5. Apply the rows and test every one. **No 404s on any indexed address. No redirect chains.**
6. **Any old address with no new home is Kain's call, never a default.** Nearest parent page, or gone on purpose. Bring those to Chat as a short list rather than deciding them.

**A checked-and-nothing-owed result is a real answer and gets written down.** Where a page type turns out to own no old addresses, say so in DSRD 1 section 11 rather than leaving it silent.

---

## What comes back to Chat, per page

One file in TO Chat carrying: what the theme actually held before you touched it, what you changed, the DSRD 6 record, the field list the confirmed template reads, and the redirect rows written for that type (including an empty finding).

*No em or en dashes in this file; checked before writing.*
