> **CHAT DISPOSITION, S382: ACTED ON, archived.** Written into `house-copy-standards` (handed to Kain for re-upload) and into `RULING__The_Actually_Cap_Exempts_The_Pages_Own_Keyword_S382` to Code (FROM Chat), for the gate fix. Q07010 confirmed correct as drafted; the two other named pages still need someone to check which of their "actually" instances are the keyword phrase before re-gating.

# RULING: "actually" inside a page's own focus keyword is exempt from the one-per-body cap

**From:** Kain, via Claude Cowork, S382, Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** the keyword-conflict question first raised in `DONE__Four_Jobs...` (does-cbt-actually-work, the life-coaching-course-actually-teach record) and repeated this session on Q07010 (what-a-life-coach-actually-does).

## The ruling, Kain's own words

"Actually inside the keyword itself doesn't count toward the cap, wherever it repeats for density. Actually used anywhere else in the body still counts, still capped at once."

## What this settles

The "actually" cap (Kain, S381) and keyword density can conflict when a page's own `rm_focus_keyword` contains the word "actually" and needs to repeat verbatim to clear the 1.0 to 1.5% density band. This ruling resolves it the way Cowork's own read guessed at S382 but declined to apply without a ruling: every verbatim occurrence of the focus keyword counts toward density and is exempt from the cap, however many times it repeats; any OTHER use of "actually" in the body, outside the keyword phrase, still counts and the cap still holds at one.

## What this fixes now

- **Q07010__what-a-life-coach-actually-does**: both of its two "actually" instances in the body are the literal keyword phrase "what a life coach actually does." Both exempt under this ruling. Manually verified against the ruling; the page is correct as drafted, no edit needed. `content_gate.py` still reads FAIL on this line because the exemption is not yet coded in; Code's fix is below.
- **does-cbt-actually-work** and the **life-coaching-course-actually-teach** record (named in the earlier DONE file, not yet located or re-checked this session): the same fix applies once someone confirms which of their "actually" instances are the keyword phrase itself versus loose body prose. Owed back once checked.

## For Code

`content_gate.py`'s `'actually' at most once` check (search for `n_actually <= 1`) needs to exclude occurrences that are part of a verbatim match of the record's own `rm_focus_keyword`, counting only "actually" instances outside those matches against the cap of 1. Until this lands, a page correct under this ruling will still print FAIL on that line, so a human or Cowork check against this ruling's text is the interim standard, same as `content_gate.py`'s own document says to do for anything the standards file has not yet been given.

## OWED BACK

Nothing from Chat; recorded for Code's gate fix and for whoever next opens the does-cbt-actually-work / life-coaching-course pages.

*No em or en dashes in this file; checked before writing.*
