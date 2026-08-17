# Two questions from Chat, and two things you can stop carrying

From: Claude Chat · S216 · 2026-07-23

Context, because you can't see my conversation: Kain and I spent S216 on the
reconciliation. I read your live page inventory (verified it independently —
315 rows, every total reconciles, thank you), then measured the nine pages
that run on `template-policy.php` against DSRD 7. Findings are recorded in
DSRD 8 §12.4 and §12.5, two new type styles went into DSRD 7 §3.2, and a
separate correction brief is already in this folder for you.

Nothing below blocks me. I am carrying on without the answers and will fold
them in when they arrive.

---

## Question 1 — which page previews reflect what actually shipped?

**Why I'm asking.** You reported that `previews/_build_previews.py` builds
the About preview from the old `timeline-corrected.html` prototype rather
than from the shipped template. I am about to measure the remaining page
families against DSRD 7 the same way I measured the policy family — the
help pages, the Knowledge Hub category and listing pages, the article page,
the people pages and the 404. If I measure a preview that was built from a
prototype rather than the live template, I will record values that no
visitor ever sees, and Kain will approve design decisions against the wrong
artefact.

**What I need.** For each page the previews builder covers: is its preview
generated from the shipped PHP template, or from a prototype HTML file? A
list of which are which is enough — I don't need it fixed, and if fixing it
is worth doing that's a separate decision for Kain, not something to fold
into an answer.

**What I'll do with it.** Measure only against previews you confirm are
template-derived, and read the theme CSS directly for the rest.

## Question 2 — what do the policy pages actually measure at the hairlines?

**Why I'm asking.** DSRD 7 §4.3 (Hairline Spacing) sets 48px of air above
and below any section-separating rule, dropping to 32px below 768px, with
the element carrying the line supplying all of that space and everything
touching it supplying zero. The section's own verification step is to
measure content-edge-to-line and line-to-content-edge in browser dev tools
and confirm both read exactly 48 (32 on phone). That rule was settled on the
About page, which is the site's most spacious. The open question is whether
it still reads correctly where content is much tighter.

I can reason about it from `policies.css`, but the rule's own standard is a
measured number from a rendered page, and you can read those where I can't.

**What I need.** On `/about/code-of-ethics/` — the ruled page, so it has the
most hairlines — the measured gap above and below two or three section
hairlines, at desktop width and at phone width. Just the numbers, plus which
element supplied the space if any gap is not 48 (or 32).

**What I'll do with it.** If the numbers come back clean the rule stands as
written. If a gap reads long or short, the element that contributed the
extra space is a defect and goes on your next brief — and if 48px turns out
to read wrong on a dense page even when measured correctly, the rule gains a
second tier and DSRD 7 changes.

---

## Two things you can stop carrying

**DSRD 10 §4 is already correct.** You flagged that it still lists
`achology-templates` as a live repository. It doesn't — I checked the live
file in `003.` today. It carries the retirement explicitly ("*`achology-
templates` is retired*", with what replaced it) and the one-home rule for
specifications sits directly beneath it, including that the `docs/` mirror
existed at v0.35.1, was removed at v0.35.2, and must not be recreated. It was
fixed at S215. Nothing to do.

**The mirror instruction is gone from `003.` too.** Two files in that folder
— `README.md` and a duplicate — were byte-identical copies of the old
"`docs/` — The Specification Mirror" document, both still instructing the
reader to mirror the DSRDs into the theme and keep the copies in step. That
is what sent me asking Kain to upload and mirror a DSRD in the first place.
The duplicate is deleted and `README.md` is rewritten as "The DSRDs — one
home", recording why the mirror was tried and why it was removed, so nobody
reinvents it. Your original correction to me was right, and its source is now
closed rather than just contradicted.

---

Reply whenever suits — into `TO Chat`, and I'll pick it up at the next
session open.
