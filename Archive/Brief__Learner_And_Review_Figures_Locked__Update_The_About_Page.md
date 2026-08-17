# Brief from Chat — the learner and review figures are locked; the About page needs updating

From: Claude Chat · S217 · 2026-07-23
Approved by Kain in session. This is a build instruction, not a question.

---

## The decision

Kain confirmed the current figures from the Udemy instructor dashboard on 23 July 2026 and **locked them for the remainder of the pre-launch build**:

- **695,578** — total learners (unique students, not enrolments)
- **175,162** — reviews / total ratings

Every document and page uses these two figures until go-live. No page carries a different one. The rounded `670,000+` and `679,000+` conventions are retired — the exact figure is used, with no `+`, because the rounded form is what allowed two different numbers to coexist unnoticed for months.

The true-north record is **DSRD 5**, which now carries both figures with the confirmation date and the lock statement.

---

## What has already been changed in the specifications

All verified by read-back this session. You do not need to do anything about these — they are listed so you can see the figure is consistent everywhere before you touch the theme.

| Document | What changed |
|---|---|
| DSRD 5 (true north) | Totals row and the overall summary line; lock statement added |
| DSRD 4 §14.2 | Trust Line variant 3 |
| DSRD 8 | Access All Areas stats line; membership card stats line |
| DSRD 9 §23 | About lede, terminus line, statistics panel, 2025/26 milestone stat |

---

## What I need you to change in the theme

`page-about.php` carries the old figures in at least four places, and `404.php` may too. **Please grep the whole theme for `670,000`, `679,000`, `679,926` and `171,306` rather than working only from this list** — I can read the theme but I have not enumerated every occurrence, and the point of this brief is that no page is left carrying a different number.

The four I have seen directly:

1. **The About page lead paragraph.** Currently reads "We've spent a decade teaching more than 670,000 students from 216 countries…". The figure becomes **695,578**. Note the sentence says "more than", which no longer fits an exact figure — the phrasing needs to become "teaching 695,578 students from 216 countries", or similar. **If that reads badly to you, say so rather than forcing it** — the copy is Kain's and I would rather adjust the sentence than have you ship something awkward.

2. **The `AboutPage` schema description**, in the JSON-LD block at the foot of `page-about.php`. Currently "About Achology: a decade teaching applied psychology to 670,000 students in 216 countries." The figure becomes **695,578**. This one matters twice over: the file's own comment says the description mirrors the page's Rank Math meta description, so **that meta description needs the same change** or the two drift apart.

3. **The timeline terminus line.** Currently "670,000+ mature learners from around the world have brought the Achology story this far." Becomes "**695,578** mature learners from around the world have brought the Achology story this far." The `+` goes.

4. **The 2025/26 milestone stat and the statistics panel.** The milestone stat becomes **695,578**; the panel's "Total Student Ratings" becomes **175,162**. The odometer's final value should land on the same figure as the milestone — if it is derived rather than hardcoded, check that it still resolves correctly.

---

## One thing to check, not to change

DSRD 5's totals row still records **872,284 aggregate enrolments**, which is from an earlier pull and was not refreshed on 23 July. Kain mentioned an average of roughly 2.7 courses per learner, which does not reconcile with 872,284 across 695,578 learners — that would be about 1.25 each.

I have flagged it in DSRD 5 as the one figure in that table not refreshed. **Do not act on it and do not use it in any page.** It is named here only so that if you see an enrolment-based figure anywhere in the theme, you flag it rather than trusting it.

---

## Acceptance

The theme carries `695,578` and `175,162` and nothing else, on every page and in every schema block, and a grep for the four old figures returns nothing. Ship it with your usual brief.
