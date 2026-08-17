# RECORD: both S247 build items, one built and one already done

**From:** Claude Code, S048. **Date:** 2026-08-06. **Theme:** v0.38.55, live.
**Answers:** `BRIEF__Disclaimer_Copy_And_404_Live_Query_S247.md`, both build items.

## Build item 1: the Brand Disclaimer section. Built, live, verbatim.

**Page:** https://achologytest.com/policies/disclaimers/

### The copy is the signed copy, proved rather than read back

Rule 8 says Code never drafts content, so the only honest check is a character
comparison against the brief, not me reading it and saying it looks right. A
script diffs the built section against the brief paragraph by paragraph:

```
signed paragraphs: 5   built paragraphs: 5
  para 1  IDENTICAL  (61 words)
  para 2  IDENTICAL  (100 words)
  para 3  IDENTICAL  (59 words)
  para 4  IDENTICAL  (59 words)
  para 5  IDENTICAL  (68 words)
links in the section: 2
   href="/policies/refund-policy/"                        text: refund policy
   href="https://www.tradingstandards.uk" target=_blank rel=noopener
                                                          text: tradingstandards.uk
VERDICT: VERBATIM
```

Both ruled links, no others, and the outward one opens in a new tab with
`rel="noopener"` per DSRD 3 §2.5. Confirmed again on the rendered live page
after deploying: the section is present, five paragraphs, both links carrying
exactly those attributes.

**One discrepancy, reported rather than rounded away.** The five paragraphs
total **347** words; the brief states 352. Every paragraph is
character-identical to the brief's own text, so the difference is in how the
brief counted its own copy, not in what was placed. Nothing to fix on the page,
but worth correcting in the brief's record if 352 is quoted anywhere else.

### Placement, and the one judgement I made

The brief left placement to the page's structure and said to stop and ask only
if the page gave no obvious slot. It gives one. This page already runs
unnumbered framing sections at both ends, "The Purpose of These Disclaimers"
opening and "Final Position" closing, with the twelve numbered disclaimers
between them. The Brand Disclaimer is framing rather than a disclaimer, so it
takes an unnumbered `h2` matching those two, and nothing renumbers.

It sits at the **opening** end, second heading of fifteen, directly after "The
Purpose of These Disclaimers". Two reasons: it establishes who Achology is and
who owns it, which the twelve numbered sections then qualify; and its closing
invitation to check us against the Chartered Trading Standards Institute reads
as a frame the reader carries into the page rather than an afterthought.

**Choosing the opening slot over the closing one is the only judgement in this
build.** It is one move to reverse if Kain wants it at the foot instead.

### Gate

`page_gate` v5 on the live page, cache purged: **28 pass, 0 fail**, canonical
carved out as designed, 0 em and 0 en dashes, 40 links all resolving, nothing
failed to load.

**Rank Math is not rechecked here, and cannot be.** The brief asks for it, and
the score is only readable inside wp-admin. The outward authority link the
brief was written to add is in place, which was the mechanism behind the
80-point target. Someone with the admin open should confirm the number.

### DSRD 6 record delta for the Disclaimers page

Only §1 and §5 move, and both move the right way: §1 gains a section whose copy
is signed and verbatim, with the front-door rule satisfied (the section names
Achology Transactions Ltd and says what it is in the sentence it first appears
in); §5 item 4 gains one internal cross-link and the page gains its first
outward authority link. No other chapter's verdict changes. The page's existing
record stands otherwise.

## Build item 2: the 404 Popular Questions. Already done, verified on the page.

**No change was needed and none was made.** The work the brief commissions is
already in the theme and has been for some time. Rather than report that from
the code, here it is from the rendered pages.

`404.php` runs the live query, the same one `archive-faq_article.php` runs for
the /help/ landing, with `posts_per_page` at 4 rather than 6:

```php
$ach_popular = new WP_Query( array(
    'post_type'      => 'faq_article',
    'posts_per_page' => 4,
    'meta_key'       => 'achology_popular',
    'orderby'        => 'meta_value_num',
    'order'          => 'ASC',
) );
```

There is no hardcoded questions array. The `$ach_doors` array still in the file
is a different block, the six "Where to instead?" doors, which the brief does
not touch.

**Proved on the live pages.** The 404 page's four questions and the /help/
landing's top four are the same four, in the same order:

| # | On the 404 | On /help/ |
|---|---|---|
| 1 | What is Achology? | What is Achology? |
| 2 | How do Achology courses work? What's the learning experience like? | same |
| 3 | What does Achology membership include? | same |
| 4 | How much does Achology cost? | same |

Layout unchanged: same header row, same badge, same four-question shape, and
the empty-state line is present in the template for when no article carries a
rank. DSRD 9 §28.5 is untouched, as §28.8 requires.

**So item 2 closes as already satisfied**, on the same principle the collapse
brief states for a family that turns out already collapsed: file the
verification evidence and it closes the same way.

## One thing found in passing, not acted on

The /help/ landing page's browser title reads "FAQ Articles | Achology TEST
Site", which is the post-type archive default rather than a written title. The
"TEST Site" half is correct on the build ground and will change at cutover, but
"FAQ Articles" is not a title anyone wrote. It is out of scope for this brief
and belongs to /help/'s own turn in the walk; recorded here so it is not lost
between now and then.

*No em or en dashes in this file; checked before writing.*
