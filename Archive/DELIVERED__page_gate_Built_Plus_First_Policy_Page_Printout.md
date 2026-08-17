# DELIVERED: page_gate is built, with its first policy-page printout

**From:** Claude Code · **Date:** 2026-07-27 · **Re:** `BRIEF__Build_The_page_gate_Machine_Verifier.md`

## Definition of done, against your four conditions

1. **The script exists in the theme repo.** `page_gate.py`, at the theme root
   beside `css_gate.py`.
2. **It runs with one command against any URL.**
   `python3 page_gate.py <url> [<url> ...]`, plus `--map` for a one-line-per-page
   summary across many pages and `--json` for machine reading. Exit 0 pass,
   exit 1 fail.
3. **Its printout for one policy page is filed here.** Below.
4. **The CLAUDE.md line is installed.** Already done as part of the standing
   instruction: every DSRD 6 record filed here carries that page's `page_gate`
   printout, and a record without it is incomplete.

Every value it compares against was read from the DSRDs at build time and is
cited in the output line itself, not taken from your brief. `--map` will run the
whole walk in one pass when you release it.

## How it reaches the page, which you need to know

**SiteGround's server-level Antibot CAPTCHA answers automated clients with a
challenge screen (HTTP 202) instead of the page.** Their support confirmed today
that it cannot be whitelisted per IP or disabled per site from the account.
Their Blocked Traffic tool does not touch it.

I did not defeat the challenge and will not. Instead `page_gate` asks the server
for the page **from inside the server**, over the SSH access we already hold,
where the challenge does not apply. A small local mirror fulfils every request
the browser makes by fetching the same path down that line, so the browser
renders the real page with the real stylesheets, scripts and images exactly as
the server produced them. What is measured is the page, not a copy of it.

Consequence for scheduling: a page takes two to three minutes rather than
seconds, because every asset queues down one SSH connection. Across roughly
twenty built pages that is under an hour, unattended.

## The printout: /policies/refund-policy/

```
==============================================================================
page_gate  https://achologytest.com/policies/refund-policy/
==============================================================================
  FAIL      hairline-present   desktop boundary 1 (policy-breadcrumb | policy-header): no hairline, gap 48.0px
                               ^ DSRD 7 §4.3 ruling 1
  PASS      hairline-spacing   desktop boundary 2 (policy-header | policy-body): 49 above, 48 below
  FAIL      hairline-spacing   desktop boundary 3 (policy-body | policy-endnote): 50.6 above, 49.0 below (want 48/48)
                               ^ DSRD 7 §4.3 ruling 4
  FAIL      hairline-present   tablet boundary 1 (policy-breadcrumb | policy-header): no hairline, gap 48.0px
                               ^ DSRD 7 §4.3 ruling 1
  PASS      hairline-spacing   tablet boundary 2 (policy-header | policy-body): 49 above, 48 below
  FAIL      hairline-spacing   tablet boundary 3 (policy-body | policy-endnote): 50.6 above, 49.0 below (want 48/48)
                               ^ DSRD 7 §4.3 ruling 4
  FAIL      hairline-present   mobile boundary 1 (policy-breadcrumb | policy-header): no hairline, gap 48.0px
                               ^ DSRD 7 §4.3 ruling 1
  PASS      hairline-spacing   mobile boundary 2 (policy-header | policy-body): 33 above, 32 below
  FAIL      hairline-spacing   mobile boundary 3 (policy-body | policy-endnote): 34.6 above, 33.0 below (want 32/32)
                               ^ DSRD 7 §4.3 ruling 4
  PASS      hairline-edges     no line at page top or bottom
  PASS      header-to-content  desktop: 48.0px (want 48)
  PASS      header-to-content  tablet: 48.0px (want 48)
  PASS      header-to-content  mobile: 32.0px (want 32)
  PASS      content-width      page-container: 1200px
  PASS      content-width      article-container: 880px
  PASS      h1                 32px / 700 — "Refund Policy"
  PASS      gutters            desktop: 48 / 48 (want 48)
  PASS      gutters            tablet: 32 / 32 (want 32)
  PASS      gutters            mobile: 20 / 20 (want 20)
  PASS      meta-title         47 chars: Refund Policy | Achology Courses And Membership
  PASS      meta-description   117 chars: Achology's refund policy sets out when you can request a ref
  FAIL      canonical          (missing)
                               ^ DSRD 6 §3.3
  PASS      dashes             0 em, 0 en
  PASS      assets-load        nothing failed
  PASS      links-resolve      38 checked, all resolve
------------------------------------------------------------------------------
  FAIL   18 passed, 7 failed, 0 for review, 0 not built yet
```

**This is a printout, not a verdict.** No fix has been made. The walk has not
started; I am waiting on your answer about its order.

## What the printout raises, and the one thing I will not decide

**A. The breadcrumb-to-header junction has no hairline.** The 48px spacing is
there and correct at all three widths; the line is not. Whether that junction is
a "block boundary" under DSRD 7 §4.3 ruling 1 is exactly the sort of call the
standing instruction forbids me from making.

DSRD 9 §26 calls the breadcrumb "the first content row", which reads as part of
the page's opening rather than a block in its own right. If that is right, this
is not a boundary, no line is wanted, and `page_gate` should stop counting the
breadcrumb as a block. If it is wrong, nine policy pages need a line added.

**One line from you decides it, and it changes the checker as well as the
pages.** I have not touched either.

**B. The closing-note line runs about 2.6px wide of 48.** Real drift, small, on
the shared template, so it will be on all nine. This one is unambiguous and I
will fix it when the walk starts.

**C. No canonical address is declared, and it is site-wide.** Not a policy-page
defect. I checked three unrelated pages (Trust Statement, About, Our People) and
none carries one either, and Rank Math has no canonical setting stored at all.
DSRD 6 §3.3 requires it on every page. This is one Rank Math configuration
change rather than twenty page fixes, and it belongs in the runbook I filed
earlier rather than in the walk. Flagging it here so it is not "fixed" nine times
over as if it were a page defect.

## For the record: what the checker caught in itself

Its first five runs each produced a confident page of numbers, and every one was
wrong in a different way: it measured a bot-challenge screen and reported it as
the page; it reported the documented 1104px inner width as a defect; it looked
for blocks one wrapper too high and found none, which read as a clean page; it
measured to a block's padding edge rather than to the last visible content; and
it matched a boundary to a line that belonged to the next boundary down.

Not one of those was visible by eye, and all five would have gone into a
hand-written record as fact. That is the argument for building it before the
nine records rather than after, which is the question still with you.
