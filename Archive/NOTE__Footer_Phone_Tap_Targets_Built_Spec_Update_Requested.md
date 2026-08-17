# NOTE: footer phone tap targets built on Kain's ruling; one spec sentence requested (S043)

## The ruling and its origin

During S043 Kain asked for an honest assessment of the footer at all three widths. I reported that the phone accordion's links, while true to the design, are small touch targets, and that giving each a taller touch area would change nothing visually. Kain ruled in session: "yes please do the phone one", and directed this note to you. Under the one-home rule this needs its sentence in the spec, which is yours to write.

## What shipped

footer.css, inside the existing phone media block: each accordion link becomes an inline block with vertical padding that negative margins hand straight back. Touch area grows from a 20px text-height to a 46px hit height; the rendered page does not change. The hover underline offset is compensated so the line stays at the text's foot, including the school-coloured underlines, which inherit the same rule.

DSRD 8 section 19.9, read fresh at edit time, stays satisfied word for word: "Links appear below heading with slide-down animation (0.2s ease). Same Source Sans 3 14px/400 as desktop. 10px spacing." Font, animation and visible spacing untouched.

## Evidence

1. Baseline before the change, live at 375: seven link text boxes captured at quarter-pixel resolution; tap heights 20px.
2. After deploy, same page, same instrument: all seven text boxes byte-identical to the baseline; tap heights 46px; underline compensated.
3. css_gate pass, dash gate clean on the added lines.
4. Deployed to the build site directly (Kain has handed uploads to Code as of S043); server checksum matches local; SiteGround caches purged.

One operational note: the stylesheet URL still carries the previous version string, so a returning browser with the old copy cached keeps yesterday's smaller targets until the next version bump republishes the URL. The next shipped change set carries the bump; new visitors are already on the new file. Nothing visual differs either way.

## Requested from Chat

One sentence into DSRD 8 section 19.9's accordion rows (wording yours), so the spec records that accordion links carry an enlarged touch area with unchanged rendering. Ruling 2's footer heading work remains separate and still waits on QUESTION__Footer_Heading_Achology_Accent_Collision.md.

No em or en dashes in this file, checked before writing.
