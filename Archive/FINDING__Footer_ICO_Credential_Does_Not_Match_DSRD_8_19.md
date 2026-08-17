# FINDING: the footer's ICO credential does not carry the string DSRD 8 section 19 registers

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.16.
**Found on:** page 2 of the S047 walk, /policies/terms-and-conditions/. The sub-footer is site-wide chrome, so this is every page.
**Needs:** one line of authorisation. The fix is a single string in one file and the replacement wording is already written in the document, so no new words are being drafted.

## The standard

DSRD 8 section 19, quoted from the canonical document read this turn:

> "**Left side ICO registration credential** *(added 2026-07-15, section 19 unlocked and relocked at Kain's request):*"
>
> "| Content | 'Registered with the ICO · ZB662679' (middot separator, no em-dash) |"
> "| Link | `https://ico.org.uk/ESDWebPages/Entry/ZB662679` |"
> "| Rationale | ICO registration is a legal obligation, not an accreditation. Shown as the registration number linking to the live public ICO register entry, **not** the ICO logo, which would imply an endorsement that does not exist. Linking the live register (rather than hosting the certificate PDF) keeps it always-current and exposes no personal data. |"

## What is built

Read off the live page this turn:

```
<span class="footer-copyright">&copy; 2026 Achology Transactions Ltd. All rights reserved.
  <span class="footer-ico-sep" aria-hidden="true">&middot;</span>
  <a class="footer-ico" href="https://ico.org.uk/ESDWebPages/Entry/ZB662679"
     target="_blank" rel="noopener"
     aria-label="Achology's ICO data protection register entry (opens in a new tab)">ICO Registered</a>
</span>
```

| Item | DSRD 8 section 19 | Built | Verdict |
|---|---|---|---|
| Link target | `https://ico.org.uk/ESDWebPages/Entry/ZB662679` | identical | Pass |
| Middot separator | required | present, correctly `aria-hidden` | Pass |
| Visible content | `Registered with the ICO · ZB662679` | `ICO Registered` | **FAIL** |
| The registration number | shown, and is the whole point of the credential | **not shown anywhere** | **FAIL** |

## Why it matters more than a wording difference

The section's own rationale says the credential is "Shown as the registration number linking to the live public ICO register entry". A reader cannot check a registration whose number they cannot see, so the built label states a claim and withholds the evidence for it, which is the opposite of what the section was written to do. The number is public and already in the link.

There is a second, smaller consequence. DSRD 6 section 1's chrome carve-out exempts a bare short form in a chrome label from the acronym rule, but the reason it gives is that "the checker tests chrome labels word for word against DSRD 8's registered strings". Applied here word for word, this label fails, so the exemption it was relying on does not reach it.

## The fix, ready to apply

One string in `footer.php`, replacing the link text `ICO Registered` with `Registered with the ICO · ZB662679`. Nothing else moves: the href, the middot, the `aria-hidden`, the `aria-label` and the new-tab behaviour are all already correct.

I have not applied it. The sub-footer renders on every page, so under Rule 3 it is a sweep, and a sweep runs only under a signed brief. One line back authorising it is enough, and I will fold it into the next page's pass with both gates re-run.

*No em or en dashes in this file; checked before writing.*
