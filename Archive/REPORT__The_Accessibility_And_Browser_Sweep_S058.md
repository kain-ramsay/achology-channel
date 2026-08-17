> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Received whole; the commission side is accepted as closed. Its four residues are homed: (1) the contrast fault is already recorded in GUIDANCE__Standardising_The_Type_Across_The_Site_S269 section 6 and rides the type scale sweep in Code's queue, ruled by Kain on a render at the machine; (2) the copy fixes (eleven acronyms, the two dashes on /learn/articles/) are held with the page-work stop, closing when the component sweep completes, same holding as the DSRD 6 machine sweep residue; (3) the /learn/ question is answered in REPLY__Accessibility_Sweep_Received_And_The_Learn_Redirect_S273 in FROM Chat: the 302 is an acceptable interim while the Knowledge Hub homepage (PRD Pr1.8) does not exist, and the question reopens as a page decision when that page is designed; (4) the Safari and Edge gap is macOS 13, which is Kain's machine and Kain's decision, named to him at the S273 open. Board cards moved: none owed; checked by query, no card carries this work.

# REPORT: the accessibility scan and the browser check are built and run, and the site has one systemic accessibility fault

**From:** Claude Code, Session 058. **Date:** 2026-08-14.
**Answers:** `COMMISSION__DSRD6_Gate_Machinery_Backfill_And_Why_Question_S264.md`, part 2. **This closes my side of that commission.**
**Reads with:** `REPORT__The_DSRD6_Machine_Sweep_Across_All_25_Page_Designs_S058.md`, filed earlier the same session.

---

## 1. The one finding that matters most

**Eighteen of the twenty-five page designs fail WCAG 2.2 AA, and every single failure is the same fault: colour contrast.** Not eighteen problems. One problem, in eighteen places.

axe rates every one of them **serious**. The elements it names are pale text on white across most of the component library:

`.policy-endnote`, `.shelfp__b`, `.ap-eyebrow`, `.kh-article__meta`, `.card--article .card__author`, `.help-single__updated`, `.kh-hub__overline`, `.kh-listing__count`, `#help-group-pre-purchase`, `#help-articles-title`, `.rv-bar__go`, `.tm-tab__n`, and a bare `cite`.

**This is the finding Chat already made once, and it is wider than it looked.** `GUIDANCE__Standardising_The_Type_Across_The_Site_S269` §6 records the section header supporting line measuring 3.19 against white, site wide, below the 4.5 bar, found by Chat's own self-critique at S268. The scanner has now found the same fault independently, and in a dozen more classes than the one that was noticed.

**Five designs come through the scan completely clean:** /about/, /manifesto/, /policies/, /refund-policy/ and /founders-letter/.

**It is one fix, not eighteen**, and it belongs with the type standardisation pass rather than as its own job: the guidance note already names it as the pass that should carry it. It is a colour decision on approved pages, so it is Kain's on a render, not mine.

## 2. What was built

**§7, the accessibility scan.** axe 4.10.2 injected into the assembled live page and run against WCAG 2.2 AA, which is the bar §7 names. The scanner lives at `~/.claude/achology-tools/`, deliberately outside the theme: Rule 11 keeps outside code out of a theme that serves a site taking card payments, and §7 names axe itself, so this is the standard being followed with the theme kept clean. It can never reach the server. Downloaded on Kain's word, S058.

**§11 item 6, the desktop browser check.** A new instrument, `browser_check.py`. It loads the representative page in Chrome and Firefox and checks five things a person would call a broken page (it loads, nothing failed to arrive, no uncaught script error, it has an h1 with words in it, it does not scroll sideways), then compares the two engines against each other.

**Both are now inside the sweep and run unconditionally.** Not behind a flag: §11's other three checks would go on passing while item 6 had never run on any page, and a chapter reading as measured on ground nothing has looked at is the S054 failure this commission exists to end.

## 3. Two of the four browsers cannot run on this machine

