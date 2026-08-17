# Ship brief — v0.36.14 and v0.36.15

From: Claude Code · 2026-07-23 · both pushed, `achology.zip` rebuilt.
Kain uploads the zip; nothing below is live until he does.

---

## v0.36.14 — the schema and video build

Everything your approved brief listed, and nothing beyond it.

**`VideoObject` on the About page.** New ACF group in Local JSON,
`acf-json/group_about_videos.json`: a Repeater named `member_story_videos` with
the six fields DSRD 10 §8 specifies, every one required. `page-about.php` emits
one `VideoObject` per completed row, with `embedUrl` built from the Vimeo ID and
no autoplay parameter. Until Kain and Karen fill the group in, it emits nothing —
which is the intended state, not a failure.

Two build decisions worth your record:

- **The group's location rule is resolved in code**, in a new `about-setup.php`.
  ACF binds a group to a page by post ID, and an ID is a fact about one database,
  not about the site. The Local JSON carries a placeholder and the theme rewrites
  it to whatever ID the page with slug `about` holds wherever the theme is
  running, so the binding survives the staging-to-production clone with no admin
  step. If you are recording §8's implementation, this is the detail to record.
- **A row short of any required value is dropped, not emitted.** Google gives no
  result to a `VideoObject` missing one of its four required properties, so a
  broken block is worse than no block. `duration` is the exception: an unreadable
  `MM:SS` drops just that property and the row still earns its result.

**`BreadcrumbList` on `/about/` and `/policies/`.** Both worded from the same
trail the visible breadcrumb prints, so the two cannot drift. Rank Math's
breadcrumb output is switched off for both pages by a filter in
`rank-math-feed.php`, which also drops the `WebPage` reference that pointed at
the removed node.

**One thing you should know about that switch-off:** Rank Math currently emits no
`BreadcrumbList` anywhere on the site. The filter is a guard, not a fix. It
matters if the setting is ever turned on.

---

## v0.36.15 — your correction brief, defects only

Applied: the three RGB companion tokens, the rgba swaps in `policies.css`, the
citation repoints, the dead-CSS deletion in `about.css` after verification, and
the colour longhand swaps. **Verified value-identical in a live browser**: nine
token-versus-literal probes injected into a rendered page, all nine computed the
same value, including the two rgba opacities.

Three places where the brief and the code did not agree:

**1. The rgba count is six, not eight.** `rgba(198, 78, 20, 0.32)` appears three
times, not four: the "shared underline treatment" the brief counts as a fourth is
the same declaration already counted. The eighth is the icon rule in item 3.
Everything the brief pointed at was swapped.

**2. One of the three "DSRD 8 §13" citations is not a separator citation.** The
comment on `.policy-body .help-popular` at the top of the link rules names the
`/help/` question-door **component**, not its spacing. Repointing it to DSRD 7
§4.3 would have claimed a specification the component does not have — and it is
the same missing section you flagged yourself in that brief. It now records the
gap in one line instead. The other two, which are genuinely about the 48px
separator, are repointed to §4.3 as you asked.

While there: **DSRD 7 §4.3 cites "the Related Questions block (DSRD 8 §12.4)",
but §12.4 lists six policy-family blocks and Related Questions is not among
them.** One of the two needs adjusting; both are yours.

**3. Item 3 is not applied, and should not be as written.** `.policy-next__icon`
does duplicate `.icon-section-header-container`'s declarations exactly. But it is
not `template-policy.php`'s alone: it is used by `404.php`, `page-about.php`
thirteen times, `help-parts.php`, and both policy content partials — around
twenty-five markup sites. `about.css` then gives it four colour variants
(`ic-tint`, `ic-orange`, `ic-slate`, `ic-dark`) and a larger 46px box on the
About grid. Deleting the rule and swapping classes in one template would strip
the box, radius and tint from every other use, and break the About grid's
centring, since the variants supply colour but not `display: flex`.

The value-identical alternative is to group the selector rather than delete it:

```
.icon-section-header-container,
.policy-next__icon { ... }
```

Zero markup churn, zero pixel change, duplication gone, and `about.css`'s
overrides keep winning on specificity. The cost is that a base-layer rule then
names a policies-family class. That is a structural call about where the shared
icon container lives, so it is yours and Kain's, not mine to take inside a
defects-only pass. Say the word and it is a two-line change.

---

## Also in this folder

- `Report__Per_Page_Type_Schema_Inventory.md` — every page type, every schema
  type, source attributed mechanically from the live site. It settles the
  provisional rows and turns up two live Standard breaches, including two
  `Article` blocks on the article page that §9's own row currently sanctions.
- `Reply__Preview_Provenance_And_Hairline_Measurements.md` — both your questions.
  The short version: no preview is generated from a shipped template, most are
  weeks stale, and the Code of Ethics hairlines measure exactly the dense tier
  §4.3 specifies at both widths. Two measured defects on the default-tier policy
  pages are in there for your next brief.

## What I need from you

Nothing blocking. When you have settled the four decisions in §3 of the
inventory, send them as one brief and I will build them together.
