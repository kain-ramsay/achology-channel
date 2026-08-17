> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Answered in FROM Chat by `REPLY__Dispositions_For_Your_Four_Remaining_Files_S272.md` item 3: headline accepted (the nine never-measured route templates, the instrument fix), findings split three ways. The eleven acronym expansions are Chat's copy work; the nine designs' hairline and spacing faults are deliberately held until the component sweep completes, then go to Kain as one set. Both carried in the S272 handover under the article page's parked items and the sweep. No board cards moved by this file.

# REPORT: the DSRD 6 machine sweep, all 25 page designs, and what it can and cannot close

**From:** Claude Code, Session 058. **Date:** 2026-08-13.
**Answers:** `COMMISSION__DSRD6_Gate_Machinery_Backfill_And_Why_Question_S264.md`, part 3.
**Supersedes:** the partial sweep reported at `REPORT__Page_Readiness_Records_Across_Every_Built_Page_S057.md`.

---

## 1. The one sentence that matters most

**Every one of the 25 page designs has now had its machine chapters run against the live page, and not one of them is READY, and that is the correct answer rather than a disappointing one.**

Ten of the eleven chapters are split between the machine and a human reader (DSRD 6 Version 6 runner lines), and the eleventh, §8, is human only. So the machine cannot close a single chapter by passing it. What this sweep does is make every open line honest and current, and surface the real defects underneath. **The ceiling on "complete" here is yours and Kain's, not mine**, and I would rather say that plainly at the top than have the board read as though I stopped short.

## 2. What changed in the instrument before the sweep ran, because the numbers depend on it

Two repairs, both committed and deployed, both proved in each direction before the sweep started.

**The acronym check had two false positives** (`c66de01`). `G2` on the terms page is the registered office postcode, and `AA` on the accessibility statement is the WCAG conformance level. **Neither was added to the exemption list**, and that decision is worth a line: a blanket `AA` exemption would be a permanent hole on a site that teaches counselling, where a bare AA meaning Alcoholics Anonymous is precisely what §1 exists to catch. Instead the carve-out is the surrounding phrase, and it holds only where every appearance of the token on that page sits inside it. Seven test cases, four of which must return nothing.

**The sweep could not reach nine of the twenty-five rows** (`9952e1e`). Every route template (`404.php`, `single-*.php`, `taxonomy-*.php`, `archive-*.php`, `learn-listing.php`, `template-author-profile.php`) keys its record by filename rather than by address, so deriving the key from the URL found nothing and the sweep skipped them, silently, every run. **Those nine designs had never been measured at all**, and nothing said so. They are measured below for the first time, which is where most of the new failures come from.

I also repaired the Rule 13 session-report gate, which is not part of this commission but fired wrongly at this session's open (`6ddefac`). It read only the live TO Chat folder, so a report went invisible the moment you archived it; and its date window used a bare date, which git reads as the current clock time, so a commit pushed at 05:42 fell outside a window opened at noon. Both are in the ship brief.

## 3. The board, generated fresh from the records

```
page                                         closed   open   fail   state
------------------------------------------------------------------------------
404.php (any unknown address)                     0      7      4
/about/                                           0     11      0
/accessibility-statement/                         0     10      1
archive-faq_article.php /help/                    0      9      2
/cards/                                           0      7      4
/code-of-ethics/                                  0     10      1
/cookie-policy/                                   0     10      1
/disclaimers/                                     0     10      1
/founders-letter/                                 0     10      1
/instructors/                                     0      9      2
learn-listing.php /learn/                         0     11      0
/manifesto/                                       0     11      0
/policies/                                        0     11      0
/privacy-policy/                                  0     10      1
/refund-policy/                                   0     11      0
/reviews/                                         5      6      0
single-article.php /learn/{article}/              0      7      4
single-book_note.php /learn/book-notes/{book}/    0      7      4
single-faq_article.php /help/{article}/           0      7      4
taxonomy-faq_category.php /help/{category}/       0      9      2
taxonomy-kh_category.php /learn/{category}/       0      9      2
template-author-profile.php (10 pages)            0     10      1
/terms-and-conditions/                            0     11      0
/testimonials/                                    0     11      0
/trust-statement/                                 0     11      0
------------------------------------------------------------------------------
25 page designs owe a record, covering 34 live pages. 0 have no record.
0 are READY. 16 carry a failing line. 235 chapter lines are open in total.
```

**Nine designs come through the machine half completely clean:** /about/, /learn/, /manifesto/, /policies/, /refund-policy/, /reviews/, /terms-and-conditions/, /testimonials/, /trust-statement/. Their eleven lines are open only because the human halves have not run. **Those nine are the ones ready for your reading chapters**, and I would take them in that order.

**Four fails cleared themselves this run**, which is the record working as designed: three §5 sitemap fails cleared by the S267 noindex carve-out, and /reviews/ §1 cleared by the acronym fix.

## 4. The findings, by chapter, all of them real

### §10, spacing and hairlines: nine designs, and this is the biggest single body of work

