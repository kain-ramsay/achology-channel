# REPORT: the book note page audited against §32, the Amazon answer (it does not work), and the export you asked for

**From:** Claude Code, Session 83. **Date:** 25 August 2026.
**Answers:** `ASK__Export_The_Draft_Private_And_Scheduled_Content_S307.md` in full, both halves.
**Measured on:** the rendered page at `/learn/psychology/book-notes/mans-search-for-meaning/`, theme v0.99.5, at 1440, 768 and 375, plus the approved prototype and the two governing DSRD sections read this turn.

---

## 1. The Amazon button does not work. Do not let Karen cancel Genius Link.

**Asked:** confirm the Buy on Amazon button resolves through Amazon OneLink to a country store with the right tag.

**It does neither.** Measured on the rendered page:

- Both Amazon links, the hero button and the shelf button, resolve to **`https://www.amazon.com/dp/0807067997`**. A bare US product URL.
- **There is no `tag=` parameter on either.** No affiliate tag, so no commission is earned on any click, from any country.
- **There is no OneLink script on the page.** The full external script list is the theme's own five files plus Complianz. Nothing from Amazon, nothing from Genius Link.

**So every click on that button today earns nothing, and a reader outside the United States lands on the wrong store.** The six dollars a month is not the thing to cut; it is currently the only thing doing this job at all.

**What closing it needs, and one part of it is not mine.** The URL comes from the CSV's own column, so tagging is a data change and cheap. **OneLink itself is third-party JavaScript on a site that takes card payments, which Harness Rule 11 makes Kain's decision and not mine.** I am not installing it and I am not proposing a workaround. Put it to him as a decision, with the monthly saving named, and I will build whichever way he rules.

## 2. The export: 105 rows

Attached below as one table: title, address, post type, status, template. **69 articles and 36 pages, every one a draft. No private and no scheduled content exists on the install.**

The addresses are the real intended ones, resolved through `get_sample_permalink()` rather than the raw `?p=` form a draft returns from `get_permalink()`, so they are usable for your reconciliation as they stand.

The 69 articles are the 51 biographies and 18 instructor articles held under Kain's S083 ruling. The 36 pages are the academy and school structure.

*(Table filed as `EXPORT__Unpublished_Content_S083.md` beside this file, so this report stays readable.)*

## 3. The book note page, audited against DSRD 9 §32 and DSRD 8 §20

**The page is built, complete and correct.** All nine blocks of §32.1 are present and in order. The five locked H2s are exact. The travelling shelf carries its full content stack. The three responsive tiers behave as §20.4 and §32.9 item 9 specify, including the shelf sitting above the note below 1024px, verified by rendered position rather than by markup order. No horizontal scroll at any of the three widths.

**Every difference I found between the built page and those two documents traces to a later ruling by Kain that neither document ever received.** That is the finding, and it is Chat's to fix in the documents rather than mine to fix in the theme.

| Where | The DSRD still says | The build correctly does | The ruling that moved it |
|---|---|---|---|
| §32.3 hero overline | 11px | 12px | The nine step type scale, `RULING__The_Nine_Step_Type_Scale_Approved_S056`, swept under the brief Kain signed at S270 |
| §32.3 book author line | 19px | 18px | same |
| §32.4 body text | 17px | 16px | same |
| §20.2 contents list links | 13px | 12px | same |
| §20.2 contents list heading | 11px | 12px | same |
| §20.3 current-section highlight | #C64E14 | #B8460F | `--color-orange-link` darkened for AA contrast, Kain S248, on the rendered options |
| §32.2 reading column | "measures 880 at desktop" | 792px | Never true. The approved prototype's own container is `max-width:1200px; padding:0 48px`, so 1104 minus the 264 shelf minus the 48 gap is 792. The 880 appears to have been carried over from the article page's column |

**Line-height and weight were not touched**, which is right: the S270 brief forbids it in as many words, and I checked rather than assumed. Body paragraphs render at 16px on a 1.75 line-height, the H2s at 24px with 32 above and 16 below, and the pull quote at 18px italic with its 3px orange edge and 20px indent, all exactly as the prototype has them.

**One correction to my own working, recorded because it nearly became a false report.** I first read the tablet tier as putting the shelf below the note and was ready to call it a fault. I had read markup order rather than rendered position. The `order: -1` rule is present and works at both tiers. The page was right and my measurement was wrong.

## 4. What is actually left on this page, and it is Kain's eye rather than my hands

§32.9 closed all nine open items on paper, but two of them close **"in Safari on the live page"** by their own wording, and neither sitting has happened:

- **Item 8, the moving highlight in the contents list.** Built and working; the marked line goes `--color-orange-link` at weight 600 and every anchor resolves. §32.9 says it is judged with the shelf pinned beside the text, which only exists on the real page.
- **Item 9, tablet and phone.** Built to the three tier spec. §32.9's own words: "Code builds it, Kain rules it in Safari."

**Nothing else on this page is waiting on anybody.** It is going to Kain in Safari this session.

## 5. What is asked of Chat

1. **Correct the seven rows in section 3** in DSRD 9 §32 and DSRD 8 §20. Both documents predate the type sweep and the S248 colour ruling and now describe a page that no longer exists.
2. **Put the OneLink decision to Kain** under Rule 11, with the monthly saving named. The Genius Link cancellation is on hold until he rules.

*No em or en dashes in this file; checked before writing.*
