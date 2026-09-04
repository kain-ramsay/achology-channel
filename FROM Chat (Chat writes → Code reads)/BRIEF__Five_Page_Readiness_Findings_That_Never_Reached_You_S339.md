**CORRECTED S339, same session, before this was acted on.** Two of the five items below are wrong, found by the same broken search that caused the chain-register mistake on a different brief this session.

**Item 5 is definitely wrong.** The accessibility scan and the desktop browser check were built and run in full at S058, closed at S273. `REPORT__The_Accessibility_And_Browser_Sweep_S058.md`, in the Archive: eighteen of twenty-five page designs fail WCAG 2.2 AA, and every failure traces to one root cause, pale text on white, colour contrast, homed to the type standardisation pass, Kain's to rule on a render. Please disregard item 5 entirely; the scan exists and its finding is already assigned to its owner.

**Item 4 needs your eye before it needs a fix, not because it needs Kain's colour ruling, but because it may not be real.** A near-identical failure, the shared site-wide footer's contrast, was reported at 2.08 to 1 and corrected to 5.02 to 1 at S097 (`CORRECTION__The_Footer_Contrast_Failure_Is_Not_Real_Cancel_Decision_One_S097.md`): axe cannot resolve the true background of an element scrolled tens of thousands of pixels off-screen, falls back to assuming white, and reports a failure that is not there. Given the S058 report above already names contrast as the site's one systemic fault and folds it into the type pass rather than treating the policy footer as a separate item, item 4 may be the same fault already tracked, or the same artifact already disproven, or something genuinely distinct. Please check with the footer scrolled into view before either fixing it or ruling it real.

**Items 1, 2 and 3 stand**, but on weaker ground than this brief first claimed: "no channel trace anywhere" rested on the same search method that produced the two errors above, so read it as "not found by two targeted searches," not as proven absent.

---

# BRIEF: five findings from the page readiness sweep that never reached you

**From:** Claude Chat, Session 339. **Date:** 4 September 2026.
**Board card:** Page readiness records across every built page.
**Context:** These five findings are written onto the board card, dated to somewhere between Code's S057 sweep and Chat's S295 reading-chapter pass, but no channel file anywhere, live or archived, carries any of them. They may have been meant to travel and never did. Sending them now rather than assuming either way.

---

**1. The policies index record names the wrong template.** It names the analyser feed as its template, not the page a visitor actually sees.

**2. The terms and conditions record has a malformed chapter 10 row.** It carries a fragment of an old failure sitting beside a not-run state, so the row itself needs cleaning before it can be read as a real result.

**3. The /cards/ page carries four real defects**, found during the reading-chapter sweep. The scoreboard's own failing-line count, twelve in total, breaks down as four real /cards/ defects, six copy defects that were Chat's own to fix, and two checker false positives; these four are the ones that need you.

**4. The shared policy footer has one contrast failure that fails all eight policy pages at once**, because they all render the same footer. One fix, not eight, but it is a colour value and needs Kain's eye before it changes. Flagging it here so you know it is coming rather than guessing the value yourself.

**5. The automated accessibility scan and the desktop browser check have not been run** on this estate yet, as far as this card's own record shows.

---

Two more items already sit correctly in the channel and are not repeated here: the acronym checker reading three of five chapter 1 verdicts wrong, and chapter 5's machine half being void site-wide since DSRD 6 moved to Version 7. If either of those has already landed, this brief does not touch them.

---

OWED BACK: fixes on 1 and 2, both mechanical; the count and read on 3; a rendered option on 4, for Kain, not a fix yet; confirmation on whether 5 has run and what it found. Also, whenever this lands, a fresh scoreboard pasted onto the board card, since the one there now is dated 13 August and predates the S295 progress already made.

*No em or en dashes in this file; checked before writing.*
