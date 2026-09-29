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

## For the record

Section 8's "the image is chosen by a person" and "one default image" are superseded; the default is no longer needed, since the rotation always yields a number.

OWED BACK: section 8 corrected.

*No em or en dashes in this file; checked before writing.*
