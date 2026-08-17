> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Read and dispositioned in FROM Chat by `REPLY__Dispositions_For_Your_Four_Remaining_Files_S272.md` item 4: three instrument repairs committed and deployed, the record placed under version control, no ruling owed. No board cards moved by this file.

# SESSION REPORT: S058

**From:** Claude Code, Session 058. **Date:** 2026-08-14 (the session opened on the 13th and ran past midnight, so its log spans both days).
**Assembled from the version control log** per Harness Rule 13 Version 3.2, plus hand-added lines for work that touched no file in the theme repository. Hand-added lines are marked.

Theme at v0.60.17, unchanged: nothing that renders was touched this session. Six commits, all pushed and deployed, all three deploy proofs current (local, server, zip).

**One note on this file's own date, because the gate caught it.** It was first written mid-session dated the 13th, and the three commits after midnight then sat outside its window, so the Rule 13 gate correctly reported them as unreported. The date now reads the session's close rather than its open. Worth recording rather than silently correcting: a session that runs past midnight is the one case where a report can be filed, be honest, and go stale the same night.

---

## First, a line S057 owes and its report does not carry

**`cfc808a`, the about.css dead-class deletion, all 35, with the kept render-proof instrument.** It landed at 05:42 on 13 August, after `SESSION_REPORT__S057.md` had already been written at 00:56, so no session report names it. Its own report, `REPORT__The_35_About_CSS_Dead_Classes_Deleted_S057.md`, is in TO Chat and carries the detail. Recorded here so the log and the reports agree again.
**Board card:** the about.css dead-class deletion card.

---

## Finished

**The two acronym false positives, fixed.** Commit `c66de01`. `G2` inside the registered office postcode and `AA` inside "at Level AA" were both being read as unexplained acronyms. Neither joined the exemption list: the carve-out is the surrounding phrase instead, so a bare use of either token anywhere else on a page still fails. Seven test cases, four of which must return nothing. Detail in the sweep report.
**Board card:** the DSRD 6 backfill across built pages.

**The sweep can reach the nine route-template rows.** Commit `9952e1e`. Every route template keys its record by filename rather than by address, so `--sweep` derived the wrong key and skipped all nine, silently, every run: those nine designs had never been measured at all and nothing said so. `--sweep` now accepts `rowkey=URL`. Five test cases including the query-string case that would have broken it.
**Board card:** the DSRD 6 backfill across built pages.

**The DSRD 6 machine sweep, all 25 page designs, one page at a time.** Nine designs come through the machine half completely clean; sixteen carry a real failing line; none is READY and none can be, because ten of the eleven chapters need a human runner. Four stale fails cleared themselves, which is the record working. Filed as `REPORT__The_DSRD6_Machine_Sweep_Across_All_25_Page_Designs_S058.md` with the findings grouped and four questions back to Chat.
**Board card:** the DSRD 6 backfill across built pages.

**The Rule 13 session-report gate, two bugs.** Commit `6ddefac`. It read only the live TO Chat folder, so a report went invisible the moment Chat archived it, and it announced forty unreported commits at this session's open when they were already written up. Fixing that revealed a second bug in the same function: the date window used a bare date, which git fills from the clock, so a commit pushed at 05:42 fell outside a window opened at noon. The six existing acceptance cases had passed through both bugs untouched because they substituted the two functions that carried them; two new cases use a real folder scan and a real temporary repository, and the run proves both go red against the previous version, pinned by its sha rather than HEAD.
**Board card:** the harness machinery card.

**The version history and overnight running investigation, answered whole.** Hand added: read only, no repository file involved. Filed as `ANSWER__Version_History_For_The_Project_Record_And_Overnight_Running_S058.md`. The headline is that there is no backup of this machine at all: Time Machine has never been configured, there are no snapshots, the prototypes repository Chat commissioned at S257 has no remote, and 593 files inside this project are currently iCloud placeholders, several of them approved prototypes. My answer on overnight running is not yet, and the condition is one evening's work.
**Board card:** the overnight running and project record card.

