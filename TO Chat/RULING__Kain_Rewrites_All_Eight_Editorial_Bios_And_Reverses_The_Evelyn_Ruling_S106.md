# RULING: Kain rewrote all eight Editorial Team bios himself, and one of them reverses your S350 ruling

**DOCUMENT TYPE:** ruling, from Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Given by:** Kain, live in the S106 sitting, as eight finished paragraphs handed over for pasting.
**Filed under Harness Rule 14**, and it reverses `RULING__The_Evelyn_Montgomery_Item_Is_Withdrawn_Permanently_S350`.
**Board card:** the Our People page.
**Shipped, deployed and read back off the live pages before this file was written.**

---

## 1. What he did

He rewrote and simplified the second bio paragraph for **all eight Editorial Team members** and handed them over as finished copy: Amelia Sinclair, Benjamin Lockwood, Charlotte Avery, Declan Fitzpatrick, Evelyn Montgomery, Frederick Martin, Isabella Whitmore and Jackson Hartley.

**One field, `bio`, reaches both surfaces**, which is worth recording because it made the job small: the same string draws the card on the Our People hub and the second paragraph on each profile page. Confirmed by hand on Evelyn's before anything was written, on the live hub and her live page.

**All eight are live**, deployed and read back individually off the rendered hub and the eight rendered profile pages rather than off the file that was written.

## 2. The reversal, and it is the reason this file exists

**Evelyn Montgomery's is among the eight.**

Your S350 ruling said her bio is withdrawn permanently, that nothing on that page changes, and that "if any future file appears to reopen it, that file is wrong and this one governs."

**Kain overturned it himself, in this sitting, by handing me a rewritten paragraph for her.** His word is the project's highest authority and it postdates the ruling by hours.

**He was told before it was written, not after.** The commitment I made when the eight arrived was to say it back rather than quietly contradict a standing instruction, and I did: he was shown that her paragraph was in the set, that your ruling made her untouchable, and that changing it was his to do. He confirmed and told me to publish all eight.

**So S350's Evelyn ruling is spent rather than broken**, and the record should say so rather than leaving a permanent ruling sitting against a live page that contradicts it. That is yours to write home.

**Nothing about this reopens the S348 item.** That item asked for a repeat to be cut from a paragraph and its premise did not survive the read. What happened here is different and simpler: he rewrote all eight himself.

## 3. Three corrections in his copy, each authorised by him rather than made quietly

His text carried three things that could not go in as written. He was shown all three in one message and ruled: "please fix all three."

- **An em dash in Frederick's**, between "for its exact purpose" and "a skill that is often more difficult". His own site-wide rule bans it and the automatic gate refuses the edit outright. It is a comma. Described rather than quoted here, because quoting it failed this channel's own dash gate on the first attempt, which is the rule working on the file that reports it.
- **"an trustworthy analyst" in Isabella's.** Now "a trustworthy analyst".
- **"recognize" in Evelyn's**, against the site's UK English and against her own paragraph's "recognising". Now "recognise".

**One typographic call taken rather than asked**, and named because it touched his text. Benjamin's apostrophe in "doesn't" arrived curly. Every apostrophe in `people-setup.php` is straight and WordPress curls them on render, so it is written straight: consistent with the file and identical on the page. No word changed.

## 4. The proof

Theme commit `7cb712c`, deployed, cache purged, local and server and zip measured as agreeing at v0.167.65.

`php -l` clean on the server. The diff carries **8 insertions and 8 deletions, every one a `bio` line**, and **no em or en dash in any added line**. The five dashes remaining in that file are all in code comments no reader sees and all predate today.

**Read back on both surfaces:** all eight paragraphs found on the live Our People hub, and all eight found on their own live profile pages.

---

OWED BACK: the Evelyn reversal written into whatever document holds the S350 ruling, so the record stops contradicting the page. Nothing else.

*No em or en dashes in this file; checked before writing.*
