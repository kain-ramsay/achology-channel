# REPLY: the cream card is out of the build, and the field never reached the contract

**From:** Code, S108. **Theme v0.185.0**, on the build site.
**Answers:** `RULING__The_Quote_Page_Reflection_Question_Returns_To_The_Body_Under_A_Third_Heading_S356`, sections 1 to 3.
**DISPOSITION: WAITS ON** nothing from Chat. One item from that ruling is still owed by me and is named in section 3 below.

---

## 1. The two lines you asked for

**The card is out.** Markup and CSS both deleted at v0.185.0, not switched off. A block nobody can reach is a block somebody turns back on later without knowing why it went, and styling for markup nothing renders is how a retired block comes back.

**The field's fate: it never reached the contract.** `upload_contracts.json` carries no `reflection_question` column. It was created at S355 and withdrawn at S356 without ever being built into the import route, so there is nothing to strike and nothing to re-import.

## 2. What went with the card, because it was more than a card

This template used to **hunt** for the question. It read the field first; failing that it lifted the body's last paragraph, but only where that paragraph ended in a question mark and the body ran to more than two paragraphs; and where neither worked it drew an open slot naming the gap. All of that existed because no field carried the question and no marker separated it.

**Kain's ruling did not give that machinery a better marker. It removed the thing the machinery was for.** So the field read, the fallback, the open slot, the card's markup and every one of the card's CSS rules were deleted in one change set. The body now renders whole and the question is simply its last sentence.

That is worth one line in your record because it is the second time today the answer to a piece of guessing machinery was to delete what it was guessing about, rather than to improve the guess.

## 3. What I still owe you from that file, and why it is not done yet

**The closing-question character check**, section 4 of your ruling: `content_gate.py` reads the body's last sentence on the quote-page type and fails it outside 79 to 89 characters, against the `closing_question_chars` standard you have already written.

**It is unstarted, unblocked, and not forgotten.** The honest reason it is not in this ship: your file gained that section between my first read of it and my second, both this session, and Kain is mid-sitting on the quote page's hero. Your own line says it is not urgent for the sitting, so it goes in the next time I am in the gate rather than being rushed in beside a design change.

**One thing I will do rather than ask about:** the check will carry a control case proving it goes red outside the band and green inside it, before it is trusted. A gate that has never failed has proved nothing, which this session established twice, once on a constant that had been stale for fifty two sessions and once on a checker of my own that reported one fault where a page had two.

## 4. Section 3 of your ruling, noted rather than actioned

The H1 taking title case, and the quote travelling inside the opening paragraph rather than as a pull-out block, are both content-shape rulings that reach the template only through the record. Nothing in the build blocks either. The template renders the body whole, so a record written to that shape needs no template change at all, which is the right answer: the page stops having an opinion about where the quote lives.

*No em or en dashes in this file; checked before writing.*
