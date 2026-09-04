# ASK: four things are blocked, each on a decision that is not mine. Filed rather than worked around.

**From:** Claude Code, Session 099. **Date:** 4 September 2026. **Session type:** factory.
**Under:** Harness Rule 5 and The Shared Rules section 3. Kain ruled in this sitting that these are filed, not solved.
**Board cards:** the harness card; Instructor Articles; Help articles, title-derived focus keywords on all 250; the Kit card.

Each of the four names the one fact that would unblock it, so it can be tested rather than judged.

---

## 1. H9's reviewed register cannot see a script outside the theme, so a commissioned import stays blocked

**The fault, read this turn.** `h9_publishing_wall.py`, in `reviewed_scripts()`, resolves each register entry against two folders and no others:

    for folder in (THEME, os.path.join(THEME, "tools")):

**`import_instructor_articles.py` lives in the Content Production Factory folder.** The lookup never finds it, the hash is never compared, the entry is skipped, and H9 blocks the import as publish-capable.

**The reading is already done and on the record.** S098 read all seven of its install-reaching payloads line by line and wrote the entry, hash and reason into `h9_reviewed_scripts.json`, with an `INERT_TODAY` field saying plainly that the entry grants nothing today so nobody mistakes it for cover. **The main payload is quoted in the register rather than summarised:** the post status is a hardcoded literal `draft`, so no input can make it publish.

**Why it is not mine.** Widening that lookup is a change to the wall itself, and Kain's governing rule for H9 is that "I could not tell" is a fail. A wall that starts resolving names outside the theme is a materially wider wall, and that is not a judgement Code takes alone.

**There is a second question underneath it, and it is the more important one.** The register's own `_how_to_add_one` says: satisfy yourself the script "cannot create or publish a post". **This script creates.** It creates drafts, which is not the thing the wall exists to stop, but the register's own sentence does not cover the case. That sentence is yours to widen or to refuse. It was not quietly rewritten from here.

**Unblocked by:** a ruling on both halves. **Testable fact:** `reviewed_scripts()` resolving a name in the Content Production Factory folder.

**What it holds up:** the three held instructor articles cannot import, so `BRIEF__Import_The_Three_Held_Articles_And_Re_Import_The_Two_Biographies_S334.md` cannot start at all.

## 2. Article I18 needs one external link and I cannot mint its address

Full detail is in `REPLY__Three_Of_Your_Measurements_Do_Not_Hold_S099.md`, section 3. In short:

I18 is the only instructor article record that fails its gate, and it fails on one line, `external link to the source present`. It **does** name Stephen Covey's fifth habit in its body, so there is no drafting to do: a link goes round words that already exist.

**What blocks it is the destination.** `RULING__Install_OneLink_And_Tag_Every_Book_Link_S309` says every book link is tagged through OneLink, and that ruling's own disposition, re-checked at S095, says the OneLink snippet has never arrived anywhere. I18's sibling I14 already carries a `geni.us` address, so the tagged form is in use; only the means to make a new one is missing.

**Unblocked by:** the OneLink snippet arriving as a file, or your word that this one link may use the publisher's own page like the nine Egan links do. **Testable fact:** a file carrying the OneLink snippet existing in the channel.

## 3. The Kit form. Nothing has changed, and this section is a correction of my own first draft

**This section originally said the Kit account needed a paid plan and put that to Kain as a money question. That was wrong, he caught it in the sitting, and it is corrected here rather than edited away.**

**What is actually true, read off the install this session.** The Kit plugin is active. `_wp_convertkit_settings` carries a live access token. The account is connected and paid; Kain connected it at S091 and confirmed it again today. `convertkit_forms` is `[]`.

**So the block is exactly what the S091 disposition always said it was: no form exists in the Kit account yet.** Not the plan, not the connection, not the plugin.

**How I got it wrong, because the shape of it matters more than the fact.** I called the Kit MCP connector, which is a different route with no bearing on this ruling, got an "upgrade your plan" refusal, and reported a tool's error message to Kain as a fact about his money. The correct line was already sitting directly beneath the one I wrote. Two commands against the install would have settled it, and I ran them only after he pushed back. That is my own recorded failure mode, a partial signal treated as a finding, and it is the second time in three sessions.

**What is genuinely owed, and it is yours or Kain's, not mine.** One form has to exist in Kit before the shortcode has anything to render. Which form, and what it says, is a marketing decision. **Kain has asked not to be brought decisions in this stretch, so it comes to you first:** if you can specify the form, he approves it in one look and makes it in Kit's own web interface, and check two is then one render away.

**Unblocked by:** one form existing. **Testable fact:** `convertkit_forms` on the install returning a non-empty list.

## 4. The 250 help answers wait on where the UKRLP line sits, and that is Kain's eye

This one is already correctly stated by your own file, and I am filing it only so it sits with the other three rather than being the one nobody counts.

`REPLY_AND_RULING__Yes_To_The_External_Link_Add_The_UKRLP_Line_Everywhere_S338.md`, section "One thing left open, on purpose", says: "Where the line sits on the page, and how it looks, is a small visual decision and has not been made. Do not guess it."

Everything else about that pass is settled and I have nothing to add to it. **Kain asked in this sitting not to be given design decisions**, so I have not put it to him and I will not until he asks. It waits.

**Unblocked by:** Kain seeing the line on a rendered page and saying where it goes. **Testable fact:** none. This is a genuine human wait and it is written as one rather than dressed up as a machine test.

---

## What these four have in common, which is the part worth your attention

**None of them is hard.** Three are a single word from somebody, and the fourth is a lookup path. Between them they hold up a commissioned import, a finished article, an email capture and a 250 page pass.

They also share a shape with the scope wall fault this session fixed: work that stopped and was correctly reported, then sat. The reporting worked. What did not work is that a filed block has no owner and no trigger, so it waits until somebody happens to read it again.

---

OWED BACK: a ruling on item 1, both halves; a word on item 2; Kain's yes or no on item 3, at his convenience. Item 4 needs nothing from you.

*No em or en dashes in this file; checked before writing.*
