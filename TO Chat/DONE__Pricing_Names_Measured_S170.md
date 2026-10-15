> Chat: the pricing bundle school names fall under 4.5 on the real page at three widths (6 of 7 between 4.1 and 4.4 at 1100, 768 and 390; two at 3.2 and 3.6 at 390), so Kain looks at them, as RULING__Four_Theme_Decisions_S169 item 2 says. The 1440 reading did not come out clean; see below.

# DONE: the pricing bundle school names measured in WebKit (Code, factory session, S170, Thursday 15 October 2026)

**What was measured.** The build site's pricing page in Playwright WebKit. Each school name's text colour against the worst pixel behind its own lines of text, with the text made transparent so only the wash and the card show, and with every fixed overlay (cookie banner, back-to-top) hidden. Names are 18px at weight 600, which is not WCAG "large text", so 4.5 is the bar.

**Result (worst contrast ratio behind each name; the order is NLP, CBP, Life Coaching, Person-Centred, Mindfulness, Mental Health, Personal Growth):**
- 1100 wide: 5.10, 4.37, 4.35, 4.26, 4.82, 4.39, 4.37.
- 768 wide: 5.00, 4.30, 4.28, 4.19, 4.74, 4.32, 4.29.
- 390 wide: 3.17, 4.11, 4.09, 4.15, 4.70, 4.15, 3.55.
- The Access All Areas Pass (white on dark) reads 9.2 and passes.
- **1440 wide: not reliable.** Several names read 1.0 to 1.4, which cannot be right (text colour equal to its background); something at that width is still being sampled behind the text. It is not reported as a result. The ratios at the other three widths bracket the code's own bounds from cloud job 1 (3.90 to 5.44).

**Reading.** Five of the seven schools fall under 4.5 at 1100 and 768 (all but NLP and Mindfulness), and at 390 six of seven do. So the wash does pull the names under the bar, as F4 feared. This is a design decision, so Kain looks and rules; nothing was changed.

**Where it is.** The script is a scratch file and is not kept; the method is above. Branch `factory/four-decisions-s169` (four theme commits and the carve-out test, six cases pass) is pushed; merge and deploy wait for a theme session through the theme queue.

OWED BACK: Kain's look at the pricing bundle names (a theme item); Chat's read of the 16 staged articles and a yes or no on one retry of an unreadable fact check (from DONE__Second_Rerun_Narrowed_Fact_Check_S169).

*No em or en dashes in this file; checked before writing.*
