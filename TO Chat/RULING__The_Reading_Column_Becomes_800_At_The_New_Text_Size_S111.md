# RULING: the reading column becomes 800px, ruled at the new text size, with 760 rendered and rejected

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 111. **Date:** Friday 11 September 2026.
**Given by Kain live in the S111 foundations sitting**, on the rendered help answer in Safari, tabbed, one width at a time, with the body role already carrying the size he ruled earlier in the same sitting.
**Owning document:** DSRD 7 section 4.1, the Container Max-Width Tokens table and the measure rule beneath it. Chat writes it.
**Filed under Harness Rule 14.** It is the second of two rulings this sitting and it depends on the first: `RULING__The_Reading_Text_Is_Bigger_With_More_Space_And_It_Is_Decided_Before_The_Width_S111`.

---

## 1. The ruling

**Kain's words, in order, walking the tabs one at a time.** On the second option against the first: *"yes, it does"*. On the third: *"Thats too far - please stick with the touch narrower option"*.

**The reading column moves from 880px to 800px.** Measured on the rendered page at the body role he ruled first: **about 94 letters a line, down from about 116 before this sitting began.**

**760px was rendered and rejected in the same breath**, which matters as much as the choice: the answer is now bounded on both sides rather than open.

## 2. What actually delivered the change, and why the order was the whole game

| | letters a line |
|---|---|
| before this sitting, 880px at the old body | **116** |
| after his first ruling, 880px at 18px on 1.75, column untouched | **103** |
| after his second ruling, 800px at the same body | **94** |
| the Udemy help page he brought as his comparison | **about 98** |

**The text ruling did most of the work and the column did the rest.** Had the sitting run in the order it was built, the width would have been chosen against 116 and then reopened the moment the text grew. He stopped it and said so before that happened.

**His own comparison is answered on the way past.** He raised Udemy on the reading that our column was far narrower than other sites'. Ours was in fact the longer line, and the site now sits just inside where Udemy sits rather than well outside it.

## 3. What this reaches, measured rather than assumed

`--container-article` is read in **21 places across nine stylesheets**, measured this session with comments stripped. Every one is either the reading column itself or something aligned to its leading edge, which is why they were given the same token in the first place:

`base.css` `.article-container`; `knowledge-hub.css` `.kh-article__inner`, `.kh-article__band > .page-container > *`, `.kh-foot__sep`, `.kh-foot__signature`, `.kh-hub__intro`, `.kh-listing__intro`; `book-note.css` `.bn-hero .breadcrumb-bar`, `.bn-hero__grid`, `.bn-read`; `course.css` seven reading and text blocks; `help.css` `.help-hero`; `people.css` three; `quote.css` `.kh-quote__inner`.

**So the change is one token, not a sweep of 21 numbers**, and everything aligned to the column stays aligned to it. That is the whole reason the token exists.

**One question that is genuinely open and is not mine to answer.** 880 was ruled by Kain at S085 as the container width for *every content page*, and section 4.1 says so in those words. This ruling replaces it for the reading column. **Does 880 survive anywhere, or does it retire the way 620 did?** On the measurement above nothing reads it except through this token, so the honest answer looks like retirement, with 880 kept as a record the way 620 is kept. Chat's call, or Kain's, when section 4.1 is rewritten.

## 4. What Chat is asked to write

1. **Section 4.1, the Container Max-Width Tokens table:** the content column is **800px**, ruled by Kain at Code's S111 on the rendered page at the 18px body, with 760px rendered and rejected. The 880px row moves to the same footing as the retired 620px row, kept as a record so an 880 met in an old file is recognised.
2. **The measure rule beneath it:** the measured line is about 94 letters at the ruled body. That rule's open sentence, that the reading column "is a rendered sitting in Safari with Code, on a real page in Mulish, and never a paper measurement taken here", is now closed, and the sitting it called for is this one.
3. **Section 4.1's sentence "It is not put to him again on any page" belonged to the 880 ruling.** It carries over to 800 unchanged.

## 5. What has not happened

**Nothing is swept and no theme file has been changed.** Kain's constraint at the open of this sitting stands: nothing moves until he has ruled on the whole reference page. Both rulings so far are recorded and rendered, and neither is built.

OWED BACK: confirmation that section 4.1 is rewritten, and a ruling from Chat or Kain on whether 880 retires or survives.

*No em or en dashes in this file; checked before writing.*
