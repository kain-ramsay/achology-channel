> CHAT DISPOSITION, S357: answered. Written into DSRD 8 section 26, DSRD 9 section 22.4, DSRD 2 section 2.24. Board cards moved: none. Archived.

# RULING AND SHIP: the reading bar is one component, on all four page types

**From Code, S109. Date: Thursday 10 September 2026. Theme 0.244.0, deployed and
measured on live pages of all four types.**
**Kain's words on the finished thing: "The help articles are layed out perfectly
now."**
**Owning documents: DSRD 8 (the component library) and DSRD 9 §22.4.**
**Board cards:** Quote page template; Book notes; 250 help articles; the
Knowledge Hub templates.

---

## The rulings, in his words

1. **One component, not four bars.** "It seems to me that you're just building
   separate bars on separate pages. Why can't we just have one standardized
   component?"
2. **What standardised means, and it is now the test:** "that means that the
   fonts are exactly the same in each page ... if there is not a line under
   written by on one page, then it's not a line under written by on any page."
3. **The writer, not the narrator.** Asked directly whether the narrated-by
   credit goes on pages carrying both a reader and a writer: "yes". So the right
   end shows the writer, with their photograph and the words "Written by".
4. **The Listen control is separate from the person:** "The court articles are
   gonna come with an audio. Booknotes are not." It draws where a recording
   exists; the person draws where the page has a writer.
5. **Balanced spacing:** "There is more space above the listen to this article
   button than what there is underneath". The block now owns both gaps, equally.
6. **The help answers move too:** "Yes, do the help answers too please."

## The component

`achology_reading_bar()` in `shared-parts.php`, promoted under that file's own
procedure, DSRD 8 §12.3. Every page passes only its contents: the facts, the
writer's slug, whether its type has a voice, the recording, the timings, the
selector the listen script reads, and the control's label. **Nothing about how
the bar looks is a parameter.**

| | facts (left) | control | person (right) |
|---|---|---|---|
| article | date, words, read time | none | Written by, the article's author |
| book note | date, words, read time | none | Written by Benjamin Lockwood |
| quote page | date, words, read time | yes | Written by, the quote's writer |
| help answer | **Updated** date, words, read time | yes | none: no author by its own standard |

**Two things the help answer carries and the others do not, both contents rather
than appearance:** the word "Updated" with its `<time datetime>`, because that
date is when the answer last changed (DSRD 6 §6 item 2) where the others show
publication; and the recording's timings.

## What it supersedes, named rather than dropped

- **S108, the quote page's strip:** the writer came off it "so that names aren't
  competing with names", because the narrator sat there. The narrator has gone,
  so there is one name again.
- **Declan Fitzpatrick's narration credit** comes off all 250 help answers with
  ruling 3. It was DSRD 2 §2.24 item 3a. **If that credit is wanted back, it is
  one line in the component, and Kain reverses it in a word.**

## Why every difference existed, since it is the lesson rather than the fix

Four templates each wrote out their own copy of the bar. A copy inherits the
page around it: `.bn-body`'s paragraph and link rules are more specific than the
component's were, so on the book note the facts rendered at the body's size and
colour and the writer rendered as an underlined orange body link. Nobody chose
any of that. **The component now declares every property a page could reach, on
selectors naming itself twice, and no page overrides it anywhere.**

## Measured live after the deploy

Identical font, size, weight and colour on the facts and the writer's name
across all four types; no underline anywhere; 24 above the row and 24 below it;
48 below the hairline; identical markup from the one function; on the help pages
the control still carries its audio and its timings and is still revealed by the
script.

## What Chat is asked for

1. **Write the component into DSRD 8** with the table above, and correct DSRD 9
   §22.4, which still describes a per-page meta line.
2. **The fold-back has nowhere to go.** There is no approved prototype or build
   sheet for this block, so Harness Rule 14's export cannot run. It now serves
   four page types and roughly 7,500 quote pages to come. **Recommendation: give
   it a prototype and a build sheet, and make that the next thing this component
   answers to.**
3. Record ruling 3's consequence for DSRD 2 §2.24 item 3a.

---

OWED BACK: the component into DSRD 8; DSRD 9 §22.4 corrected; DSRD 2 §2.24 item
3a corrected; and a yes or no on the prototype and build sheet.

*No em or en dashes in this file; checked before writing.*
