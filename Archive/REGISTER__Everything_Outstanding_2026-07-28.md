# REGISTER: everything outstanding, measured today, nothing left in a conversation

**Written:** 28 July 2026, S228 close. **From:** Claude Code. **For:** Claude Chat.
**Why:** Kain asked whether the agenda carried into the last two sessions is still
standing, and said the point is that no pending item is stranded in a conversation
somewhere. This is that sweep. Everything below was measured against the live site
today, not recalled from notes.

His conclusion, and I agree with it: the next session is a site-wide tidy-up and
optimisation session.

---

## 1. The one that keeps getting displaced: Rank Math scores in bulk

Kain's instruction at the close of 27 July was to open the next session on this. It
has now been displaced twice, by the help-article rebuild and by today's clean-up.

**Measured today: 0 of 249 help articles carry a Rank Math score.** Not a low
score. No score at all. All 249 carry a focus keyword, a search title and a search
description, so the analyser has everything it needs; nothing has ever triggered
it, because Rank Math computes the score in the browser on save and every one of
these was written by WP-CLI.

**The theme-built pages, measured today:**

| Page | Score | | Page | Score |
|---|---|---|---|---|
| about | 86 | | terms-and-conditions | 90 |
| code-of-ethics | 85 | | privacy-policy | 86 |
| manifesto | 85 | | disclaimers | 85 |
| policies | 70 | | refund-policy | 85 |
| accessibility-statement | 84 | | trust-statement | 81 |
| cookie-policy | 80 | | **testimonials** | **4** |
| **instructors (Our People)** | **4** | | **kain-ramsay** | **4** |
| **declan-fitzpatrick** | **4** | | 8 other profiles | **none** |

The 4s and the nones are the pages whose editor box is empty by design because the
page lives in the theme, so the analyser has nothing to read. The 80s and 90s were
written in by an import rather than measured, so they are not evidence of anything.

**One timing point in our favour.** Had this run two sessions ago, today's work
would have thrown every score away: all 249 articles were rewritten and every one
republished. Running it now is the right order, not the late one.

## 2. New today, and the most serious thing in this register: all 249 audio recordings are stale

Every help article carries a Listen player reading the article in Kain's cloned
voice, with per-sentence follow-along highlighting driven by a timings file.

**All 249 mp3 files predate today's rewrite.** 200 were generated on 15 July and
49 on 27 July. Every article was rewritten on 28 July.

So on every article in the section the Listen button now reads out text that is no
longer on the page, and the highlighting follows sentences that no longer exist.
It is invisible unless someone presses play, and nothing in any gate would catch
it, because the files are present and the player works.

This is a consequence of the rebuild that nobody, me included, thought about at
the time. 253MB of audio across 249 files needs regenerating from the current
text, with the pronunciation set Chat ruled at S226 (VALTS as "valts", DiMAP as
"dee-map", the Code of Character and Conduct never voiced as an acronym, and the
rest). The pipeline exists and has been run twice.

**Note for the record:** Chat's S226 section 5 commissioned "the audio run for the
49". That run had already happened on 27 July, so that item was closed before the
message arrived. It is now reopened along with the other 200.

## 3. The focus keywords are import artefacts, not search phrases

Checking whether the keywords still fit the rewritten articles turned up something
different. The keywords are slug-shaped strings: "achology knowledge hub free",
"which achology company contracting", "milestones achology history".

- The exact keyphrase appears in the article body in **9 of 249**.
- Every word of it appears somewhere in **161 of 249**.

Rank Math scores primarily on the exact keyphrase appearing in the title, the
description, the URL and the opening of the content. Against phrases shaped like
these, a bulk run will produce poor scores that are accurate reflections of a bad
keyword rather than of a bad article.

**So the bulk score run and the keyword question have to be settled together**,
and the keyword question is editorial, which makes it yours and Kain's, not mine.
The search titles and descriptions themselves look sound: all 249 are present, and
every one still shares most of its wording with the article underneath it.

## 4. Commissioned and not started

| Item | Source | State |
|---|---|---|
| The three-part hairline check, and the report of what is non-conforming under the new text-colour rule | `ANSWER__Hairline_And_Colour_Rulings_S226.md` sections 2 and 4 | **not started** |
| `page_gate --map` across every built page, filed as one map for Kain to set the walk order from | `00__ANSWERS__Walk_Order_Check3_And_Breadcrumb_Hairline.md` section 1 | not started, and the reconciliation walk waits behind it |
| The breadcrumb hairline: render `/policies/refund-policy/` twice, one variable changed, for Kain to judge by eye | same, section 3 | not started |
| Collapse every duplicated block into its one home: the About preview's hand-authored CSS blob, frozen preview content, remaining private copies | `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` | not started |
| Bring every built page to standard, one at a time, through the DSRD 6 gate | `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md` | not started, queued behind the map |
| Check 3 of `page_gate`: fail only on spacing declared outside a DSRD 8 component | `00__ANSWERS__Walk_Order_Check3_And_Breadcrumb_Hairline.md` section 2 | not built |

The hairline check is the one I would flag hardest. It was commissioned this
morning and asks three specific things be reported separately, and none of them
has been. If a sweep did set 48 at phone width, the theme is off-spec right now.

## 5. Waiting on you

- **H6 timing.** You ruled the new-or-modified rule lands at harness version 3, not
  as a patch now. I had already built and committed it an hour earlier and it is
  live. Leave it, or disable it until version 3?
- **The three repeated links**, done on Kain's direct instruction with you
  unavailable. Reported in full in `REPORT__S229_Rulings_Carried_Out.md` section 5,
  together with the harness seam it exposes: the harness has no answer for "Kain
  has decided and Chat cannot file it".
- **The help-standard fold-in to the `help-answer` skill**, which you said is
  Chat-side and going on the board.

## 6. Closed today, so it does not come back

The whole clean-up brief: register pass, the 45 acronym cases, the CCaC
replacement, ATL, Wiser People, the GAP-012 re-sync, and the link map. Plus the
harness install with all six hooks, the permissions change, my own 87 duplicate
links, and the theme history tidied into truthful commits. Section state: 249
articles, 2,426 links, no broken or unterminated link, `article_gate` clean
throughout.

## 7. What I would put in the next session, in this order

1. The stale audio, because it is the only item where the live site is currently
   telling visitors something untrue.
2. The keyword decision, then the bulk score run, then the theme-page scoring fix.
   These three are one job and doing them apart wastes the run.
3. The hairline and colour check, which is overdue and small.
4. The `page_gate --map` run, which unblocks the reconciliation walk and everything
   queued behind it.

Kain's own framing, and it is the right one: a site-wide tidy-up and optimisation
session.

---

HARNESS | Scope: audit every outstanding item across the project and file it as one register | Spec quoted: yes (CLAUDE.md channel and session-close rules; DSRD 2 section 2.24 for the pronunciation set referenced) | Gates: not applicable, nothing changed on the site; every figure measured live today, and one figure I nearly filed was checked and found wrong before it was written | Page: not rendered | Outside scope: none
