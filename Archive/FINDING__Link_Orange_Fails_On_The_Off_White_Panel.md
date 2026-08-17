# FINDING: the AA-safe link orange is not AA-safe on the off-white panel, and DSRD 7 section 1 says it is

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Found on:** page 6 of the S047 walk, https://achologytest.com/policies/disclaimers/
**Needs:** a correction to DSRD 7 section 1, and then a decision on the affected links. This one is general, not local to one page.

## What the document claims

DSRD 7 section 1, quoted from the canonical document read this turn:

> "**AA-safe orange:** #C64E14 (`--color-orange-link`; role widened, Kain 2026-07-16) the orange for SMALL text: body-copy links, overlines, breadcrumb current page, small button labels, heading accent words. Brand orange #ED6922 is 3.16:1 on white and fails AA below large-text size; **#C64E14 clears 4.5:1.** Brand orange stays for large text, borders, fills and icons."

The claim "#C64E14 clears 4.5:1" carries no background with it. Read plainly it says the colour is safe wherever small text goes, and the name given to it, "AA-safe orange", says the same thing more strongly.

## What it actually measures

Both figures read off the rendered Disclaimers page this turn, alpha composited:

| Link colour | On | Measured | Needs | Verdict |
|---|---|---|---|---|
| #C64E14 at 16px | white #FFFFFF | **4.67 to 1** | 4.5 | Pass, by 0.17 |
| #C64E14 at 15px | off-white #F3F4F4 | **4.23 to 1** | 4.5 | **Fail** |

On this page that is six links, all of them inside the section 12 cross-reference table whose cells carry the off-white background: Terms and Conditions, Refunds Policy, Privacy Policy, Cookie Policy, Trust Statement, Accessibility Statement. Nine other body links on the same page, on white, pass.

## Why this is general rather than one page's problem

The colour clears the threshold on white **by 0.17**. There is no room in it. Any tint behind it takes it under, and the system uses that exact tint deliberately and often. DSRD 7 section 4.4 names where: "the `.policy-next--bubble` close panels (help.css), the About page grey blocks, and the grey-backdrop card row (DSRD 8 section 13A)", all of them `--color-off-white` #F3F4F4.

So the rule is simple and worth stating plainly: **wherever a body link sits on the off-white panel anywhere on the site, it is below AA.** I have measured it in one place. I have not swept for the others, because a sweep needs a signed brief, but the ones DSRD 7 section 4.4 lists are where to look first.

The system already half knows this. DSRD 8 section 19 says, in passing, "The section 13.2 value exists because brand orange fails large-text AA on the off-white panel", so the off-white panel is understood to be the harder context. What has not happened is anyone checking the link orange against it.

## What I have not done

I have not changed the colour. A palette value is Kain's, and Rule 5 forbids me filling that gap. I have also not swept for other instances, per Rule 3.

## What would close it

1. **DSRD 7 section 1's sentence needs a background attached to it.** As written it licenses exactly this mistake anywhere in the system. Something of the form "clears 4.5:1 on white; on the off-white panel it does not" would stop the next person repeating it, whatever is decided about the colour itself.
2. **Then Kain's call**, knowing the number: a slightly darker link orange for the tinted context, or the links on tinted panels take the existing colour and the shortfall is recorded as an exception in the form DSRD 7 section 5.1 already uses for the primary button.

Worth noting which way I would lean if asked, though it is his: option 1's cost is one more named palette value, and the AA-safe orange's whole reason for existing is that someone did this arithmetic once before and named a colour for it. Doing it once more for the tinted context finishes the job that value started.

*No em or en dashes in this file; checked before writing.*