| Browser | State |
|---|---|
| Chrome | real Chrome, driven directly. **Runs.** |
| Firefox | installed at S058 (153.0.4), driven through Playwright. **Runs.** |
| Safari | installed, but this Mac is macOS 12.7.6 and Playwright does not support WebKit on it. **Not run.** |
| Edge | the current version requires macOS 13. Downloaded and installed at S058, aborted on launch against this OS, removed again. **Not run.** |

Both gaps are the operating system, not the tooling, and closing them means macOS 13, which is Kain's decision and not a small one. **Every printout names Safari and Edge as not run with the reason**, so nothing reads cleaner than it is.

What is lost is smaller than two of four sounds. Edge is Blink, the same engine as Chrome, so its absence costs least. **Safari is WebKit and its absence is the real gap**, and it is the browser a large share of Achology's visitors will use.

## 4. Both instruments were proved failing before either pass was believed

Both came back clean on their first real page, which is the result worth trusting least: a clean page and a scanner that is not looking produce the same green.

**The accessibility scan** names a missing image description, a text colour that fails the contrast ratio, and a form field with no label, and still passes a page with none of those. Seven cases.

**The browser check** names a page that does not load, a request that failed to arrive, an uncaught script error, a missing heading, sideways scrolling, and each of the four ways the two engines can disagree, and finds nothing on a good page or on a difference inside tolerance. Thirteen cases, four of which must find nothing.

## 5. What the browser check found, and it earned its place on the first run

**It caught a defect nothing else had:** `/learn/` is not a page. It 302-redirects to `/learn/articles/`, confirmed at the server. The browser check reported no h1 in Chrome; page_gate independently refused to grade it as a redirect. **My sweep had been using the wrong representative address for the Knowledge Hub listing design**, and both instruments said so in different words.

Re-run at `/learn/articles/`, that design measures properly and shows three real faults, including **one em dash and one en dash in its copy**, which no earlier run had seen because no earlier run had reached the page.

**A question for Chat, not a proposal.** PRD §5.1 Pr1.8 names a Knowledge Hub homepage template at `/learn/`. Today `/learn/` is a 302 to a listing page. Whether that redirect is intended until the homepage exists, and whether a 302 rather than a 301 is right, is a DSRD 1 question.

**The engines disagreed on two designs:** the policy family page (75px difference in page height between Chrome and Firefox) and the trust statement (45px). Both are above the 40px tolerance and both are worth a human eye rather than a fix: a height difference of that size is usually a font metric or a collapsing margin behaving differently, and it is the kind of thing that is invisible until someone looks at the right browser.

## 6. The board now

```
25 page designs owe a record, covering 34 live pages.
0 have no record.  0 are READY.  22 carry a failing line.
211 chapter lines are open in total.
```

**More designs carry a failing line than before (22, up from 16), and that is the sweep working rather than the site getting worse.** Two whole chapters that had never been measured are now measured. A failure that was always there and is now visible is the entire point.

**Still zero READY, and still nothing I can change.** Ten of the eleven chapters need a human runner and §8 is yours by definition. §4 remains unrunnable on the build ground: both schema validators fetch the page themselves and the host answers an outside request with a captcha wall.

## 7. What is now owed, and none of it is mine

1. **The contrast fault**, one decision covering eighteen designs, on a render, with the type standardisation pass.
2. **The eleven acronym expansions**, and the em and en dash on the listing page, both copy.
3. **The §10 hairline and spacing faults** on nine designs, which need a ruling because the pages are approved.
4. **The human reading chapters.** Nine designs come through every machine check clean and are ready for that reading: /about/, /manifesto/, /policies/, /refund-policy/, /reviews/, and the four others whose only failures are copy.

**My side of the S264 commission is complete.** Parts 1, 3 and 4 were closed earlier; part 2 is closed by this report; part 5's question was answered when the commission was first worked. The only thing I have left undone anywhere in it is §4, and that is the build ground rather than the work.

*No em or en dashes in this file; checked before writing.*
