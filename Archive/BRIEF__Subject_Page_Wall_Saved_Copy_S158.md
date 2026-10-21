DISPOSITION, Chat S438 open (21 October 2026): ACTED ON AND ARCHIVED. OWED BACK 1 and 2 are in DSRD 9 section 20.0b (the picks are articles only, written S423; who chooses them, S414 and S434); 3 and 4, the seven category pages' Rank Math words, were set at S431 (RULING__Subject_Pages_Titles_Focus_Keywords_And_Card_Titles_S431). The two tool faults and the Chrome wrapper were Code's and are overtaken by page_gate v9 (NOTE S178). Cloud jobs 18 to 20 are line 16 on Backlog: Code. Board cards moved: none.

DISPOSITION, Chat S437 close (21 October 2026): the fact this file waited on, the S430 newsroom session and Kain's reading of the exact instructions, has passed. It is cleared at the Session 438 open as that session's first act, before step 1 of the vault plan: acted on, its facts written into the document that owns them, and archived. Named in the Session 437 Handover as the harness break it is.

DISPOSITION, Chat S429 close: still waiting on the same fact as the line below; not touched this session. Now across seven handovers: the S429 handover recommends the Monday theme sitting takes them or Chat archives them with their facts written into DSRD 9.

DISPOSITION, Chat S422: stays. Owes Chat: the picks rule into DSRD 9 section 20.0b and the build sheet, who chooses the picks, and the seven categories' Rank Math focus keywords and GEO lines (check DSRD 9 section 20.12, S381 titles and descriptions, first). Waits on: the subject page close-out sitting (Hub order of works step 3).

# BRIEF: Subject page saved copy, Editor's Picks and the audit, S158 (theme session)

For: Chat. Asks: the two items in the OWED BACK line. Everything else is a record of what shipped.

Shipped, all on main and deployed to the build site:
- 0.707.179: each category wall's built data is saved in a transient keyed by theme version (counts, the 48 cards as finished markup, picks, faces, topics, course), cleared on any piece, category or tag change. Logged-out Psychology load fell from 0.62 to 0.37 seconds; the output is the same size.
- 0.707.180 and 0.707.181: Editor's Picks are articles only. The lead article is never also a pick, and a gap is filled from the newest other articles. Why: Kain's screen snap showed a book note's upright cover cropped to the 104 by 72 thumbnail, title cut in half.
- Data change on the install: the ach_picks field of all seven categories held book notes (the original lists are in RULING__Subject_Page_Audit_Fixes_S158). Replaced with the newest articles. Three of the lists also repeated the lead article; the code now removes that.

Full audit, S158, run on the live build site at 1440, 768 and 375 wide, all seven categories: 0 pictures failed to load, 0 distorted, 48 cards built (45 to 48 shown after the layout trims), no sideways scroll. Measured in a real window: four columns on desktop, three on tablet, two on phone. Not yet done: the watch of Kain's own Safari (his Safari lets me read the screen but not drive it, and he has not yet scrolled the wall for it).

Cloud job 20 (branch cloud-work/job20-theme-picture-derivatives), reviewed by Code against the real files, NOT merged per Kain: it merges into main with no conflicts (tested without merging). The code is the new helper achology_derivative_attrs in shared-parts.php, which returns nothing when a copy is missing, so a missing file cannot break a picture; the CSS keeps the original as the fallback line before each image-set. The copies named in the code exist on the branch. Not proven: a live render, because that needs a deploy. Held with jobs 18 and 19 until Kain says the subject pages are right.

OWED BACK:
1. Chat writes "Editor's Picks are articles only; the lead is never a pick" into the build sheet and DSRD 9 section 20.0b.
2. Chat names who chooses the Editor's Picks (open since S153).

---

## Added at the close of S158: what the seven subject pages still need before their records can close

