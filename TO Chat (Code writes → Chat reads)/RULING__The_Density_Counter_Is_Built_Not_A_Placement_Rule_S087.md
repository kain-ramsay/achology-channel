# RULING: the density counter is built, and the placement rule Kain proposed was talked out of on the evidence

**From:** Claude Code, Session 087, 26 August 2026.
**Ruled by:** Kain, directly in session, at the close of the S087 sitting.
**Filed under Harness Rule 14.** Two things travel with it: a change to what a gate script checks, which normally arrives as a commissioned brief, and a body of measurement that bears on DSRD 6 §5 item 11's recorded contradiction.
**Board card:** the Knowledge Hub scoring card.

---

## 1. What Kain proposed, and why it was not taken

His words:

> "Could we set a rule, on all book notes and author biographies, that the first occasion, the middle and the last time an author's or person's name is mentioned in an article, it is done so in full, as per the key term we need to rank for? What do you think?"

Then, when given an assessment:

> "Will this actually be likely to serve us? I don't want to make suggestions that you just follow. This needs to actually work for us."

**It was measured before it was answered, on the Carl Jung biography: 1,891 words, the full name present four times, the surname alone 39 times, and a pronoun 77 times.** Three fixed full mentions is fewer than the page already carries, so the rule would not have moved a single page. Its first-mention third is also already required twice over: by DSRD 6 §1's front-door rule, and by move 4's requirement that the phrase appear in the opening tenth of the body.

**Two further things it would have got wrong.** On a book note the phrase we rank for is the book's title, not the author, per item 11's own by-page-type list, so the rule would have done nothing for book note scores at all. And the density pass already commissioned at S309 produces full-name mentions spread through the whole piece as a side effect, including near the close, so the rule would largely have described work another rule already does. The growth governor forbids exactly that.

**Kain took the assessment and ruled the counter instead.** Recorded here because he asked directly not to be agreed with, and the honest answer was no.

## 2. What was built, on his word

`search_gate.py` gains `keyword-density`, a row on every page. It reads the focus keyword and the body from the install, counts the phrase, and reports the count, the word count and the percentage together.

**The real finding underneath his question, which is the reason this exists.** "About fourteen uses", as the S309 brief puts it, cannot be checked by anybody. Nobody can see it by eye and nothing counted it, so it was a standard that depended on somebody being careful. That is what he had put his finger on, and it is closed by a counter rather than by a rule.

**Three things about how it is built, each because the alternative would have been quietly wrong.**

It counts `post_content` and never the rendered page, because item 11 says "Every Rank Math test reads the editor content and the Rank Math fields; nothing added by the template counts." A count off the rendered page would include the header, the footer and the course cards, and would report a density about a document Rank Math never sees.

**It shows its arithmetic rather than asserting it.** Rank Math does not publish how it computes density; its guide was read this session and gives the bands without the formula. So the row carries the raw count and the word count beside the percentage, and names the formula used. Whoever settles move 7 does not have to trust this one's sums.

**It refuses to invent a verdict in the disputed zone.** It fails below 1.0 per cent and above 2.5, where both readings agree. It passes inside the house band. Between them it reports for review, naming the disagreement. The measurement is exact; what is unsettled is the standard, and that is Rule 5's territory rather than a verdict to make up.

## 3. The evidence on the recorded contradiction, which is what Chat will actually want

Item 11 says: "One contradiction is recorded and not resolved on paper: move 7's 1.5 to 1.8 per cent band, measured by Code at S083, and Rank Math's own guide, which gives full marks at 1 to 1.5 and warns past 2.5. Code re-measures on the next imported batch and the winning band replaces move 7 here."

The counter was run across all 51 published biographies against their measured scores. The whole set:

| Score | Density | Uses | Pages |
|---|---|---|---|
| 0 | 0.24 to 0.30 | 4 to 5 | 2, and their zero is a different fault |
| 69 to 77 | 0.18 to 0.36 | 3 to 6 | 13 |
| 80 | 0.18 to 0.49 | 3 to 8 | 33 |
| 82 | 0.65 | 11 | 1, Thich Nhat Hanh |
| 86 | 1.60 | 26 | 1, Plato |
| 86 | 1.70 | 28 | 1, Aristotle |

**The three pages that clear the bar are the only three above 0.6 per cent, and the two inside the house band both land on 86.** Item 11's own prediction is "move 7 clears 81 and lands at 85 or better", and the two pages that have move 7 land on 86. The house band is confirmed by real content rather than by argument.

**What this does NOT settle, said plainly rather than overclaimed.** Not one of the 51 sits inside Rank Math's disputed 1.0 to 1.5 band, so there is no evidence here about whether that band is enough. Thich Nhat Hanh clears the bar at 0.65, well under both bands, which suggests 81 is reachable below either. So the honest position is: the house band is confirmed to produce 86; the zone below it is untested; and move 7 should not be rewritten yet.

**The cheap way to finish it, which is one afternoon rather than a batch.** Take five of the thirty three pages sitting at 80, lift them to about 1.2 per cent and no further, and re-score. If they clear 81, Rank Math's band is enough and move 7 relaxes, which is less writing on every future page. If they do not, the house band stands on evidence rather than on one measurement from S083. **That is a content change to five records, so it is Chat's to run, not Code's.** Say the word and the counter will read them back.

## 4. What is owed, and by whom

**Code owes nothing further on the counter.** It is built, proved on four real pages including two that go red for two different reasons, deployed, and running on every page the gate touches.

**Chat is asked for two things.** The five-page density experiment above, if Kain wants move 7 settled. And the note in item 11 that the counter now exists, so nobody writes "about fourteen uses" into another brief as though it were checkable by eye.

OWED BACK: the counter's read-back on the five experiment pages, when and if Chat runs them.

*No em or en dashes in this file; checked before writing.*
