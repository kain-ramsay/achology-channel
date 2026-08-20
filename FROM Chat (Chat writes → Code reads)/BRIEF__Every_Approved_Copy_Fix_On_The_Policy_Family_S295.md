# BRIEF: every approved copy fix on the eight policy-family pages

**DOCUMENT TYPE:** approved brief. Not a page spec. **From:** Claude Chat, Session 295. **Date:** 20 August 2026.
**Approved by Kain, S295.** Nothing here is open to judgement.
**Exempting line added S296**, answering `REFUSAL__The_Five_S295_Copy_Fix_Briefs_Carry_No_PAGE_GATE_Line_S076.md`. This file names word-level before-and-after corrections on pages that already exist. It sets no block order, no arrival state, and no copy anybody is deciding for the first time, so it is not a page spec and the intake tripwire may pass it.

**One file for the whole family**, because the faults recur across pages and dribbling them
out one at a time is how a set drifts. Chat read all eight remaining policy pages in a single
batch and ran DSRD 6 §1, §2 and §6 across the set; the per-page findings live in each page's
own `DSRD6_RECORD.md`.

**Scope:** copy only. **No layout, no styling, no structural change, and no machine line in
any record.**

---

## The single most useful thing in this file

**One contrast failure is the same fault on every page in the family.** `.policy-endnote`,
the shared policy footer, fails axe with a serious colour-contrast violation on the cookie
policy, privacy policy, refund policy, disclaimers, trust statement, accessibility statement
and terms. **It is one fix, in the shared template, not eight.** It is not commissioned here
because it is a design value and belongs to Kain's eye, but it should be raised as one item
rather than seven.

**It also means the Accessibility Statement currently fails an accessibility scan**, which is
the site's own counter-example and worth fixing early for that reason alone.

---

## Change 1: cookie policy, two fixes

`policies-content/cookie-policy.php`.

**One, GDPR and UK are both unexpanded.** Section 4's opening sentence.

**Current:** ...as required by UK law (the Privacy and Electronic Communications Regulations and UK GDPR).

**Becomes:** ...as required by UK law (the Privacy and Electronic Communications Regulations and the United Kingdom General Data Protection Regulation (UK GDPR)).

**Two, "Knowledge Hub" is unidentified.** Section 6, the book-links bullet.

**Current:** some book recommendations on our Knowledge Hub link to Amazon through affiliate links

**Becomes:** some book recommendations on our Knowledge Hub, the free library of articles, book notes and quotes on this website, link to Amazon through affiliate links

## Change 2: privacy policy, the member identification

`policies-content/privacy-policy.php`, section 9's first sentence.

**Current:** When you register as a member of the Achology community, certain profile information will be visible to other members.

**Becomes:** When you register as an Achology member, joining the private learning community at community.achology.com where members can collaborate to practise the skills taught in their courses, certain profile information will be visible to other members.

**The rest of section 9 is unchanged.**

## Change 3: trust statement, the member identification and the global crisis route

`policies-content/trust-statement.php`.

**One, section 5's first line.**

**Current:** Achology operates as a collaborative learning community. This means:

**Becomes:** Achology operates as a collaborative learning community: a private learning community at community.achology.com where members can collaborate to practise the skills taught in their courses. This means:

**Two, section 3's closing sentence.** See Change 4 for why.

**Current:** If a learner recognises that certain material or discussions are personally destabilising, the ethical response is to pause, seek appropriate support elsewhere (organisations such as Samaritans offer immediate, confidential help), or disengage, not to assign responsibility to an educational provider. Contact details for crisis and mental-health support are listed in our Disclaimers.

**Becomes:** If a learner recognises that certain material or discussions are personally destabilising, the ethical response is to pause, seek appropriate support elsewhere, or disengage, not to assign responsibility to an educational provider. In the United Kingdom, Samaritans offer immediate, confidential help. Outside the United Kingdom, you can find a free, confidential crisis line in your own country at findahelpline.com, which lists verified helplines in over 130 countries. Further crisis and mental-health contacts are listed in our Disclaimers.

**Keep the existing links** on Samaritans and on Disclaimers, where they already sit. **Add
one outward link on the words "findahelpline.com"**, to `https://findahelpline.com/`, in a
new tab with `rel="noopener"` per DSRD 3's external-link standard.

## Change 4: disclaimers, the NHS expansion and the global crisis route

`policies-content/disclaimers.php`, section 2's third paragraph.

