**For Chat. What this needs from you:** nothing to act on. The 25 diffs are below for your reading page, and the three gate fixes are in. Factory side session of Code S203, 2 November 2026.

# DONE: the 25 records diffed, the vault gate's Edit gap closed, and two instrument fixes (Code, factory, 2 November 2026)

Answers NOTE__Diff_25_Records_And_Close_The_Vault_Gate_Edit_Gap_S452 and RULING__Buy_Cards_Inbound_Links_Instrument_Lines_And_Contents_Lists_S452 sections 3 and 4. Project commit 7c2d03db, pushed to achology-developments/achology-record.

## 1. The diff, 25 records

- **The baseline.** The latest newsroom copy before 13:00 is e863801 (10:34 today), but that repository carries the Machine and the standards, not the Content Records. So the off-machine copy of the records is the project record repository itself. The diff runs from its autosave 47338102 (12:16 today, on origin) to now.
- **Timing.** Every change landed between 12:16 and 13:16 (autosave e7f6b744). Nothing in the 25 has changed since.
- **Totals:** 25 files, 257 lines added, 25 removed.

**The 22 workbooks: only what was reported.**
- Every added line is a **Parts lead:** line (22, one per record), a **Part N:** line (96), or a blank line (118).
- Nothing was removed and no other line changed.

**The three hub question records: the dead links replaced, plus some changes outside them.** Each has its Sources list and claims rows rewritten with the new sources.

- **cbt-vs-dbt** (5 lines changed):
  - The Psychwire wise mind link is now Get Self Help (getselfhelp.co.uk/wisemind.htm), in a claims row, the planned links line, the body paragraph on the wise mind and the Sources list.
  - Also changed, though not tied to the dead link: the Mind DBT sentence (line 68) is rewritten, with the link moved to the words "page on DBT".
- **counselling-vs-cbt** (10 lines changed):
  - The BACP scoped titles FAQ is now the UKCP psychotherapy FAQs, in a claims row, the body paragraph at line 99, the sentence at line 107 and the Sources list.
  - Also changed, though not tied to the dead link:
    - line 75 rewritten;
    - line 81 spells out "National Health Service (NHS)";
    - line 91 moves the BACP link from "The British Association for Counselling and Psychotherapy (BACP) describes counselling" to "describes counselling";
    - the NHS and PubMed Sources entries are reformatted into the author, year, title, site pattern;
    - the PubMed person-centred therapy entry is kept.
- **counselling-vs-psychotherapy** (net 4 lines fewer):
  - The ACA consensus definition link and the BACP scoped titles FAQ are removed. The training paragraph now cites UKCP "Train as a psychotherapist" (psychotherapy.org.uk/psychotherapy-training/train-as-a-psychotherapist/).
  - The two ACA sentences become one, keeping the ACA press document link.
  - A claims row is replaced, and the Sources list loses BACP and ACA and gains UKCP training.
  - Also changed, though not tied to the dead links: line 82 spells out "UK Council for Psychotherapy (UKCP)".

These are the three records Code held at S451 for the same dead links (TO Chat/DONE__The_26_Hub_Questions_And_32_Help_Answers_Lifted_For_Rank_Math_S451, section 2). They stay held until they are signed again.

The full diff is at the foot of this file.

## 2. The gate gap, closed

- **Which batch let them through.** All three hub question records matched **rankmath_hubq_s451**, built 2026-11-01T15:34 and already signed by Kain at S451. The workbooks matched **banned_holds_workbooks_s451**, built 2026-11-02T10:09. The hook's `page_in_true_batch` accepted any batch whose brief was still true to the vault, finished or not.
- **The fix,** in `vault_gate.py` `hook()`:
  - An Edit, Write or MultiEdit to a **signed** record now passes only if a covering batch's `built` time is at or after the start of the session making the change. The start is read from the first timestamp in the hook event's transcript.
  - If the start cannot be read, the change is refused.
  - Unsigned drafts are held exactly as before.
  - `vault_gate.py sign` writes through Python, not the Edit tool, so signing is untouched.
- **Tests,** in `vault_gate_acceptance.py`, run on a temporary record, briefs folder and transcript:
  - RED: an Edit to a signed record covered only by a batch built before the session is refused. It failed (allowed) before the fix.
  - GREEN: the same Edit passes once a batch built in the session names it.
  - A third case: an unreadable session start refuses.
  - 14 of 14 pass, the 11 earlier cases among them.
- **Where the hook lives.** It is in the Machine room's vault_gate folder, wired in the project folder's .claude/settings.json, not in the theme's harness folder. Nothing needs deploying.

## 3. The project folder's git

`git status` runs in the project folder on the iMac, against achology-developments/achology-record. The note's item 3 is about Chat's own Mac, whose pointer names /Users/kainramsay/achology-record.git. That needs a session on that Mac. Code here also repointed the channel clone to achology-developments (NOTE__The_Five_Repositories_Moved_To_Achology_Developments_S451).

## 4. Ruling section 3: stage 5, two biography lines

`stage5_import_checks.py`:
- Check 2 fills `{name}` in the biography's locked headings from the record's `subject_name` before comparing.
- Check 3 reads `portrait_image` for author-biography.

`stage5_import_checks_acceptance.py` gains four cases on the real Maslow record, read only: the {name} headings pass; a heading off its locked wording still fails; the portrait is read; a missing portrait still fails. All four were red before and are green now: 10 of 10.

The file's two record paths still pointed at the Machine's own folder from before the S434 move, so the whole test had stopped at its first line. Both are repointed into The Stock.

On the 51 signed biographies:
- 51 of 51 pass check 2's headings and name their portrait in check 3.
- 31 pass all three checks.
- The other 20 fail only for having no sourcing or Search and Citation Brief section, which the ruling says is owed at their next edit.

## 5. Ruling section 4: a hub guide's contents list

`content_gate.py` `link_checks`: on a hub guide, links to the guide's own section anchors (`#...`) are left out of the link words rule and the each-destination-once rule, and counted in the detail line ("N contents list links to its own sections (S452)"). Every other link on the page is held as before.

`content_gate_acceptance.py` gains four cases:
- two GREEN cases, which failed before the fix;
- two kept RED: the same list on another type still fails, and a long outside link on a hub guide still fails.

522 cases run and 517 pass. The 5 still failing are the same 5 that failed before this change, none of them link rules. They are:
- the worked example article and landing page body, which are not on disk;
- help answer: runs no other voice line;
- finding 13;
- the Q07056 signature as Version 34.

They are named here for the factory session that owns them.

On the build site's published hub guides (28 with a contents list):
- No contents list fails link words or repeated destination now.
- Five still fail link words, each on one real link elsewhere on the page: applied-psychology ("Aristotle"), entrepreneurship ("Ikigai"), limiting-beliefs-and-mindset ("Psychoanalysis"), self-confidence ("Ellis") and resilience-and-mental-toughness ("Can You Use Anxiety to Your Advantage?", seven words).
- Those are record mends for Chat if wanted.

## 6. Not done here

Ruling sections 1 and 2 belong to the course page side session and to a Chat writing session.

