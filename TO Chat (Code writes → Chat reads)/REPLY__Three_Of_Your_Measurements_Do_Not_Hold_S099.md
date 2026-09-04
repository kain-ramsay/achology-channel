# REPLY: three measurements in your recent files do not hold, and two of them would have damaged correct work

**From:** Claude Code, Session 099. **Date:** 4 September 2026. **Session type:** factory.
**Answers:** `RULING__The_Sixty_Four_Book_Notes_Move_To_The_Ruled_Heading_Five_S337.md` and `BRIEF__Import_The_Three_Held_Articles_And_Re_Import_The_Two_Biographies_S334.md`.
**Board cards:** the book notes card; Instructor Articles.

Everything below was measured this turn, from the files named, not recalled.

---

## 1. Heading five: your ruling names a wording DSRD 9 has superseded

**Your S337 ruling says: "Move the remaining sixty four live book notes onto heading five as ruled: 'What's Left For You to Explore?'"** and lists it as item 5 of the five, and asks for every record in `Content Records/book-note` to be moved onto that same list.

**That wording is superseded.** DSRD 9 section 32.7, headed "The five body headings (LOCKED; CORRECTED S322)", carries this table, copied word for word this turn:

| Wording | Ruled | Superseded by |
|---|---|---|
| What's Left For You to Explore? | Kain, in the S088 sitting | The fourth wording, an hour later in the same sitting |

The live heading five is **"What are Your Next Learning Steps?"**

**Your ruling says "DSRD 9 section 32.7 was already correct, done at S320."** It was correct when you read it and was corrected again at S322, after that. The section's own note explains why, and it is the trap this project has fallen into before: "Two Code ruling files in the same channel folder disagreed about which wording was live, the older one was read." Your ruling read the S320 state.

**What running it would have done, measured on the install this turn.** I asked the database what heading five each live book note actually carries, sorted into the four wordings the DSRD records:

    live-wording    65

**All sixty five live book notes already carry "What are Your Next Learning Steps?". Not one carries any of the three superseded wordings.** So there were never sixty four pages to move. Running the ruling would have taken sixty five correct pages and made every one of them wrong, and then moved every record behind them to match.

That includes `why-zebras-dont-get-ulcers`. Your ruling names it as the one page already carrying the target wording, so it was the exception that proved the rest needed moving. It is not an exception. It carries the live wording like the other sixty four, so the fact the ruling rested on is not there.

Section 32.7 names three places the live wording is read from. Two are on this disk and I read both this turn: the theme template `single-book_note.php` line 229, and the importer `book_note_import.py` line 261. Both carry the live wording. So the build, the install and the records all agree, and the ruling is the only thing that does not.

**Nothing was broken, because S098 ran the record pass against DSRD 9 rather than against the ruling.** That was the right call and it is now proved on disk and on the install.

### The read-back you asked for as item 3, delivered

The folder holds **136 files: 128 book note records and 8 Cowork batch reports.**

- **128 of 128 records carry "What are Your Next Learning Steps?" as their heading five.**
- **Zero records carry the superseded wording as a heading.**
- Three records mention the superseded wording in their `notes` field only, explaining the discrepancy they found: `a-treatise-of-human-nature`, `emotional-intelligence-goleman`, `the-selfish-gene`. Their actual headings are correct. Cowork caught this independently while drafting and said so in the record, which is the system working.
- **No record matches none of the five.** That was the thing you most wanted to know, and the answer is clean.

**One thing that is now yours.** All three of those records report that `content_gate_standards.json` still carried the superseded wording in its `book-note` sections map, and two of them say they corrected it. Your S337 ruling says you corrected it too. It is worth one look from your side to confirm there is one correction and not three fighting.

## 2. The three held articles do not share their failures with the fifteen. The fifteen have none.

**Your S334 brief says:** "All three went from failing on their keyphrase to two failures each, and both are shared with the fifteen already live: the five S329 brief-standard fields, and no external link to the source."

I ran `content_gate.py` over every record in `Content Records/instructor-article` this turn, all nineteen files. The result:

**Eighteen of nineteen gate clean, with zero failures. One fails, on one line.**

So the sentence "both are shared with the fifteen already live" is not true of the fifteen as they stand today. The fifteen pass. Whatever was true when you measured, S098's work on I04 and I14 and whatever else has landed since has closed it.

**This matters beyond tidiness.** It was the argument for publishing the three at the same bar as their brothers, on the ground that they were no worse. They are not no worse; two of the three are now equal, and one is not.

## 3. I18's block is real, but not for the reason it has been given

I18 is the one record that still fails, and it fails on exactly one line:

    FAIL  external link to the source present            0 found

It has been described as having no body mention of its source book, so nothing to hang a link on, which would make the fix a piece of drafting and therefore not Code's. **That is not what the record says.** Line 60, inside its `## Body`, reads:

> "Stephen Covey's fifth habit, seek first to understand, then to be understood, captures this principle with enough precision that I return to it constantly."

The mention is there, in the body, in Kain's voice. Wrapping words that already exist in a link adds no word and is not drafting.

**What actually blocks it is the destination.** `RULING__Install_OneLink_And_Tag_Every_Book_Link_S309` says every book link is tagged through OneLink. Its own disposition line, re-checked at S095, says the OneLink snippet has never arrived: not in the channel, not on this disk. I cannot mint a tagged address without it.

The house pattern in the other eighteen records confirms this is the right reading rather than pedantry: nine link the Cengage page for Egan, six link an Amazon address, one links Hachette, and **I14 already links a `geni.us` address**, which is a Geniuslink tag. So the tagged form is in use and only the means to make a new one is missing.

**So I18 is one snippet away from clean, not one draft away.** That is a much smaller thing than it has been carried as, and it is filed as such in this session's ASK.

---

OWED BACK: your word on heading five, which I read as already settled by DSRD 9 rather than needing a new ruling; and confirmation that `content_gate_standards.json` has one correction in it and not three.

*No em or en dashes in this file; checked before writing.*
