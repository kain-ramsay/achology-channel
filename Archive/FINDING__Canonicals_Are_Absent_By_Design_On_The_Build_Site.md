# FINDING: canonicals are absent on the build site by design, and no gate can test them there

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Why it matters to you:** it changes what DSRD 6 can honestly verify, and it corrects
an assumption Kain and I both started the session holding.

## What happened

Kain opened S046 asking me to bring Rank Math up on every built page, "starting with
the missing canonicals and meta descriptions, which no page has". I audited it live.

**Half of that was wrong, and half was worse than he thought.**

- **Meta descriptions were not missing.** Every built page carried one at a healthy
  length, 122 to 148 characters across the fourteen I checked. One genuine fault
  turned up and is fixed: the About page's description still quoted 670,000 students
  against its signed spec's 695,578. That correction was executing
  `SPEC__About_Page_Locked_Structure_And_Copy.md` §4 item 1 word for word, not writing
  copy. The revised string, unchanged in every other respect and identical in length:
  "About Achology: a decade teaching applied psychology to 695,578 students in 216
  countries. What we teach, what we stand for, and who it's for." 147 characters,
  verified on the rendered page in the description, og:description and
  twitter:description alike.
- **Canonicals are missing on every page of the site**, every page type, including all
  250 help articles.

Kain then told me to set the plugin up. **I did not, and the reason is the finding.**

## The cause, read from source, not recalled

`wp option get blog_public` returns **0** on achologytest.com. The site is set to
discourage search engines, so every page carries `<meta name="robots"
content="nofollow, noindex"/>`.

Rank Math then withholds the canonical deliberately. From
`wp-content/plugins/seo-by-rank-math/includes/frontend/class-head.php`, read this turn:

```php
// If a page is noindex, let's remove the canonical URL.
if ( isset( $robots['index'] ) && 'noindex' === $robots['index'] ) {
    $this->remove_action( 'rank_math/head', 'canonical', 20 );
}
```

The absence is correct behaviour on a hidden site, with a documented reason. Nothing is
broken and nothing was misconfigured.

**Turning indexing on to "fix" it would have been actively harmful**: it would let
Google index the build site as near-duplicate content competing with the live
achology.com. That is exactly what the build-ground rule exists to prevent. I told Kain
so rather than doing what he asked, and showed him the plugin's own line as the reason.

## What this changes for DSRD 6

**Any gate row that checks a canonical cannot pass on the build site, ever, and its
failure means nothing.** The same applies to any other signal a plugin suppresses on a
noindex page. If DSRD 6 carries such a row it needs one of:

1. a stated carve-out saying the row is verified at cutover on the live domain, not on
   the build ground; or
2. removal from the build-time gate and relocation into the go-live checklist.

**My recommendation is 1**, written into DSRD 6 §12 beside the existing per-page
exemptions, because the check is real and should not be lost. It simply cannot be run
here.

**What remains fully checkable on the build ground**, and should stay in the gate:
titles, meta descriptions, Open Graph and Twitter tags, schema, headings, alt text and
internal links. All are emitted regardless of index state, and both real faults this
session were caught that way.

## For the go-live brief

Add: **confirm `blog_public` is set to 1 at cutover, then verify a canonical is present
on a sample of every page type before submitting the sitemap.** If the site goes live
still hidden, every page stays out of the index and the canonical stays absent, and the
symptom will look exactly like today's audit.

*No em or en dashes in this file; checked before writing.*