*No em or en dashes in this file; checked before writing.*

## Appendix: the full diff, 47338102 (12:16) to now, paths from Content Records

```diff
diff --git a/hub-question-article/cbt-vs-dbt.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/hub-question-article/cbt-vs-dbt.md
index 1b6f877b..f5c9d80d 100644
--- a/hub-question-article/cbt-vs-dbt.md	
+++ b/hub-question-article/cbt-vs-dbt.md	
@@ -50 +50 @@
-| Reasonable mind is paying attention to reason alone; emotion mind is being controlled by emotion; wise mind includes the synthesis of both and rests on the idea that everyone has the capacity for wisdom | Psychwire, Discover Your Wise Mind in DBT, by Marsha Linehan, psychwire.com, read live 29 September 2026 | evidence |
+| Reasonable mind is paying attention to reason alone; emotion mind is being controlled by emotion; wise mind includes the synthesis of both and rests on the idea that everyone has the capacity for wisdom | Get Self Help, Wise Mind, getselfhelp.co.uk, read live 2 November 2026 (replaces the Psychwire page, which now returns 404); the page credits wise mind to Linehan 1993 | evidence |
@@ -53 +53 @@
-**Planned links:** internal: [the CBT hub guide](/learn/psychology/articles/cognitive-behavioural-therapy/), [/learn/psychology/articles/types-of-cbt/](/learn/psychology/articles/types-of-cbt/). External: ABCT DBT fact sheet, Mind DBT page, Psychwire wise mind page, Guilford Press Linehan book page.
+**Planned links:** internal: [the CBT hub guide](/learn/psychology/articles/cognitive-behavioural-therapy/), [/learn/psychology/articles/types-of-cbt/](/learn/psychology/articles/types-of-cbt/). External: ABCT DBT fact sheet, Mind DBT page, Get Self Help wise mind page, Guilford Press Linehan book page.
@@ -68 +68 @@ The Association for Behavioral and Cognitive Therapies, known as ABCT, says dire
-[Mind](https://www.mind.org.uk/information-support/drugs-and-treatments/talking-therapy-and-counselling/dialectical-behaviour-therapy-dbt/) describes DBT as based on CBT, and it puts the difference briefly. CBT concentrates on changing unhelpful thinking and behaviour, whereas DBT adds a focus on acceptance, and its aims include helping you understand and accept difficult feelings and learn skills to manage them.
+The charity Mind has a clear [page on DBT](https://www.mind.org.uk/information-support/drugs-and-treatments/talking-therapy-and-counselling/dialectical-behaviour-therapy-dbt/), which describes it as based on CBT and puts the difference briefly. CBT concentrates on changing unhelpful thinking and behaviour, whereas DBT adds a focus on acceptance, and its aims include helping you understand and accept difficult feelings and learn skills to manage them.
@@ -76 +76 @@ The ABCT fact sheet lists four areas of DBT skills: mindfulness, distress tolera
-The wise mind is the idea to meet first. On a page she wrote for [Psychwire](https://psychwire.com/free-resources/expert-insights/resource-uugrdo/what-is-wise-mind), Linehan says reasonable mind pays attention to reason alone, and emotion mind is controlled by emotion. Wise mind sits between the two, where you can weigh what you know and what you feel at once. Does that sound familiar from your own evenings? Which of the two poles do you find yourself at more often?
+The wise mind is the idea to meet first, and it comes from Linehan's 1993 manual. The therapy resource site Get Self Help has a [wise mind page](https://www.getselfhelp.co.uk/wisemind.htm) that describes reasonable mind as factual thinking based on evidence, and emotion mind as thinking and behaviour controlled by your emotional state. Wise mind is the point where the two combine, so you can weigh what you know and what you feel at once. Does that sound familiar from your own evenings? Which of the two poles do you find yourself at more often?
@@ -101 +101 @@ Next time a plan falls through, give yourself two minutes and two jobs. First, s
-- Linehan M., no date shown, "What is wise mind", Psychwire. https://psychwire.com/free-resources/expert-insights/resource-uugrdo/what-is-wise-mind
+- Get Self Help, no date shown, "Wise Mind", getselfhelp.co.uk. https://www.getselfhelp.co.uk/wisemind.htm
diff --git a/hub-question-article/counselling-vs-cbt.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/hub-question-article/counselling-vs-cbt.md
index 4d82d7b3..6d6f8662 100644
--- a/hub-question-article/counselling-vs-cbt.md	
+++ b/hub-question-article/counselling-vs-cbt.md	
@@ -57 +57 @@ Carl Rogers, credited from a published account for the person-centred approach i
-| Between counselling and psychotherapy there is "a continuum of practice not a clear point of distinction"; some psychotherapy trainings are longer with more client hours | BACP, SCoPEd frequently asked questions on titles, bacp.co.uk, read live 29 September 2026 | evidence |
+| The way psychotherapists and counsellors work can overlap, and both use talking therapy to help someone tackle an emotional difficulty; the training for each is different | UKCP, psychotherapy FAQs, psychotherapy.org.uk, read live 2 November 2026 (replaces the BACP titles page, now gone) | evidence |
@@ -65 +65 @@ Is CBT a type of counselling. What is the difference between counselling and psy
-Internal: [CBT hub guide](/learn/psychology/articles/cognitive-behavioural-therapy/), [What is counselling?](/learn/psychology/articles/what-is-counselling/), [Carl Rogers and person-centred counselling](/learn/psychology/articles/carl-rogers-person-centered-counseling/). External: [NHS on CBT](https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/cognitive-behavioural-therapy-cbt/overview/), [Mind on CBT](https://www.mind.org.uk/information-support/drugs-and-treatments/talking-therapy-and-counselling/cognitive-behavioural-therapy-cbt/), [BACP on counselling](https://www.bacp.co.uk/about-therapy/what-is-counselling/), [BACP on titles](https://www.bacp.co.uk/about-us/advancing-the-profession/scoped/scoped-faqs/faqs-scoped-titles/), [PubMed on person-centred therapy](https://pubmed.ncbi.nlm.nih.gov/36944012/).
+Internal: [CBT hub guide](/learn/psychology/articles/cognitive-behavioural-therapy/), [What is counselling?](/learn/psychology/articles/what-is-counselling/), [Carl Rogers and person-centred counselling](/learn/psychology/articles/carl-rogers-person-centered-counseling/). External: [NHS on CBT](https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/cognitive-behavioural-therapy-cbt/overview/), [Mind on CBT](https://www.mind.org.uk/information-support/drugs-and-treatments/talking-therapy-and-counselling/cognitive-behavioural-therapy-cbt/), [BACP on counselling](https://www.bacp.co.uk/about-therapy/what-is-counselling/), [UKCP frequently asked questions](https://www.psychotherapy.org.uk/seeking-therapy/psychotherapy-faqs/), [PubMed on person-centred therapy](https://pubmed.ncbi.nlm.nih.gov/36944012/).
@@ -75 +75 @@ You've been reading about ways to get support and the three names keep sliding i
-So is it counselling vs CBT, and are they even separate? Not entirely, because CBT is a particular way of working, with its own structure and exercises, while counselling is a wider word for a conversation with a trained listener, and psychotherapy overlaps with both. The lines between them are blurry, and the professional body for counselling says as much in its own words.
+So is it counselling vs CBT, and are they even separate? Not entirely, because CBT is a particular way of working, with its own structure and exercises, while counselling is a wider word for a conversation with a trained listener, and psychotherapy overlaps with both. The lines between them are blurry, and the professional bodies say as much in their own words.
@@ -81 +81 @@ Once you can see what each one tends to involve, a leaflet or a website stops so
-The NHS describes cognitive behavioural therapy as a talking therapy in which a therapist helps you change how you think and act. You'll usually have between five and 15 sessions, depending on what you're having it for, which makes it a fairly structured piece of work with a start and an end.
+The National Health Service (NHS) describes cognitive behavioural therapy as a talking therapy in which a therapist helps you change how you think and act. You'll usually have between five and 15 sessions, depending on what you're having it for, which makes it a fairly structured piece of work with a start and an end.
@@ -91 +91 @@ For the whole subject from the beginning, our guide to [Cognitive Behavioural Th
-[The British Association for Counselling and Psychotherapy (BACP) describes counselling](https://www.bacp.co.uk/about-therapy/what-is-counselling/) as a safe and confidential space to talk to a trained professional about the issues and concerns on your mind. The counsellor listens to you "without judgment" and helps you find your own solutions to what you're facing.
+The British Association for Counselling and Psychotherapy (BACP) [describes counselling](https://www.bacp.co.uk/about-therapy/what-is-counselling/) as a safe and confidential space to talk to a trained professional about the issues and concerns on your mind. The counsellor listens to you "without judgment" and helps you find your own solutions to what you're facing.
@@ -99 +99 @@ If you'd rather start with the basic definition, our plainer piece, [what counse
-Psychotherapy is harder to pin down, and BACP's guidance on the titles [counsellor and psychotherapist](https://www.bacp.co.uk/about-us/advancing-the-profession/scoped/scoped-faqs/faqs-scoped-titles/) explains why. It says some psychotherapy trainings are longer and carry more client hours. It concludes, though, that between the two there is "a continuum of practice not a clear point of distinction".
+Psychotherapy is harder to pin down, and the UK Council for Psychotherapy (UKCP) shows why in its [frequently asked questions](https://www.psychotherapy.org.uk/seeking-therapy/psychotherapy-faqs/). It says the way psychotherapists and counsellors work can overlap, because both use talking therapy to help someone tackle an emotional difficulty, and that the training for each is different.
@@ -107 +107 @@ In a CBT session the same worry would likely be looked at more closely. She'd pu
-Is one room more serious than the other? Neither is. They answer the same feeling in different ways, and the blur between the labels is real, as BACP's own wording about a continuum of practice shows.
+Is one room more serious than the other? Neither is. They answer the same feeling in different ways, and the blur between the labels is real, as UKCP's own wording about the two overlapping shows.
@@ -119 +119 @@ Write down the thing you've been avoiding this week, then add the first thought
-- NHS, read 29 September 2026, overview of cognitive behavioural therapy (CBT), NHS website. https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/cognitive-behavioural-therapy-cbt/overview/
+- NHS, 2026 (read 29 September), "Overview: cognitive behavioural therapy (CBT)", nhs.uk. https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/cognitive-behavioural-therapy-cbt/overview/
@@ -122,2 +122,2 @@ Write down the thing you've been avoiding this week, then add the first thought
-- British Association for Counselling and Psychotherapy (BACP), read 29 September 2026, SCoPEd frequently asked questions on titles, BACP website. https://www.bacp.co.uk/about-us/advancing-the-profession/scoped/scoped-faqs/faqs-scoped-titles/
-- Person-Centered Therapy (Rogerian Therapy), read 29 September 2026, PubMed record 36944012, PubMed. https://pubmed.ncbi.nlm.nih.gov/36944012/
+- UK Council for Psychotherapy (UKCP), 2026 (read 2 November), "Psychotherapy FAQs", psychotherapy.org.uk. https://www.psychotherapy.org.uk/seeking-therapy/psychotherapy-faqs/
+- PubMed, 2026 (read 29 September), "Person-Centered Therapy (Rogerian Therapy)", record 36944012, pubmed.ncbi.nlm.nih.gov. https://pubmed.ncbi.nlm.nih.gov/36944012/
diff --git a/hub-question-article/counselling-vs-psychotherapy.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/hub-question-article/counselling-vs-psychotherapy.md
index a57d1cc7..dba9f9f9 100644
--- a/hub-question-article/counselling-vs-psychotherapy.md	
+++ b/hub-question-article/counselling-vs-psychotherapy.md	
@@ -57,2 +57 @@ The UK Council for Psychotherapy (UKCP), the British Association for Counselling
-| Some psychotherapy trainings are longer, at a higher academic level, and require more client hours and supervision; some psychotherapists choose to work under the title counsellor | BACP, SCoPEd frequently asked questions on titles, bacp.co.uk, read live 29 September 2026 | evidence |
-| Counseling defined as a professional relationship that empowers diverse individuals, families and groups to accomplish mental health, wellness, education and career goals, approved by 29 participating organizations | ACA, consensus definition of counseling, counseling.org, read live 29 September 2026 | evidence |
+| Full psychotherapy training usually starts at postgraduate level, takes between three and six years part time and needs around 450 hours of supervised clinical practice, with therapy and supervision throughout; psychotherapeutic counselling routes start at an earlier level with about three years of taught training | UKCP, Train as a psychotherapist, psychotherapy.org.uk, read live 2 November 2026 (replaces the BACP titles page, now gone, and the ACA definition page, now 404) | evidence |
@@ -66 +65 @@ Is counselling the same as therapy. Is psychotherapy deeper than counselling. Ca
-Internal: [Person-Centred Counselling Explained](/learn/general-interest/articles/person-centred-counselling/) (drafted, not yet live), [Do you need a licence to be a counsellor in the UK or US?](/help/certificates-cpd-accreditation/are-counsellors-regulated/), [Life coach or therapist: what is the real difference?](/learn/helping-people/articles/life-coach-vs-therapist/), [Is CBT the same as counselling or psychotherapy?](/learn/psychology/articles/counselling-vs-cbt/), [Is Achology therapy, counselling, or coaching?](/help/achology-basics-and-identity/is-achology-therapy-counselling-or-coaching/). External: [UKCP on psychotherapy](https://www.psychotherapy.org.uk/seeking-therapy/what-is-psychotherapy/), [UKCP frequently asked questions](https://www.psychotherapy.org.uk/seeking-therapy/psychotherapy-faqs/), [BACP on counselling](https://www.bacp.co.uk/about-therapy/what-is-counselling/), [ACA consensus definition](https://www.counseling.org/about-us/about-aca/20-20-a-vision-for-the-future-of-counseling/consensus-definition-of-counseling), [ACA on professional counselors](https://www.counseling.org/docs/default-source/resources-for-counselors/press-room-what-is-a-counselor.pdf?sfvrsn=19ca222c_4).
+Internal: [Person-Centred Counselling Explained](/learn/general-interest/articles/person-centred-counselling/) (drafted, not yet live), [Do you need a licence to be a counsellor in the UK or US?](/help/certificates-cpd-accreditation/are-counsellors-regulated/), [Life coach or therapist: what is the real difference?](/learn/helping-people/articles/life-coach-vs-therapist/), [Is CBT the same as counselling or psychotherapy?](/learn/psychology/articles/counselling-vs-cbt/), [Is Achology therapy, counselling, or coaching?](/help/achology-basics-and-identity/is-achology-therapy-counselling-or-coaching/). External: [UKCP on psychotherapy](https://www.psychotherapy.org.uk/seeking-therapy/what-is-psychotherapy/), [UKCP frequently asked questions](https://www.psychotherapy.org.uk/seeking-therapy/psychotherapy-faqs/), [BACP on counselling](https://www.bacp.co.uk/about-therapy/what-is-counselling/), [UKCP on training as a psychotherapist](https://www.psychotherapy.org.uk/psychotherapy-training/train-as-a-psychotherapist/), [ACA on professional counselors](https://www.counseling.org/docs/default-source/resources-for-counselors/press-room-what-is-a-counselor.pdf?sfvrsn=19ca222c_4).
@@ -82 +81 @@ Knowing that takes some of the pressure off the choice. You'll see what each bod
-The UK Council for Psychotherapy says [psychotherapy and psychotherapeutic counselling](https://www.psychotherapy.org.uk/seeking-therapy/what-is-psychotherapy/) are sometimes both called talking therapies.
+The UK Council for Psychotherapy (UKCP) says [psychotherapy and psychotherapeutic counselling](https://www.psychotherapy.org.uk/seeking-therapy/what-is-psychotherapy/) are sometimes both called talking therapies.
@@ -88,3 +87 @@ The British Association for Counselling and Psychotherapy (BACP) explains [what
-In the US, the American Counseling Association (ACA) spells the word with one l, and its [definition of counseling](https://www.counseling.org/about-us/about-aca/20-20-a-vision-for-the-future-of-counseling/consensus-definition-of-counseling) calls it "a professional relationship" that helps people, families and groups reach goals in mental health, wellness, education and career.
-
-A short [ACA press document](https://www.counseling.org/docs/default-source/resources-for-counselors/press-room-what-is-a-counselor.pdf?sfvrsn=19ca222c_4) goes a step further and says that counseling, therapy, talk therapy and psychotherapy are interchangeable when you work with a counselor.
+In the US, the American Counseling Association (ACA) spells the word with one l. A short [ACA press document](https://www.counseling.org/docs/default-source/resources-for-counselors/press-room-what-is-a-counselor.pdf?sfvrsn=19ca222c_4) goes further than the UK bodies and says that counseling, therapy, talk therapy and psychotherapy are interchangeable when you work with a counselor.
@@ -96 +93 @@ The bodies describe the work as able to overlap, since both counsellors and psyc
-The difference the UK bodies point to is training. BACP's guidance on the titles [counsellor and psychotherapist](https://www.bacp.co.uk/about-us/advancing-the-profession/scoped/scoped-faqs/faqs-scoped-titles/) says some psychotherapy trainings run longer, sit at a higher academic level, and ask for more client hours and supervision. It also says that some psychotherapists choose to work under the title counsellor.
+The difference the UK bodies point to is training. UKCP's page on [training as a psychotherapist](https://www.psychotherapy.org.uk/psychotherapy-training/train-as-a-psychotherapist/) says full psychotherapy training usually starts at postgraduate level, takes between three and six years part time, and asks for around 450 hours of supervised clinical practice, with therapy and supervision of your own throughout. Psychotherapeutic counselling routes, by the same page, start at an earlier level and involve about three years of taught training.
@@ -119,2 +116 @@ Think of a time someone listened to you well, and write down three things they d
-- British Association for Counselling and Psychotherapy (BACP), 2026 (read 29 September), "SCoPEd frequently asked questions on titles", bacp.co.uk. https://www.bacp.co.uk/about-us/advancing-the-profession/scoped/scoped-faqs/faqs-scoped-titles/
-- American Counseling Association (ACA), 2026 (read 29 September), "Consensus definition of counseling", counseling.org. https://www.counseling.org/about-us/about-aca/20-20-a-vision-for-the-future-of-counseling/consensus-definition-of-counseling
+- UK Council for Psychotherapy (UKCP), 2026 (read 2 November), "Train as a psychotherapist", psychotherapy.org.uk. https://www.psychotherapy.org.uk/psychotherapy-training/train-as-a-psychotherapist/
diff --git a/workbook/006-011__workbook__ellis-abc-model.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-011__workbook__ellis-abc-model.md
index 1746a2b3..4e63b7e8 100644
--- a/workbook/006-011__workbook__ellis-abc-model.md	
+++ b/workbook/006-011__workbook__ellis-abc-model.md	
@@ -204,0 +205,10 @@ Ellis's ABC model is a three-part sequence, the activating event, the belief and
+**Parts lead:** The model is explained in four parts: where Ellis found it in the Stoics, the three letters and their order, what each letter covers, and why the belief so often goes missing. Together they let you trace a feeling back to what you told yourself about an event.
+
+**Part 1:** Where the model comes from. Albert Ellis built it in 1962 on a sentence from the Stoic Epictetus, who said people are troubled less by events than by the notions they form about them.
+
+**Part 2:** The three letters. A is the activating event, B is the belief and C is the consequence, and the order carries the lesson, because people jump from A to C and leave B out.
+
+**Part 3:** What each letter covers. An event can be past or only expected, a belief is an idea you have accepted that is seldom the same as a fact, and a consequence has three layers, an emotion, a bodily sensation and a behaviour.
+
+**Part 4:** Why the belief goes missing. It arrives in an instant and feels like plain perception, so you mistake it for part of the event and say that someone made you angry.
+
diff --git a/workbook/006-012__workbook__inner-and-outer-authority.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-012__workbook__inner-and-outer-authority.md
index 8cdcb34b..b7eaab56 100644
--- a/workbook/006-012__workbook__inner-and-outer-authority.md	
+++ b/workbook/006-012__workbook__inner-and-outer-authority.md	
@@ -188,0 +189,8 @@ Inner and outer authority is a two-part idea. Concrete authority is placed in yo
+**Parts lead:** The idea is explained in three parts: the older work on where people place the control of their lives, the two kinds of authority, and why a certificate is not the same as competence. Together they let you see whom you are waiting on.
+
+**Part 1:** Where the model comes from. Julian Rotter's locus of control from 1966 and Stanley Milgram's two states from 1974 sit behind it, alongside Epictetus and Stephen Covey, and later researchers have questioned parts of Milgram's account.
+
+**Part 2:** Concrete and abstract authority. Concrete authority is placed in your life by rules, titles and people thought wiser, while abstract authority is earned by taking responsibility and coming through, and it ends at your own life.
+
+**Part 3:** Why a certificate is not competence. A certificate shows that somebody studied a subject, but competence is made by living through the work, getting it wrong and learning from the result.
+
diff --git a/workbook/006-013__workbook__self-reflection-questions.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-013__workbook__self-reflection-questions.md
index 167dc467..13688b73 100644
--- a/workbook/006-013__workbook__self-reflection-questions.md	
+++ b/workbook/006-013__workbook__self-reflection-questions.md	
@@ -192,0 +193,10 @@ Self-reflection questions are questions you answer for yourself to see how your
+**Parts lead:** The idea is explained in four parts: the thinkers who said you keep the freedom to choose your response, what lies outside you and what lies within you, why that freedom is a trained capacity, and the questions that warm up the mind. Together they prepare you to examine a recent moment of your own.
+
+**Part 1:** Where the idea comes from. Epictetus, Viktor Frankl, Aristotle and Albert Ellis each added a piece, from the things that are up to us, to the attitude a person can still choose, to virtue built by habit, to the views that upset us.
+
+**Part 2:** Outside you and within you. The weather, official decisions and other people's words lie outside you, and what remains is your response, which forms in the gap between a trigger and what you do.
+
+**Part 3:** A capacity that is trained. Choosing your response improves with practice, patience and a willingness to get things wrong, and a pause taken before you answer is called an incubation period.
+
+**Part 4:** Questions that warm up the mind. They ask where your thoughts and feelings begin, whether a memory records what happened or only what you noticed, and who has the final say over your time.
+
diff --git a/workbook/006-014__workbook__current-self-and-ideal-self.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-014__workbook__current-self-and-ideal-self.md
index 87e34823..b71d17e5 100644
--- a/workbook/006-014__workbook__current-self-and-ideal-self.md	
+++ b/workbook/006-014__workbook__current-self-and-ideal-self.md	
@@ -192,0 +193,12 @@ Current self and ideal self describes the distance between how your life stands
+**Parts lead:** The idea is explained in five parts: the research behind it, your current conditions, your ideal conditions, the perceived gap between them, and the difference between progress and fulfilment. Together they show you which part is carrying the weight.
+
+**Part 1:** Where the idea comes from. E. Tory Higgins argued in 1987 that mismatches between who we are and who we want to be bring distress, and Teresa Amabile and Steven Kramer found that progress in meaningful work lifts mood and motivation.
+
+**Part 2:** Current conditions. These are the facts of your life as they stand today, shaped by what you have done and left alone and coloured by the story you tell about yourself.
+
+**Part 3:** Ideal conditions. These are the future you picture, made of a vision, some goals and the person you hope to become, and they give you somewhere to grow without passing any sentence on who you are now.
+
+**Part 4:** The perceived gap. It is the distance between the two as it looks to you, and the wider it looks the deeper the crisis, especially when a big vision has no action behind it.
+
+**Part 5:** Progress and fulfilment. Fulfilment is the longer conviction that your life is heading somewhere worth reaching, and you earn it by seeing yourself leave unwanted conditions behind and close on wanted ones.
+
diff --git a/workbook/006-015__workbook__coveys-circle-of-control.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-015__workbook__coveys-circle-of-control.md
index 4ed8600e..f4c1db37 100644
--- a/workbook/006-015__workbook__coveys-circle-of-control.md	
+++ b/workbook/006-015__workbook__coveys-circle-of-control.md	
@@ -190,0 +191,10 @@ Covey's circle of control is a picture of two nested circles. The outer circle o
+**Parts lead:** The idea is explained in four parts: where the picture comes from, the two circles of concern and control, the three words of perspective, focus and perception, and the question of whether you are being influenced or influencing. Together they let you sort a worry into the part you decide and the part you do not.
+
+**Part 1:** Where the picture comes from. Epictetus, Julian Rotter and Viktor Frankl each described the divide between what is in your power and what is not, and Stephen Covey drew it as two circles in 1989.
+
+**Part 2:** The two circles. The outer circle of concern contains everything that touches you but that you do not decide, and the inner circle of control contains your actions, your attitude, what you want and the standards you set.
+
+**Part 3:** Three words underneath. Perspective is where you see from, focus is what has your attention and perception is how events appear to you, and the three are easily blurred.
+
+**Part 4:** Influenced or influencing. The question that ties the model together is who makes the choice, the outside forces or you, since everyone is shaped by their surroundings.
+
diff --git a/workbook/006-018__workbook__core-assumptions-of-cbt.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-018__workbook__core-assumptions-of-cbt.md
index 9a9279d9..475e3937 100644
--- a/workbook/006-018__workbook__core-assumptions-of-cbt.md	
+++ b/workbook/006-018__workbook__core-assumptions-of-cbt.md	
@@ -196,0 +197,10 @@ The core assumptions of CBT are eight working beliefs that a practitioner of cog
+**Parts lead:** The idea is explained in four parts: where the assumptions come from, the eight assumptions themselves, how each pair is used in a conversation, and what they all have in common. Together they let you try each assumption and notice what it changes.
+
+**Part 1:** Where the assumptions come from. They are the working ideas a practitioner of CBT carries into a conversation, drawn from Albert Ellis in 1962, Aaron Beck in 1976 and Carl Rogers in 1957, and each is a starting point to try and not a proof.
+
+**Part 2:** The eight assumptions. They run from assuming the best of people and treating feelings as something to understand, to the claims that people can grow, that responsibility comes first and that self-awareness comes before self-management.
+
+**Part 3:** How each one is used. The assumptions fall into four pairs, which govern how you approach a person, how you meet a feeling, how you think about change and which method you follow.
+
+**Part 4:** What they have in common. Each steers you towards curiosity and away from verdict, and the same habits of mind that pass sentence on other people pass it on yourself.
+
diff --git a/workbook/006-019__workbook__labels-and-identity.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-019__workbook__labels-and-identity.md
index eadc75f9..8117590a 100644
--- a/workbook/006-019__workbook__labels-and-identity.md	
+++ b/workbook/006-019__workbook__labels-and-identity.md	
@@ -193,0 +194,12 @@ Labels and identity describes how a word about one part of a person can harden i
+**Parts lead:** The idea is explained in five parts: the research behind it, the picture of the mug, the outside of the mug, the inside of the mug and what sits beneath. Together they let you place any word you use about yourself and see what it describes.
+
+**Part 1:** Where the idea comes from. Howard Becker and Erving Goffman published their landmark studies of labels in 1963, Erik Erikson placed identity at the centre of growing up in 1968, and Aristotle argued that virtue comes from practice and habit.
+
+**Part 2:** The picture of the mug. A mug drawn in section, with an outside, an inside and a base, separates what changes quickly from what lasts, so you can see which part a given word describes.
+
+**Part 3:** The outside of the mug. It carries your roles, titles, results, appearance and the words others use about you, all of which can change quickly.
+
+**Part 4:** The inside of the mug. It contains your thoughts, feelings, likes, urges, values and present beliefs, which are closer to you than a title but no more fixed.
+
+**Part 5:** What sits beneath. Virtue and growth lie under both and deserve to be called identity, and a description says what someone did at one time while a definition claims to say what they are.
+
diff --git a/workbook/006-021__workbook__public-and-private-self.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-021__workbook__public-and-private-self.md
index 00da7c56..520e25d2 100644
--- a/workbook/006-021__workbook__public-and-private-self.md	
+++ b/workbook/006-021__workbook__public-and-private-self.md	
@@ -197,0 +198,12 @@ The public and private self describes the difference between the self you show a
+**Parts lead:** The idea is explained in five parts: where it comes from, the picture of the iceberg, what you show, what you keep out of sight, and where the two contradict. Together they let you tell privacy from pretending.
+
+**Part 1:** Where the idea comes from. Carl Rogers described congruence in 1957 and Erving Goffman described everyday life as a kind of theatre in 1959, while the iceberg is a popular image linked to Freud that is best read as an illustration and not a scientific claim.
+
+**Part 2:** The picture of the iceberg. A small tip above the water stands for what you show, and the far larger mass below the waterline stands for what you keep out of sight.
+
+**Part 3:** What you show. It is the manner you adopt in public, often called a persona, which can be a real expression of who you are in a setting or a facade worn to hide what is there.
+
+**Part 4:** What you keep out of sight. It mixes what is rightly private, what you hide out of fear and what you cannot yet see for yourself, and the three need telling apart.
+
+**Part 5:** Where the two contradict. Incongruence is the contradiction between the face you show and the truth beneath it, and a mask worn all day costs attention you could have given to the people you are with.
+
diff --git a/workbook/006-022__workbook__where-beliefs-come-from.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-022__workbook__where-beliefs-come-from.md
index de393096..f0387f43 100644
--- a/workbook/006-022__workbook__where-beliefs-come-from.md	
+++ b/workbook/006-022__workbook__where-beliefs-come-from.md	
@@ -197,0 +198,12 @@ Where beliefs come from is a path of six steps that runs from an experience, thr
+**Parts lead:** The idea is explained in five parts: where it comes from, the path of six steps, how an experience becomes an impression, the step of reflection, and how an idea becomes a belief. Together they let you trace a firm conviction back to the moment it began.
+
+**Part 1:** Where the idea comes from. John Locke argued that the mind gains its ideas from sensation and reflection, and the six steps are Achology's own model built on his account, with help from Aristotle, Epictetus and Albert Ellis.
+
+**Part 2:** The path from experience to belief. Six steps run in order, from experience through the senses, impression and reflection to idea and belief, and reflection is the step that decides what kind of idea comes out.
+
+**Part 3:** Experience, senses and impression. An experience reaches you only through the senses, which deliver a selection of what is there, and it leaves an impression that forms fast and feels like a direct reading of what happened.
+
+**Part 4:** Reflection. This is the step of giving an impression time and examining it, which is why two people with the same impression can leave with very different ideas.
+
+**Part 5:** Idea and belief. An idea is a thought that has been formed, and a belief is an idea accepted as foundationally true, which is rarely the same as a fact.
+
diff --git a/workbook/006-023__workbook__five-categories-of-belief.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-023__workbook__five-categories-of-belief.md
index 3cb02b83..a5c37398 100644
--- a/workbook/006-023__workbook__five-categories-of-belief.md	
+++ b/workbook/006-023__workbook__five-categories-of-belief.md	
@@ -201,0 +202,14 @@ The five categories of belief are existence, association, cause and effect, pred
+**Parts lead:** The idea is explained in six parts: where it comes from, and then the five kinds of belief, which are existence, association, cause and effect, prediction and worldview. Together they let you see which kind of belief is steering a decision.
+
+**Part 1:** Where the idea comes from. John Locke, Epictetus, Albert Ellis and Gordon Allport each added a piece, from ideas arising out of experience to belief standing between an event and a response to the study of prejudice.
+
+**Part 2:** Existence beliefs. They say that something is present or absent in the world, and many cannot be settled by inspection, so a practical question about what you will build from your life is often more useful.
+
+**Part 3:** Association beliefs. They join two things so that where you find one you expect the other, and they usually grow from carrying a verdict about one person over to everything that resembles them.
+
+**Part 4:** Cause and effect beliefs. They reason that because this happened that must be true, and the word means is often the place where such reasoning hides.
+
+**Part 5:** Prediction beliefs. They are forecasts about the future, and their quality changes how the present feels, since fear points at an event that has not yet arrived.
+
+**Part 6:** Meta beliefs. These are the worldviews that sit above the others, the shared standards by which a person judges how life and people ought to be, and most arguments reach down to this level.
+
diff --git a/workbook/006-024__workbook__self-fulfilling-prophecy.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-024__workbook__self-fulfilling-prophecy.md
index c56e5033..3b8be2d7 100644
--- a/workbook/006-024__workbook__self-fulfilling-prophecy.md	
+++ b/workbook/006-024__workbook__self-fulfilling-prophecy.md	
@@ -200,0 +201,12 @@ A self-fulfilling prophecy is a belief whose own effects on behaviour end up con
+**Parts lead:** The idea is explained in five parts: where it comes from, the loop of four steps, how a belief shapes the way you show up, how others see and treat you in return, and why the loop runs both ways. Together they show you where a repeated pattern could be broken.
+
+**Part 1:** Where the idea comes from. Robert Merton named it in 1948, and Rosenthal and Jacobson's Pygmalion study of 1968 and Howard Becker's work on labels look at how expectations and labels shape treatment, though the Pygmalion finding is better read as suggestive than settled.
+
+**Part 2:** The loop of four steps. What you believe about yourself shapes how you show up, that decides how others see you, and the way they treat you arrives as apparent proof of the belief you started with.
+
+**Part 3:** A belief about yourself and how you show up. A belief is an idea you have accepted as true and not a fact, and it leaks into your manner, so someone who thinks they have little to offer tends to hang back.
+
+**Part 4:** How others see and treat you. People respond to what they can see and not to what you meant, and their treatment travels back to the belief you began with and makes it stronger.
+
+**Part 5:** It runs both ways. The loop turns in either direction, so a belief that you are decent though imperfect makes you more open and generous, while a belief that you are a burden makes you smaller.
+
diff --git a/workbook/006-025__workbook__the-map-is-not-the-territory.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-025__workbook__the-map-is-not-the-territory.md
index c8be352c..9b9d81a2 100644
--- a/workbook/006-025__workbook__the-map-is-not-the-territory.md	
+++ b/workbook/006-025__workbook__the-map-is-not-the-territory.md	
@@ -196,0 +197,14 @@ The map is not the territory is a saying from Alfred Korzybski, set out in his 1
+**Parts lead:** The idea is explained in six parts: where it comes from, the difference between perception and reality, and the four limits of a map, which is smaller than the land, leaves things out, must be interpreted and can be out of date. Together they let you test a quick judgement.
+
+**Part 1:** Where the idea comes from. Alfred Korzybski used the phrase in 1933, and the thought is far older, running from Plato's allegory of the cave to the Stoic Epictetus.
+
+**Part 2:** Perception and reality. Perception is how you see something and reality is how it is, and the two overlap without being identical, so only part of the territory gets through the filter to become your map.
+
+**Part 3:** A map is smaller than the land. Your mind cannot keep the whole of a person or a situation, so it keeps a reduced version in which detail disappears.
+
+**Part 4:** A map leaves things out. Your mind selects what matters to the worry or hope of the moment, so what it leaves out is shaped by what you were already expecting.
+
+**Part 5:** A map must be interpreted. It is only marks on paper until somebody reads it, so the same silence from a friend reads as indifference to one person and as busyness to another.
+
+**Part 6:** A map can be out of date. The land changes while the map stays the same, so a judgement formed about a colleague years ago may still be steering you after they have changed.
+
diff --git a/workbook/006-026__workbook__your-two-inner-voices.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-026__workbook__your-two-inner-voices.md
index cfd52f3c..0ee14aec 100644
--- a/workbook/006-026__workbook__your-two-inner-voices.md	
+++ b/workbook/006-026__workbook__your-two-inner-voices.md	
@@ -192,0 +193,12 @@ Your two inner voices is a picture of the mind as a voice that wants and a voice
+**Parts lead:** The idea is explained in five parts: where the picture comes from, the voice of want, the voice of conscience, the scales that weigh them, and how self-control works. Together they let you see which voice you are feeding.
+
+**Part 1:** Where the picture comes from. Plato's charioteer, Marsha Linehan's emotion mind and reasonable mind and Steve Peters's chimp and human are all pictures of the mind and not of the brain.
+
+**Part 2:** The voice of want. It asks for what is easy, gratifying or flattering, it speaks in the present tense and with urgency, and it carries real information about your needs.
+
+**Part 3:** The voice of conscience. It asks what matters and what you value, it speaks of a longer period, and it asks how you will feel afterwards or what you owe the person involved.
+
+**Part 4:** The scales. A decision is pictured as a pair of scales with a voice in each pan, and the point is to see which pan is heavier at this moment and why it has become so.
+
+**Part 5:** How self-control works. It changes the weight in the pans instead of silencing a voice, because a voice grows with what you listen to and repeat.
+
diff --git a/workbook/006-027__workbook__emotional-time-travel.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-027__workbook__emotional-time-travel.md
index 1f582f40..dd9adf87 100644
--- a/workbook/006-027__workbook__emotional-time-travel.md	
+++ b/workbook/006-027__workbook__emotional-time-travel.md	
@@ -192,0 +193,12 @@ Emotional time travel is the way attention carried into the past or the future b
+**Parts lead:** The idea is explained in five parts: where it comes from, the timeline with its three places, the now, what the past brings back, and what the future brings in. Together they let you trace a mood to where your mind had gone.
+
+**Part 1:** Where the idea comes from. Thomas Suddendorf and Michael Corballis called remembering the past and imagining the future mental time travel in 2007, Daniel Gilbert and Timothy Wilson described prospection, and Elizabeth Loftus showed how readily memories are altered.
+
+**Part 2:** The three places on the line. The workbook pictures a timeline of past, now and future along which your attention can travel in either direction, while the feeling always arrives in the present.
+
+**Part 3:** The now. Your current condition is how you feel at this moment and depends on where your attention is, so when it rests in the present the feeling usually matches the room.
+
+**Part 4:** What the past brings back. A memory is a map, smaller than the event and altered over time, so attention that returns to a painful scene brings back its feeling, sometimes in a version that was never quite true.
+
+**Part 5:** What the future brings in. The future is also a map, drawn from guesses and fears, and an expectation is a belief about what is coming that is carried as if it were owed.
+
diff --git a/workbook/006-030__workbook__socratic-questioning.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-030__workbook__socratic-questioning.md
index e3ae7187..c43c8f57 100644
--- a/workbook/006-030__workbook__socratic-questioning.md	
+++ b/workbook/006-030__workbook__socratic-questioning.md	
@@ -199,0 +200,8 @@ Socratic questioning is a way of putting open questions to a thought to test whe
+**Parts lead:** The idea is explained in three parts: where the method comes from, its four steps, and ten example questions. Together they let you check a thought before you act on it.
+
+**Part 1:** Where the method comes from. It takes its name from Socrates, who questioned people about what they claimed to know, and Christine Padesky described its purpose in 1993 as guided discovery, in which questions help a person find something out for themselves.
+
+**Part 2:** The four steps. You notice the emotion, stop, name the pattern and question the thought, and the order matters because skipping the pause turns the rest into an argument with yourself.
+
+**Part 3:** Ten questions. They are examples of the kind of question that tests a thought, such as what evidence there is for it and against it, and they are not a form to be filled in.
+
diff --git a/workbook/006-031__workbook__feelings-faith-and-facts.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-031__workbook__feelings-faith-and-facts.md
index 2faca67b..7dc7445c 100644
--- a/workbook/006-031__workbook__feelings-faith-and-facts.md	
+++ b/workbook/006-031__workbook__feelings-faith-and-facts.md	
@@ -196,0 +197,12 @@ Feelings, faith and facts are three things a life can be built on. Feelings chan
+**Parts lead:** The idea is explained in five parts: the three foundations a life can stand on, then feelings, faith and facts one at a time, and why the third stands firm. Together they let you find what your mood rests on.
+
+**Part 1:** Three things a life can stand on. Feelings, faith and facts differ in how much weight each will bear, and research on how people adapt to changes in fortune and mispredict their own feelings sits behind the idea.
+
+**Part 2:** Feelings. To base a life on feelings is to decide and to form an identity from how you feel at the time, and feelings change with sleep, food, weather and company.
+
+**Part 3:** Faith. Faith here has nothing to do with religion, and it is an attitude to the future that expects a good outcome to be possible and acts on it, although hoping for a result does not produce it.
+
+**Part 4:** Facts. Facts are whatever has been checked against reality, they do not depend on mood, and they include the good features of your situation as well as the bad.
+
+**Part 5:** Why the third stands firm. Facts stay where they are when you do not feel like looking at them, and the plain fact that nobody is perfect is what leaves room to grow.
+
diff --git a/workbook/006-032__workbook__honesty-with-yourself.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-032__workbook__honesty-with-yourself.md
index 511131f8..ac36b5be 100644
--- a/workbook/006-032__workbook__honesty-with-yourself.md	
+++ b/workbook/006-032__workbook__honesty-with-yourself.md	
@@ -194,0 +195,10 @@ Honesty with yourself is the habit of asking what is true of your own part in a
+**Parts lead:** The idea is explained in four parts: where it comes from, why your own part is hard to see, the five truth statements, and how to keep them truthful and not harsh. Together they let you find the part you play.
+
+**Part 1:** Where the idea comes from. Edward Jones and Richard Nisbett described the actor and observer difference in 1971, and Emily Pronin, Daniel Lin and Lee Ross reported a bias blind spot in 2002, while Carl Rogers and Epictetus add that how you see things shapes what you do.
+
+**Part 2:** Why it is hard to see your own part. From the inside your reasons feel clear and sensible, while another person sees only what you did, so each of you has a different account and each is partly right.
+
+**Part 3:** The truth statements. They are five sentence stems that begin "The real reason", finished about yourself as plain sentences without excuse or decoration.
+
+**Part 4:** Truthful, not harsh. A truth statement evaluates something you did and does not pass a verdict on the whole of you, and a good one points to something you could do differently on Monday.
+
diff --git a/workbook/006-036__workbook__seven-levels-of-awareness.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-036__workbook__seven-levels-of-awareness.md
index 2638610e..9e84234d 100644
--- a/workbook/006-036__workbook__seven-levels-of-awareness.md	
+++ b/workbook/006-036__workbook__seven-levels-of-awareness.md	
@@ -210,0 +211,14 @@ The seven levels of awareness are victim, conflict, responsibility, concern, rec
+**Parts lead:** The idea is explained in six parts: where it comes from, the seven levels as a whole, victim and conflict, responsibility, concern and reconciliation, and contentment and free creation. Together they let you place one area of your life on the ladder.
+
+**Part 1:** Where the idea comes from. Stephen Karpman's drama triangle of 1968 and Julian Rotter's locus of control of 1966 sit behind it, along with Epictetus on what is in our control and Seneca on the first disturbance of the mind.
+
+**Part 2:** The seven levels. They run from victim to free creation, each is a way of answering who is responsible for running your life, and each describes an attitude taken in one area and not a type of person.
+
+**Part 3:** Victim and conflict. At the lowest rung life happens to you and only others can change it, and one rung up conflict pushes back with blame and argument while still waiting for someone else to change.
+
+**Part 4:** Responsibility. It is the turning point of the ladder, and it means owning your response and your next step with no blame attached to what has already happened.
+
+**Part 5:** Concern and reconciliation. Attention widens to other people, so that compassion means understanding another person from inside their view, and reconciliation means repairing what can be repaired.
+
+**Part 6:** Contentment and free creation. Contentment is peace with how things stand alongside a wish to keep growing, and free creation is acting by choice and not from fear of what others will think.
+
diff --git a/workbook/006-038__workbook__seven-choices-of-maturity.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-038__workbook__seven-choices-of-maturity.md
index 2d229ac1..0ed9d300 100644
--- a/workbook/006-038__workbook__seven-choices-of-maturity.md	
+++ b/workbook/006-038__workbook__seven-choices-of-maturity.md	
@@ -200,0 +201,8 @@ The seven choices of maturity are seven everyday choices, each with a weaker nei
+**Parts lead:** The idea is explained in three parts: where the tradition comes from, the seven choices each set against a weaker neighbour, and how the choices connect. Together they let you see which ones you lean on.
+
+**Part 1:** Where the idea comes from. Aristotle, Benjamin Franklin, Christopher Peterson with Martin Seligman, and David Brooks each described character as built by what we do repeatedly, from virtues that lie between two faults to a chart of 13 virtues to 24 character strengths.
+
+**Part 2:** The seven choices. Each is set against a weaker neighbour, from responsibility rather than waiting to be fixed to self-control rather than reacting to everything, and you make each one again every morning.
+
+**Part 3:** How the choices connect. Nobody has all seven at once, and they support one another, because fair evaluation leaves room for the humility to take responsibility and building on facts makes self-control possible.
+
diff --git a/workbook/006-042__workbook__positive-goal-setting.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-042__workbook__positive-goal-setting.md
index 4a9cc0dc..f53a94ee 100644
--- a/workbook/006-042__workbook__positive-goal-setting.md	
+++ b/workbook/006-042__workbook__positive-goal-setting.md	
@@ -185,0 +186,8 @@ Positive goal setting is wording a goal toward what you want to have, do or beco
+**Parts lead:** The idea is explained in three parts: the research behind it, the two ways to word a goal, and how a reframe works. Together they let you make a goal that still pulls on a poor day.
+
+**Part 1:** Where the idea comes from. Andrew Elliot and Marcy Church found in 1997 that avoidance goals did worse, Tory Higgins described promotion focus and prevention focus, and Edwin Locke and Gary Latham reviewed 35 years of research on goals in 2002.
+
+**Part 2:** Two ways to word a goal. An away-from goal is worded as something to leave behind or stop, which keeps the trouble at the centre of the picture, while a toward goal is worded as something to have, do or become, which gives your attention a place to go.
+
+**Part 3:** How a reframe works. It keeps the wish and changes the wording in three steps, by asking what you would have in its place, why you care about it and how you would know it had been reached.
+
diff --git a/workbook/006-044__workbook__how-to-learn-anything.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-044__workbook__how-to-learn-anything.md
index f4c73194..d8fb6f25 100644
--- a/workbook/006-044__workbook__how-to-learn-anything.md	
+++ b/workbook/006-044__workbook__how-to-learn-anything.md	
@@ -187,0 +188,8 @@ How to learn anything is a three-part idea: learning is an outcome that needs a
+**Parts lead:** The idea is explained in three parts: where it comes from, the three ingredients of learning, and why "can't" is a belief. Together they let you test a belief that you cannot learn something.
+
+**Part 1:** Where the idea comes from. Aristotle wrote that we learn by doing, Anders Ericsson described deliberate practice in 1993, Albert Bandura looked at beliefs about your own ability in 1977, and Carol Dweck set out fixed and growth views of ability in 2006.
+
+**Part 2:** The three ingredients. Learning is an outcome in which you can now do something you could not do before, and three ingredients lead to it in order, which are desire, a strategy that works and the perseverance to keep following it.
+
+**Part 3:** Why "can't" is a belief. When someone says they cannot learn something they are stating a belief and not describing a fact, and the question to put to it is which of the three ingredients is missing.
+
diff --git a/workbook/006-046__workbook__turning-learning-into-action.md b/Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. The Achology Newsroom/03. The Stock/Content Records/workbook/006-046__workbook__turning-learning-into-action.md
index 4cfc57a9..779d4361 100644
--- a/workbook/006-046__workbook__turning-learning-into-action.md	
+++ b/workbook/006-046__workbook__turning-learning-into-action.md	
@@ -187,0 +188,8 @@ Turning learning into action is a four-step idea: understand, decide, act at onc
+**Parts lead:** The idea is explained in three parts: where it comes from, the four steps from knowing to doing, and the difference between character and reputation. Together they let you close the gap between knowing and doing.
+
+**Part 1:** Where the idea comes from. Aristotle observed that skills and virtues are formed by doing, Peter Gollwitzer showed in 1999 that plans tying a situation to a response raise the chance of follow-through, and Thomas Webb and Paschal Sheeran reviewed intentions and behaviour in 2006.
+
+**Part 2:** From knowing to doing. Learning is read from what you can now do, and it runs in four steps, which are to understand, to decide, to act at once and small, and to repeat until it sticks.
+
+**Part 3:** Character and reputation. Reputation is who other people think you are and character shows in your choices when there is nothing to gain, so a habit kept where nobody sees adds to character.
+
```
