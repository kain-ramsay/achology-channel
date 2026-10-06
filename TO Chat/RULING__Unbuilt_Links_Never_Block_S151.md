**For Chat: write Kain's S151 ruling on links to unbuilt pages into DSRD 6 (section 11.2, links resolve) and wherever the build-ground rules live (theme session). Asks nothing else.**

# RULING: before go-live, a link to a page not built yet is never a fault (Kain, S151, theme session)

Kain, in the sitting, after Code halted the 150 book note headings over 25 "broken links": "we are building a website from scratch. And the website is not live yet. So there are going to be links that go nowhere. So this problem is just going to keep on coming up ... How do we prevent you from making the same mistake again and assuming that you know links that just simply don't reach a page yet ... are broken?" He said he had explained it in the two sessions before.

What the 25 were: 16 addresses, all pages not written yet. 8 are the Seven Beliefs series (several already pending). 7 are one-off articles. 1 (Aaron Beck) is a real article at a longer address.

What Code changed so it cannot recur:
- `publish_gate.py`: on the build site, a links-resolve fault whose every target is the site's own address answering 404 is carried onto the clearance by name and never blocks an update. An outside link, a server error or a malformed address still blocks, and the live site is unchanged. Tested on five cases.
- Code's memory carries it as a standing rule.
- The go-live check is where every link must resolve.

For Chat's record: the Aaron Beck link in the Cognitive Behavior Therapy book note points at `/learn/psychology/articles/aaron-beck/`; the article is `aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology`. One correct answer; Code corrects it with the headings pass.

OWED BACK: Chat writes the ruling home. Nothing owed to Code.

*No em or en dashes in this file; checked before writing.*
