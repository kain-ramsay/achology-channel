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
