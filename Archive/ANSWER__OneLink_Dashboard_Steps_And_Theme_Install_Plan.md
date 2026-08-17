# ANSWER: OneLink dashboard steps and the theme install plan (S043, 30 July 2026)

Context, standalone: Karen's three account facts arrived via ANSWER__OneLink_Three_Account_Facts_From_Karen.md (S233). Achology is enrolled in the UK, US and Canada programmes; the tags are kainramsay01-21 (UK), kainramsay032-20 (US), kainramsay052-20 (Canada); OneLink is not yet set up. This is the write-back you asked for: (a) the dashboard half for Kain or Karen in click-by-click language, and (b) what I will then install in the theme and where, per the Amazon OneLink Install card.

Three facts I verified this session before writing the plan, so nothing below is assumed:

1. The theme holds exactly one Amazon reference today, a plain help link to Amazon's cookie help page inside the Cookie Policy body. There are no affiliate links anywhere in the theme code.
2. The Book Note button comes from the field group "Book Note Fields", field amazon_genius_link_url (label "Amazon Genius Link URL"). No template renders that field yet; the button itself lands with the Book Note template build.
3. On the build site, that field is empty on every entry. There are no existing links to convert or migrate. OneLink can go in clean.

One flag for you before the install: the field still carries its Genius Link name from the earlier approach. Under the OneLink decision it will hold plain Amazon product URLs. It works as it is, so I am not touching it; if you or Kain want the field relabelled to match reality, say so and I will fold it into the install change set.

## (a) The dashboard half, for Kain or Karen, about ten minutes

The plan assumes the Book Note buttons will point at amazon.co.uk product pages, the home store for a Scottish company, which makes the UK account the home account and the UK dashboard the place to run the setup. If the intention was ever amazon.com links instead, tell me before the install; the linking steps below still stand either way.

1. In a browser, go to affiliate-program.amazon.co.uk and sign in with the UK Associates account, the one whose tracking tag is kainramsay01-21.
2. In the menu bar across the top of Associates Central, click Tools, then OneLink.
3. On the OneLink page, click the button that offers to link your accounts (Amazon words it as "Link your accounts" or similar).
4. A list of Amazon marketplaces appears. Choose United States. Amazon asks you to sign in with the US Associates account, the one whose tag is kainramsay032-20, and approve the link. Sign in and approve.
5. Do the same for Canada, signing in with the Canadian Associates account, tag kainramsay052-20, and approving.
6. Back on the OneLink page, check that all three marketplaces now show as linked, and that the tag shown beside each one matches the three tags above exactly, letter for letter. If any tag on screen differs from what Karen supplied, stop there and tell me which one before anything else happens. This is the sanity check you asked for, done where the truth lives.
7. Amazon then shows a short piece of website code on the OneLink page. Nobody needs to install anything: select the whole code box, copy it, and either paste it straight to me in a Code session or save it in a TextEdit note on the Desktop and tell me it is there. I collect it and do the rest.

That is the entire dashboard half. Nothing else on the Amazon side.

## (b) The theme half, mine, once the code arrives

What I will install: the exact script Amazon supplies, added once, site-wide, through the theme's existing footer asset loading in functions.php, so it prints on every page just before the closing body tag, which is Amazon's recommended placement. Site-wide coverage means the Book Note template inherits it the day it is built, and any future page carrying an Amazon link is covered without another install. On pages with no Amazon link the script does nothing.

What stays untouched: the Book Note button keeps a plain Amazon product URL with no tag bolted on. OneLink applies the right country tag itself and sends US and Canadian readers to their own store; UK readers pass straight through on the UK tag.

Definition of done from the card, and how each part lands:

1. Every Amazon link localised: the site-wide footer script covers every template. I will confirm the script loads on one page from each template family after install.
2. The Book Note button on the plain Amazon URL: that is how the field will be filled, and there are no legacy values to clean, verified above.
3. Localisation verified on one rendered Book Note: the moment one Book Note holds its URL and renders, I load it in a browser, confirm the script runs and the button resolves correctly, and file the evidence here.

The install runs as its own declared change set under the harness once the code arrives, committed before and after, and nothing ships unverified. Until the dashboard half is done and the code reaches me, the card stays blocked on the Amazon side only; the theme side is ready and waiting.

No em or en dashes in this file, checked before writing.
