# DONE: I10's four machine rows written, one of them a real fail

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `REPLY__Three_Rhythm_Fails_Go_To_Cowork_And_Four_I10_Machine_Rows_Are_Yours_S361.md`.

---

**§3 and §5, written in from the S105 run.** Both pass, each with the same recorded carve-out already established elsewhere on this record (canonical and sitemap correctly absent, build ground is noindex).

**§4, schema markup, run fresh against Google's own Rich Results Test.** PASS. Articles: 1 valid item, no errors, no warnings. Breadcrumbs: 1 valid item, no errors, no warnings. The tool's own "URL is not available to Google" flag is the same noindex carve-out as §3 and §5, not a schema defect: it still fetched the page and validated both blocks.

**§9, speed, run fresh against Google PageSpeed Insights, mobile.** FAIL. Against DSRD 3 section 4.3's targets: FCP 3.0s (target 1.5s), LCP 3.5s (target 2.0s), both over. CLS 0.018 passes (target 0.05). Overall Lighthouse Performance 86 of 100. No CrUX field data exists yet, a real gap for a site with no live traffic, so this is one lab run, not a confirmed pattern, and it ran against achologytest.com directly, before the SiteGround Dynamic Cache dependency DSRD 3 section 4.4 itself names.

**Not fixed here.** A speed fail belongs to the build or the hosting configuration, not to one page's copy or markup, so I have not touched anything on the strength of a single lab run. Worth a wider read before cutover, per DSRD 3 section 4.4's own instruction to check "a representative page of each type... again across the site before cutover."

All four rows written into `DSRD6_RECORD.md`, dated and sourced.

---

OWED BACK: whether the speed fail is worth widening to other page types now or held for the pre-cutover sweep DSRD 3 already calls for.

*No em or en dashes in this file; checked before writing.*
