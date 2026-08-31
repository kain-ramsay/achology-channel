> **CHAT DISPOSITION, S324:** read in full. Its three travelling findings (the field-authority exemplar's heading level, the two book note fields with no source, the instalments help article) are Chat's and are named in the S324 handover's register for the next website session. Stays until that session acts on them.

# SESSION REPORT: S090

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**What this session was:** the backlog session Kain ruled at S089, run in the order he approved. No new work was taken on.

Assembled from the version control log of the three repositories, plus the hand-added lines marked as such at the foot.

---

## Finished

| What was finished | Board card |
|---|---|
| The eighteen master slugs read out of the Book Note master and returned. Thirteen found, five named as absent. `REPLY__The_Eighteen_Master_Slugs_S090` | Book note production |
| The three S320 course page questions answered: the lecture rows, the real checkout terms, and the S185 question wordings. `REPLY__The_Three_S320_Course_Page_Questions_S090` | Course page |
| The confirmed book note column contract, read out of the template. `REPLY__The_Confirmed_Book_Note_Column_List_S090` | Book note production |
| The route for the S079 captures, measured rather than reasoned. `REPLY__The_Route_For_The_S079_Captures_S090` | Page readiness records across every built page |
| The folder map generator pointed at the project root, and every map regenerated | Folder navigation and map currency |
| `content_gate.py` taught to read `section_count`, with acceptance | Content gate |
| The redirect workbook's column governance sentence written in | Redirect map |
| All fourteen testimonial videos whitelisted over the Vimeo API, read back per video. `REPORT__The_Fourteen_Testimonial_Videos_Whitelisted_S090` | Video Testimonials page |
| Kit's plugin installed, check one fully answered. `REPORT__The_Two_Kit_Plugin_Checks_S090` | Plugins and site configuration |
| The image and icon machinery, both halves, built and first run. `REPORT__The_Image_And_Icon_Machinery_S090` | Image and icon optimisation |

**Ten instructions came off the channel, head-lined DONE and archiving with this close.**

## Started and not finished

| What | What remains |
|---|---|
| The machine-two ssh key file, `machine-two/move-onto-ssh-key.command`. Built, syntax checked, and its ssh command shape proved on this machine | **Kain double clicks it.** Nothing else. Until he does, the Chat machine is still on the keychain login |
| Kit's plugin, check two | **Kain connects the Kit account**, one OAuth click in the WordPress admin. Everything up to that point is source-proved |
| The S306 ruling's other two items | Both need Kain's eye, not Code's hands: the mid-grey supporting-line sweep across the course card, and the Enrol Now colour options rendered in Safari |

## Deliberately not touched, on Kain's instruction at the open

The policy page widths, 620 to 880, and the four content templates. Both need his eye on one rendered page first.

## The session did not end where this report first said it did

**This section originally read "no theme version bump and no deploy", and it was true when it was written.** Kain then asked for the chrome sitting immediately rather than next session, and the session ran on for four sittings and eight ships. **A report that says nothing shipped when eight versions shipped is the exact drift Rule 13 exists to prevent**, so it is corrected here rather than left standing, and the correction is named rather than made quietly.

### The four chrome sittings, all closed

**All four chrome components are now signed**, which is what eleven Knowledge Hub page designs were waiting behind.

| Sitting | Outcome | Board card |
|---|---|---|
| 2, the breadcrumb | Holds as built. **Two documents are wrong** and the correction is yours: DSRD 8 §25 and DSRD 9 §27 both say the 1200 page frame, and the trail has never done that on any page. `RULING__The_Breadcrumb_Holds_As_Built_And_Two_Documents_Are_Wrong_S090` | Cards and chrome sweep |
| 3, the Where next panel | Holds as built. **The duplication case does not exist**: one component, two ruled variants, two lines of page spacing. `RULING__The_Where_Next_Panel_Holds_And_Is_Not_Duplicated_S090` | Cards and chrome sweep |
| 4, the site-wide footer | Holds as built. **A sixth social button nobody ever ruled was found on all 27 templates and removed.** `RULING__The_Footer_Holds_And_An_Unruled_Sixth_Social_Button_Is_Removed_S090` | Cards and chrome sweep |

Each left behind its prototype, its data file with a gate block, its folder README and its ruling, as the S282 commission requires.

### The page work Kain asked for directly in the sitting

Listed here because work he asks for in the room never travels the channel on the way in, so this report is its only route out.

| Shipped | What |
|---|---|
| v0.120.0 | His rewritten Policies and Standards header copy, both paragraphs, given whole |
| v0.120.1 | His tightened first paragraph on the same page |
| v0.120.2 | Two verified outbound links in that page's second paragraph only |
| v0.120.3 | The Policies header paragraph takes the locked body-link treatment |
| v0.121.0 | **The Policies cards take the locked inset panel band**, DSRD 7 §4.4 applied to a page that did not follow it. His words on seeing it: "possibly the best looking policies page I've ever seen" |
| v0.121.1 to v0.121.5 | His About lead paragraph, five wordings in the same sitting. The fifth is live |
| v0.122.0 | His rewritten purpose panel on the About page, both paragraphs |
| v0.123.0 | The unruled sixth social button removed |

Every one was deployed, and every one was read back off the live page word for word rather than trusted to the upload.

### Three findings from that half of the session

**One. The Policies header paragraph sat outside every link rule on the page.** Kain's two outbound links shipped in browser-default blue with a heavy underline. It had never carried a link, so nothing had ever exposed it. Found by reading the page back, not by any gate. The locked sitewide body-link treatment was extended to it verbatim.

**Two. A gate refused approved work and was right to.** The intake tripwire refuses a page edit with no signed spec. The S266 ruling types a copy substitution at an existing call site as exempt and names `page-about.php`, but that ruling is the document that CREATED the type-line practice, so it predates its own rule and carries no type line. **Nothing was switched off.** A waiver row was added to `spec_intake_waivers.md` naming what it waits on, beside the row its sibling document already has. It prints loudly on every run until Chat writes one line into that file.

**Three. `page_artefact.py` can capture nothing and report success.** A capture of `/privacy-policy/` wrote a 39 byte empty page and printed a success line with file sizes beside it. The tool does not check that it captured anything. The prototypes filed this session are captures that were opened and read back.

---

## Three findings that travel, because none of them is Code's to fix

**One. The frozen `field-authority-article` exemplar loses its own body to the gate.** It writes its body sections at `##`, the same level as the record's structural headings, where every other content type uses `###`. `extract_body()` therefore ends the body at the first section heading and measures **195 words of a 2,414 word file**. Every check downstream of that measured the hook alone. It is a record fix and it is Chat's. It would have hit all 154 Salvage articles.

**Two. Two of the ten book note template fields have no source anywhere.** `author_website_url` and `goodreads_url` are read by `single-book_note.php` and each guards a link, and neither is held by any column in the master or any field in any record. Both checked this session. So it is a decision, not a rename.

**Three. The live help article on instalments understates what the till offers.** It says "two, three or in some cases four monthly payments". The checkout offers up to five on a single course, six on a bundle and twelve on Access All Areas. That is wrong rather than merely vague, and it is published.

## One waiver, recorded rather than worked around

H9, the publishing wall, refuses every `wp eval` and `wp eval-file` at the install, because it cannot read what such a command would do. It also refused a read-only probe this session that wrote nothing. The same facts were obtained through read-only `wp option get`, `wp post list` and source reads instead. **No check was weakened and nothing was switched off**, and it is recorded because a harness that refuses approved work should leave a trace rather than a silent detour.

## Hand added, with no machine record behind them

- The Vimeo API pass touched no file in any repository. Its proof is the per-video read-back in its own report.
- Kit's plugin was installed on the server, which no local repository sees.
- The two Kit checks' evidence came from reads of the live install and of two plugins' source on the server.
- The three-page first run of the media checks produced no committed artefact; its findings are in its own report.

*No em or en dashes in this file; checked before writing.*
