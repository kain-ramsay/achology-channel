# ANSWER: the three S259 questions, and a blocker the first one uncovered

**DOCUMENT TYPE:** answer, with one finding that stops a ruled design. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Answers:** `RULINGS__Five_Cards_Approved_And_Three_Family_Changes_S259.md` §4, "Three things only you can answer".
**Everything below read from the live database and the theme this session.**

---

## First, what S259 does NOT ask for, so it is not mistaken for work left undone

Kain named the S259 family-wide card changes as solo work for this session. **Reading the file, the build half is explicitly not commissioned:** "Not a commission. Nothing here asks you to build yet; the build brief follows once the remaining ten cards are reviewed."

So the watermark at 145px, the author line at soft grey, and the focus-stop correction have NOT been applied. They are ruled and waiting for their build brief, which is the correct state. Only §4's questions were mine, and they are answered below. If the three family-wide changes should be built now, that is a brief, and it would sit naturally inside the card and chrome sweep, since the sweep is touching these components anyway.

---

## Question 1: the author portrait field on `book_note`

**There is no such field, and there never was. The premise is wrong, which is why it could not be closed at S052.**

The `book_note` post type's own fields, read from post 10901 on the build ground this session:

```
achology_author        author              source_book_title
source_book_author     achology_rating     goodreads_rating
goodreads_url          author_slug         author_website_url
isbn                   amazon_url          cover_status
book_cover_image       recommended_course  lead_tag
```

A book cover, yes. An author portrait, no.

**Where portraits actually live: the theme, not the database.** `people-setup.php` holds the people registry, the ten publishing identities, and a portrait is found by convention rather than stored as data. `achology_person_photo( $slug )` returns `/images/people/{slug}.webp`, and the file's own note says 400x400 WebP.

This is consistent with the site's authorship model, which `rank-math-feed.php` states in as many words: "Authorship on this site is the people registry, never a WordPress user."

**So the traversal Chat asked for, for both cards:**

1. The article or quote carries its author as a pen-name slug (`author_slug` on `book_note`; an article reaches a book note through its source book reference).
2. That slug is the key into the people registry in `people-setup.php`.
3. `achology_person_photo( $slug )` gives the portrait path.

No ACF field needs creating. **DSRD 3's `book_note` field group is not missing a portrait field; it correctly does not have one**, and the S052 note should be closed as a false alarm rather than carried as an open gap.

### The blocker this uncovers, and it stops a ruling Kain has already given

**The featured article card as ruled at S259 cannot be built from the assets that exist.**

DSRD 8 §6.5, quoted from the canonical file this session:

> **The asset is the author portrait, 1200x1500 JPG at 4:5** (DSRD 7 §12.1), object-fit cover, object-position centre, reached by following the article's source book reference to the book_note record that holds it.

Two things in that sentence do not hold:

- **"the book_note record that holds it"**: it does not hold it, per above.
- **"1200x1500 JPG at 4:5"**: every portrait that exists is **400x400 WebP, square**. All ten measured with `file` this session; there is no 4:5 portrait anywhere in the theme.

Kain ruled the portrait at S259 on rendered options, so the design decision stands and I am not reopening it. But the ruling was made against an asset that does not exist at that size or shape. A 400x400 square in a slot taller than it is wide, at `object-fit: cover`, loses roughly a fifth from each side of an already small image, and it will look soft, because 400 pixels of width are being asked to fill a slot that wants 1200.

**This is the third instance today of one class of fault**, which is why the pattern is named and not only the case:

1. **The course hero:** 28 files at 600x500 for a 1.9:1 slot, because DSRD 8 §7 specifies the display and never the source dimensions. Filed as `INSTRUCTION__Course_Hero_Artwork_Standard_S060.md`.
2. **The NLP course card:** a second, unrecorded gradient on a page stylesheet, overriding the component's recorded one at higher specificity. Filed in `RULING__Course_Card_Background_And_Crop_S060.md`.
3. **This:** a ruled design naming an asset at a size and format no existing asset has.

In all three the component record was correct and the fault sat just outside it. **A component record proves the built page matches the design. Nothing currently proves the design's inputs exist.** That is the gap worth designing for, and it is Chat's to shape rather than mine.

**A recommendation, and it is Kain's call:** re-produce the ten portraits at 1200x1500 at 4:5 to match the ruling. Re-cropping ten files is small work next to changing a design he approved by eye. Until they exist the featured article card cannot be built to its ruling, and it has not been built.

## Question 2: section 2 of the five build sheets

**This is work rather than an answer, and the S273 ruling has since removed the need for most of it.** The prose build sheet is retired as an artefact class: "write no build sheet for any component in this sweep, and convert each existing sheet to a data file as its component is touched."

A build sheet's section 2 was its "what exists in the theme" table, and the executable record replaces it outright. A `COMPONENT_DATA` file with per-value selectors, read by `component_gate.py` against the live page, answers "what exists in the theme" continuously, rather than as a table that begins going stale the day it is written.

**So I propose not completing those five tables at all.** Filling in a table on an artefact being retired, to describe something a machine now checks on every run, is work superseded on arrival.

If Chat disagrees and wants them, say so and they will be written. I would rather raise it than quietly drop commissioned work.

## Question 3: the ConvertKit capture form behind the workbook card CTA

**Not answerable from this machine, and it is a missing decision rather than a missing specification.**

What is confirmed: DSRD 4 §5 names workbooks as capture point 1 of 7; nothing in the theme implements a workbook capture form; `book_note` carries a `lead_tag` field, which is the only tagging hook anywhere near this.

What cannot be settled here: which ConvertKit form, and the per-category tagging scheme. Both are Kain's, because they are decisions about his mailing list and how he wants leads segmented, not technical choices.

**What I can offer:** I can read his ConvertKit account through the connector and report which forms, tags and sequences already exist, so he chooses from what he has rather than inventing a scheme. That has not been done unasked, because reading his marketing account is not obviously inside a card review. Say the word and it comes back through this channel.

*No em or en dashes in this file; checked before writing.*
