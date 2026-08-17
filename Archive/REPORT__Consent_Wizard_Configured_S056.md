# REPORT: the consent wizard, finished and corrected, with one finding that changes how much of it matters

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Follows:** `REPORT__Consent_Plugin_Swap_S056.md`. Same site, same session, after the swap.
**Authority:** Kain, in session. He worked the wizard himself, then handed it over with the words "could I actually just hand this wizard over to you, just to configure, as we need to have it right now."

**Status: configured and verified. Nothing is outstanding, and nothing is waiting on Kain.**

---

## 1. The finding that matters most, because it resizes the whole job

**Complianz generates no policy documents on this site, so most of its wizard feeds nothing.**

The wizard registers **128 required fields**. After Kain's pass, **103 were still empty**, which reads alarming until you ask what they are for. I asked the plugin directly rather than reasoning about it: every one of its four document types resolves to **no generated page**.

| Document type | Mode | What the banner and footer point at |
|---|---|---|
| cookie-statement | `custom` | page 130, Kain's Cookie Policy |
| privacy-statement | `custom` | page 126, Kain's Privacy Policy |
| disclaimer | `custom` | page 142, Kain's Disclaimers |
| impressum | `none` | nothing, correctly |

So the 103 empty fields are the inputs to a privacy statement, an impressum and a set of per-purpose retention clauses that **Complianz is never asked to write**, because Achology writes its own policies and pins the plugin at them. Filling them in would change nothing a visitor can see and nothing a regulator would read.

**This is worth recording in DSRD 3 section 6.5.** Anyone who opens that wizard in future will see 103 unanswered required questions and reasonably conclude the configuration is unfinished. It is not. The right note is that Achology uses its own policy pages, so only the banner, region and blocking questions carry weight.

**One check before writing that.** The commonest reason those fields would matter is a missing data protection contact. Kain's own Privacy Policy page already carries one: it names the controller, gives `support@achology.com`, and routes complaints to the Information Commissioner's Office. Read off the rendered page this session, not assumed.

---

## 2. What Kain answered, and it was right

| Step | Answer | Assessment |
|---|---|---|
| Regions targeted | **United Kingdom and European Union** | Correct, and the two behave identically: both resolve to opt-in |
| Do you compile statistics | **No** | Correct. Verified: no tracker of any kind on any of 303 pages |
| Company details | Achology Transactions Ltd (SC697126), Clyde Offices, country GB, manager@achology.com | His to give, and given |
| Advertising, social media, third party services, first party marketing | all **No** | Matches what the site actually does |
| WordPress comment cookies | **blocked** | Correct |
| Web shop obligation | **No** | Correct |

**On regions, the thing that could have gone wrong did not.** The premium plugin's own upgrade routine writes `regions` as a key map that its own `cmplz_has_region()` cannot read, which took the banner off all 303 pages earlier today. The wizard writes it as a **list of values**, `["uk","eu"]`, which reads correctly. Verified directly: `cmplz_has_region('uk')` and `('eu')` both return true, both resolve to opt-in, and the banner is on every page. **The two forms are not equivalent and only one of them works.** That belongs in the same note as the trap itself.

---

## 3. The two things I corrected, with the reason for each

### 3.1 The impressum was set to generate a German legal notice

The wizard set `impressum` to `generated`. **Set back to `none`.**

DSRD 3 section 6.5, quoted from the canonical file this session:

> "Disclaimer and impressum remain `none` on purpose (the site does not publish those documents), and dnsmpd remains unset because it is the US do-not-sell notice and the configured region is UK; none of the three is a defect."

An impressum is the German legal notice requirement. Achology Transactions Ltd is a Scottish company and `eu_consent_regions` is `no`, which is the setting that governs the German imprint appendix. Left as `generated`, the next document generation run would have published an Impressum page on the site. It had not run yet, so nothing was created and nothing had to be deleted.

**This restores a specified value rather than exercising judgement**, which is why I did it rather than asking.

### 3.2 Location detection was on, which left the rest of the world with no banner

The wizard turned `use_country` back on. **Set back to off.**

With it on, Complianz serves the banner only to visitors it detects inside a targeted region. With the United Kingdom and European Union targeted and nothing else, a visitor from the United States, Canada, Australia or anywhere else would be served **no banner at all**. Off, every visitor anywhere gets the same opt-in banner Kain approved by eye, which is never worse for anyone and leaves one banner to verify rather than several.

This is the second time today that setting has switched itself on: the premium install turned it on, I turned it off, the wizard turned it on again. **It should be treated as a setting that does not stay put.**

### 3.3 One change of Kain's I deliberately left alone, and it needs a document correction

