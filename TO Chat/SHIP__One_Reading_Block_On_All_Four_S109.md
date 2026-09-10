# SHIP: one reading block on all four Knowledge Hub page types. Theme 0.235.0

**From Code, S109. Deployed, cache purged, and measured on all four live pages
at desktop and at phone width.**
**The ruling behind it:** `RULING__One_Reading_Block_On_All_Four_Page_Types_S109`.

## What changed, in files

Four templates, two stylesheets, two tools. The article and the book note draw
`.ach-listen-bar` instead of `.kh-article__meta`; the quote page's block moves
below its title; the help answer is untouched, because it was already the shape
everything else moved to.

## The two tools that named the old strip, moved with it

`publish_gate_body_acceptance.py`'s fixture and `tools/fold_back.py`'s measuring
selector both pointed at `.kh-article__meta--body`. Left alone, the first would
have gone on passing against a page shape that no longer exists and the second
would have measured null and reported a gap of nothing. Both now name the bar.

**`.kh-article__meta` and its separator rule stay in knowledge-hub.css for one
turn**, unproved rather than deleted blind; `css_deletion_proof.py` runs against
the rendered pages before they go. `.kh-article__author` is NOT dead: both
templates still draw it inside the new block.

## Two faults found by photographing the phone, and fixed rather than shipped

1. **The facts row broke inside a fact.** With four facts instead of three the
   row went full width on a phone and wrapped anywhere: "8 Sep / 2026", "Kain /
   Ramsay", four columns of two lines. The row now wraps whole facts.
2. **Then a separator could sit at the edge of a wrapped line**, first at the
   end of one and, once the dot travelled with its fact, at the start of the
   next. No rule in CSS can see where a line breaks, so on a phone the dots go
   and space does their work, 4 down and 16 across, both steps of the scale. The
   desktop row keeps the specification's " · ".

## What was checked before it went, and after

PHP lint on all four templates, on the server, before anything was sent. The
publish gate's body acceptance suite, 13 of 13. After the deploy, on the live
pages: the bar present on all four with its rule, the old strip gone, the quote
page reading title then bar then standfirst, the article line free of the
publication, and the phone width photographed on each.

**`page_gate` fails the article and the help answer and neither failure is this
change.** The article's seven are a supporting line at 36 words, an acronym used
before it is spelled out, a breadcrumb one step shallower than its address, an
orphan verdict the crawl could not reach, a thin keyword, a master-format image
and fifteen images with no srcset. They stood before this change set. Raised
here rather than left in a printout.

## What I need from Chat

Everything is in the ruling file: the standard into DSRD 9 section 22.4, the
superseded standfirst sentence, Kain's one word on "Updated", and a yes or no on
this component getting a prototype and a build sheet.

---

OWED BACK: nothing beyond the ruling file's four lines.

*No em or en dashes in this file; checked before writing.*
