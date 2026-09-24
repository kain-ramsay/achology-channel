> **CHAT DISPOSITION, S382: ACTED ON, archived.** Folded into DSRD 8 section 31 (navigation order, book button, signed record, one new paragraph on the rail's labels) and section 32 (one hairline-spacing correction). `INSTRUCTION__DSRD_8_Corrected_Reexport_The_Book_Note_Prototype_S382` sent to Code, FROM Chat, telling him to re-export. Theme 0.406.0 to 0.411.0, the hero-side rulings in this same record, are named as open in DSRD 8 rather than folded in; they belong to the hero, not the side column, and have no section of their own yet.

**Needs from Chat:** fold these into DSRD 8 section 31's three flagged paragraphs, then say the word and the book note prototype is re-exported once, carrying all of it (your S360 reply, sections 1 and 6).

# RECORD: the book note side column rulings, theme 0.401.0 to 0.414.0

**From:** Claude Code, S131, Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** `REPLY__The_Book_Note_Batch_From_S114_And_S115_Answered_S360.md`, section 6: "file the missing ruling detail for 0.401.0 through 0.414.0".

**How this was written.** One file for the run, since the sitting was one continuous pass on one column. Each section below is the commit that shipped that version, copied from the theme's own history rather than recalled: its subject line, date and message, which quote Kain where the sitting had his words and carry the measured figures. **The hover contrast you named as unsourced is sourced in 0.414.0:** white on the primary orange measured 3.16 to 1 on a 14px semibold label, against a bar of 4.5, so the brand dark was taken as the fill instead. Later ship notes (0.620.0 onward) moved the primary button to the AA-safe orange site-wide; that postdates this run and is recorded in its own commits.

## 0.401.0: the book note's side column puts navigation first and the cover becomes a thumbnail

*Commit `a6066ea`, 2026-09-14.*

Kain, S114, on the rendered page: 'the sidebar and the book notes, it doesn't work. The table of contents is the second half at the bottom of the side panel, and the book and the button consume the entire top half.'

MEASURED BEFORE IT WAS TOUCHED, which is what turned a complaint into a number. The contents list began 611px down an 880px panel, 69 percent of the way down. The cover alone was 384 of that, 44 percent of the whole column, and it is the same picture the hero showed at the same size a moment earlier. The hairline shipped at 0.399.0 earlier in this same sitting made it about 70 worse: that separation was right and it was applied to a stack that was already in the wrong order.

TWO CHANGES. The contents goes to the top of the column. The cover shrinks to a 72 wide thumbnail beside the Amazon button, the two forming one short block under the hairline, which turns over with the order so the same line now sits beneath the contents with the ruled 48 on both sides.

THE THUMBNAIL STILL DOES THE COVER'S REAL JOB, which is not decoration: it opens as the hero leaves the screen so a reader always knows which book they are in. At 72 wide it does that for a fifth of the height.

THE COLLAPSED COVER HAS NO WIDTH, not just no height. A box that kept its width while closed would indent the button against an empty space for the whole first screen, and the gap beside it is a margin rather than the grid's column-gap for the same reason: a gap between tracks is drawn whether or not anything is in them.

THE ARTICLE PAGE IS NOT TOUCHED and the rules say so in their selectors. Its picture is a square crop rather than a 2:3 jacket, it carries no buy button beside it, and its contents list is shorter, so none of the arithmetic above applies to it.

css_gate PASS on knowledge-hub.css.

## 0.402.0: the book note column loses Know Your Psychology and takes the cover with its button beneath

*Commit `a1f7a8e`, 2026-09-14.*

Kain, S114: 'just lose the Know Your Psychology logo as I've asked you to, just replace that with a book image ... and have the View this Book on Amazon link directly underneath that. That takes up the second half of the card, of the column, and that's fine. There's just too much in that top column with that Know Your Psychology built in.'

THE ORDER IS CONTENTS, THEN THE BOOK, done with order rather than by moving the markup. This component is shared with the article page and the markup order is the article's, picture then offer then contents, so reordering the source would have moved the article's picture with it. Know Your Psychology stays on the article page, which has no book to put there.

THE SCREEN-HEIGHT BOX GOES WITH THE PANEL IT WAS HOLDING. That machinery existed only to keep the contents at the top and the mark at the foot of the screen (Kain, S112). With nothing left to pin down there, a fixed height would only force the cover and its button to overflow it: measured, the stack is 975 against an 880 box on a 1000 tall screen. The panel takes its natural height and travels.

THE COVER IS BACK TO THE COLUMN'S FULL WIDTH, which is the size it was always worth showing at and the size there was never room for while the panel was holding the mark at its foot. The 72 wide thumbnail shipped an hour earlier was the wrong answer to the right problem: Kain's words on it were 'that looks rubbish. You can't see the image.'

The button sits directly under the cover at full width, so the label is on one line rather than wrapping the way it did beside a thumbnail, which the previous ruling had named as a cost.

css_gate PASS on knowledge-hub.css.

## 0.403.0: the Know Your Psychology image returns, at the head of the book note column

*Commit `a649a3c`, 2026-09-14.*

Kain, S115: 'placing the Know Your Psychology image, the one that you just removed from the page, at the top of the page, above the table of contents.'

TAKING IT OFF AT S114 WAS NOT WRONG, AND THAT IS WHY IT CAN COME BACK HERE. What he objected to then was where it sat: pinned to the foot of a screen-height box, holding the contents and the cover apart and squeezing both. Removing it is what let the cover return to full size. At the head of a column that no longer has a height to fight over, it costs the contents 135 and nothing else.

IT TAKES THE BLOCK SEPARATION, 48 and a hairline, the same as between the contents and the book beneath it, so the column now reads mark, line, contents, line, cover and button.

THE PANEL BECOMES A FLEX COLUMN so the mark can be ordered above the stack it is a sibling of. In the markup the mark comes after that stack, which is the article page's order and is not moved: this page reorders what it draws, exactly as it already does for the contents inside the stack.

css_gate PASS on knowledge-hub.css.

## 0.404.0: the side column's hairline separation comes down from 48 to 32

*Commit `a53e478`, 2026-09-14.*

Kain, S115, on the rendered rail: 'There's, like, way, way, way too much space above and beneath the hairlines. It's completely inappropriate for the side column.'

HE IS RIGHT AND THE FAULT IS IN HOW HIS OWN RULE WAS READ. 48 above and below every hairline is his standing rule and it was applied here without asking what it was written for. It was written for the reading column, which is 800 wide. In a 256 column, 96 of air between two blocks is more than a third of the column's own width and reads as a hole rather than a separation. Air scales with the measure it sits in, and a rule quoted without its measure is a rule half read.

Code recommended taking the 48 when the standard was settled a day earlier, having named the height cost and then argued against its own reservation. That is recorded in the stylesheet beside the number.

EVERY SEPARATION IN THE COLUMN MOVES, on both page types, so the standard stays one thing: the hairline under the picture block, the two on the book note's own stack, and the one above the reading list. The column's order is unchanged: 16 from a label to its list, 24 inside a list, 32 and a hairline between blocks.

The reading column's own 48 is untouched. It is a different measure and the rule is correct there.

css_gate PASS on knowledge-hub.css.

## 0.405.0: the column's three labels take a step up and the count line goes lighter

*Commit `41a4ac1`, 2026-09-14.*

Kain, S115, having asked directly whether the contents heading was the right size: 'all three labels a step bigger, and a lighter count line.'

ALL THREE OR NONE. The contents heading, the reading shelf's label and the way out of that shelf are one set: same face, same weight, same capitals, same orange. Moving one would have left the other two looking like a mistake. 12 to 14 on all of them, in one rule that names all three so the set cannot drift apart again.

THE TRACKING BECOMES RELATIVE WITH THE SIZE. Two were already on .1em and the contents heading was on a fixed 1.2px, which is .1em at 12 and .086em at 14. A tracked label that does not track with its own size is a value that was right once.

THE COUNT LINE LOSES ITS WEIGHT, and it is the half of this that answers the original question. The heading's size was not the fault. The line beneath it carried the same size and the same 600 as the heading, so the block opened with two lines of identical type and neither won. 12 is the smallest step there is, so nothing could drop the size: the weight moves instead, 600 to 400.

That weight was raised deliberately once, when everything around it was at 600 and it was the odd one out. Both notes now sit together beside the value, so the next session can see it moved twice and why.

## 0.405.1: the contents heading actually takes the step up, from the rule that was winning

*Commit `5d709f8`, 2026-09-14.*

Found on the read-back, not assumed shipped. 0.405.0 named all three of the column's labels in one rule and moved two of them: the shelf's label and the way out of it went to 14 and the contents heading stayed at 12.

WHY. A later rule sets that heading through a :not(.kh-aside__head--share), which outranks the rule naming the three together. Same shape of fault as the reading label at 0.399.1 yesterday, in the same stylesheet: a second declaration further down quietly deciding the value.

The set is still named in one rule up there AND kept in step here, rather than that rule being deleted, because the cascade is what decides and whoever changes the value up there needs to find this one.

## 0.406.0: the book note hero's date line takes the author line's treatment

*Commit `3f3b0fa`, 2026-09-14.*

Kain, S115, asked how many type treatments the hero carried. Measured: two faces, six treatments, four of them Mulish at four sizes. He ruled on the pair that looked unconsidered, the author line at 16 and 500 and the date and read time three lines below it at 14 and 400: two small supporting lines doing the same job at two sizes and two weights.

THE DATE MOVES UP RATHER THAN THE AUTHOR MOVING DOWN, and that is not a preference. The author line's 16 is Kain's own from S086 and the reason sits directly above it in this stylesheet: '12 makes the author's name too small to be the fact it is'. Pulling it down to meet the date would have quietly overturned a ruling of his while appearing to tidy up.

SCOPED TO THIS HERO. The listen bar is a shared component carrying the same facts on help answers, quote pages and the Knowledge Hub, and none of those has an author line above it to match. Changing the component would have moved four page types to settle one.

The hero now carries four Mulish treatments rather than five, and the two that read as metadata read as one thing.

css_gate PASS on book-note.css.

## 0.407.0: the book note heading carries the author, and the line under it goes

*Commit `8ae53d1`, 2026-09-14.*

Kain, S115, on a hero he counted five pieces of text in: 'rather than keeping Book Authored by Jordan B Peterson, we just assign the words by the author name after the book name followed by colon Summary and Key Ideas in a lighter weight of the same size font.' Asked which half went lighter, he ruled: 'by Tara Brach: Summary and Key Ideas' together.

THE STORED TITLE IS NOT TOUCHED. The heading is composed from the title WordPress holds and the author the record carries. He was told before this was built that the visible heading and the stored title would stop matching, and accepted it. Nothing in the head, the metadata or the sitemap moves.

IT SPLITS ON THE FIRST COLON AND NOWHERE ELSE, because the stored titles are '{Book}: Summary and Key Ideas' and a book whose own name contains a colon would otherwise lose half of it. A title with no colon, or a record with no author, falls through to the title exactly as stored: 99 rows sit behind this page type and a composition that cannot fail safely is a composition that will.

SAME SIZE, ONE WEIGHT DOWN, AND NOTHING ELSE. Not a smaller step, not a different colour, not a lower opacity. The line has to read as one heading with two halves rather than as a heading with a caption stuck to it, which is what the separate line under it was.

ONE THING WENT WITH THAT LINE AND IT IS NAMED RATHER THAN LOST. The author's name was a link to their page on this site. A link inside an H1 that looks exactly like the heading around it is not a link anyone can find, so it was not carried up: the route to an author's page from a book note is now the body's own, inside Where the Author is Coming From. Raised with Kain in the sitting.

css_gate PASS on book-note.css.

## 0.408.0: the book note's heading takes Kain's folded-heading rule

*Commit `0a4e4c9`, 2026-09-14.*

Kain, S115: 'apply a rule to the header now so that the title is presented neater on each page, kind of similar to the rule you applied to the subtitle.'

THE RULE ALREADY EXISTED AND HAD NEVER REACHED THIS PAGE TYPE. His S081 ruling is that a heading folding onto a second line splits 60 to 70 percent onto the top line rather than evenly, and his words then were 'apply this to every heading that folds'. The routine that does it lists the article page's title, the article's H2s and H3s, the section labels and the contents rows. It never listed the book note's title, so 99 pages have been folding however the browser felt like it since that ruling was made.

It shows now because the heading gained the author's name an hour ago and was breaking mid-name.

IT CARRIES AN INLINE SPAN AND THAT IS FINE. The routine measures the element's own client rects and sets a max-width on it, so a heading whose second half sits in a span is measured and narrowed exactly like one made of plain text.

## 0.408.1: the folded-heading rule counts lines, not inline fragments

*Commit `63f6083`, 2026-09-14.*

Found on the read-back of 0.408.0 rather than assumed shipped. The book note's title took the rule and came out worse: a two line heading reported five lines and a top share of 21 percent, and the binary search then narrowed the box to satisfy a ratio that was never real.

WHY. A range over a heading returns one rect per inline FRAGMENT, not one per line. On a heading made of plain text those are the same thing, which is why this was right for as long as every heading in the list was plain text. The moment a heading carries a span, one line comes back as two or three rects and every number downstream is wrong.

IT WAS ALREADY WRONG ON THE CONTENTS ROWS, which have carried a number span and a title span since long before today. Nobody saw it because a wrong ratio there still produces a plausible looking break, which is the whole reason it survived: the fault was invisible until a heading folded badly enough to look it.

Rects are now grouped into lines by their top, to within a pixel of rounding, before the ratio is taken.

## 0.409.0: the author's name never breaks across two lines in the book note heading

*Commit `2a5eb5b`, 2026-09-14.*

Kain, S115, asking for the title to be presented neater. With the fold rule measuring correctly, the visible fault that remained was the break itself: 'Radical Compassion by Tara / Brach: Summary and Key Ideas'. Of all the places a long heading can fold, through the middle of somebody's name is the one a reader notices.

ONE SPAN PER AUTHOR, NOT ONE ROUND THE WHOLE STRING. Three of these records name more than one author, the longest being 'Kerry Patterson, Joseph Grenny, Ron McMillan', and holding all of that on one line is wider than the column at this size: it would push the hero sideways rather than fold. Each name is wrapped on its own, so a break can land between two authors, where a reader would break it out loud, and never inside one.

ONE COMMENT IN THE FIRST CUT OF THIS DESCRIBED BEHAVIOUR THE CODE DID NOT HAVE. It claimed nowrap allowed a break after a comma, which it does not: nowrap on a whole string forbids every break in it. The comment was written before the multi-author case was worked out and was corrected with the code rather than shipped.

css_gate PASS on book-note.css.

## 0.409.1: the folded-heading rule refuses a stranded last line

*Commit `7050b3e`, 2026-09-14.*

Kain, S115, asked for the title to be presented neater. With the name held whole, the book note heading folded onto three lines of 359, 462 and 83, the last carrying the single word 'Ideas'.

THE EXISTING RULE HAD NOTHING TO SAY ABOUT THAT. It aims the TOP line at the 60 to 70 band, which is the whole of his S081 ruling and is the right goal for a heading that folds onto two. A heading that folds onto three can satisfy it and still end on one word.

NARROWING IS WHAT FIXES A STRANDED WORD, which reads backwards until you try it: a slightly narrower box pushes a word down from an earlier line and the last line grows. It stops the moment the line count would rise, so a heading is never made longer to make it tidier, it never goes below three quarters of the width the main search chose, and it gives up rather than searching forever.

It only runs on headings of three lines or more, so every two line heading on the site is untouched and Kain's S081 split is exactly as it was.

## 0.410.0: the heading's lighter half begins after the colon

*Commit `42e9f2a`, 2026-09-14.*

Kain, S115: 'we need everything behind the colon to be the same font weight as the book name. So the book name and then by author, that will be the same weight, including the colon, and then Summary and Key Ideas, we'll just keep that as the lighter weight font across all book notes.'

RULED TWICE IN THE SAME SITTING AND THE SECOND STANDS. Asked which half went lighter he first said 'by Tara Brach: Summary and Key Ideas' together; looking at it rendered he moved the split to the colon. The book, the author and the colon are now one weight and only the subtitle is lighter.

The colon is written by the template rather than carried in from the stored title, so it stays attached to the author's name it follows. Punctuation belongs to the word before it, and a colon stranded at the head of a lighter span would be the thing a reader noticed.

css_gate PASS on book-note.css.

## 0.411.0: the book note's closing paragraph steps down one size

*Commit `603e135`, 2026-09-14.*

Kain, S115, on the rendered page: 'could I ask you to maybe reduce the size of the font in this final paragraph? For me, it just kinda feels like we're kinda closing the article off nicely by maybe making it one font size smaller.'

ONE STEP, NOT A NEW VALUE: 18 to 16, both on DSRD 7's scale, and the leading holds its 1.75 ratio so the paragraph keeps the body's rhythm at a smaller size rather than becoming a different kind of text.

IT IS FOUND RATHER THAN MARKED. :last-of-type on the body's own paragraphs lands on the closing one without the template having to tag it, so a book note whose last section gains or loses a paragraph still closes on the right one. Everything after it, the tags, the reading shelf and the signature, is furniture rather than prose, so the last paragraph of the body and the last paragraph of the writing are the same element.

css_gate PASS on book-note.css.

## 0.412.0: the author portrait names the person, credits the photographer in English, and gives its hairline room

*Commit `dc2ccc7`, 2026-09-14.*

Kain, S115, on the rendered page: 'there's not appropriate spacing on that whatsoever ... there needs to be the author's name above the kind of the text you've got there. Having a CC BY-SA 3.0, having a code there, that's just not good.'

HE WAS RIGHT ABOUT SOMETHING WORSE THAN THE CODE. The line read 'Gage Skidmore, CC BY-SA 3.0' directly beneath a photograph of Daniel Siegel, with nothing saying Gage Skidmore was the photographer. Under a portrait a bare name reads as the person in it, so the caption was naming the wrong man.

THREE CHANGES. The name of the person pictured sits above the hairline in the body's own type. Below it, a sentence: 'Photograph by Gage Skidmore, used under a Creative Commons licence', with the last three words linking the exact deed. And the hairline gets 16 either side instead of 8.

THE ATTRIBUTION IS STRONGER FOR BEING READABLE. A Creative Commons licence asks for the creator named and the licence identified; a sentence that names the photographer and links the deed does both, and does them better than a code nobody can expand. The link carries the version, so nothing is lost by keeping it out of the prose. Public domain reads 'Photograph in the public domain', ours reads 'Photograph by Achology', and a licence the parser cannot read keeps its words and loses only its link, which is the safe way round.

THE URL IS DERIVED, NOT LISTED. A table of licences would need editing every time a new one appeared in the data, and the day it was not edited the line would silently drop its link.

SIXTEEN EITHER SIDE, NOT THIRTY TWO OR FORTY EIGHT. Eight is the step for things that belong together, which is the opposite of what a hairline does. But this block is 240 wide inside an 800 column and sits inside a paragraph with the writing running round it, so the column separation would push the text beside it out of shape. Air scales with the measure it sits in, one step further down than the side column took this morning.

css_gate PASS on book-note.css.

## 0.412.1: the drawn mark is not called a photograph and does not carry its name twice

*Commit `3130eea`, 2026-09-14.*

Both found on the read-back of 0.412.0, on the variant that has no photograph at all.

IT CALLED AN ILLUSTRATION A PHOTOGRAPH. The drawn name plate took the same credit path as Achology's own photographs and rendered 'Photograph by Achology' under a plate that plainly is not one. It reads 'Illustration by Achology' now, on its own credit value rather than by sharing the photograph's.

AND IT PRINTED THE NAME TWICE. The plate reads 'TARA / Brach' and the new caption added 'Tara Brach' again eight pixels below it. The name line is for a photograph, which cannot say who it is; the mark is made of the name and says it already.

Achology's own PHOTOGRAPHS, which is Gerard Egan and Kain Ramsay out of the people folder, are unaffected and still read 'Photograph by Achology', because for them it is true.

## 0.413.0: the portrait caption gets its air above and the credit drops to two quiet lines

*Commit `7f5fcfe`, 2026-09-14.*

Kain, S115, on the render: 'add a little bit more space above the author name, create a little bit less space above and beneath the hairline, and the contribution, make that smaller on potentially two lines, photograph by name then second line used under a Creative Commons licence, and just have that in much, much smaller text.'

THE SIXTEEN MOVES UP RATHER THAN DISAPPEARING. It was above and below the hairline; it is now above the caption as a whole, and the hairline takes eight either side. The block has the same total height and the space is where it does something.

BOTH HIS READINGS OF THAT HAIRLINE ARE RIGHT BECAUSE ITS JOB CHANGED BETWEEN THEM. An hour ago it sat directly under the photograph, separating the picture from its credit, and eight was far too tight for that. It now sits between the author's name and the credit for the photograph OF that author, which belong together, and eight is the step for exactly that.

ELEVEN IS THE ONLY SIZE ON THIS PAGE NOT ON DSRD 7'S SCALE. The scale stops at twelve and the credit already was twelve, so there was nothing to step down to. It is written as a one-off with its reason beside it rather than tokenised: a token invites a second use, and a second use is how a scale gains a step nobody ruled. If a second place genuinely needs it, that is when it becomes a tier and goes to Kain.

The terms take their own line, which is what makes the smaller size read as a quiet footnote rather than a cramped sentence. The break is a block span rather than a br, so it still reads as one sentence to anything reading the page aloud.

css_gate PASS on book-note.css.

## 0.414.0: the Amazon button takes the brand dark as a fill

*Commit `0cd10a3`, 2026-09-14.*

Kain, S115, on the rendered page: 'it's actually a little bit invisible sitting at the bottom right hand corner of the page. So why don't we just make that the same Achology dark grey, with a fluctuation of your choice on hover.'

THE OUTLINE WAS RIGHT FOR WHERE IT USED TO BE. It took a hairline border and dark type at S113, when it sat directly under a 384 tall cover near the top of the column with the contents beneath it. It now sits at the foot of the column, last thing, on white, and a hairline outline at the bottom of a white column is a button that has to be looked for.

THE HOVER WAS LEFT TO ME AND THE OBVIOUS CHOICE WAS MEASURED AND REJECTED. Filling with brand orange is the site's own action colour, but the label is 14px semibold, which is not large text, and white on the primary orange measures 3.16 to 1 against a bar of 4.5. It would have looked right and failed.

So the fill deepens and the label warms: the ground to the darker footer tone, the words to the small-text orange that exists precisely for dark grounds, Kain's own ruling at S248. Measured from the tokens: 5.68 to 1. Unmistakably ours without being loud.

css_gate PASS on book-note.css.

*No em or en dashes in this file; checked before writing.*
