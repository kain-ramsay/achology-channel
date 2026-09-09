# RULING: the page title is one size on every Knowledge Hub page, workbook included

**From:** Code, S108. **Theme v0.180.0**, on the build site.
**DISPOSITION: WAITS ON** DSRD 9's book note section, for the one correction in
section 3. The build and the gate are both done.

---

## 1. What Kain did, and it is worth copying

He asked me to open three page types in Safari at once, and then asked one
question: **is the article heading using the same size font in each type of
post, yes or no?**

No. The quote page and the article page both set the page title at the 33 step.
The book note set it at 42.

**That is a whole class of drift caught by one question and two tabs.** It is
worth Chat knowing the method, because nothing in the written record would have
surfaced it: each page's own spec was internally consistent, and only putting
them beside each other showed the difference.

## 2. The ruling

> "yes please, and will you somehow remember to make this a standing rule for
> the workbook pages too?"

**Every Knowledge Hub page type sets its H1 at the 33 step**, whatever the page
looks like around it: the quote page, the article, the book note, and the
workbook when it is built.

## 3. What Chat is asked to correct

**One line, in DSRD 9's book note section.** Wherever it names the hero title's
size, it should read the H1 page title step, not the hero step, with the reason
below. Nothing else on that page changes.

**The reason is already in base.css and was simply not being followed.** The
scale names the 33 step "H1 Page Title" and the 42 step "Hero Heading". They are
two different roles. The book note has a page title that happens to sit inside a
hero band, and it had taken the band's setting rather than its own.

**The tracking goes with the size, and this is the part a document usually
misses.** The `-0.01em` belongs to the 42 step, where it stops large caps
drifting apart. At 33 the H1 step carries none. Keeping the tracking would have
left this page's title set differently from the other two while appearing to
match, which is worse than the original fault because it looks fixed.

## 4. Measured before and after, on the rendered pages

- This book's title runs two lines instead of three, so "Key Ideas" no longer
  hangs alone on a third line.
- The hero band comes down by about a fifth, which pulls the cover, the
  description and the Amazon control into one group.
- The longest title in the set goes from two lines to one.
- The book note now computes to 33 at desktop and tablet, matching the quote
  page and the article page exactly.

## 5. How the standing rule is kept, and a gate fault found doing it

Kain asked me to remember it. **A rule I merely remember is a rule that dies
with the session, so it is enforced instead.** `page_gate.py` already checks
every page's h1 against `H1_SIZE`, so the rule reaches the workbook template
before that template is written.

**But that constant said 32, and had done since S056.** Kain's own S056 ruling
moved the scale from 32 to 33 and base.css was corrected then; the gate's
constant was not. It survived because `TOLERANCE` is 1.0, so a real 33 missed a
stale 32 by exactly the tolerance and passed.

**A check that passes the right answer for the wrong reason also passes the
wrong answers either side of it.** At 32 that row accepted 31, 32 and 33 alike.
Corrected to 33.

**One thing named rather than assumed away.** The gate would have caught 42 even
at the stale value. So either the book note has never been run through
page_gate, or the row was passed over. I do not know which, and I am not going
to guess. Running every built page against the corrected constant is the next
job and it is mine.

## 6. What this does not cover

**Whether the book note's hero should still be a hero at all** now that its
title is the same size as an article's. That is a visible design question, so it
is Kain's on a rendered page, not Chat's and not mine. It is not urgent: the
band still works, and he has seen it.

*No em or en dashes in this file; checked before writing.*
