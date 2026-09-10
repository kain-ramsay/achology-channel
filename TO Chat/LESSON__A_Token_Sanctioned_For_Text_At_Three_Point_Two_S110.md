# LESSON: a colour token is sanctioned for text at a ratio text cannot legally use

**From Code, S110. Date: Thursday 10 September 2026. The page it was found on is
fixed at theme 0.324.0; the token's own note is not mine to change.**
**Found** while fixing the UKRLP credit line on the help answers, which Kain
asked for as its own small change after it had failed the gate all afternoon.

**Owning document:** DSRD 7 section 1.1, the colour standard, and base.css's own
token comment which restates it.
**Board card:** none.

---

## The line in base.css

`--color-mid-grey: #8A9199` carries this note:

> single-line captions, meta, separators, decorative icons ONLY, 3.2:1

Three of those four are non-text: separators and decorative icons answer to the
3:1 non-text bar, and 3.2 clears it.

**Captions and meta are text.** Ordinary text answers to 4.5:1. Measured on white,
#8A9199 is 3.19:1, so a caption or a meta line drawn in this token fails WCAG
1.4.3 before anybody has typed a word into it.

## What it cost on one page

The help answer's UKRLP registration line took this token, correctly by that
note, and was the ONLY accessibility violation axe reported on all 250 help
answers. The gate reported it every time that page was run today.

The fix was one token up: `--color-soft-grey` at 5.47:1, which base.css already
names for "secondary supporting text". It keeps Kain's S100 ruling that the line
reads as quiet meta, because 5.47 against the answer's own 10.48 is still plainly
subordinate. Zero violations after, on both help page types.

## Why this is a document fault and not a page fault

**The next page to follow that note lands where this one did.** Nothing stops the
token being used for a caption; the note actively invites it. Any component
reaching for a quiet meta line and reading that sentence gets the wrong colour
and a gate failure it did not cause.

**And the ratio is stated as though it were a licence.** "3.2:1" beside a list
that includes text reads as "and this is fine", when for half the list it is not.

## What Chat is asked to decide

Whether the note should read that the token is for NON-TEXT only, with meta and
captions sent to `--color-soft-grey`; or whether it keeps meta and captions and
the ratio is called out as failing for those two uses.

**I have not swept the site for other users of the token in text.** That is a
sweep and needs a brief. It is worth knowing the count before the note is
rewritten, and I can produce it on one instruction.

---

OWED BACK: a ruling on the note, and a word on whether the sweep is wanted.

*No em or en dashes in this file; checked before writing.*
