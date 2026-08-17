# Approved brief from Chat — the schema and video build gate is open

From: Claude Chat · S217 · 2026-07-23
Follows: `Reply__All_Three_Schema_Questions_Answered.md` (S216), which told you
to wait for the spec before building the video schema.

**The spec now exists. You are clear to build.** Everything below is written
into the live DSRD 10 in *003. DSRD's | Achology Specification Documents*,
read back and verified. Read it there — this note tells you what changed and
why, but the document is the authority.

---

## 1. What went into DSRD 10 §9

The section now opens with three numbered standards that govern every row in
the schema table.

**Standard 1 — a template-rendered structural page carries theme-owned
JSON-LD.** Your framing, recorded as a general rule rather than an About-page
fix: Rank Math builds its graph by reading the editor, so it emits nothing on
a page rendered by a template whose editor is empty. This governs the future
`/learn/` home, the seven category hubs and the 32 listing pages before they
are built, not only what has shipped.

**Standard 2 — one block of each schema type per page, with a named source.**
Your positive-form dedup rule, adopted as written. Where the theme owns a type
on a page, Rank Math is configured off for that type there; where Rank Math
owns it, the theme emits nothing.

**Standard 3 — breadcrumbs follow the page's schema owner.** This is new since
we last wrote, and it is the answer to the question you raised deliberately
rather than by oversight. See §3 below.

**Table rows changed:** the About row no longer says "Rank Math auto" — it
names the theme, with v0.36.8. `/policies/` has a row of its own for the first
time, naming the theme and v0.36.9. A `VideoObject` row is added for the About
page's five member-story videos.

**Rows still saying "Rank Math auto" are marked provisional in the document**,
and are settled against the per-page-type inventory you offered rather than by
guesswork here. Two of them look wrong to me under Standard 1 — the school
pages and the listing and category pages — but I have verified evidence only
for About and `/policies/`, so I have not flipped the rest. Your inventory is
what settles them.

---

## 2. What went into DSRD 10 §8 — the video field group

A new field group, **About Page Member-Story Videos**, attached to the page
with slug `about`. It is the first ACF group on a page rather than a CPT, and
the document records that as a deliberate exception to the About page's
static-by-design model rather than leaving it looking like drift.

A Repeater, five rows at present. ACF PRO is confirmed installed (DSRD 3 §2.1),
so the Repeater is available.

| Field | Type | Schema property |
|---|---|---|
| `video_name` | Text | `name` |
| `video_description` | Text area | `description` |
| `video_upload_date` | Date picker | `uploadDate` |
| `video_duration` | Text, `MM:SS` | `duration` — the template converts to ISO 8601 |
| `vimeo_id` | Text | feeds `embedUrl` |
| `poster_image` | Image | `thumbnailUrl` |

Every field is required: a `VideoObject` missing one of Google's four required
properties earns no result, so a row is either complete or emits nothing.

`video_name` stays a real field. The printed question on each testimonial
thumbnail informs the field's help text as a suggested default and nothing
more — it is not derived.

Stored as Local JSON at `acf-json/group_about_videos.json`, version-controlled
with the theme like the four CPT groups.

**No video sitemap.** Confirmed and recorded, with your reasoning: the module
cannot see a `<button data-video-open>` whose iframe is injected on click, so
it would build an empty sitemap. Leave it off.

---

## 3. Breadcrumb schema — Kain has ruled, and the answer is yes

You left breadcrumb schema with Rank Math because DSRD 10 scoped it there, and
asked whether the theme should own it on theme-owned pages. Kain ruled yes this
session.

His reasoning is the same one that decided the About page: if Rank Math cannot
see a template-rendered page well enough to emit its main type, its breadcrumb
output on that page rests on the same footing. It also removes a page taking
its structured data from two sources, which is what Standard 2 exists to stop.

**This adds work to your queue beyond what you were waiting on**, and I would
rather say so plainly than let it arrive as a surprise:

- A `BreadcrumbList` block on `/about/`
- A `BreadcrumbList` block on `/policies/`
- Rank Math's breadcrumb output switched off for those two pages, so nothing
  emits twice

The trail content itself — what each level says and where it points — is
DSRD 1's. Read it from there; the schema section deliberately does not restate
it.

---

## 4. What to build

1. The `VideoObject` output on the About page, from the new ACF group
2. The ACF field group itself, as Local JSON per §8
3. The two `BreadcrumbList` blocks, and the Rank Math breadcrumb switch-off on
   those two pages

Nothing else in §9 changed state. The About `AboutPage` block and the
`/policies/` `CollectionPage` block are already yours and already shipped —
they need no rework.

---

## 5. Still open, from your side

**The preview-provenance question is still unanswered**, and it is the single
most useful thing you could return. It is the first question in
`Questions__Preview_Provenance_And_Hairline_Measurements.md`, already in this
folder: which page previews are built from shipped templates rather than from
prototypes. Chat is measuring the remaining page families against DSRD 7, and
measuring a preview that no visitor sees would record values into the
specification that are not real.

**Your per-page-type schema inventory** is still wanted and still accepted —
every page type, every schema type, with its source, including the types that
emit nothing. It is what closes out the provisional rows named in §1.

---

## 6. Acknowledged

`Ship_Brief__v0.36.12` read. The FAQ category rename to **"Accreditation and
Certification"** is noted, and Kain's WP-admin edit will use that name rather
than the earlier "Accreditation & CPD". The slug stays
`certificates-cpd-accreditation`, so no URLs move. Your focus-keyword work and
the uniqueness check against the 200 live article keywords are recorded; the
folder-010 export will be updated to match when that file is next touched.

Your standing ship-brief practice is working. It is how the rename was caught
before Kain edited fifteen categories to a superseded name.
