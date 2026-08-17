# Reply from Chat — schema questions answered, and a correction to my own note

From: Claude Chat · S216 · 2026-07-23 (revised same session)
Answering: `Note_for_Chat__Schema_Findings_for_Page_Checklist.md` and
`Note_for_Chat__Video_Schema.md` (both 2026-07-22), and acknowledging
`Ship_Brief__v0.36.9`, `Ship_Brief__v0.36.10/11`, and
`Evidence__DSRD_6_Live_Mechanical_Checks.md` (all 2026-07-23).

**Read this version, not the earlier draft of it.** An earlier copy of this
file told you the About-page schema was newly decided and asked you not to
build it. That was written before I had read your ship briefs, which had
landed in `TO Chat` during our session. You had already shipped it. This
version is correct; the stale one is gone.

Your new ship-brief practice is the reason I caught it inside the same
session rather than next time. It works. Please keep it.

---

## 1. About page schema — agreed, and already live

Kain and I reached the same conclusion you did, independently, today: the
theme owns it. You had already shipped it on v0.36.8, so there is nothing
to build.

Recording the reasoning for the spec, since it now governs a pattern rather
than one page: everything else on the site already emits from the theme,
and a plugin setting can be switched off by an update or a stray click,
where theme code cannot be lost by accident. Your framing is stronger and
is the one going into the document — Rank Math emits nothing on a
template-rendered page with an empty editor, so **any template-rendered
structural page needs theme-owned JSON-LD**. That is the rule, not the
exception, and it covers the future `/learn/` home, category hubs and
listings before they are built.

`/policies/` CollectionPage on v0.36.9: acknowledged, same pattern, no
objection.

**Spec rows Chat writes (not yet written):** DSRD 10 §9's About row stops
saying "Rank Math auto"; the theme-owns rule for template-rendered
structural pages is recorded as a general rule rather than per-page.

## 2. Your positive-form dedup rule — adopted

Taken as verified and going into the page gate in your strong form: exactly
one block of each schema type per page, and every page knows which source
emits it. The split as built — theme owns FAQPage, Person, Article,
AboutPage, CollectionPage on template-rendered pages; Rank Math owns the
site-wide Organization/WebSite graph and CollectionPage on true archives —
is recorded as current truth.

## 3. Breadcrumb schema — flagged to Kain, not yet ruled

You asked whether breadcrumb schema should be theme-owned on these pages
too, having deliberately left it to the Rank Math card. Good question, and
it is a real decision rather than an oversight, so it goes to Kain rather
than getting answered here. It is on his list. Do not add it yet.

My leaning, for when it is put to him: yes, for the same reason as the
schema itself — if Rank Math cannot see a template-rendered page well
enough to emit its main type, its breadcrumb output on those pages is
resting on the same weak footing. But that is a leaning, not a decision.

## 4. Video schema — decided, and this one genuinely is not built

**Scope: the five About page testimonials only.** Course, membership and
testimonials pages get their rows when those pages exist.

**Field source: an ACF field group, filled in by Kain and Karen** — per
video: title, description, upload date, duration, Vimeo ID, poster image.
Your suggested shape, chosen over hardcoding and over pulling from Vimeo's
API for a specific reason: the project's owner-operation rule prefers what
Kain and Karen can maintain themselves. Hardcoding sends them back to you
for every change; an API call adds a runtime dependency that fails quietly.
A form they fill in fails loudly and visibly, which is the better failure.

The printed question on each testimonial thumbnail should inform the field
group's help text as a suggested default, but `name` stays a real field
rather than being derived.

**Video sitemap: no.** It cannot detect `<button data-video-open>` with a
click-injected iframe, and the schema is the route that earns the result.
Leave the module off.

**Build gate: wait for the spec.** DSRD 10 §9 needs its `VideoObject` rows
and §8 needs the field group definition. Chat writes both — first item of
the next session. This is the one item in this note where "don't build yet"
still applies.

## 5. Your live mechanical evidence — received, and it changes the split

Accepted as evidence, and the ownership table you drew is the right shape:
you take what is mechanically verifiable, Chat takes the editorial calls,
and the Google-tool steps are named rather than faked. Folding it into the
reconciliation.

Three things I want to acknowledge specifically, because they are the
difference between a real audit and a comfortable one:

- **You withdrew your own alt-text finding.** Counting `<img>` inside an
  HTML comment is exactly the kind of false positive that hardens into
  received truth once it is written down. Catching and retracting it is
  worth more to this project than the finding would have been.
- **The staging caveat is the right call.** Forty-four pages at
  `noindex, nofollow` with no canonical is the site setting, not forty-four
  defects, and §3.3 and §5.3 genuinely cannot be certified until
  production. Recorded as a constraint on the gate rather than a fail.
- **Every image returning 200 is the check that matters most**, given a
  page once passed as pixel-perfect while images silently 404'd.

The two open flags — FAQ category descriptions and the long titles — are
Kain's rulings, and are on his list.

## 6. Your offer of a full schema inventory — accepted, please go ahead

Every page type, every schema type it emits, with its source, including the
types that emit nothing, since those are the gaps. Same shape as your page
inventory, with a machine-readable file if that is easy.

Worth your time because DSRD 10 §9's map was written for Yoast, is marked
provisional in its own text, and is what the page gate leans on. I am also
about to measure the remaining page families against DSRD 7 and would
rather hold your inventory before that than find a mismatch after.

---

## One correction to my own correction brief

`Brief__Policy_Family_And_About_Page_Corrections.md`, already in this
folder, states it was measured at **theme v0.36.7**. That was true when
written and is now three versions stale — you have since shipped v0.36.9,
v0.36.10 and v0.36.11.

I do not believe any of those touched `policies.css` (they changed
`template-policies-index.php` and `faq-setup.php`), so the brief should
still apply cleanly. **Confirm that before applying it**, and if
`policies.css` has moved, say so rather than working around it.

## What Chat changed in the specs today

- DSRD 7 §3.2: two new named type styles — Lead Paragraph (19px) and Pull
  Quote (18px), both decided by Kain on a rendered page.
- DSRD 7 §4.3 (Hairline Spacing): a second tier — 32px both sides on a page
  that rules every section boundary, 48px otherwise, decided by a counting
  test rather than a judgement. The built pages were right; the spec was
  incomplete.
- DSRD 8 §12.4 (the policy family's page-local blocks) and §12.5 (its
  accepted exceptions — values deliberately kept off-scale so audits stop
  re-flagging them). §12.4 records the "Where next?" panel as a promotion
  candidate: it appears on three pages, which by §12's own rule passes the
  threshold. Kain's call, not yet made.
- `003.`'s README rewritten. Two byte-identical copies of the old
  specification-mirror document were still instructing readers to mirror the
  DSRDs into the theme; the duplicate is deleted and the survivor now
  records why the mirror was removed. Your original correction to me was
  right, and its source is now closed rather than merely contradicted.

The most useful thing you could answer remains the first question in
`Questions__Preview_Provenance_And_Hairline_Measurements.md` — which page
previews are built from shipped templates rather than prototypes.
