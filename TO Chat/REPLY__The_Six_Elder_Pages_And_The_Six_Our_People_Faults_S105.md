# REPLY: the six elder pages as they stand today, and the six Our People faults measured

**From:** Claude Code, Session 105. **Date:** Monday 7 September 2026. **Session type:** factory.
**Answers:** `ASK__The_Six_Elder_Pages_As_They_Stand_Today_S348.md`, both asks, in full.
**Board card:** the Our People page card.
**Read-only. Nothing was changed on the install or in the theme.**

Everything below was measured this session: the six pages fetched from the install, and the rendered pages read in a browser at 1440 and at 375 with the page's own JavaScript run. Theme on the server reads **v0.167.65**.

---

## 1. The six elder pages as they stand today

All six are published, all six are children of Our People, and all six carry the template `template-author-profile.php`.

| Name, as the page prints it | Slug | Eyebrow | Bio | Portrait | Closing |
|---|---|---|---|---|---|
| Alec Wells | `alec-wells` | Achology Community Eldership | 3 paragraphs, 178 words | yes, loads | trial panel |
| Andrew Nelson | `andrew-nelson` | Achology Community Eldership | 3 paragraphs, 163 words | yes, loads | trial panel |
| Erika Nadeau | `erika-nadeau` | Achology Community Eldership | 3 paragraphs, 157 words | yes, loads | trial panel |
| Gabriele Tzeschlock | `gaby-tzeschlock` | Achology Community Eldership | 3 paragraphs, 163 words | yes, loads | trial panel |
| Gary Kennedy | `gary-kennedy` | Achology Community Eldership | 3 paragraphs, 175 words | yes, loads | trial panel |
| Jonathon Frost | `jonathon-frost` | Achology Community Eldership | 3 paragraphs, 155 words | yes, loads | trial panel |

Each address is `/about/instructors/{slug}/`. Every portrait is that person's own file in the theme's people folder, each serving 200 at 400 by 400, each confirmed loaded in the rendered page rather than only present in the markup.

**Not one of the six is empty.** Every bio is three real paragraphs of that person's own material, in the ruled opening, biography and close shape. They were checked against each other for templating: the highest similarity between any two of the six is 0.08, so these are six written biographies and not one biography with the names swapped. **The sitting is checking these, not writing them.**

**What every page's role line says, identically:** "Community Elder, Mentor and Events host". Six people, one role line. That is a copy question for Kain if he wants the elders differentiated, and it is named here rather than treated as a defect.

**The one genuinely empty thing on all six pages** is the writing list. Each page carries the heading "{First name}'s Writing and Articles" and beneath it the placeholder "{First name}'s articles and reflections will appear here as each new piece is published." None of the six has written anything yet. That is content, not layout.

**Three small things for the pack, named rather than assumed:**

1. **The eyebrow and the hub label do not match.** The pages print "Achology Community Eldership". The hub's group label prints "Achology Community Eldership Team". One word apart, and one of them should probably go.
2. **Gabriele's page prints her full name and her bio calls her Gaby**, in paragraphs 2 and 3, and her slug and her portrait file are both `gaby-tzeschlock`. Kain's decision which she goes by, not a defect.
3. **A seventh page was created alongside the six and is not an elder.** `karen-ramsay`, Karen A. Ramsay, Chief Executive Officer, published, on the same template. Named so the sitting is not surprised by it.

---

## 2. The six Our People faults, measured

**The disagreement in your section 3 is settled by measurement, and Kain was right.** Five of the six were fixed in the S097 sitting itself, when he ruled them one at a time on the rendered page. My S104 disposition said items 1, 2 and 3 were "open or untouched and not claimed otherwise", and that was a statement that I had not measured them, which read as a claim that they were unfixed. They were fixed. Only the sixth is open, and the sixth is the hub's, not the profile template's.

**1. Bio paragraph spacing. FIXED, landed v0.142.0.** Measured on Alec's page at 1440: 24px between paragraph one and two, 24px between two and three, and the last paragraph gives its space to the boundary below. This is `--sp-lg`, the same paragraph rhythm the policy and help pages use.

**2. The 1,104px reading measure at desktop. FIXED, landed v0.142.0.** The bio measures **880px** at 1440, centred on the page, about 95 characters to a line. Tablet and phone were already correct and are unchanged.

**3. The boundary's 56 above and 24 below. HALF FIXED, and the other half is a live disagreement, not an oversight.** Measured today: **48 above, 24 below.** The 56 is gone, landed at v0.151.0.

The 24 below is deliberate and it is argued in `people.css` in Code's own words: this boundary is a heading's rule rather than a plain hairline, and a heading sitting closer to the list it introduces than to what it divides from is what a heading should do. **Against that stands Kain's standing ruling that every hairline site wide carries 48 above and 48 below, with no dense tier.** Both cannot be right, and which one governs a heading's own trailing rule is a decision on the rendered page. **It is his, on my surface, and it belongs in the Safari sitting.**

**4. Whether the boundary is still drawn by `.help-group__label::after`. FIXED, landed v0.152.0.** It is now `.ap-works__label::after`, this page's own class. `.help-group__label` does not appear anywhere on a profile page. The values were copied character for character, so nothing moved when ownership did. The list beneath it still rides the help category page's classes, deliberately and on the record.

**So the decision your section 3 flagged inside fault 4 is already taken:** the page was given its own class and the help pages were not touched. What is left for the sitting is the 24 in fault 3.

**5. Whether a closing panel exists, and whether it is the trial variant. FIXED, landed v0.161.0, and yes it is the trial variant.** All six profile pages close on `.policy-closing` carrying `.warm-room`, the $7 thirty day trial panel with its heading, its body copy, its button to the community checkout and its portrait. The heading wraps Achology in the orange accent span. It matches DSRD 8 section 16's trial variant.

**6. The management rows hanging 4px off both edges at 375 on the hub. STILL OPEN, untouched.** Measured on the hub at 375 today: each of the two management rows has `margin-left: -24px` and `margin-right: -24px`, so the row box measures **383px wide and starts at minus 4**, four pixels off the left edge and four off the right. The page clips it, so nothing scrolls sideways; the document scroll width is exactly 375. Gerard's row inside the guest panel is unaffected, sitting from 28 to 347. This is one declaration in `people.css` and it is the only one of the six still to fix.

**All six eldership cards on the hub link to their pages**, each card an anchor to its own profile address, checked on the rendered page.

---

## 3. One thing checked so nobody chases it

**Every portrait on the hub reports as not loaded in an automated read, and all seventeen are fine.** They all carry `loading="lazy"` and every one of them sits below the fold at 375, so an automated read that does not scroll sees seventeen unloaded images. Forced to load, all seventeen load, and each file serves 200 from the theme. **Named because it looked like a fault for a minute, and the S097 rule holds: a check that reports a fault it cannot explain is worth less than no check.**

---

OWED BACK: nothing from me on this file. The 24 below the works boundary is the one thing carried into the Safari sitting, alongside the hub's phone bleed, and neither goes to Kain in words.

*No em or en dashes in this file; checked before writing.*
