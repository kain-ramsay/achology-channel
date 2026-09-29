**Needs from Chat:** write Kain's rotation rule into The Workbook Design Standard section 8, replacing "the image is chosen by a person, never at random"; the rule is already live in the cover folder's README and its rotation list.

# RULING: workbook cover images are used in turn, 1 to 37, then round again

**From:** Claude Code, S139 (factory), Tuesday 29 September 2026. **To:** Claude Chat. Given by Kain in this sitting, on seeing the Karpman workbook render without its cover picture and logos.

## Kain's words

"I've put 37 images into that folder because it's completely irrelevant which image each workbook uses. What I would like to happen is for you to choose one at a time and systematically use them all in turn. Thirty-seven and then just keep on using them ... use number one then number two for workbook two three for workbook three so on and so forth ... they're all generic images it doesn't matter which ones get used it just needs to be a different a different one for each workbook on rotation ... I want you to develop a system for for managing this and placing them. No one is going to instruct you ... You need to do the process for systematically using one through to 37 then one through to 37 every time you create workbooks."

## What is built

- **The rotation list:** `000__COVER_ROTATION.csv` in the Workbook Cover Images folder (Educational Publishing System project). One row per workbook in the order made: slug, image number, date, session. The next workbook takes the number after the last row's; after 37, back to 1. A workbook on the list keeps its number when re-rendered. Row 1: karpman-drama-triangle-workbook, image 1.
- **The folder README** (`000__WHAT_IS_IN_HERE.md`) now states the rule in Kain's words and replaces "a person chooses it".
- **The render applies it itself:** reads the list, assigns the next number to a new workbook, writes its row, and places that image faintly behind the front and back covers (as the hand-and-pen image sits in Kain's master template).
- **The logos, the same way every time:** the Know Your Psychology logo in the source course's school colour at the top of both covers, the Achology Publications logo at the foot, from the website assets' logo folders.
- **The Karpman workbook is re-rendered** with image 1 and both logos: `RENDER__The_Karpman_Workbook_S139.html` in TO Chat.

## Two more rulings, same sitting, on the rendered covers

1. **A white panel behind the cover text.** Kain: the image behind the text blocks "clashes ... ideally we'd have some sort of semi-transparent block behind the blocks of text that just makes the text on the page more readable". Built first at white 86% with solid white boxes; Kain then asked for "something in between ... so that the background image is still partially visible". As approved for his look: the front cover's title and description, and the back cover's block, sit on white at 55% with a 10px corner; the back cover's two boxes on white at 70%. Kain had approved the image itself: "I love how you've built that image in. It looks really, really neat."
2. **Every workbook ships as a locked PDF whose writing spaces can be typed in.** Kain: "people can edit the space that we give them for jotting notes. But they can't ... edit the actual handbooks and put their own names or their own logos ... So they're kind of locked but they're editable ... with the links within pointing ... to the correct places." Built: `RENDER__The_Karpman_Workbook_S139.pdf` in TO Chat, printed from the render; a typeable multi-line field over every block of writing lines and a two-digit field beside each 1 to 10 score (9 fields); links live and absolute (the course page on achology.com, the membership checkout); permissions allow opening, printing, copying text and filling the fields, and nothing else (RC4-128, owner password random and not kept). **Honest limit:** PDF permissions are honoured by normal readers (Preview, Acrobat, browsers) but can be stripped by someone determined with the right tool; they stop casual editing, not a determined one.

3. **No one-word last line, anywhere in a workbook.** Kain, on the cover description ending on "it." alone: "is there a way you can set some kind of standard? ... prevent a minimum number of characters from making their way onto and forming a new line of text." Built: the last two words of every paragraph, list item and heading are joined by a non-breaking space, and the text wraps with `text-wrap: pretty`; every render then measures the last line of every block and fails any that holds one word or fewer than 12 characters. Proved both ways this session: with the fix off the check named 6 such lines (the cover's "it." among them); with it on, 0. Kain approved the panel balance at 55%: "this is definitely the right balance ... very neat indeed."

Chat: DSRD 2 section 3.4 and The Workbook Design Standard gain all three (the panel as part of the cover; the PDF as the delivered format).

## For the record

Section 8's "the image is chosen by a person" and "one default image" are superseded; the default is no longer needed, since the rotation always yields a number.

OWED BACK: section 8 corrected.

*No em or en dashes in this file; checked before writing.*
