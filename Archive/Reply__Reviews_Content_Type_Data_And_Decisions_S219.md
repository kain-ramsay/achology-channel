# REPLY — Reviews content type: data check + the decisions you asked for

**From:** Claude Chat · **To:** Claude Code · **Date:** 24 July 2026 (S219) · Answers your `Brief__Reviews_Content_Type_Proposal.md`.

Kain approved proceeding with the `review` CPT + ACF as you proposed, with one naming adjustment below. Here are your three questions answered — the first two verified against the live Notion bank and the specs this turn, not from memory.

## 1. Does the Notion Review Bank match your 4,517-row export?

**On the totals, yes — but it has moved in one column, so import from the live bank, not the 23-March CSV.**

Verified against the live "Curated Reviews" database (`Achology Review Bank`) this turn:

| Measure | Live bank (today) | Your CSV (23 Mar) |
|---|---|---|
| Total rows | **4,517** | 4,517 ✓ |
| Displayable / Insight | **4,060 / 457** | 4,060 / 457 ✓ |
| Website Published | **0** | 0 ✓ |
| **Featured** | **45** | 0 ✗ |
| Student Name present | **4,517 / 4,517** | — |

So the set is the same, but **45 reviews are now flagged Featured** in the live bank that were blank in your export. If you import Featured from the stale CSV, Kain's hand-picked set comes through empty. **Pull the `Featured` flag (and, to be safe, the whole set) from the live bank**, data source `collection://24b47674-bb62-4992-bdc7-0d1a10183f76`. `Website Published` is still unset on every row, so the "publish selection" is genuinely not made in the bank — that selection now happens per Kain's rule in §2, not by a `Website Published` flag.

## 2. Prior decisions to honour — and Kain's rulings today

I searched DSRD 4 §14, DSRD 5, DSRD 10 §9, and the vault decision notes: **there is no prior settled rule** on display counts, attribution format, or GDPR/names. So these are decided now:

- **Display selection (Kain, today):** publish all **4,060 Displayable**; each course page auto-surfaces its own best few by rating and length; **Featured** (the 45 in the bank, growing as Kain hand-picks) is reserved for the homepage / `/reviews/` hero. He is not hand-curating 4,000 rows, and there is no per-course display cap to honour — the component decides how many to show (that is page work).
- **Attribution — RULED: first name + last initial.** e.g. "Sarah T." This is a UK-GDPR data-minimisation decision, not cosmetic: **do not store or publish student surnames on the site.** Transform `Student Name` at import — take the first name plus the first letter of the last name and a full stop — and store only that derived display name in the `review` CPT. The full surname stays in the Notion bank; it does not travel into WordPress. Full names are not published anywhere on achology.com.
- **GDPR rationale (for the record):** republishing ~4,000 identifiable people's full names on Achology's own site is a fresh processing of their personal data; the first-name + initial form keeps the proof credible while sharply reducing identifiability. Kain ruled the initial-only form; full names were explicitly not chosen.

## 3. Your low-count data flag

Acknowledged. "Mindset Mastery" at 3 reviews (and the handful at 40–73) is real — the course-page review block needs a graceful low-count state so a sparse course doesn't look broken. That is **page-template work** and stays with the page card, not the CPT/ACF build; noted so the component spec carries it.

## Net for your build

Proceed with the `review` CPT + ACF group as proposed (reviewer display-name, star rating, review date, review text, source course, primary school, tier, featured), Local JSON, one-time import — **from the live bank**, with the **first-name + last-initial transform applied at import**. This is consistent with the S219 schema decision (the `/reviews/` page carries `WebPage` + `BreadcrumbList`; an individual review's `star_rating` is that reviewer's own score, never aggregated — DSRD 10 §9). The display components remain page work. Confirm back on `TO Chat` once the CPT + import are in and the name transform is verified on a sample.
