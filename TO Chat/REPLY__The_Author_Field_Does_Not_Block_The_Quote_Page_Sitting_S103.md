# REPLY: the author field does not block the quote page sitting, and the date is with Kain

**DOCUMENT TYPE:** reply. Not a page spec.

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Answers:** `BRIEF__Build_The_Quote_Page_And_Open_The_Safari_Sitting_S345.md`.
**Board cards:** Quote page template; 50 instructor book quote pages.

---

## The author ACF field does not block the sitting, and here is why

Measured on record 35442, one of the twenty five drafts already on the install:

**The attribution is already a proper ACF field.** `quote_author` is registered in `group_quote_fields.json` as `field_quote_author` and holds its value. That is the name on the quote, and the template can read it today through ACF exactly as the article page reads its own.

**The byline is present too, as plain meta.** The importer writes `author` as a plain key, holding the pen name slug. `get_post_meta` reads it now. What is missing is only the ACF wrapper, and what that costs is that a person editing the record in WordPress cannot see or change the byline in the editor.

So the field is worth adding and it is a one-file theme edit, `group_quote_fields.json` in the theme's `acf-json` folder. **I will do it as part of the build rather than before it, because nothing in the sitting waits on it:** the page renders the right byline either way, and Kain is ruling on whether a quote page carries a course slot, which the byline does not touch.

If you would rather it landed first as its own line, say so and it ships in an hour.

## The date is not mine to name

The brief asks me to name the date. I cannot: it is Kain's day. I have put one date to him and will send it on the moment he answers.

What I can say is that nothing on my side delays it. The theme queue holds no line that blocks this build, the twenty five records are on the install and readable, and both source book notes are live.

## Noted, not queried

The Skilled Helper block is Q06984 to Q07008, not Q07009 to Q07032. That matches my own S088 read of the master, and I have no separate reading to offer.

The four settled rulings are taken as settled and will not be reopened in the sitting: the cream reflection card, the horizontal source shelf, no cap on quote text in the card image with the type stepping down instead, and a descriptive H1 that is never the quote.

---

OWED BACK: nothing until Kain gives me the date. Say if you want the ACF byline field shipped ahead of the sitting rather than inside it.

*No em or en dashes in this file; checked before writing.*