**The S264 commission's part 2, finished later the same session.** Commits `2e4e572`, `dfb7bea`, `d00c33d`. The §7 automated accessibility scan (axe 4.10.2, WCAG 2.2 AA, injected into the assembled page) and the §11 item 6 desktop browser check. Both were green on their first real page, so both were shown failing before the pass was accepted: the scanner names a missing image description, a contrast failure and an unlabelled form field, and the browser check names a page that does not load, a failed request, a script error, a missing heading, sideways scrolling, and the two engines disagreeing with each other. Seventeen cases between them, eight of which must find nothing. Both now run inside the sweep, unconditionally, so §11 can never read as measured while item 6 has never run.
**Two of the four browsers cannot run on this machine, and it is the machine rather than the tooling.** Safari is installed but Playwright does not support WebKit on macOS 12.7.6; current Edge requires macOS 13 and aborted on launch when it was installed, so it was removed again. Chrome and Firefox run, and they are the two different engines. Every printout names Safari and Edge as not run, with the reason.
**Board card:** the DSRD 6 backfill across built pages.

**The 35 school and course pages verified against the S267 spec.** Hand added: no repository file involved. All 35 exist as drafts with the right parents and titles matching DSRD 5 character for character, checked by script. Filed as `REPORT__The_35_School_And_Course_Pages_Verified_S058.md`, which also carries a harness break of mine and a structural finding about overlapping school bundles.
**Board card:** the school and course page creation card.

**A request for direction, filed to Chat rather than put to Kain.** Hand added. `REQUEST__What_To_Build_Next_And_The_PRD_Build_Gap_S058.md`, carrying the finding that roughly half of the PRD's §5.1 page templates do not exist, including the homepage, the course page and the school page.
**Board card:** whichever the sequence decides; the request names none.

**The sweep with both new checks, run and filed. THIS CLOSES THE S264 COMMISSION ON MY SIDE.** Hand added: the run itself touched no repository file. Filed as `REPORT__The_Accessibility_And_Browser_Sweep_S058.md`. The headline is one fault, not many: 18 of the 25 designs fail WCAG 2.2 AA and every failure is colour contrast, which is the same fault Chat found on section headers at S268, now found in a dozen more classes. Five designs scan completely clean. The browser check earned its place on its first run by catching that `/learn/` is not a page but a 302 to `/learn/articles/`, which means that whole design had been swept at the wrong address; re-run properly it shows an em dash and an en dash in its copy that nothing had seen before.
**Board card:** the DSRD 6 backfill across built pages.

**Kain's ruling on how every turn ends, acted on and filed.** Hand added. Filed as `RULING__Every_Turn_Ends_With_A_Proposed_Next_Action_S058.md`. He asked three times why my turns had stopped proposing a next action and rejected two answers as guesswork; the cause was a collision between CLAUDE.md line 45 and the S055 memory note, both of which told me to carry on without asking. The ruling names the one line in CLAUDE.md that Chat needs to narrow.
**Board card:** the working practice card.

## Not finished

**The internal linking question inside the S267 spec.** Its page-creation half is done and reported; its closing question, what internal linking work has actually run across the 249 help articles and what the counts are now, has never been answered. That file therefore stays live in FROM Chat.
**Board card:** the school and course page creation card, and the internal linking strategy card behind it.

**§4, schema markup, on all 25 designs.** Not a gap in the work: both validators fetch the page address themselves and the build ground answers an outside request with a captcha wall. It stays `not run` until cutover and is recorded rather than carried.

**§4, schema markup, cannot be run on this build at all.** Confirmed independently again this session. Both validators fetch the page URL themselves and achologytest.com answers an outside request with a captcha wall. It stays `not run` on all 25 records until cutover. This is a structural limit rather than work outstanding, and it is recorded so it is not rediscovered.

## One thing worth the board seeing rather than only the fix

Both bugs in the Rule 13 gate had been live since the gate was built, and its acceptance test passed six of six through both of them, because every case substituted the two functions where the bugs were. A test that only exercises the arithmetic between two mocks proves the arithmetic. The two cases added this session are the first in that file to touch the real code, and the run now has to prove they can fail before it is allowed to claim they pass. Third time in three sessions that a green check turned out to be checking something other than what it claimed.

*No em or en dashes in this file; checked before writing.*
