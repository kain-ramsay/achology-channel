# Both questions answered — preview provenance, and the hairline numbers

From: Claude Code · 2026-07-23 · theme v0.36.15
Answers: `Questions__Preview_Provenance_And_Hairline_Measurements.md`

---

## Question 1 — which previews reflect what shipped

Short answer: **none of them are generated from a shipped PHP template.** The
distinction that matters is not template-versus-prototype, it is how stale the
CSS baked into each file is. Measuring any of them records values a visitor does
not see.

**How the builder works.** `previews/_build_previews.py` takes an older preview,
`policy-trust-statement.html`, as its donor, cuts the `<main>` out of it, and
rebuilds a new `<main>` from a Python string template that reproduces the page
frame by hand. It then injects the current `base.css`, `policies.css`,
`components.css` and `help.css` into the file verbatim. So a freshly built
preview is: **current theme CSS, applied to hand-reproduced markup, inside
prototype-era chrome.** The one part genuinely shared with production is the
policy body copy, which it reads from `policies-content/{slug}.php`, the same
partials `template-policy.php` includes.

**Which files the builder actually writes**, and therefore which carry current
CSS (all last built 22 July):

- `404.html`
- `about-manifesto.html`
- `about-code-of-ethics.html`
- `about.html`
- `about-fiveacts-*.html`
- plus each one's `-lightweight` sibling

**Everything else in `previews/` is a static artefact that has never been
regenerated.** It carries whatever CSS was current on the day it was written:

| Files | Last written | Note |
|---|---|---|
| The seven `policy-*.html` previews | 2 July | Includes `policy-trust-statement.html`, the donor |
| `policies-index.html`, `_LOOK-HERE-policies-index.html` | 1 July | |
| `people-*.html` (4 files) | 3 July | |
| `kh-article.html` | 12 July | |
| `card-library-brochure.html` | 13 July | |
| `help-landing.html`, `help-article.html`, `help-category-prepurchase.html` | 16 July | |
| `help-category-support.html` | 18 July | |

**Concrete proof they are stale**, not just old: the builder carries a line that
strips a drifted token override, `.policy-page { --color-soft-grey: #354149; }`,
which no current theme CSS contains and which darkened every soft-grey use.
That override is still present in all seven 2 July policy previews. It is absent
from every file the builder writes.

**So, for the families you are about to measure:**

- **The 404** — the preview is current, but read the CSS anyway; the markup is
  hand-reproduced.
- **Help pages, Knowledge Hub article, people pages** — do not measure the
  previews. Five to twenty days stale, hand-built, never regenerated.
- **Knowledge Hub category and listing pages** — no preview exists at all.

**What I would measure instead.** The staging site renders the real templates
with the real CSS, and I can read computed values off it in a browser at any
width, which is what I did for question 2 below. If you name the page families
and the properties, that is a faster and more truthful loop than the previews,
and it needs no preview rebuild. Whether the previews are worth repairing is a
separate call for Kain, and I have not touched them.

---

## Question 2 — the hairline numbers on `/about/code-of-ethics/`

Measured in a browser on the live staging page, box edge to line and line to box
edge, at 1440px and at 375px. Both widths gave identical numbers, so one table
covers both.

| Hairline | Space above | Space below | Supplied by |
|---|---|---|---|
| `h2` "The Principles That Shape the Standards" | 32px | 32px | the `h2` itself: `margin-top` above, `padding-top` below |
| `h2` "Two Codes, Two Layers of Integrity" | 32px | 32px | same |
| `h2` "Code of Ethics Bi-Annual Training" | 32px | 32px | same |
| The Aristotle host block | 32px | 32px | same |
| Related Questions (`.help-popular`) | 48px | 48px | the block itself |

**This reads clean against DSRD 7 §4.3 as you rewrote it at S216.** The page
separates every section with a hairline, so it is the dense tier: 32px both
sides, at every width, no breakpoint change. It measures exactly that. The
Related Questions block arrives with its own 48px standard and keeps it on a
dense page, which §4.3 states explicitly, and it measures exactly that too.
Nothing else contributed space at any of the five lines. **The rule stands as
written; no second tier is needed.**

---

## Two defects I found while I had the ruler out

Both are on the **default-tier** policy pages, not the dense ones, and both are
value defects rather than a contributed-space defect: the element carrying the
line supplies the wrong amount itself. Measured on `/policies/privacy-policy/`
and `/policies/cookie-policy/`, identical on both, at 1440px and 375px.

| Hairline | Measured | §4.3 requires | Gap |
|---|---|---|---|
| `.policy-header` bottom rule | 24px above, 48px below | 48 / 48 desktop, 32 / 32 below 768px | 24px short above at desktop; and neither side drops to 32 on phone |
| `.policy-endnote` top rule | 48px above, 24px below | as above | 24px short below at desktop; same missing phone tier |

Both are asymmetric by the same 24px, in mirror image, which suggests one
decision made once and applied to both ends of the page. Fixing them **would move
the page** — it adds 24px in two places at desktop and removes 16px at phone —
so I have not touched it. It is a design change for Kain, not a defect I should
absorb into a corrections pass.

The 404's header hairline has the same phone-tier gap: it holds 43px above and
48px below at 375px where §4.3's default tier wants 32/32. The 43px itself is
your recorded optical correction (DSRD 8 §12.5) and I have left it alone; it is
only the missing phone tier that is unaccounted for.

---

## Both of the things I was carrying are dropped

DSRD 10 §4 and the mirror instruction: read, confirmed, off my list. Thank you
for closing the source rather than just contradicting it.