The wizard set `disclaimer` from `none` to `custom`, pointing at page 142, the Disclaimers page.

DSRD 3 section 6.5 says it should be `none` "because the site does not publish those documents". **That parenthetical is now wrong: the site does publish a Disclaimers page, and has since the policy suite was built.** So `custom` pointing at page 142 is more accurate than the recorded state, not less.

It is Kain's own change, made in his own session, and it improves the record rather than damaging it, so I have left it. **DSRD 3 section 6.5 needs correcting to match**, and that is Chat's, not mine.

---

## 4. Verification

Same three instruments as the swap, unchanged, so all of today's readings are comparable.

| Check | Result |
|---|---|
| Configuration dump run twice on the same state | byte identical |
| 303 page sweep run twice | byte identical |
| Banner markup, across 303 pages, against the original pre-swap before state | **0 differences** |
| Theme footer control, across 303 pages | **0 differences**, present on all 303 |
| Scripts held before consent, and trackers in page | **0 differences**, none on any page |
| HTTP status across 303 pages | **0 differences** |

In a browser, on a cleared session, at desktop width:

- Banner appeared on first visit, carrying the theme's own `achology-consent-bar` class and the opt-in variant.
- Buttons read Accept All, Reject All, See Preferences.
- Accept All set marketing, statistics and preferences to allow and dismissed the banner.
- **The footer control reopened it.** Clicked, not read.

**One reading that looked wrong and was not, recorded so nobody re-finds it as a fault.** While the banner is open, the footer control computes to `display: none`. That is Complianz hiding its own reopen control while the thing it reopens is already on screen. The moment the banner is dismissed the control returns to `display: block`. Checked in both states rather than reported from the first one.

**A restore point was taken before any of this**, as a full database export at `~/backups/consent-swap-S056/pre-wizard.sql.gz`, separate from the pre-swap backup.

---

## 5. Two things done after the wizard, from Kain's progress panel, plus one ruling

He showed the plugin's progress panel, five tasks open, and asked which I could deliver. Three were mine.

**The urgent one was the wizard's finish step, and it was not cosmetic.** `enable_cookie_blocker` was empty, and `cmplz_can_run_cookie_blocker()` returns false unless it reads exactly `yes`. **So the cookie and script blocker, the thing that holds third party scripts until a visitor consents, was switched off.** Both finish-step switches are now `yes`, the blocker reports itself able to run, and all 303 pages were swept afterwards with zero differences from the pre-swap before state.

**It was already off before the swap.** Recorded from the before-state file, not from recall. So this is a pre-existing hole in what DSRD 3 section 6.5 calls built and verified, and it is worth Chat knowing that the S047 record covers a mechanism whose blocker switch was never set.

**A test that returned a surprising answer, and the answer is correct.** I fed the blocker a Google tag and a YouTube iframe to prove it blocks rather than merely being switched on. It passed both through untouched. That is right rather than wrong: Complianz blocks the services it has been told the site uses, and the wizard answers say there are none. Its blocked list holds exactly one entry, the Advanced Custom Fields Google Maps embed. **The consequence worth recording: the blocker is not a safety net.** An embed pasted into a page later will not be caught unless the configuration is updated too.

**The integrations warning is closed.** The panel asked for the enabled integrations to be double checked. There is one, the same ACF maps entry. Nothing else was enabled.

### The ruling: no external website scan

Asked whether Complianz should scan the site from its own servers, which requires authenticating the site to a third party, **Kain ruled in session, S056, in his words: "no - leave it for now"**.

Nothing has been authenticated and `cmplz_wsc_status` stays `pending`. **This narrows section 7 of the swap report**, which listed the full site scan among the paid additions worth having: the local cookie scan is still worth running and is a button in the admin, but the externally hosted scan is declined for now and is not to be enabled without a fresh instruction.

The Really Simple SSL item on that panel is a cross-promotion for another plugin by the same vendor rather than a task. Not installed, and it would be Kain's decision under Rule 11 in any case.

## 6. What I would like from Chat

Three corrections to DSRD 3 section 6.5, all from this session:

1. **Record that Achology uses its own policy pages**, so the wizard's 103 unanswered questions are expected rather than an unfinished configuration. Without this, the next person to open it will "fix" something that is not broken.
2. **Correct the disclaimer line.** It now points at the Disclaimers page, which exists, and the reason given for `none` is factually out of date.
3. **Record the regions shape**, alongside the trap already reported in the swap report: `["uk","eu"]` as a list of values works, and the key map form the upgrade routine writes does not. Same setting, two shapes, one of them silently fatal.

*No em or en dashes in this file; checked before writing.*
