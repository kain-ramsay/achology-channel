# RULING: the body picture follows the page's subject, on any article that says who it is about

> **CHAT DISPOSITION, S365: CLOSED.** Written into DSRD 2 section 1.5 and DSRD 8 section 34. `subject_name` given its home (record field, required with `author_slug`). Kain's call on the 28: publisher press photo where terms allow and are recorded, otherwise the book cover. Both answered in `FROM Chat/RULING__Answers_To_Code_S117_To_S120_And_Kains_S365_Rulings_S365.md`. Board: Article page, via Code.

**Filed by Claude Code, Session 120. Date:** 16 September 2026. **Session type:** factory, with theme change sets made on Kain's word in the sitting, per Harness Rule 1.
**Given by Kain directly in this sitting**, on the rendered pages in Safari. Filed under Rule 14 so Chat writes it into the document that owns it, DSRD 2 on the article page and DSRD 7 section 15 on the component.

---

## What he ruled, in his words

On being shown the finished author biographies: **"any article that names someone, especially within the title, could we apply the same the same component and use either a book or, um, an image of them?"** and, on the answer being put to him, **"Yes, please do that Claude - this will elevate the entire Knowledge hub to a far greater level - credibly, and visually."**

Earlier in the same sitting, on the drawn name plate the pages had been falling back to: **"whilst that card that you've designed looks nice, and it does look nice, it's actually pointless if you think about it ... why would we want to just draw our own card when we can use an actual photograph, an image of the person, or a photograph, or image of their actual books."**

And, on the biography pages before any of this: **"build an image of either the person or the book in the middle of these author articles, main body of works and ideas."**

## What was built on it

**The test is the field, never the text.** An article draws a subject picture when it carries `author_slug`, the person it is about, and not otherwise. This was put to Kain before it was built, with the measurement behind it: 67 of the published articles mention one of these people somewhere in the writing, and a picture chosen from a passing mention would be wrong as often as right.

The caption's name comes from a new `subject_name` field, falling back to the page's stored focus keyword only where that keyword IS the subject. Every one of the 51 biographies satisfies that test and Aaron Beck's article does not: its keyword is "revolutionized cognitive psychology", a phrase and not a person. **`subject_name` needs a home in the record and the importer, which is a specification decision and therefore Chat's.**

## What is live now

- **All 51 author biographies carry a real picture**, checked one page at a time on its own address: 46 the person, 5 their book.
- **Three older field-authority articles** now carry their subject: Aaron Beck, Albert Ellis, Hans Eysenck.
- **23 photographs that had been sourced, licensed and recorded months ago** were converted into the theme, having never been converted before. That is the only reason those pages had a plate.
- **Two wrong people were struck** and are gone: the Susan Forward picture is a HUD housing director of that name, the William Irvine one an engraving of a Continental Army general. Both entered through a Commons name search.

## The finding Chat needs, because it decides the rest of the job

**Of the 29 book note authors with no portrait, 28 have no free licence photograph anywhere.** Checked one at a time through Wikidata: Tara Brach, Kelly McGonigal, Norman Doidge, Kristin Neff, Edgar Schein, William Ury and the rest return no portrait held against the person. Only Karl Popper did, and he is now live on his own note. The tool was proved against Daniel Goleman and Brené Brown, who resolve correctly, so this is a fact about free licensing and not a fault in the search.

**The route that works is the person, never the name.** Every row in the photographs record marked P18, Wikidata's image property, is the right person. All three wrong faces this project has published came from rows marked "search". Two new committed tools now hold that method: `tools/author_photo_fetch.py`, which resolves the human first and refuses a licence it cannot read or a file too small to use, and `tools/author_portraits.py`, which converts to the theme's 600 by 750. Neither chooses a face; a person checks a contact sheet.

**So the open question for Kain, and it is his because it is money and risk, not craft:** the 28 remaining authors have plenty of photographs online and effectively all of them are owned by somebody. The options are to license them, to use each author's publisher press kit where its terms allow it, or to leave those notes with the name mark, which is what the book note family was designed to do and which costs nothing. Code will not put a picture on a site that takes card payments without a recorded source.

OWED BACK: a home for `subject_name` in the record and the importer, and Kain's call on the 28.

*No em or en dashes in this file; checked before writing.*
