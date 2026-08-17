# INSTRUCTION: Build the Date Line Into Every Help Article (Kain-approved, S230)

**From:** Claude Chat, Session 230, 28 July 2026
**To:** Claude Code
**Type:** Approved instruction: a small template addition to the /help/ FAQ article template.

## Context (standalone)

Help articles currently display no dates. Kain has ruled they should: a visible freshness signal is standard support-centre practice, and the AI answer engines reward it (Perplexity weights recently updated content heavily). The 249 were genuinely rewritten and republished in the last twenty-four hours, so their updated stamps are real and current.

## The work

1. **The visible line.** Add a "Last updated: [date]" line to the FAQ article template, in the article's meta area near the H1, styled quietly to the design tokens (small, soft grey, unobtrusive). Human-readable date format (e.g. "Last updated: 28 July 2026").
2. **Real timestamps only.** The displayed date reads WordPress's actual modified timestamp for the article. Never a hardcoded or asserted date.
3. **The original date.** Where an article's WordPress published date is genuine, it stands. Where migration has made the published date meaningless (e.g. it equals the import date rather than any real origin), set the published date to June 2020, which Kain has ruled as the stated origin of the help section's first versions. State in your report how many articles kept a genuine date and how many took the June 2020 baseline.
4. **Schema.** Add datePublished and dateModified to the FAQ article's structured data, fed from the same real timestamps, so engines read the dates without guessing.
5. **Rendered approval before it ships (rule 16).** Render the template with the date line on one article and return it through TO Chat for Kain to view in Safari before the change deploys across the 249. The wording, size and placement are his call by eye.
6. Confirm article_gate stays clean, and report through TO Chat.

## Order

Small; slot it with the link ceiling check (same template territory), after the keyword score run, before the page_gate map.

## Spec note

Chat is amending DSRD 2 §2.24 (the FAQ article component list) to carry the date line as a numbered component in the same session, so the spec and the build stay in step.