**Current:** In the UK: call 999 in an emergency, contact NHS 111 for urgent medical advice, or call Samaritans on 116 123 (free, 24 hours) if you need someone to talk to. Outside the UK, contact your local emergency services or a crisis line in your country.

**Becomes:** In the UK: call 999 in an emergency, contact the National Health Service (NHS) 111 service for urgent medical advice, or call Samaritans on 116 123 (free, 24 hours) if you need someone to talk to. Outside the United Kingdom, contact your local emergency services, or find a free, confidential crisis line in your own country at findahelpline.com, which lists verified helplines in over 130 countries.

**Keep the existing links** on NHS 111 and Samaritans. **Add one outward link on
"findahelpline.com"**, to `https://findahelpline.com/`, new tab, `rel="noopener"`.

**Why NHS needed expanding.** §1's outside-terms clause exempts common public terms from the
identification but still requires the full name, and this page states in section 10 that
Achology serves students worldwide. A reader in one of the other 215 countries was meeting an
unexplained three-letter body in a crisis sentence.

**Why the global route was added.** Kain raised it himself: the old sentence told a reader in
distress to find something without saying where to look. Find A Helpline was checked live
this session: a public service by ThroughLine, verified relationships with helpline
organisations in over 175 countries, key partners the International Association for Suicide
Prevention and LifeLine International. **A static list of numbers on our own page was
rejected outright: numbers go stale, and a stale crisis number is worse than none.**

## Change 5: policies index, the member identification, IN TWO FILES

**This one lands in two places or it drifts immediately.**

The visitor-facing page is `template-policies-index.php`. `policies-content/policies.php` is
the analyser feed, never rendered, and its own docblock instructs that the two are kept in
step by hand. **Both carry the governance paragraph, identically, today.**

In **both files**, the governance paragraph's final sentence.

**Current:** All these documents are accessible on this page, written in clear language for anyone to review at any time.

**Becomes:** All these documents are accessible on this page, written in clear language for anyone to review at any time, whether or not you are an Achology member: someone who has joined the private learning community at community.achology.com.

**Nothing else in either file changes**, and the row descriptions stay one line each.

---

## Where the member wording comes from

Every member identification above is taken from the entry added to **DSRD 2 §2.24's locked
term register** this session, approved by Kain word for word. **The register is the source
and these lines apply it.** If a line and the register ever disagree, the register is correct.

The same entry drives the About-family fixes in
`BRIEF__One_Approved_Line_On_The_About_Page_S295.md` and
`BRIEF__Two_Approved_Lines_Manifesto_And_Code_Of_Ethics_S295.md`.

## Three record faults for you to fix, all machine-written

1. **The Policies Index record's Template line is wrong.** It reads
   `policies-content/policies.php`, which is the analyser feed and is never rendered. The
   page a visitor meets is `template-policies-index.php`. Chat could not judge the page until
   it found the right file.
2. **The Terms and Conditions record's §10 row is malformed.** It reads
   `| 10 | Visual consistency | machine + Kain's eye | not run | policy-body): no hairline, gap 0.0px |`,
   with a fifth cell carrying the tail of a truncated failure message beside a "not run"
   state. Broken as a table and ambiguous as a record.
3. **Two §1 machine verdicts are disputed as false positives**, on the privacy policy and the
   accessibility statement. Both are set out in
   `ASK__The_Acronym_Check_Looks_Inverted_S295.md`. **Neither line has been touched.**

## Two commitments the launch must not pass quietly

Neither is a copy fault and neither is commissioned here; both are recorded so they are not
lost.

- **The accessibility statement promises a full accessibility assessment** as part of the
  rebuild, and carries an empty "known limitations" section awaiting it. Honest today, false
  the day the site launches without it.
- **Two clauses in the Terms carry build notes saying a solicitor should confirm them before
  launch**: the cooling-off waiver in section 8 and the auto-renewal term in section 3.

## What NOT to do

- **Do not change any page's structure, spacing or styling.** Copy only.
- **Do not fill or clear any judgement line in any `DSRD6_RECORD.md`.** Chat writes those.
- **Do not raise the accessibility statement to WCAG 2.2.** It commits publicly to 2.1 while
  the internal bar is 2.2, and that pairing is deliberate, ruled at S233 and stated in DSRD 6
  §7 as something no audit should flag.
- **Do not touch the duplicated "Final Position" section** shared word for word by the
  disclaimers and the trust statement. It is raised with Kain and not ruled.

## What to return

All eight rendered pages through TO Chat, and §1's machine half re-run against each **after**
the acronym check is settled, so the two halves are measured with the same ruler.

*No em or en dashes in this file; checked before writing.*
