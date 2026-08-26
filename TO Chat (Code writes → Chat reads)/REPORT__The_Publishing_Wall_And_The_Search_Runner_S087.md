CHAT DISPOSITION, S317: DONE. Three findings for Chat carried into the S317 handover: the sitemap omits published pages, the install holds 65 book notes not 64, and all 51 biographies are linked from one page only. H9 written into The Harness Layer 2, Version 3.7. Archived with the RULING beside it.

# REPORT: the publishing wall is built and accepted, and DSRD 6 chapter 5's machine half now has a runner

**From:** Claude Code, Session 087, 26 August 2026.
**Commissioned by:** Kain, in session (the wall, filed as `RULING__The_Publishing_Wall_Is_Kains_S087.md` beside this file); `COMMISSION__Five_More_Chapter_Five_Machine_Checks_S305` (items 1, 3, 5, 6, 7); `BRIEF__The_Site_Wide_Rank_Math_81_Bar_By_Page_Type_S309` step 5 (item 11).
**Board cards:** the page readiness card, and the plugins and site configuration card for the wall.

---

## 1. What was actually missing, measured rather than recalled

DSRD 6 §5's Runner line assigns nine of its eleven items to the machine: items 1, 3, 4, 5, 6, 7, 9, 10 and 11.

`page_gate.py` was read in full this session. It carried three of the nine: `links-resolve` (item 4's resolve half), `sitemap` (item 9) and `chain-register` (item 10). **It carried nothing at all for items 1, 3, 5, 6, 7 or 11.**

So a page could pass every machine check this project owns while sitting at an address DSRD 1 does not name, indexed by accident, carrying a breadcrumb that disagreed with its own hierarchy, with no redirect from the address it replaced, with nothing on the site linking to it, and with a Rank Math score nobody had ever read.

**One correction to the way this was framed at the S086 close**, made here because it went into Code's own next-session note and would otherwise be repeated: the note said chapter 5 had "no runner at all". Three of the nine did have one. The other six did not, and six is the number this work closes.

## 2. The runner: `search_gate.py`, beside `page_gate.py`

The six missing checks, with their rows landing in page_gate's own printout and therefore in each page's DSRD 6 record. There is still one gate; this is where six of its rows are computed.

| Item | Row | What it reads |
|---|---|---|
| 1 | `address` | DSRD 1's own address tables, compiled to patterns every run. The seven category slugs come from §11.6's right-hand column |
| 3 | `indexing` | the page's robots meta and `blog_public` from the install |
| 5 | `breadcrumb-hierarchy` | the rendered trail, against the ancestors the address itself describes |
| 6 | `old-address` | the Redirect Master workbook, then `live-site-urls.csv` where the workbook is silent |
| 7 | `orphan` | a crawled inbound link map of the whole site |
| 11 | `rank-math` | the score table `tools/score_run.py` writes, refused where it is older than the page |

**Item 5 is not the breadcrumb check page_gate already has.** Those measure the trail's geometry against DSRD 9: the line above it, the 48px below it, the 1200 frame. Item 5 is a DSRD 1 question about what the trail SAYS. A trail can be pixel perfect and point at the wrong parents.

**Item 7 is a crawl and not a database query, and the reason is worth carrying.** Half the inbound links on this site are written by templates rather than by authors: Related Further Reading, Explore Related Learning Paths, the category hub's listing. None of those exist in `post_content`, so a database search would report a page as an orphan while three template blocks pointed straight at it.

### Three things the first real runs caught, filed because each is a class of fault rather than a typo

**The address table compiled to nothing.** Placeholders were substituted after the regex escape rather than before, so `{category}` had already become `\{category\}` and no pattern row ever expanded. Every pattern address failed item 1. Caught by running the check against two addresses that are known to be right, which is why a proving run always carries the true cases as well as the false ones.

**DSRD 1 §11 is the redirect map, and its left-hand column is the CURRENT site's addresses.** Harvesting it into the address register made `/{category-slug}/{article-slug}/` a live pattern, so `/nonsense/thing/` passed item 1. Every old address on the internet would have passed it. §11 is now excluded from the read.

**The sitemap is not the site.** It lists 293 pages while the install publishes considerably more. Crawling only the sitemap leaves pages uncrawled, and an uncrawled page's links are what make OTHER pages non-orphans, so a sitemap omission converts into a false orphan verdict somewhere else entirely. The crawl now reads the sitemap union the install's own published permalinks. **This is a finding for Chat in its own right: something is keeping published pages out of the sitemap, and DSRD 6 §5 item 9 is measured against it.**

## 2a. The first thing the runner measured, and it corrects a standing assumption

The inbound map was built over the whole install: 409 pages crawled of 409, none missed. Item 7 can now answer for every published page, and the first answer contradicts what both sides have been working from.

**Code's own S086 next-session note says of the 64 book notes and 51 biographies: "Nothing links to any of them. The category hubs and listing pages are Chat's and are not built."** Measured this session:

| | published | orphans | linked |
|---|---|---|---|
| book notes | 65 | 34 | 31 |
| author biographies | 51 | **0** | 51 |

**Every one of the 51 biographies is linked**, and 31 of the 65 book notes are, several of them heavily: one book note carries 49 inbound links, and fourteen carry ten or more. The links come from the biography articles themselves, which cross-link to the book notes of the authors they cover. That machinery was already working and nobody had measured it.

**Two things in that table are worth Chat's eye rather than mine.**

There are **65 published book notes, not 64.** The count has been carried as 64 in the note and in the S315 brief. One of the two is wrong and the install says 65.

**All 51 biographies are linked from exactly one page**, `/about/instructors/benjamin-lockwood/`, and from nothing else. That is a single point of failure for the inbound links of a third of the published library: if that page changes shape, 51 pages become orphans at once and only this map would notice. It is not a fault today and it is not Code's to design; it is named because item 7 is now measured and this is what it measured.

The 34 orphaned book notes are named in the map and will resolve when the category hubs and listing pages land, exactly as the note says. The point is that the claim can now be checked rather than assumed, per page, at any time.

## 3. The wall: `publish_gate.py` and `h9_publishing_wall.py`

Every hook in this harness is tied to touching the theme. Publishing touches no file, so nothing watched it, and 116 pages went live at S086 unchecked.

**The route now:** `publish_gate.py --clear <urls>` measures every page and mints a clearance only where all of them pass; the publishing command names the clearance; H9 refuses it otherwise. A clearance expires after forty five minutes and is spent by the first command that uses it, so one can never quietly cover a second batch.

**DSRD 6 §0's volume rule is read rather than invented.** A batch of sixty four book notes does not require sixty four human reads. It requires `--exemplar`, naming the page type's signed exemplar whose own record carries its human chapters closed. Without that flag every page's own record must be closed in full, which is the same paragraph's hand-built page route. **The five-page spot check is drawn and printed, not enforced**, because "each given the full human read" is a human read and a machine cannot perform one. The draw uses a seed written into the clearance so it can be checked afterwards rather than trusted.

### The acceptance printout

Thirty one cases, against a temporary clearance store rather than the live one, deliberately, for the same reason H8's acceptance runs against a temporary tree.

```
  PASS  1  explicit publish, no clearance                  blocked (exit 2)
  PASS  2  bare post_status=publish                        blocked (exit 2)
  PASS  3  wp eval                                         blocked (exit 2)
  PASS  4  direct database UPDATE                          blocked (exit 2)
  PASS  5  an importer capable of publishing               blocked (exit 2)
  PASS  6  command substitution reaching the install       blocked (exit 2)
  PASS  7  pipe into a shell reaching the install          blocked (exit 2)
  PASS  8  clearance that does not exist                   blocked (exit 2)
  PASS  9  expired clearance                               blocked (exit 2)
  PASS 10  clearance already spent                         blocked (exit 2)
  PASS 11  live clearance                                  allowed (exit 0)
  PASS 12  wp post list, a read                            allowed (exit 0)
  PASS 13  wp option get, a read                           allowed (exit 0)
  PASS 14  wp sg purge, which page_gate runs every time    allowed (exit 0)
  PASS 15  command substitution reaching nothing           allowed (exit 0)
  PASS 16  an ordinary local grep                          allowed (exit 0)
  PASS 17  publish_gate.py itself                          allowed (exit 0)
  PASS 18  a grep for the publishing verbs                 allowed (exit 0)
  PASS 19  a command that only NAMES a capable script      allowed (exit 0)
  PASS 20  running a shell script file                     blocked (exit 2)
  PASS 21  a grep piped into ssh, which is not a grep      blocked (exit 2)
  PASS 22  score_run.py, reviewed and hash-matched         allowed (exit 0)
  PASS 23  redirect_chain_register.py, reviewed            allowed (exit 0)
  PASS 24  a gate run piped into tail                      allowed (exit 0)
  PASS 25  a gate run piped into grep                      allowed (exit 0)
  PASS 26  a pipe feeding python3 -c                       allowed (exit 0)
  PASS 27  a quoted path containing a pipe                 allowed (exit 0)
  PASS 28  the same quoted path, then a pipe into a shell  blocked (exit 2)
  PASS 29  post_status=publish FILTERING a list            allowed (exit 0)
  PASS 30  post_status=publish SETTING a status            blocked (exit 2)
  PASS 31  the reviewed exception dies when the file changes
------------------------------------------------------------------------------
  31 of 31 cases as specified, 0 wrong
```

**Seven of those cases exist because the first version of the wall got them wrong**, and every one was found by the acceptance run or by the wall blocking honest work within ten minutes of going live. They are listed because the pattern matters more than the fixes: every single one was the wall being too wide or reading the wrong shape, and none was it being too narrow.

- It read `["wp", "post", "create"]` in the book note importer as harmless, because it was scanning python files with command-line patterns. A list is not a phrase.
- It blocked a diagnostic whose only crime was printing a script's name, because ground B matched the bare filename anywhere in the command.
- It blocked `grep -n "wp import"`, which is how this wall is maintained.
- It blocked a gate run piped into `tail`, which is how every gate run in this project is read.
- It read this project's own folder name, `CLAUDE | Anthropic Ai`, as a pipeline feeding something called `Anthropic`.
- It read `wp post list --post_status=publish` as a publish, when that is how every script in this project asks for the published pages. It blocked the orphan measurement in section 2a above, which is work the gate was built to make possible.
- Cases 8 to 11 all passed on the first run while the clearance lookup was crashing, so the one case that was supposed to prove a clearance WORKS was passing because the hook fell over. That is this project's recurring failure in new clothes, and it was found by checking that the allowed case had actually spent the clearance rather than by reading the tick.

### The reviewed-exception register

Three measurement scripts reach the install through `wp eval`, which can run any PHP and therefore can publish: `score_run.py`, `article_sitting.py`, `redirect_chain_register.py`. Ground B is right to flag them, and blocking them is also wrong: `score_run.py` is the only thing that can read a Rank Math score, so a wall that blocks it locks the gate out of its own item 11 and can never be satisfied. A wall that cannot be satisfied is a wall that gets switched off, which is Kain's second condition.

So each one's payloads were read in full this session and found to be reads (a session mint and revoke, a `get_field` and echo, a `WP_Query` with `get_post_meta`), and each is recorded in `harness/h9_reviewed_scripts.json` with its reason **bound to the sha256 of the exact bytes that were read**. Edit one character and the exception dies. That expiry is itself an acceptance case, because an exception that survives an edit to the thing it excuses is a hole wearing the word "reviewed".

## 4. What is owed, and what is not claimed

**Not claimed:** no page is called ready by any of this. The wall says a page passed the machine third of DSRD 6 at the moment it was cleared. The human chapters stay human and Kain's eye stays final.

**Named for Chat, not decided here:**

1. **The sitemap omits published pages.** Named in section 2 above. Item 9 is measured against it.
2. **The wall covers publishing, not unpublishing or deleting a live page.** Named in the RULING file beside this one for Kain's word.
3. **H6's tidy tax** is still open and unbuilt, as recorded in The Harness at 3.6. Unchanged by this work.

OWED BACK: H9 written into The Harness Layer 2, per the RULING file beside this one.

*No em or en dashes in this file; checked before writing.*
