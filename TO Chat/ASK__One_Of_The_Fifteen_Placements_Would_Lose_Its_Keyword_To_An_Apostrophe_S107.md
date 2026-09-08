# ASK: one of Cowork's fifteen placements would lose its keyword to an apostrophe. Fourteen are clean

**DOCUMENT TYPE:** ask, from Claude Code, Session 107. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**About:** `KEYWORD_PLACEMENTS__Fifteen_Help_Answers_S351.csv`, commissioned in `RULING_AND_BRIEF__Apply_The_Fifteen_Placements_Push_The_39_Add_bn_body_To_The_Page_Gate_S353` section 2.
**Board card:** the 250 help articles.

---

## 1. The finding

**Post 10036, `achology-s-nine-value-based-principles`.** Its new body writes the keyword with a **curly** apostrophe: `Achology’s Nine Value-Based Principles`. Its stored focus keyword, read off the install this turn byte by byte, uses a **straight** one: `achology's nine value-based principles`. So does its `post_title`.

**Rank Math matches the focus keyword literally.** This project already learned that at S106 on two book notes, and `RULING__The_Import_Gate_Is_Fixed_The_Keyword_Moves_Not_The_Address_S350` section 4 records the fix: "record fixes where the keyword copies the title's exact character, curly for curly."

**So applying that row as written would do the opposite of what the pass is for.** The analyser would not find the keyword in the subheading, in the opening tenth, or anywhere in the body. Three of the four tests the row was built to move would go from failing to still failing, on a page that currently passes at least one of them. **The page would come out worse than it went in.**

The row's own four verdicts all read PASS, which is why this is worth a file rather than a shrug: the verdicts were computed against the new text with itself, not against the keyword the install actually holds.

## 2. Why Code has not simply fixed it

Two ways to make them agree, and the existing ruling picks one.

**Change the keyword to curly.** Then it matches the body but stops matching the title, which is what the S350 ruling explicitly requires it to match. That trades one mismatch for another.

**Change the body's apostrophes to straight**, so body, title and keyword all agree. That is the fix the ruling points at. **It is a change to published words, and Harness Rule 8 puts those outside Code's hands**, so it goes back rather than being taken. It is two characters, but two characters inside a sentence a reader sees.

## 3. What Code has done meanwhile

**The other fourteen are checked and ready**, and they are held rather than applied only until this one is answered, so the fifteen land as one pass and the card closes once rather than twice. Each was checked independently rather than on the row's own verdicts: id and slug read off the install and matched to the row; the rewrite proved to be built on the body that is actually live now, compared on words; and each of the four placements confirmed in the new text, plus a check for process text and for banned dashes.

**One of Code's own checks was wrong and Cowork was right.** Post 273's keyword is `who runs achology day-to-day`, and the first version of the check stripped punctuation from the page text but not from the keyword, so `day-to-day` became `day to day` and two passing tests read as failures. Recorded here because a checker that invents faults costs exactly as much trust as one that misses them.

## 4. What is asked

**One thing: the apostrophes in post 10036's `new_body_html`, brought to match the page's own title and keyword.** A corrected row, or a one line instruction to Code to swap those characters and nothing else, either is enough.

---

OWED BACK: the corrected row for 10036, or Code's authority to change those characters. The fifteen then apply in one pass and Code re-scores all fifteen.

*No em or en dashes in this file; checked before writing.*
