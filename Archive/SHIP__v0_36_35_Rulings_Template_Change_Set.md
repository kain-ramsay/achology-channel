# SHIP BRIEF: v0.36.35, the S233 rulings template change set (S043)

What shipped (commits 5578608 before, 686fc48 after, pushed; zip rebuilt, awaiting Kain's upload):

1. Ruling 1: site-wide scroll padding in base.css, the measured 72px header plus 8px. Proven live by instrumented check: an anchor target that landed at 0 under the sticky bar now lands 8px clear of it.
2. Ruling 4: .policy-meta moves from mid grey to the soft grey token. Read with DSRD 7 section 1.1, the two documents agree on soft grey as the only destination: it is the darkest text token short of body dark, it passes AA for reading, and 1.1 assigns scanned single lines to it while reserving body dark for sentence text. Both adoption dates and every last-updated line render through this one rule.
3. Ruling 9: template-policy.php now renders the H1 before the document figure and its buttons. The float follows the H1 with a 16.4px pullback (16px H1 margin plus the 0.4px line-box excess), landing the figure at exactly the approved 38px drop. Verified by live rehearsal on both doc pages at 1280, 768 and 375: zero delta on every landmark and every body line wrap, at quarter-pixel resolution. The only change is the H1's invisible box width; glyph position identical.
4. Ruling 3 verified NOT confirmed: aria-expanded syncs with the panel on open, close, Escape and overlay click, checked live and in header.js code. The line closes with no fix; full detail goes in the records.
5. Ruling 2 is WAITING on QUESTION__Footer_Heading_Achology_Accent_Collision.md (filed alongside this brief).

What I need from Chat:

1. The ruling 2 answer (one lever, the question file has my recommendation).
2. Awareness for the register: the doc-page previews (manifesto, code of ethics) must NOT be rebuilt until the collapse brief reaches their frozen header markup. The builder bakes the old figure-before-H1 order; rebuilt against v0.36.35 CSS it would render the figure wrongly placed. This is DSRD 3 section 2.6 drift, already on the collapse brief's list; noting the new sharpness.
3. Nothing else. Records for both doc pages and the policy family update after Kain uploads and the live re-checks run.

Still open from this set: ruling 4 names "any dated template"; the help articles' updated line is the second dated template and runs as its own small declared change set next. One observed spec divergence for the register, report only: DSRD 8 section 19.5 lists the footer link "Our Manifesto"; the built footer and its ruled rename carry "Achology Manifesto".

No em or en dashes in this file, checked before writing.
