# Brief for Claude Code — policy family + About page corrections

From: Claude Chat · S216 · Approved by Kain before sending.

**Scope: defects only.** Every item below is a correction with a verified
target. No design decisions travel in this brief. Nothing here changes a
rendered pixel — every swap is to an identical computed value, or removes
code that styles nothing.

Measured against DSRD 7 §1–§5, reading `policies.css`, `base.css` and
`template-policy.php` from disk at theme v0.36.7.

---

## 1. Add three RGB companion tokens to `base.css`

The theme already uses this pattern for school colours
(`--school-accent-rgb`). Three brand colours are missing their companions,
which is why they appear typed out by hand wherever transparency is needed.

Add alongside the existing brand palette tokens:

```
--color-orange-rgb:       237, 105, 34;   /* #ED6922 */
--color-orange-link-rgb:  198, 78, 20;    /* #C64E14 */
--color-dark-footer-rgb:  45, 57, 64;     /* #2D3940 */
```

Verified: each triplet is the exact decimal equivalent of the hex token
already defined in `base.css`.

## 2. Replace the raw rgba values in `policies.css`

Eight uses, all of brand colours already tokenised. Each swap produces an
identical computed colour.

| Current | Replace with | Occurrences |
|---|---|---|
| `rgba(198, 78, 20, 0.32)` | `rgba(var(--color-orange-link-rgb), 0.32)` | 4 — `.policy-body a`, `.policy-doc-textlink`, `.policy-endnote a`, and their shared underline treatment |
| `rgba(45, 57, 64, 0.82)` | `rgba(var(--color-dark-footer-rgb), 0.82)` | 1 — `.policy-doc-lightbox__backdrop` |
| `rgba(45, 57, 64, 0.45)` | `rgba(var(--color-dark-footer-rgb), 0.45)` | 2 — the lightbox panel and book shadows |
| `rgba(237, 105, 34, 0.07)` | see item 3 — the rule is removed entirely | 1 — `.policy-next__icon` |

Leave `rgba(255, 255, 255, 0.14)` and `rgba(255, 255, 255, 0.85)` as they
are: plain white at an opacity, no token needed.

## 3. Remove the duplicated icon container

`.policy-next__icon` in `policies.css` redeclares
`.icon-section-header-container` from `base.css` — same 36×36px box, same
10px radius, same 7% orange tint, same 18px icon inside.

Delete the `.policy-next__icon` and `.policy-next__icon svg` rules and
apply the shared `base.css` classes in `template-policy.php` instead.
Values are identical, so the rendered result must not change — verify the
"Where next?" rows on `/about/manifesto/` before and after.

## 4. Repoint three stale DSRD citations in `policies.css`

**DSRD 8 §13 has never existed.** DSRD 8 runs §6–§12, then §18 and §19.
Verified against the live file in `003.` today.

All three citations describe the same thing: a section separator carrying
48px of air on both sides. That standard is **DSRD 7 §4.3 (Hairline
Spacing)**. Repoint all three:

1. the `.policy-body .help-popular` comment — the Related Questions block
2. the same block's separator note, "measured from the article page"
3. the `.policy-page--404 .help-popular` comment in §12 of the stylesheet

Comment text only. No CSS values change.

**Do not repoint the `DSRD 8 §12` citation on the handbook reader.** §12
(Page-Local Blocks) is the correct home; it simply does not yet list the
policy family's blocks. Chat is adding them — the citation becomes correct
without you touching it.

## 5. Verify, then remove dead CSS from `about.css`

Carried from S214 and **not independently re-verified by Chat** — confirm
before deleting.

The `.fa-ghost`, `.fa-name` and `.fam-num` rules are reported to style a
founder-card block with zero occurrences in `page-about.php` (~15 lines).
Search the theme; if genuinely unreferenced, delete. If any is in use,
leave it and say so.

## 6. Replace colour longhand in `about.css`

Also carried from S214. Brand colours typed out rather than referenced:
six uses of `#fff`/`#ffffff`, two of `#354149`, two of `#ED6922`, two of
`#D85A1B`, one of `#8A9199`. Swap each for its existing token
(`--color-white`, `--color-dark`, `--color-orange`, `--color-orange-hover`,
`--color-mid-grey`).

Two values are genuine one-offs with no token: `#3E4E5A` and `#F5A05C`.
Leave both, and add a one-line comment on each saying it is a deliberate
one-off, so a later audit stops re-flagging them.

---

## Explicitly not in this brief

Recorded by Chat as accepted exceptions in DSRD 7 — **leave exactly as
built**, because changing them would move the page:

- the 15px table base size and its 14px Como header row
- the `16px 20px` table cell padding
- the 3px, 2px and 6px micro-values in the index and route rows
- the lightbox's one-off `0 24px 64px` shadow
- the 43px optical correction on the 404 header
- every tuned Aristotle watermark offset

## One gap flagged, not for you to fix

The `/help/` question-door component has **no specification section in any
DSRD**. DSRD 8 §12.2 refers to it as though it exists; DSRD 9 names only
`help.css` as its source. Chat owns closing this. Recorded here so the
reconciliation sees it.

## Definition of done

Items 1–4 and 6 applied; item 5 verified then applied or reported back.
The policy pages and the About page render identically to before at
desktop, tablet and phone — confirm by eye, since a visible change means a
swap was not value-identical. Reply down the channel with what changed and
anything you found that this brief got wrong.
