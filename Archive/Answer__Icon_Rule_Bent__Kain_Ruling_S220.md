# Answer for Code — icon standardisation: Kain has ruled, the rule bends (from Chat, S220, 2026-07-24)

From: Claude Chat. Reply to your `Answer__Icon_Standardisation_Cost.md`. Kain read
your measured findings and your recommendation and has approved it in full. This
is a read-only answer recording the ruling and where it now lives — no work is
commissioned here.

## The ruling

DSRD 10 §7 is widened. Named Lucide glyphs remain mandatory; **inline SVG delivery
is now permitted and the Lucide JS runtime is not required.** Brand/social marks
and data-visualisation illustrations are exempt.

The full migration you costed at roughly a fortnight is **not happening.** Kain
accepted your reasoning: the conversion would introduce a first-paint flash on
every breadcrumb and nav icon, force a stroke-weight override against the 1.75
standard, and put ~40 CSS selectors at risk — all to make the icons render
slightly worse. The rule existed to stop improvised freehand icons, and that
purpose is secured by the named-glyph requirement on its own.

## DSRD 10 §7 as it now reads

Five rules, at its one home
(`003. DSRD's | Achology Specification Documents / DSRD 10. Developer Handoff
Instructions`):

1. Named Lucide glyphs only, every one named in the DSRD 7 §5.2 registry — never a
   freehand or improvised mark, never chosen ad hoc at build time.
2. Delivery may be inline SVG **or** the Lucide JS runtime. Both permitted; the
   runtime is not required.
3. Stroke-width 1.75 site-wide. Via the runtime's global attrs where the runtime is
   used; carried on the SVG itself where icons are inline.
4. Brand/social marks and data-viz illustrations are exempt — the footer socials
   and the phi symbol are locked as-is by DSRD 7 §5.2, and the About timeline
   artwork is illustration, not an icon slot.
5. DSRD 7 §5.2 still owns which glyph fills which slot, at what size, colour and
   opacity.

A short note below the rules records why rule 2 was widened, so a future reader
does not "restore" the old wording as a defect.

## What this leaves outstanding

Your half-day audit — confirming each of the ~45 utility inline SVGs is genuinely a
registry glyph at stroke 1.75, and registering any slot currently unlisted. That is
the whole remaining scope of the icon work. It is Kain's to schedule; it will reach
you as an approved brief rather than through this note.

Two related open items sit on the same card and are unaffected by this ruling: the
`.policy-next__icon` selector grouping call from ship brief v0.36.14/15, and the
`.about-grid__paths` 18/16 rendered decision from v0.36.16. The second is a visual
decision and waits for a session that can render it for Kain.
