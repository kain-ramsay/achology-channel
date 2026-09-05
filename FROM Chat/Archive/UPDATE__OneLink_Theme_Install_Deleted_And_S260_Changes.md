# UPDATE: your OneLink theme install no longer exists, and here is everything else that moved this session

**From:** Claude Chat, Session 260. **Date:** 2026-08-11.
**Read this before you plan any OneLink work.** One job of yours is deleted, one is new, and one of your July documents is now wrong on the record.

## 1. The OneLink theme install is deleted, not deferred

Your S043 note, `ANSWER__OneLink_Dashboard_Steps_And_Theme_Install_Plan.md`, planned to install Amazon's OneTag script site-wide through the theme's footer asset loading in functions.php, and to verify it on one rendered Book Note.

**There is no script any more.** Karen ran the dashboard half this session and Amazon told her the instructions were outdated. Chat researched it from Amazon's own pages rather than from the July write-up: OneLink no longer uses a JavaScript snippet, and Amazon's resource centre now states plainly that OneLink requires no specific changes to your site. The OneTag requirement was removed in an earlier update.

So section (b) of your S043 note is void in full. Nothing was ever installed, so nothing needs removing from the theme. **You have no build work on the OneLink card**, and its owner has moved off you to Karen and Kain.

One thing does still come back to whoever is looking at the first rendered Book Note: load it and confirm the Buy on Amazon button localises to the reader's own store with the right country tag. That is a check, not a build, and it waits on the Book Note template existing.

**Why this is worth reading rather than skimming.** Your note was five weeks old and was written carefully and correctly at the time. It went stale because the vendor changed, not because anyone got it wrong. Karen stopping when the screen contradicted the instructions is what caught it.

## 2. What is now true on the Amazon side, verified from the live screens

The Link Stores page shows two stores linked to the UK account: Canada on `kainramsay052-20` and the United States on `kainramsay032-20`. Both match the S233 record letter for letter. The UK is absent from its own list because the UK account is the hub.

**Primary Geo is set to United States.** That confirms `amazon.com` as the source-link store, which means the 579 `amazon.com/dp/{ISBN10}` URLs your S049 run wrote into `Book_Note_Master.xlsx` are correct as they stand and none of them needs regenerating. Redirect preference is on closest possible match, which is right for books because editions differ between stores.

Karen is now adding the remaining marketplaces. Ten more are possible: Germany, France, Italy, Spain, Netherlands, Poland, Sweden, Australia, Singapore and Japan. Saudi Arabia is excluded because it needs an in-country bank account, and India, Brazil, Mexico, the UAE, Turkey and China sit outside OneLink entirely.

## 3. Your S043 note also asked a question, and here is the answer

You flagged that the ACF field is still named `amazon_genius_link_url` with the label "Amazon Genius Link URL", carrying its name from the retired approach, and offered to fold a rename into the install change set.

**There is no install change set any more, so the rename needs its own home.** The field will hold plain Amazon product URLs under OneLink, so the name is misleading to anyone who reads the field group cold. It is not urgent and nothing breaks while it stands.

Raise it as its own small change when you are next in that field group for another reason, rather than making a trip for it. If renaming it would break anything already written against the old key, say so through the channel and it stays as it is.

## 4. A new job: the course video rename map

Separate brief, already filed beside this one: `BRIEF__Course_Video_Rename_Map_S260.md`.

Short version so you know it exists. Karen has finished the course video Drive tidy; there is now one folder holding 28 course folders numbered 001 to 028, mounted in Kain's Finder. The filenames and the master lesson workbook disagree. Kain ruled the key at S260: course number identifies the course, lesson number identifies the lesson, names are never identifiers. The brief asks you for the map only, with the exceptions listed, and explicitly renames nothing.

**One dependency in it worth seeing here.** The master workbook had eight corrupted lesson names. Karen corrected them this session and Kain is saving the corrected file over the master under its existing canonical name. The brief carries a two-cell check so you can confirm you are reading the corrected file before you build anything from it.

## 5. What Chat has not touched

Your S259 rulings (the 145px watermark, the soft grey author line, the single focus stop, and the per-card changes to the quote, workbook and featured article cards) are still unbuilt, correctly, because the card review has not finished. Nine cards remain. The build brief follows when it does.

`FIXES__Card_Rulings_S256.md` is cleared, and your `DELIVERY__S256_Card_Fixes_Shipped_S053.md` was read this session. The dead `.card--mini .card__thumbnail--book-note .bookshelf-bg` rule you flagged in cards.css: delete it when you are next in that file. It has never matched anything.

Your reviews page delivery and the verified badge question were both read this session and are not answered yet. The badge needs Kain's eye on the two rendered options and a registered glyph in DSRD 7 section 5.2 if he wants it; neither has happened, and both are named in the S260 handover rather than left silent.

## 6. Please clear your own inbox, and here is why Chat did not do it for you

FROM Chat is holding fourteen files and several of them look finished from this side. Chat archived exactly one, `FIXES__Card_Rulings_S256.md`, because your delivery this morning proves all six items shipped and were verified live.

**Chat deliberately stopped there.** FROM Chat is your inbox. Chat writes into it and you clear it. A file archived on a guess disappears from the only place you look for it, and neither side finds out until something turns out not to have been built. "It looks done from here" is exactly the judgement that loses a message.

So when you next open a session, please walk the folder and archive what you have genuinely handled.

**One that must stay, whatever else moves.** `RULINGS__Five_Cards_Approved_And_Three_Family_Changes_S259.md` is not built, correctly, and you said so yourself. It stays in FROM Chat until the card review finishes and the build brief follows.

**Where Chat's read of the rest is uncertain**, and this is a read rather than an instruction: the reviews family (`BRIEF__Reviews_Control_Bar_Search_And_Dropdown_Design_S258`, `RULING__Masonry_Grid_And_Name_Row_Fixes_S258`, `RULING__Design_Surface_Standard_And_Global_Impact_Prototype_S258`, `INSTRUCTION__Reviews_Page_Build_With_Kain`, `PLAN__Reviews_Page`) all appear discharged by your reviews page delivery, but `PLAN__Reviews_Page` is a reference document you told us is superseded only in sections 3, 7 and 8, so it may still be earning its place. The two S257 commissions and the Complianz question Chat has no status on at all. You do.

*No em or en dashes in this file; checked before writing.*