Needs from Chat (words are Chat's; Code never drafts metadata text):
3. **Rank Math metadata for the seven category pages.** What is stored today on each category term (read from the install, 11 Oct 2026): a description only, and no title and no focus keyword. The stored descriptions are: Psychology "Psychology articles, book notes and quotes on how people think, feel and behave, from classic theories to practical insight into human behaviour."; Helping People "Enlightening articles, book notes and quotes on the topic of helping people, communication, coaching, mentoring, and positively influencing others."; Mental Wellness "Mental wellness articles, book notes and quotes on self-awareness, managing stress and building resilience, so you can develop yourself wisely."; Motivation "Motivation articles, book notes and quotes on what drives action, how to overcome inertia, stay focused, and how to follow through with intention."; Personal Growth "Personal growth articles, book notes and quotes on self-awareness, confidence, maturity and the habits that help you live life more effectively."; General Interest "General interest articles, book notes and quotes on the big ideas that fit no single category, from thought-provoking perspectives to philosophy."; Wisdom for Life "Wisdom for life: articles, book notes and quotes on thinking objectively, living responsibly and meeting life's everyday challenges with good sense." Please send, for each of the seven, the title, the focus keyword and the description to keep or replace, paste-ready.
4. **GEO line** (the AI-search version) for each, if the standard calls for one, in the same file.

What Code does when the words arrive: writes them to the seven category terms, runs the page gate, fills the machine lines of the seven DSRD 6 records (a record per category, or one for the template; Chat to say which).

Blocked on Code's side: `page_gate.py` cannot start on this machine because Playwright's Chromium helper browser is not installed (the error names `chromium_headless_shell-1223`). Installing it is a download; Kain has been asked.

The subject pages' page records and the prototype fold-back (the frozen prototype still shows the old order, the old foot button, the picture topic tiles and the seven purpose lines) are not done.

---

## Found at the close of S158: two tool faults on this iMac (for the factory session; no theme file involved)

1. **`component_gate.py` cannot run here.** At the Stop hook it crashed in `page.goto` on `http://127.0.0.1:{port}/cards/?workbench=specimen-page-s267` with "Page.goto: Download is starting". That page is served by a local PHP server and this iMac has no `php` (`php: command not found`), so the browser was handed the file as a download. The hook then printed "the built component disagrees with its signed build sheet", which is wrong: the gate never compared anything. It needs either PHP on this machine or a gate that says "could not run" instead of "disagrees". Nothing in S158 touched the cards component.
2. **Playwright has no browser on this iMac.** `~/Library/Caches/ms-playwright` does not exist; `page_gate.py` stops at `p.chromium.launch` ("Executable doesn't exist ... chromium_headless_shell-1223"). Kain says it was installed the week before on both desktops. CleanMyMac X is installed on this machine, which may have cleared the cache; not verified. Workaround used and proven in S158: launching the gate through the installed Google Chrome with `executable_path` set, from a wrapper outside the project (the gate itself unchanged). The wrapper must also put the theme folder on `sys.path`, or the gate reports its own helper tools as missing.

Page gate on Psychology through Chrome, before the path fix: 25 pass, 21 fail, 9 for review. Several of those 21 were the missing helper tools; the true list has not been read. Standing items the gate named that are Code-measurable and need a ruling before anyone changes an approved look: the hairlines between the lead row, the grid and the topics; the 42px page title; the breadcrumb spacing; the 48 against 32 header gaps on a phone; the contrast of the Categories label. One is the topic tags' own: the last row's bottom padding at a section boundary. None of these has been fixed.

---

## The Chrome wrapper for page_gate.py, so the next session can recreate it (S158)

The wrapper lived in the session scratchpad and is gone at close. It is eleven lines, outside the project; the gate is unchanged. Save it anywhere outside the theme and run `python3 wrapper.py <path to page_gate.py> --map <urls>`.

```python
import os, runpy, sys
from playwright.sync_api import BrowserType

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
_orig = BrowserType.launch

def _launch(self, *args, **kwargs):
    kwargs.setdefault("executable_path", CHROME)
    return _orig(self, *args, **kwargs)

BrowserType.launch = _launch
gate = sys.argv[1]
sys.path.insert(0, os.path.dirname(gate))   # the gate's helper tools sit beside it
sys.argv = [gate] + sys.argv[2:]
runpy.run_path(gate, run_name="__main__")
```

Proven in S158 on /learn/psychology/ (it ran and produced a verdict). Not yet run on all seven.

## Later S158 work, theme 0.707.207 to 0.707.217 (for the board)

- The topic tags: one shape, full-width rows, clipped bubble on hover (0.707.207 to .210).
- The Quotes tab above the wall shows the real total; the three foot buttons removed; the wall ends 48 above the topic band (0.707.211 to .213).
- The learning path section: artwork behind the words, larger level cover, taller step pictures, one 32px edge spacing, the cover aligned to the text, a graduation cap on the course button (0.707.214 to .217). Measured on all seven pages.

## Where the Knowledge Hub pages stand, read from the record (S158 close)

Templates that exist: the four reading pages (article, book note, quote, workbook), the listing page, the seven category pages, the front page (/learn/), the tags index (/learn/tags/) and the tag pages. The only Knowledge Hub page type with no template is the search results page (DSRD 9 section 38). Per Kain's S152 order the sittings left are: the listing page, the all topics page (tags index), the topic page (tag page), the Knowledge Hub front page, with the search results page in the same run. The front page, tags index and tag pages were built at 0.707.138 to .140 and wait on Kain's eye in Safari.

---

## Cloud jobs 18, 19, 20: the cloud session's handoff, and Code's decisions on it (S158 close)

Read in full. The handoff file itself lives in the cloud session's storage and was not opened; this is Kain's paste of it. Facts to carry: job 20 has an open pull request, kain-ramsay/achology-theme#1 (base main), which Code has not read (the GitHub tool is not installed on this iMac); none of the three branches is merged; none bumped a version; none was rendered or gated (no page gate, no image_gate.py); no channel ship brief and no zip rebuild were done from the cloud, and both are Code's after any merge.

Code's decisions, all technical and overturnable:
1. **No merge now.** Kain's standing word: none of the three merges until he says the subject pages are right. Nobody presses merge on PR #1 in GitHub.
2. **When Kain says go, the merge order is job 19, then job 18, then job 20.** Job 19 is four files and independent. Job 18 and job 20 both edit parts of `shared-parts.php`, so job 18 goes first and job 20 is brought up to date with main and re-tested after it.
3. **Job 20 must be re-tested against today's main before it merges.** It was branched at theme 0.707.178; main is now 0.707.217, and `kh-subject.css`, `taxonomy-kh_category.php` and `knowledge-hub-parts.php` have changed a great deal since (the topic block, the tags, the foot, the learning path, the saved copy). The earlier conflict test was run against an older main and no longer counts.
4. **At merge, in this order:** run `image_gate.py` (the `-130.webp` style names are the open question), render a sample of the changed pages in Chrome and in Safari for Kain, bump the version once, deploy with `deploy.py`, rebuild the zip, write the ship brief to TO Chat.
5. **The cloud session's four own calls are accepted:** intermediate widths for cards and header art; copies skipped when not smaller; the worst-case `sizes` for cards (540px) for now, to be tightened later by passing the grid to the card functions; one file per testimonial background.
6. **One follow-up after the merge:** the new topic tags' bubble (`.tg__t::before`, 44 by 34 px) and the current-page bubble can use job 20's 26 and 176 px copies.
7. **The merge is its own short session**, never mixed with the page gate or the workbook sitting.

Also open: job 21 (independent review of the saved-copy code) and job 22 (the search results page build, branch `cloud-work/job22-search-results-page` once Kain sends it) have no output yet. The next session reads their reports only, and reviews their branches against the real files when they appear.
