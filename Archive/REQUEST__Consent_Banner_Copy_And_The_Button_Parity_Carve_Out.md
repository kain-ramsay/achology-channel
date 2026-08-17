# REQUEST: the consent banner's words, and a carve-out DSRD 7 section 5.1 needs

**From:** Claude Code, S047. **Date:** 2026-08-05. **Version:** v0.38.21, live.
**Follows:** `RULING__Kain_Approved_Installing_The_Consent_Plugin_S047.md`.

Two things: one you need to write, one you need to record.

## 1. The words. This is the only part still wrong, and it is yours

The banner currently shows the plugin's default paragraph, verbatim:

> "To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions."

Fifty-eight words, American spelling, and it reads like a licence agreement. Kain's instruction in session was "we obviously want the words to be as minimal as possible", and the design guidance agrees: keep the message short, link to the policy for the detail, use plain language rather than legal or technical terms.

I have not rewritten it. Rule 8 puts every published word with you, and I am not repeating my S046 breach.

**What is needed:** a heading and one short sentence, plus the three button labels if you want to change them. What is on the buttons now, and why:

- **Accept** and **Decline** are DSRD 3 section 6.5's own words ("equal-prominence Accept and Decline choices"), so I used them rather than the plugin's "Deny".
- **View preferences** and **Cookie settings** are the plugin's and DSRD 3 section 6.5's respectively.

One constraint on whatever you write: the two choices must stay equally plain. Wording that makes declining sound like a loss ("you may lose features") is the same dark pattern as making the button greyer, and the current text does exactly that in its last sentence.

## 2. The carve-out DSRD 7 section 5.1 needs

**What changed and why.** Kain asked whether the banner had been designed against any best practice. It had not, and I told him so. Researching it produced one finding that is not about taste.

The ICO's equal-prominence requirement is not only about size and click count. It covers, in the guidance's words, "colour schemes that don't make one option more appealing", and the practice guidance states it as button parity: same size, same colour contrast, same font weight, same-level placement, with asymmetric prominence named as legally problematic.

Our banner had Accept in solid brand orange and Decline as an outline. That is the asymmetry the regulator has been writing to companies about. **Both buttons now take DSRD 7 section 5.1's secondary treatment and are pixel-identical.**

**The conflict this creates, which is why you need to record it.** DSRD 7 section 5.1's pairing rule says:

> "Where two buttons sit side by side as a pair, they contrast: one primary solid and one secondary or ghost, never two of the same style, so the pair reads as a main action and an alternative."

The consent banner now breaks that rule deliberately. It has to: the whole point is that neither choice is the main action. Without a recorded carve-out, the next person to run a design audit will see two identical buttons, read section 5.1, and "fix" it straight back into a compliance problem.

**Suggested wording, yours to improve:** section 5.1's pairing rule gains an exception for consent and choice interfaces, where a regulator requires the options to be presented with equal prominence, and the pair therefore takes one identical treatment.

## 3. What else changed, for the record

- Placement: the plugin parked the card 10px from each screen edge, which Kain spotted immediately by eye. Now `--sp-xl` on both, and on a phone it becomes a full-width bar at the site's own 20px gutter.
- Shadow: the plugin's hand-typed black shadow replaced by `--shadow-card-hover` (DSRD 7 section 5.4).
- Both changes are in `footer.css` and pass `css_gate`.

## 4. What is verified

Built and driven on the rendered site, not read from the source: the banner appears for a first-time visitor; Decline records deny for statistics, marketing and preferences while functional stays allow, with zero third-party scripts loaded; the choice persists across pages; and the footer "Cookie settings" control reopens it.

One trap worth recording in DSRD 10 for whoever maintains this: the obvious way to add that footer control, the `[cmplz-manage-consent]` shortcode, renders a container the plugin's own script reads as "suppress the banner". In a footer it would have silently stopped the banner appearing on every page of the site. The built control uses the markup the script actually binds to instead.

*No em or en dashes in this file; checked before writing.*
