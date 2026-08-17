> **DISPOSITION, Session 267, 12 August 2026.** All three answered and written home. The sitemap is a carve-out: DSRD 6 section 3 row 3 now covers a signal a plugin emits that the noindex setting contradicts, with the sitemap named as the first case and verified live at cutover. The schema line reverts to not run, under a new general rule at the head of DSRD 6: any chapter line dated before 11 August 2026 was measured against a shorter list and reverts, and every future widening resets its own chapters in the same edit. The founders' letter meta title is replaced with a 51 character string. Answers written to Code. Archived.

# QUESTION: the sitemap lists noindex pages, and one chapter pass predates the standard it claims to meet

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Three things, all found by the new machine checks on their first runs.** Two are questions I cannot settle. One is a defect whose fix is copy, and copy is not mine.

## 1. The sitemap lists pages the site says are hidden. Carve-out or defect?

**The fact, verified by hand before this was written.** `/reviews/` carries `noindex`. `page-sitemap.xml` lists `https://achologytest.com/reviews/`. Both are true right now, and Rank Math generates the sitemap.

**Why I cannot settle it.** DSRD 6 §5 item 9 says: "The 404 page and any page deliberately hidden under item 3 are correctly absent, not present." So a noindex page in the sitemap is the contradiction the standard names, and the check reports it red.

But the build site is noindex site-wide by design (`blog_public` 0), so this fires on **every page**, and it looks very like the canonical carve-out DSRD 6 §3 row 3 already records. **It is not the same thing, though, and that is exactly why I am asking rather than deciding.** The canonical carve-out covers a signal a plugin **suppresses** on a noindex page. This is the reverse: a plugin **emitting** a page the indexing settings say is hidden. §3's sentence covers "any other signal a plugin suppresses", which does not stretch to this.

**What I need:** either the carve-out extended in DSRD 6 to cover a plugin emitting on the build ground, verified live at cutover exactly as the canonical is, or a ruling that it is a real defect and Rank Math should exclude noindex pages from the sitemap. Until then the gate reports it red on every page, which is honest and noisy.

**My reading, offered as one and not acted on:** it is the build ground, the same family as the canonical, and the right home is one extra sentence in §3's carve-out rather than a new rule. The cutover check already has to confirm `blog_public` is 1 and sample the canonicals; confirming the sitemap in the same sitting costs nothing.

## 2. §4 on /reviews/ reads `pass` against a standard that did not exist when it was written

The `/reviews/` record was written at S054 from the S053 gate run. **§4, schema markup, reads `pass, 2026-08-11`.**

DSRD 6 Version 6, ruled at S264, requires **both** checkers: "Every page therefore passes two tests: Google's Rich Results Test ... and the Schema Markup Validator at schema.org." The S053 run predates that rule and cannot have run the second checker. It also cannot be run now: neither validator can reach the build site past SiteGround's bot challenge, and neither publishes an API.

Should §4 go back to `not run` until the two-checker requirement can actually run at cutover, or does it carry a recorded exception saying the second checker is unavailable on the build ground? **I have not changed it either way.** It is a judgement line on a page I built, and §0 keeps me out of those.

**This is worth more than the one line.** Every chapter passed before S264 was passed against a shorter standard. Version 6 added the second schema checker, the sitemap line, the accessibility scan floor, the 400 percent reflow check, the automated link check, the form delivery test, and the browser-and-device check. **Any pass dated before 2026-08-11 was measured against a different list.** Right now that is one page, so it is cheap to settle. It will not stay cheap.

**§5 answered itself and needs nothing.** It read `pass, 2026-08-12`; the machine now fails it on the sitemap contradiction above, and the sweep overwrote the line to `fail` while carrying the old value into it, so nothing is lost and the change is visible.

## 3. A defect whose fix is copy: the founders' letter meta title is 65 characters

Found by the new §3 uniqueness check on its first run. DSRD 6 §3 row 1: "stays within about 60 characters so search results don't cut it off." Seven of the eight pages checked are clean; that one is over.

The title is copy, so it is not mine to rewrite (Rule 8). Send the replacement wording and it lands in the next pass.

## What I have done meanwhile

Nothing on any of the three is decided by me. The sitemap check reports red and says in its own printout that the question is with you. The §4 line is untouched. The founders' letter title is unchanged.

*No em or en dashes in this file; checked before writing.*
