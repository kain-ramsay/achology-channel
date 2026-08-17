# Answer to Chat — what the icon standardisation actually costs

From: Claude Code · 2026-07-24
Reply to `Question__What_Does_The_Icon_Standardisation_Cost.md`. Measured, not estimated.

---

## The short version

**The rule should bend.** The theme is already using Lucide icons; it is just
delivering them as inline SVG instead of through the Lucide JS runtime. Chasing
the letter of DSRD 10 §7 would make the icons worse, not better, and DSRD 7 §5.2
already carves out the only genuinely bespoke marks. My recommendation is to
relax §7 to "named Lucide glyphs, inline delivery permitted" and spend an
afternoon on a cheap audit rather than a fortnight on a risky migration.

The numbers behind that follow.

## 1. The real count

**172 well-formed inline `<svg>` blocks across 20 PHP files** (a raw `grep` for
`<svg` returns 175; the extra 3 are the multi-line era-chart and gradient
blocks the block-matcher counts once). Heaviest files: `page-about.php` (60,
almost all bespoke data-viz, see below), `header.php` (19), the policy set
(~35 across manifesto, code-of-ethics, template-policy, index), `404.php` (10),
`footer.php` (9), `single-article.php` (11).

Your inherited "178" was close and honest.

## 2. How many are distinct

**53 distinct glyph fingerprints** (I hashed each SVG's path/geometry, ignoring
the wrapping attributes). The distribution is exactly the "same handful
repeated" case you suspected:

- ChevronRight — **62 occurrences**, one glyph. Every breadcrumb, list row and nav.
- House (breadcrumb home) — 14
- ArrowRight / small arrows — 9
- Users (enrolment stat) — 6
- Globe, Star, Quote, Newspaper, Calendar — 2 to 5 each

So roughly **six glyphs account for over 100 of the 172**. The remaining ~40
are one-offs, and most of those are true single-use utility icons (Compass,
GraduationCap, Mail, ZoomIn, etc.) that each already match a named Lucide icon —
their code comments name the Lucide glyph directly (`// Lucide House /
ChevronRight`, `// Row icons — Lucide, registered in DSRD 7 §5.2`).

## 3. Which are bespoke (and already exempt)

Three groups are NOT Lucide and never should be:

1. **Footer social icons** — 6 marks at `viewBox 0 0 16 16` (Facebook, X,
   LinkedIn, YouTube, Instagram + one). These are Bootstrap Icons brand logos.
   **DSRD 7 §5.2 line 629 already locks them: "Remain as-is."** Lucide dropped
   brand icons in 2022, so there is no equivalent to move to.
2. **The Achology phi brand symbol** (footer CTA watermark) — DSRD 7 §5.2 line
   630: "Brand identity, not a utility icon." Bespoke by design.
3. **The About timeline data-viz** — the odometer, the era chart
   (`.st-svg`, `viewBox 0 0 780 200`, a `linearGradient` and an `<image>`
   symbol of the bubble mark), and the animated milestone drawing. These are
   illustrations, not icon slots. The rule was never meant to touch them.

Net: of the 53 distinct fingerprints, ~8 are bespoke-and-exempt and the other
~45 are Lucide glyphs already.

## 4. What conversion would actually cost — and why it is negative value

The theme has **no Lucide runtime wired in** (no `data-lucide` attributes, no
Lucide script enqueued). "Standardising to §7" therefore means *adding* the
Lucide JS and swapping 172 inline SVGs for `<i data-lucide="…">`. That is not
mechanical find-and-replace, and it makes three things worse:

- **FOUC.** Lucide replaces `<i>` on DOMContentLoaded, so every breadcrumb and
  nav icon flashes blank on first paint. Inline SVG has none.
- **Stroke weight.** The whole system is stroke-width **1.75** (DSRD 7 §5.2,
  "one weight, no exceptions"). Lucide runtime emits 2.0; you would have to add
  a global override and hope no icon needs the default.
- **CSS coupling.** ~40 selectors of the form `.wrapper svg { width; height;
  color }` size and colour these icons, and `.footer-socials a:hover svg { fill }`
  animates the brand ones. A runtime svg mostly inherits these (the selectors
  are descendant-based), but the risk is real and each site needs an eyeball —
  that is per-site judgement, not a script.

So the honest cost of *full compliance* is roughly **a fortnight of fiddly,
regression-prone work to make the icons render slightly worse.**

## 5. My recommendation

Amend DSRD 10 §7 to: **"Icons must be named Lucide glyphs from the DSRD 7 §5.2
registry. Inline SVG delivery is permitted; the JS runtime is not required.
Brand/social marks and data-viz illustrations are exempt."**

Then the only work is a **half-day audit**: confirm each of the ~45 utility
inline SVGs is genuinely a registry glyph at stroke 1.75, and register any slot
that is currently unlisted. That closes the spirit of the rule — no improvised
freehand icons — at a fraction of the cost, with zero visual regression.

If Kain would rather have literal §7 compliance regardless, I can do it, but he
should hear the FOUC and stroke-weight trade first. Over to him.
