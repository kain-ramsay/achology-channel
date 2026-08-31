# RULING: the Policies page takes the card band, and its header copy is Kain's own

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Authority:** Kain, in session, in Safari, on the whole rendered page.
**Shipped:** theme v0.120.0 through v0.121.0, deployed, all three deploy proofs current.
**Filed under:** Harness Rule 14.

---

## 1. The card band, approved on the rendered page

**He asked for it in his own words:** "on the Achology's Policies and Standards page, please apply our principle that lets cards sit outside the container be applied to the different policy cards."

**He approved it in his own words, looking at the whole page in Safari:** "Yes, it does. Its possibly the best looking policies page I've ever seen."

**Nothing was designed to do it.** It is DSRD 7 section 4.4, the locked inset panel width, applied to a page that did not yet follow it. Quoted from the canonical file, read this session: "the 880px article column plus a 32px (`--sp-xl`) bleed each side, built as `margin-inline: calc(-1 * var(--sp-xl))` with matching 32px inner padding, so content inside the panel returns to exactly 880px."

**What it fixed, measured before and after on the live page.** Every heading and paragraph on the page starts at 280 at desktop. Each card also started at 280 and carried 24px of its own padding, so the words inside the card began at 305. The page had two left edges 25px apart. The card now reaches 32px further out on each side and holds 32px inside, so its words land back on 280.

**Read back off the live page after deployment, at three widths:**

| Width | The card | The page's writing | Sideways scroll |
|---|---|---|---|
| 1440 | left 248, width 944 | h1 at 280; card text at 281 | none |
| 1039, just under 4.4's boundary | left 80, width 880 | h1 at 80, width 880, flush | none |
| 390 | left 20, width 350 | flush with the h1 | none |

**The 1040 boundary is section 4.4's own and was not chosen here.** Below it the bleed is off, so nothing changed on a phone or a tablet.

**What this is for you.** Section 4.4 describes the mechanism but names no page that uses it. The Policies index is now one, ruled by Kain on a render, and DSRD 9's section for this page should say so.

---

## 2. His rewritten header copy, given whole, in session

He handed both paragraphs and they are set verbatim in `template-policies-index.php`. The page carries no excerpt, checked on the install, so the template default is what every visitor reads.

**Rule 8 keeps Code out of drafting page copy and this does not breach it:** nothing was written here. His words were placed and read back off the live page word for word.

**One punctuation substitution, made openly and told to him in session.** His second paragraph arrived with an em dash before "someone who has joined". DSRD 2 section 3.0, his own S222 ruling, bans it "anywhere in Achology copy ... with no exception", and the gate refuses a file containing one. It is a colon, which is what that same sentence already used. Not one word changed. He was told and can overturn it.

**The copy, as it now stands live, for whichever document owns this page's content:**

> This page outlines the rules, policies and standards that govern Achology, including our legal policies, business practices, and the timeless principles we hold ourselves (as a training organisation) to. All our policies are transparent and publicly accessible, so you always know where you stand with us.

> Achology is owned and run by its remaining original founders, Kain and Karen Anne Ramsay, through two registered companies in Scotland, UK. Achology adheres to best practices for public trading and is supported by seven legal policies, a Manifesto, and a Code of Ethics that oversee its online teaching and mentorship activities. All these documents are available on this page, written in clear language for anyone to review at any time, whether or not you are an Achology member: someone who has joined the private learning community at community.achology.com.

---

## 3. Two outbound links, in the second paragraph only

He asked for "two relevant external links that open in a new tab ... but only in the second paragraph".

**Neither was invented and both were fetched and read back before shipping.**

| The words | Where they go | Why that one |
|---|---|---|
| two registered companies in Scotland, UK | the Companies House record for SC697126 | opened this session and its heading read: "ACHOLOGY TRANSACTIONS LTD." The number is not new copy; the Privacy Policy and the Terms and Conditions already publish it |
| best practices for public trading | tradingstandards.uk | the Chartered Trading Standards Institute, which the Disclaimers page already links for this exact idea |

Both carry `target="_blank"`, `rel="noopener"`, and a visually hidden "opens in a new tab", verified on the rendered page as genuinely hidden at 1px and clipped.

**A fault found by reading the page back rather than by any gate, and worth your attention because it is a gap rather than a slip.** The two links shipped in the browser's default blue with a heavy underline. `.policy-header__copy` sits in `.policy-header`, not `.policy-body`, so it was outside every link rule on the page; it had never carried a link, so nothing had ever exposed that. The locked sitewide body-link treatment, Kain's own of 2026-07-14, was extended to it verbatim in v0.120.3. No new value was chosen.

**One gap named rather than quietly filled.** DSRD 7 section 1.0 asks for a visible outbound marker on external links, and **no policy page carries one today.** The only sized marker in the theme is `bn-ext`, which belongs to the book note. Inventing a second is a visual decision and therefore Kain's, so these two links took the shape the Disclaimers page already uses. **That is a real question for him, and it is now the only thing outstanding on this page.**

OWED BACK: the DSRD 9 section for the Policies page updated with the card band and this copy; section 4.4 gaining the Policies index as a named user; and a decision, when convenient, on the outbound marker on policy pages.

*No em or en dashes in this file; checked before writing.*
