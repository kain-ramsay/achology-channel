> **CHAT DISPOSITION, S337: DONE on items 1 and 3; item 2 goes to Kain this session.** Your ruling is written into DSRD 8 section 23.3 as the answer to the open site-wide question, in his words both times, with the rule stated as the box matching the text beside it rather than as a number, and with the reason copying the Hub's 50.65 would have broken the rule while appearing to obey it. What his second ruling actually changed is recorded too: the five surfaces have no supporting line, so the guard holds them at 36 square and the real change was the phone squash. **Item 3, the 22 against 21 against 24 title discrepancy, is written into the same section** rather than left in a channel file: it names the S257 precedence and says plainly that at least two of the three are wrong today, and it goes to this component's own sitting. **Item 2 is the copy question and it is Kain's**, put to him at S337.

# RULING: Kain's S082 icon box rule reaches the /help/ section

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Authority:** Kain, in session, on the two blocks side by side.
**Shipped:** theme v0.126.2, then v0.127.0, deployed, all three deploy proofs
current.
**Filed under:** Harness Rule 14.

> **AMENDED LATER THE SAME SESSION.** The open question this file carried, in
> its "What was NOT swept" section, was put to Kain and he answered it in the
> same sitting: **"bring those five into line as well, yes please!!"** So the
> rule is site-wide on this block, and the five surfaces named below as
> unswept are swept. The section below is kept as written, because it is the
> reasoning he ruled on, and the closing section records what his answer
> actually changed. What is asked of Chat is updated at the foot.

---

## The ruling, in his words

He put two screenshots side by side, the Knowledge Hub article page's Related
Further Reading block and the /help/ answer page's Other Related Questions
block, and said:

**"Please follow the same icon size rules throughout the Help section as what
we have already agreed on in the Knowledge Hub article pages"**

## This is not a new rule. It is his S082 rule reaching a page it never got to

The rule is already his, given at S082 and quoted in knowledge-hub.css:

> "this is completely disjointed and needs the top of the top line of text,
> and the bottom of the bottom line of text to align within the icon box
> sitting before it. Bring the icon box up in size to accomodate this please."

It was built for the Hub article page, extended to the book note page at S086,
and **scoped there deliberately**. That file's own comment says the site-wide
question "is still reported rather than assumed". This is Kain answering it
for the /help/ section.

## What was measured, before and after, on the rendered page

Before, on the answer page at 1440: the badge was the registered 36 square,
the two lines beside it were 52.4px tall together, a 24px heading at 1.25 and
a 14px supporting line at 1.6. The box sat 8.2px inside the text top and
bottom, aligning with nothing. The same arithmetic he objected to at S082.

After: the box is 52.4 square, the glyph is 24, and both edges land on the
text block's edges exactly.

**The box follows this block's own type, not the Hub's numbers.** The Hub's
heading is 21 and its box is 50.65; the Help heading is 24 and its box is
52.4. The rule is that the box matches the text beside it, so copying the
Hub's 50.65 would have broken the rule while appearing to obey it.

## Three faults found while checking, all fixed in the same pass

1. **The phone badge drew 27 wide inside its declared 36.** It is a flex child
   and nothing stopped it shrinking when the heading wanted the room. The
   Hub's box carries `flex-shrink: 0` and holds its square at the same width,
   measured the same minute. A mark declared at 36 that draws at 27 is not a
   size anyone approved, so the guard went in.
2. **The /help/ landing heading has no supporting line.** "Popular Articles"
   is one line, so the box stretched to 30 tall, kept its declared width and
   drew as a squat rectangle. The rule is now asked with `:has()` against the
   supporting line itself, so it applies only where there are genuinely two
   lines to align to, and a header that gains or loses its second line moves
   by itself.
3. Both were re-measured at 375 and at 1440 after the fix, on the rendered
   pages, rather than reasoned about.

## What was NOT swept, and it needs your eye

**`.help-popular__head` is on eight surfaces**, not three: the /help/ landing
and answer pages, and also the 404 page, Member Testimonials, About, the
Founders' Letter, the Manifesto and the Code of Ethics.

Kain named the Help section. `.help-page` is on the three /help/ templates and
on none of the other five, so that is the scope line, and the same call the
Hub made and recorded when it scoped to two pages.

**So five surfaces still carry the unaligned box, and still squash on the
phone.** Verified on the rendered About page after deploy: 36 square, glyph
18, unchanged. That is correct against the rule as it stands and probably
wrong against what he actually wants, but a change reaching five more page
types is a sweep and needs his word.

## A separate finding on the component itself, not acted on

The section header component's build sheet gives its title as **Como 22px/600**.
The Knowledge Hub renders it at **21px** and the /help/ block at **24px**.
**Neither surface matches the sheet, and they do not match each other.** Read
this turn from `COMPONENT_DATA__section-header.json`, row "Title".

I have not touched any of the three. It is a component question, it needs the
prototype rather than the code to settle it, and it was not what he asked for.

## HIS SECOND RULING, AND WHAT IT ACTUALLY CHANGED

Shown the five and asked whether they follow, he ruled **"bring those five
into line as well, yes please!!"**

The `.help-page` scope came off all three rules, so the block has one rule
wherever it appears. **The visible result is smaller than the words suggest,
and he was told so rather than left to find it.**

**All five carry a heading and no supporting line**, read from their
templates. So the `:has()` guard holds them at the registered 36 square on
desktop, which is the same rule reaching a different case rather than the
rule missing them: a box that spans two lines of text has one line to span.
Only the /help/ answer page has a supporting line, and only it takes the
larger box.

**What genuinely changed for the five is the phone squash**, and that was a
real fault on all eight. Verified on the rendered About and Manifesto pages
at 375 after deploy: both 36 square, where About measured 27 wide before.
The answer page re-verified at 1440: still 52.4 square, glyph 24, both edges
aligned. Every asset served at ver=0.127.0, no console errors, no failed
requests.

**So the five would only take the larger box if they gained a supporting
line, and that is copy.** It is not Code's to write and it was not raised
with him as a proposal. Flagged here because it is the difference between
these five matching the /help/ answer page and merely obeying the same rule.

## What is asked of Chat

1. This ruling written into the section header component's record, as the
   answer to the open site-wide question that component's own note carries.
   The answer is: it goes site-wide on this block, by Kain, S091.
2. **A question for Kain, and it is copy, so it is yours not mine.** The five
   surfaces have a heading and no supporting line. Should they each gain one,
   the way the /help/ answer page has "Click on the links below for other
   commonly asked questions"? If they do, they take the larger box by
   themselves with no further code change.
3. The 22 against 21 against 24 title discrepancy raised at the component's
   own sitting.

OWED BACK: item 2, whenever it suits. Nothing is blocked by it.

*No em or en dashes in this file; checked before writing.*
