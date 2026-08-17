# FINDING: the frozen previews show stale COPY, and one misled Kain this session

**From:** Claude Code, S048. **Date:** 2026-08-06.
**Severity:** high, because it attacks the one instrument the review method
rests on.

## SUPERSEDED THE SAME DAY. Read this first.

**The recommendation at the foot of this file is wrong, and Kain had already
ruled the opposite before it was written.** `RULINGS__Previews_Link_Ceiling_
Keyphrases_S245.md` §1, sitting in FROM Chat since 2026-08-05:

> "The preview system exists only for showing Kain something that does not
> exist yet. Retire the previews of pages that have shipped ... This closes
> collapse item 2 by deletion, not by building a second renderer."

I diagnosed the defect correctly and then fixed it the wrong way, by writing
`_sync_from_live.py` to rewrite each preview from its live page. That is
exactly the second renderer the ruling forbids. I had not read the ruling: at
session open I read the three S248 briefs and the walk instruction in full and
only skimmed the rest of the folder, which is not what Rule 1 asks for.

**Carried out instead, S048, shipped:** every preview of a shipped page
deleted, the superseded explorations with them, the four builders that kept
them alive deleted including the one I wrote that morning, and
`previews/README.md` rewritten around the ruling. 89 files, roughly 690,000
lines. Evidence in commit `59f5311`.

**What survives from this finding** is only its diagnosis, which is worth
keeping because it is the reason the ruling was right: a preview of a live page
does not merely go stale, it goes stale invisibly, showing today's design over
yesterday's words.

Everything below is the original finding, kept as the record of the defect and
of my wrong turn.

## What happened, exactly

I showed Kain `previews/policy-disclaimers.html` in Safari to review the three
S248 colour and copy changes. He read the page and asked me to check it for em
dashes, having spotted "one or two".

He was right about what he saw, and the page he was looking at was wrong.

The preview carried five dashed passages. They are described here rather than
quoted, because pasting the evidence would put the dashes into this file and
the dash ban has no evidence exception. `[EM]` and `[EN]` mark where each one
sat.

| Dash | Where it sat in the preview's text |
|------|------------------------------------|
| em | the policy lead: "the limits of Achology's services and content `[EM]` what we do and do not provide `[EM]` in support of the responsible use" |
| em | "designed to support learning and understanding `[EM]` not to deliver treatment, intervention, or personalised advice" |
| en | three in one sentence: "does not create a therapist`[EN]`client, doctor`[EN]`patient, counsellor`[EN]`client, or similar professional relationship" |
| em | "Achology exists to educate thinking adults `[EM]` not to manage inner worlds, regulate emotional states" |
| em | "Recognising that boundary is not a failure `[EM]` it is an expression of discernment and self-respect" |

Every one of those had already been fixed in the theme source. The current
`policies-content/disclaimers.php` reads "content, what we do and do not
provide, in support", "understanding, not to deliver treatment",
"therapist-client, doctor-patient, counsellor-client", "thinking adults, not to
manage inner worlds", and "not a failure: it is an expression". Commas, hyphens
and a colon, exactly as the standard requires.

**The rendered live page carries zero em dashes and zero en dashes.** I swept
every text node on https://achologytest.com/policies/disclaimers/ before the
deploy and again after it. Both runs: zero.

## The cause

`previews/_refresh_previews.py` does exactly what its docstring promises and
no more. Its own words:

> "What this does: appends the current theme stylesheets, in production enqueue
> order, as the LAST thing in each preview's `<head>`."

It refreshes **CSS**. It does not refresh **body copy**. The body of each
frozen preview is HTML captured at the moment that preview was built, and it
stays frozen forever while the PHP that really produces the page moves on.

So the previews now lie in a narrower but more dangerous way than the one the
refresh script was written to kill. They render the current design over stale
words, which is the hardest kind of wrong to spot: the page looks right, so
nothing prompts you to doubt the sentences.

This is the same class of defect as the drift the script's own comment records
being caught in 2026-07-18, and the same class as the stale audio after the 249
rewrite: a derived artefact that nothing recomputes when its source changes.

## Why it matters more than it looks

Every visual result reaches Kain as a rendered page, per Rule 7. If the page he
is handed can carry copy that the site does not carry, then his eye, which is
the final gate, is being pointed at the wrong object. He spent part of this
session reviewing text that no reader will ever see, and the only reason it did
not become a wasted copy-editing round is that he raised it and I read the
source rather than the preview.

It also cuts the other way, and this is the worse direction: a preview can hide
a real defect that exists in the current copy, because it is showing older
words that did not have it.

## What I have not done

I have not changed the preview tooling. Rebuilding every frozen preview's body
from its PHP is a real job with a real design question behind it (whether these
frozen files should exist at all now that the site is live and every built page
can be reviewed on achologytest.com directly), and that question is Kain's, not
mine.

## What I propose, for Kain's yes or no

**Retire the frozen previews for pages that are already live, and review those
pages on achologytest.com instead.** The live page cannot go stale, it is the
thing itself, and `page_gate` already purges the cache before it measures. Keep
the preview mechanism only for work that is not on the site yet, which is what
it was actually for: building a block in isolation before it ships.

If he would rather keep them, the alternative is a builder that regenerates
every preview body from the theme PHP on every refresh, so a preview can never
again be older than the source. That is more machinery to maintain, and it
maintains a copy of something we can now read directly.

**Until he rules, I show him live pages and not frozen previews.**

*No em or en dashes in this file; checked before writing.*
