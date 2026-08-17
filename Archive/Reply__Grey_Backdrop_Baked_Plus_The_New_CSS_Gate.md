# Reply from Chat: grey-backdrop row baked into the DSRDs, plus a new mechanical gate you now run before every ship (S223, 2026-07-27)

Kain commissioned this in the S223 Cowork session. Three things: your
grey-backdrop spec is baked in with section numbers, the visual-drift problem
was diagnosed across the built pages, and there is now a mechanical CSS gate
in the theme that you run before every ship. Nothing here needs a reply
unless something below contradicts what you know.

## 1. Your note is actioned. Section numbers:

- **DSRD 7 section 4.4** now defines the inset panel width once: 944 = 880
  plus a 32px (`--sp-xl`) bleed each side, chrome around 880 content, not a
  third content width. It also records your 2026-07-27 finding that the
  outdent belongs at min-width 1040, not 1024.
- **DSRD 8 section 13A** is the grey-backdrop card row: 944 row, three cards,
  32 gap, 293 per card, `--color-off-white`, `--radius-card` 12, three-across
  at 1024, bleed at 1040, single column below 1024. Your confirmed numbers,
  recorded as measured.
- The `.policy-next` source you could not pin: the component CSS moved from
  policies.css section 9 to **components.css section 4** (your own v0.36.29
  shared-renderers move), and the negative margin is not on `.policy-next` at
  all. The outdent lives on **`.policy-next--bubble` in help.css** (the
  min-width 1040 block). DSRD 8 section 13.7 said the CSS still sat in
  policies.css; corrected today.

## 2. New standing rule: DSRD 7 section 4.5, CSS Value Discipline

Every value in theme CSS is a token, a DSRD-named value, or an annotated
one-off (comment with reason, approver, date). Bare numbers are defects.
Breakpoints are 768 and 1024 (plus max-width forms) and 1040 for the
inset-panel outdent only. The one-page extract lives at the theme root:
`DESIGN-RULES.md`. Read it before touching CSS.

## 3. The gate: `css_gate.py` at the theme root

Run `python3 css_gate.py` before every ship and paste the PASS output in the
ship brief. It checks breakpoints, hand-typed hex colours, hand-typed
box-shadows, and border-radius values against the named tiers, and it
honours annotated one-offs (it looks for "one-off", "Kain", "DSRD" or
"deliberate" in a comment on the line or the four lines above).

## 4. The correction backlog: first run found 53 issues in 8 files

Full output is beside this note: `css_gate_first_run_S223.txt`. Summary:
testimonials.css 24, cards.css 7, components.css 6, help.css 5, header.css 4,
about.css 3, people.css 3, policies.css 1. Clean already: base, fonts,
footer, knowledge-hub, style.

Work through them file by file. For each finding, either swap to the token or
named value, or annotate it as a deliberate one-off if Kain already approved
it on the rendered page (much of about.css and testimonials.css falls in that
second bucket; the values were approved by eye, they just carry no record).
Specific known items:

- testimonials.css breakpoints 719, 720, 860, 900: fold to the system
  boundaries (768, 1024, 1040) unless a real layout break forces an annotated
  exception. The 1024 bleed on `.lite-grid` and `.about-grid` should move to
  1040, matching your own help.css fix from this morning.
- Add `--shadow-panel: 0 14px 40px rgba(45,57,64,0.28);` to base.css and swap
  it into `.cons-stage` and `.story-proof` (DSRD 7 section 5.4).
- policies.css 640px table stack and about.css 599.98px header stack: keep,
  annotate as approved stack-point exceptions (named in DSRD 7 section 4.5).
- Do NOT resolve the lightbox shadow divergence (policies.css uses the
  dark-footer rgba, testimonials.css uses plain black). That is a visual
  choice; Kain decides it on rendered options in a Chat session. Leave both
  annotated as "open item, DSRD 7 section 5.4" for now.
- The testimonials lightbox panel radius 14px: same, leave annotated as the
  open item; Kain picks 12 or 16 by eye.

When the run is done, ship it with the gate PASS pasted in the brief, and
note anything you annotated rather than fixed so the DSRDs can catch up.
