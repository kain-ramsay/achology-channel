# DELIVERY: the card sheet, and the five build facts per card

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Answers:** `COMMISSION__Build_The_Card_Sheet_For_Review_S255.md`.

**The sheet is built, deployed and committed** (`e3d7ccc`). **It has no URL
yet**, because it needs a WordPress page to attach to and Rule 8 puts page
creation with Kain alone. He has been asked for one empty page called Cards;
the moment it exists the sheet renders at its address and I will send the link.

Everything below needs no page and is delivered now.

---

## 1. What is on the sheet

Rendered from its live component, nothing re-authored:

| Section | Card | Renderer |
|---|---|---|
| §6.1 | Article card | `achology_kh_card()` |
| §6.2 | Book note card, vertical | `achology_kh_card()` |
| §6.3 | Quote card | `achology_kh_card()` |
| §6.4 | Workbook card | `achology_kh_card()` |
| §6.5 to §6.8 | All four featured cards | `achology_kh_featured_card()` |
| §7 | Course card | `achology_course_card()` |
| §13A | Grey-backdrop row, member cards | `achology_member_voices()` |

Grids are the real ones: `.kh-grid`, `.product-section__grid`, and §13A's own
grid from `components.css`. No width and no breakpoint is invented on the sheet.

**The course card shows six of the twenty-eight**, picked by name length, the
three longest and the three shortest, so the row shows the wrapping you asked
for. **There is no second rendition of the course card in the theme.** The Book
Note prototype's version lives in the page folder's HTML, outside the theme, so
the sheet shows the only component that exists.

## 2. Registered, and could not be rendered

| Card | Why |
|---|---|
| §6.2 book note, **horizontal** | `cards.css` has `.card--book-note--horizontal`. No template emits it |
| §8 School bundle card | `.card--bundle` in CSS. No template emits it |
| §9 Access All Areas card | `.card--aaa` in CSS. No template emits it |
| §10 Membership cards | `.card--membership` and both modifiers in CSS. No template emits them |
| §14 Review card | Neither CSS nor template. It belongs to the Reviews page, unbuilt |

**A second problem, separate from the component one.** The database holds **one
article and one book note, no quotes and no workbooks**. So the quote and
workbook cards have no real post to render, and "the longest real title, the
shortest, a quote past the clamp" cannot be honoured on any type. The sheet
says so in place rather than faking content.

## 3. Cards authored in more than one place

**§6.9 compact cards.** No component. The markup is authored inside
`single-article.php`, and **four of its five instances are hardcoded
placeholders pointing at `href="#"`**. Left off the sheet: rendering it there
would author it a third time.

---

## 4. The five build facts

Read off the components, reported as facts, nothing corrected.

### 1. Is the card a real link?

**The four standard and four featured Knowledge Hub cards: yes, and by an
unusual mechanism.** The shell is a `<div>`. Clickability comes from
`achology_kh_card_stretch()`, which emits a real anchor:

```html
<a class="card__stretch" href="{url}" tabindex="-1" aria-hidden="true"></a>
```

It is a genuine `<a href>` in the markup, so a crawler follows it. It is
removed from the tab order and from the accessibility tree, so a keyboard and a
screen reader never reach it. **No JavaScript is involved anywhere**, which
answers the part of your question that mattered most: no card's route exists
only in JavaScript, and no listing page is short of internal links.

Each card also carries visible anchors in its footer.

**The course card is the exception: it has no stretch anchor at all.** Its
shell is inert and only its two buttons are links, `Learn More` and
`Enrol Now`. Clicking the card itself does nothing.

### 2. What is the link's accessible name?

**The card title is inside no anchor on any card type.** The stretch anchor is
empty and `aria-hidden`, so it announces nothing. The named links are the
footer ones:

| Card | Announced link names |
|---|---|
| Article | "Read this Article", and "{n} Minute Read" |
| Book note | "Read Book Note", and "{n} Minute Read" |
| Quote | "Unpack this Quote" |
| Workbook | "Download Workbook" |
| Featured article | "Read this Article", and "{n} min read" |
| Featured book note | "Read Book Note", and "{n} min read" |
| Course | "Learn More", and "Enrol Now opens in a new tab" |

**So the thing you anticipated is real:** a listing page of twenty-four article
cards offers twenty-four links named "Read this Article" and twenty-four named
"{n} Minute Read", and no link anywhere carries the article's title.

### 3. What heading element does the card title emit?

Fixed in the component, never passed in by the caller.

| Card | Element |
|---|---|
| Article, book note, workbook | `h3` |
| Featured article, featured book note | `h3` |
| **Quote** | **none.** The quote text is a `div`; the card has no title element |
| **Course** | **none.** `<div class="card__course-title">` |

### 4. Do card images carry width and height, and lazy loading?

| Image | Dimensions | Lazy |
|---|---|---|
| Article banner, workbook strip, featured image areas | yes, WordPress adds them to `get_the_post_thumbnail()` | yes, same source |
| Book note bookshelf backdrop | **yes**, `width="900" height="1350"` | yes |
| **Book note cover itself** | **no width, no height** | **no `loading` attribute** |
| **Course hero image** | **no width, no height** | yes |

The book cover is the one worth flagging against the 0.05 CLS target: it sits
directly beside a backdrop that does reserve its space, so the two halves of
one panel behave differently.

### 5. What is in the alt attribute?

| Image | Alt |
|---|---|
| Bookshelf backdrop | `alt=""`, correctly decorative |
| Course hero image | `alt=""`, correctly decorative |
| Book cover | `"{book title} cover"` |
| Post thumbnails | whatever the media library holds, not set by the component |
| Watermarks, quote mark, stat icons | `aria-hidden="true"` on the wrapper, correctly decorative |

Nothing decorative is described and nothing meaningful is left undescribed,
with the one caveat that post thumbnail alts sit outside the component.

---

## 5. Observations, kept separate as you asked

Nothing below was changed.

1. **Two wordings for one thing.** Standard cards say "{n} Minute Read";
   featured cards say "{n} min read". Same data, same family, different words.
2. **The quote card is the odd one out three times over:** no heading element,
   no read-time link, and the only standard card whose body carries a different
   class (`card__body--quote`).
3. **The course card is the only card in the system whose surface is not
   clickable.** Whether that is deliberate is exactly what the review can settle.
4. **The title is never a link on any card.** It is consistent, so it reads as
   a decision rather than an oversight, but it is the single biggest difference
   between how these cards read to a person and how they read to a crawler or a
   screen reader.
5. **The stretch anchor is considered work, and its docblock says so:** the
   duplicate link is hidden from assistive tech precisely so it is not announced
   twice. Recording that because it looks like a defect at a glance and is not.

*No em or en dashes in this file; checked before writing.*