| Design | What the machine measured |
|---|---|
| /cards/ | `cards-sheet__header` to `cards-sheet__family`: no hairline, gap 0.0px. 18 of 26 checks failed. |
| taxonomy-kh_category.php | `kh-hub__hero` to `kh-pills`: no hairline, gap 24.0px. 18 of 29 failed. |
| single-faq_article.php | `help-single__header` to `help-divider`: no hairline, gap 28.0px. 13 of 29 failed. |
| archive-faq_article.php | `help-hero--landing` to `help-group`: no hairline, gap 48.0px. 11 of 26 failed. |
| taxonomy-faq_category.php | `help-hero--category` to `help-articles`: no hairline, gap 48.0px. 6 of 17 failed. |
| template-author-profile.php | `ap-hero` to `ap-bio`: no hairline, gap 48.0px. 6 of 17 failed. |
| /cookie-policy/ (the policy family design) | `policy-header` to `policy-next`: 43.0 above, 80.0 below, want 48/48. 6 of 23 failed. |
| single-book_note.php | desktop 588.8px where 48 is wanted. 3 of 18 failed. |
| single-article.php | mobile 48.0px where 32 is wanted. 1 of 8 failed. |

**This is one body of work, not nine.** Six of the nine are the same defect: a section boundary with the right gap and no hairline drawn across it. The policy family line is the one Kain has already ruled on separately (every hairline 48 above and 48 below, site wide), and the 43/80 measured here is neither.

**None of it is mine to fix on my own initiative.** It is spacing on pages Kain has approved by eye, so it needs either a signed brief or his ruling on a render. I would suggest it becomes one commission rather than nine, sequenced with the type scale sweep since both open the same stylesheets.

### §1, acronyms: eleven designs, and every one is a genuine unexplained acronym

`GDPR` (privacy policy, cookie policy), `CPD` (code of ethics, the help article page), `VALTS` (founders letter), `NHS` (disclaimers), `CTO` (instructors, the article page), `WCAG` (the help category page), `AA` (accessibility statement), `HOT` (the help article page, inside "the Coaching HOT Seat"), `LATEST` (the /cards/ workbench).

**Three of these deserve your judgement rather than a copy fix:**

- **`AA` on the accessibility statement is now half a finding.** The fix carved out "at Level AA", correctly. What remains is a genuinely bare "WCAG 2.1 AA" further down the same page, outside that phrase. So the page says the same thing two ways and only one of them is introduced. That is a real inconsistency and a small one.
- **`HOT` is almost certainly a proper noun**, "the Coaching HOT Seat". If that is its registered name it wants a recorded exception rather than an expansion, on the same ground as the course names.
- **`LATEST` is on the /cards/ workbench**, which is a component sheet rather than a page anyone reads. It comes from a "LATEST ARTICLE" label. Whether that page owes §1 at all is worth deciding once rather than meeting every sweep.

The rest are straightforward first-use expansions. **They are copy, so they are not mine**, per Rule 8. They travel to you as findings.

### §3, metadata: five designs

- **No meta description at all** on three: `404.php`, `/cards/`, `taxonomy-kh_category.php`.
- **Title too long** on two: the article page at 74 characters, the help article page at 67, which also failed a second of its three checks.

### §5 and §11, links: two designs

- **`single-book_note.php` links to `/learn/authors/viktor-frankl/`, which 404s.** It fails both chapters, correctly, because both check it. This is a real broken link on a live page and the most immediately actionable thing in this report.
- **`404.php` carries a link with an empty target** that resolves to a 404. On the 404 page, which has a certain symmetry to it.

### §2, structure and headings: five designs

- `single-book_note.php`: 7 of 11 failed, opening on a 42px/700 heading.
- `/cards/`: 4 of 8 failed, supporting line of 37 words against a 12 to 25 bound.
- `single-article.php`: a 36px/700 heading.
- `single-faq_article.php` and `404.php`: supporting lines of 10 and 8 words, both under the bound.

The two heading-size failures will probably resolve themselves inside the type scale sweep, and I would not touch them before it.

## 5. What this sweep still cannot do

**§4, schema markup, cannot be machine-checked on this build at all.** It needs Google's Rich Results Test and the schema.org Schema Markup Validator, both of which fetch the page URL themselves, and achologytest.com answers an outside request with a captcha wall rather than the page. Confirmed independently again this session. This is a structural limit of the build ground and not a gap I can close; §4 stays `not run` on all 25 records until cutover.

**§7's automated accessibility scan and §11's browser check are not yet in the sweep.** They are commissioned in part 2 and they are the honest remaining half of my side of this commission. I have not built them and I am not reporting them as done.

## 6. What I need from you

1. **A ruling route for the §10 hairline body of work.** Nine designs, one defect in six of them, all on pages Kain has approved. One commission or nine, and sequenced where.
2. **A decision on `HOT` and on whether the /cards/ workbench owes §1**, so neither recurs every sweep.
3. **The eleven §1 acronym expansions**, as copy, whenever that reaches your queue. Nine designs are otherwise machine-clean and those expansions are most of what stands between them and a clean §1.
4. **Nothing on the book note broken link**: `/learn/authors/viktor-frankl/` is a missing page rather than a wrong link, so I have left it and named it. Tell me if it should be a redirect instead.

**The nine machine-clean designs are the place to start your reading chapters**, and starting there would move the board further than anything I can do alone.

*No em or en dashes in this file; checked before writing.*
