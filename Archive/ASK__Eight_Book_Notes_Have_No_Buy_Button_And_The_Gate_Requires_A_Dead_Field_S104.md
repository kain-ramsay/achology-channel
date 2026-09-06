CHAT DISPOSITION, S347, 6 September 2026: closed by Kain. He ruled in the S347 sitting that Code owns this whole item and has already solved it. Nothing is owed by Chat: the eight product URLs are not going to Karen, and the required-field change in content_gate_standards.json is Code's, not a Chat commission. Board cards: Book Notes, the psychologist expansion; Amazon OneLink.

# ASK: eight book notes have no buy button, and the reason nothing caught it is that the gate requires a retired field

**DOCUMENT TYPE:** ask, from Claude Code, Session 104, factory session. **Date:** 6 September 2026.
**Found by:** Kain, in the S104 sitting, reading The Ultimate Life Coaching Handbook and asking why it had no Get this book button and how many others were the same.
**Board cards:** Book Notes, the psychologist expansion; Amazon OneLink.

---

## 1. The count, measured off the install

**67 published book notes. 59 carry a buy button. Eight do not.**

| Post | Slug |
|---|---|
| 33804 | homage-to-catalonia |
| 33810 | journey-to-the-heart |
| 33813 | mental-efficiency |
| 33819 | peace-power-and-plenty |
| 33828 | the-bridge-across-forever |
| 33840 | the-power-of-truth |
| 35419 | the-ultimate-life-coaching-handbook |
| 33845 | thrift |

**The 59 that do carry one meet DSRD 2 §5.1 exactly**, checked rather than assumed: all 59 are product URLs, none is a search URL, and all 59 carry `tag=kainramsay01-21`. So the standard holds everywhere it is met at all, and these eight are an exception rather than the leading edge of a wider fault.

## 2. Nothing is lost at import, and the link is not missing. It is under the wrong name.

`single-book_note.php` renders the button from `amazon_url`. On all eight that field is empty, on the record and on the install alike.

**But every one of the eight carries an Amazon link under `amazon_genius_link_url`**, which is the field `content_gate_standards.json` lists as REQUIRED for a book note. `amazon_url`, the one the template actually reads, is listed as OPTIONAL.

So the gate requires a field nothing renders, and treats the field that renders the button as optional. **A book note can lose its buy button and every check still passes.** That is how this reached 67 published pages with nothing going red, and it is the part worth fixing rather than the eight rows.

**The name is dead in the standard too.** DSRD 2 §5.1, quoted from the canonical file this turn: "*This supersedes the retired Geni.us (Genius Link) plan (ruled S231, board card retired and merged into the OneLink card). The old geni.us and `buy.geni.us/Proxy.ashx` links, the TSID 112892 account, and the outstanding job of creating 172 more of them are all void: no live geni.us link is used anywhere on the new site, and the paid Geni.us account is cancelled.*" The field carrying that plan's name outlived the plan.

## 3. Repointing the template would not fix it, and this is the part that needs a decision

**The eight values are Amazon SEARCH links, not product links, and none carries the affiliate tag.** Three, read in full:

```
the-ultimate-life-coaching-handbook
  https://www.amazon.co.uk/s?k=The+Ultimate+Life+Coaching+Handbook+Kain+Ramsay
thrift
  https://www.amazon.co.uk/s?k=Thrift+Samuel+Smiles&i=stripbooks
homage-to-catalonia
  https://www.amazon.com/s?k=Homage+to+Catalonia+George+Orwell&i=stripbooks
```

DSRD 2 §5.1's own sentence: "**Every book's purchase button links to the Amazon product URL held on the book's master row, carrying the UK associate tag as a query parameter: `?tag=kainramsay01-21`**".

A search URL is not a product URL, and an untagged link earns nothing. So pointing the template at the old field would put eight buttons live that fail the standard on both counts and pay Achology for none of the clicks. **Not done, and not recommended.**

**One of the eight is a `.com` address on a UK-tagged programme**, which OneLink handles for a visitor but which is not what the standard names.

## 4. What is asked, three things with one owner each

**One, Karen or Chat: the eight product URLs.** Real Amazon product addresses on each book's master row, tagged, so `amazon_url` can be filled the way the other 59 were at Code's S102 pass. **The Ultimate Life Coaching Handbook is the one that matters commercially**: it is Achology's own book, Kain ruled it Essential Reading in this same sitting, and it is now the only Essential Reading note on the site with no way to buy it.

**Two, Chat: the required-field list.** `content_gate_standards.json`'s book note block should require `amazon_url` and stop requiring `amazon_genius_link_url`, which names a retired plan. **What a gate checks is not Code's to change**, so this is a commission rather than something done here. Code's recommendation is to require the live field and drop the dead one in one edit, so no record can pass carrying only the retired name.

**Three, and this is Code's the moment two lands:** a run across all 103 book note records naming any that still carry only the old field, so the eight do not turn out to be nine.

## 5. What was NOT done, said plainly

Nothing was changed. No template repointed, no record edited, no meta written. The button's absence is correct behaviour on an empty field, and the fault sits upstream of the page.

---

OWED BACK: the eight tagged product URLs, and the ruling on the required-field list in section 4 item 2.

*No em or en dashes in this file; checked before writing.*
