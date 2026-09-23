# SHIP: the voice checks now catch a page that is about a piece of writing, on quote pages and help answers too; the 38 are held strict; the re-run hit list

**From:** Claude Code, S131 (factory session), Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** `BRIEF__Widen_The_Voice_Checks_To_Catch_About_A_Piece_Of_Writing_S380.md` (head-lined DONE). Approved by Kain in session, S380: "Yes, please do."
**Board card:** Search and citation layer for every EPS page.

## What changed in `content_gate.py`

1. **Self-description widened.** "no paragraph describing the article" now catches `this piece`, `this article` and `this post` in either case anywhere in a paragraph (so "In this post" is inside it), `What follows`, `It closes with`, and the existing `It then moves / turns / looks`. `By the end` and `Along the way` are left out.
2. **Quote pages** take two lines only: self-description, and "the quoted person is not narrated", with the person read off the record's `quote_author` (matched to the people list for a first name; otherwise the name's own first word). The standard source line ("This quote by Kain Ramsay was taken from his lecture ...") passes both. No opening, first-heading or meta line runs on this type.
3. **Help answers** take one line: self-description. A help record carries no `post_status` field, so the counted-on-published rule never applies to it and the line fails outright.
4. **The 38 rewritten instructor articles carry `voice_standard: s130`** in their records, so they are checked strictly. All 38 pass every voice line strict.
5. Book notes, author biographies, workbooks and workbook landing pages stay out.

**Proved:** `content_gate_acceptance.py` 125 of 125, 19 of them new: each new phrase red (seven), the two left-out phrases green, the help answer's one line red and green and nothing else run, the quote page's source line passing, its narration red, its self-description red, no opening, heading or meta line on it, a book note not checked, and a published record counted until marked s130, then failed.

## The read-only re-run over every live record of the covered types

685 live records read (instructor, field-authority, hub question, help answer, quote page). No page was changed. 152 pages carry a hit. Field-authority records carry no `post_status` field either, so their opening and self-description lines fail outright rather than count; the instructor articles outside the 38 are counted. Help answers: no hit.

The hit list follows, exactly as the gate printed it. Code cannot tell which of these are the 58 Cowork is fixing, because that list is not in the channel; Chat can match them.

```
records read: 685

     5  field-authority-article | FAIL | voice: first heading does not repeat the title
    62  field-authority-article | FAIL | voice: no paragraph describing the article
    54  field-authority-article | FAIL | voice: opens speaking to the reader
     9  instructor-article | FAIL | voice: first heading does not repeat the title
    27  instructor-article | counted | voice: no paragraph describing the article, co
    38  instructor-article | counted | voice: opens speaking to the reader, counted
    12  quote-page | FAIL | voice: the quoted person is not narrated

pages with a hit: 152
- field-authority-article/10-ethically-dubious-experiments: FAIL voice: opens speaking to the reader (I still remember reading the actual transcript of Stanley Mi)
- field-authority-article/12-psychological-principles: FAIL voice: no paragraph describing the article (3, opening 'This piece explains why the field has no single agreed list '); FAIL voice: opens speaking to the reader (Search for the most important psychological principles. Ever)
- field-authority-article/13-morally-dubious-psychology-experiments: FAIL voice: no paragraph describing the article (5, opening 'This is a roll call of thirteen studies once listed, on this'); FAIL voice: opens speaking to the reader (For eleven days on a locked ward in Montreal, a woman heard)
- field-authority-article/20-common-cognitive-biases-that-influence-your-decisions: FAIL voice: no paragraph describing the article (4, opening '"Cognitive bias" has become a phrase people reach for the wa')
- field-authority-article/a-guide-to-breaking-bad-habits: FAIL voice: opens speaking to the reader (Most people who want to break a bad habit start with the sam)
- field-authority-article/a-guide-to-building-inner-resilience: FAIL voice: no paragraph describing the article (1, opening 'Building any one of these alone is possible. Building all fo'); FAIL voice: opens speaking to the reader (Something has shifted lately. Somewhere in the last few year)
- field-authority-article/aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology: FAIL voice: no paragraph describing the article (1, opening 'This piece goes through both: what Beck actually did differe')
- field-authority-article/albert-banduras-social-learning-theory: FAIL voice: opens speaking to the reader (Watch a toddler pick up a phone. They hold it to their ear e)
- field-authority-article/an-antidote-to-narcissism: FAIL voice: opens speaking to the reader (Somebody calls a difficult colleague a narcissist. Somebody)
- field-authority-article/balanced-lifestyle-seven-practical-steps-to-achieve-life-balance: FAIL voice: no paragraph describing the article (7, opening 'This piece checked. Tracing the real research behind popular')
- field-authority-article/benefits-of-practical-learning-why-experience-outweighs-academic-knowledge: FAIL voice: opens speaking to the reader (Ask anyone who has done the same job for twenty years whethe)
- field-authority-article/conditioning-fear-insights-from-the-little-albert-experiment: FAIL voice: no paragraph describing the article (1, opening 'So which baby was Little Albert. Historians of psychology ha'); FAIL voice: opens speaking to the reader (A baby lies on a mattress in a hospital nursery. A researche)
- field-authority-article/connection-and-authenticity-in-life-coaching: FAIL voice: opens speaking to the reader (A coach asks all the right questions. The structure is textb)
- field-authority-article/decide-with-confidence-10-timeless-principles-for-wise-decision-making: FAIL voice: no paragraph describing the article (1, opening 'A companion piece on this site names twenty of the specific '); FAIL voice: opens speaking to the reader (The old version of this page promised ten timeless principle)
- field-authority-article/delayed-gratification-insights-from-the-marshmallow-test-study: FAIL voice: no paragraph describing the article (1, opening "This article looks at what Walter Mischel's original study a"); FAIL voice: opens speaking to the reader (For decades, one small experiment has shaped how people thin)
- field-authority-article/depth-perception-insights-from-the-visual-cliff-experiment: FAIL voice: opens speaking to the reader (Put a six month old baby on a sheet of glass. On one side, a)
- field-authority-article/dialogue-versus-monologue: FAIL voice: no paragraph describing the article (1, opening 'The friend who talks so well, the one from the very start of')
- field-authority-article/dynamics-of-leading-effective-diplomatic-discussions: FAIL voice: no paragraph describing the article (1, opening 'This piece works through both. It uses the actual evidence, ')
- field-authority-article/embracing-your-shadow-side: FAIL voice: no paragraph describing the article (1, opening 'Most self-help content blurs the two together. This piece wi')
- field-authority-article/essential-character-traits-for-personal-growth-and-development: FAIL voice: no paragraph describing the article (3, opening "Martin Seligman's own career runs through this one framework")
- field-authority-article/ethically-questionable-insights-from-the-robbers-cave-experiment: FAIL voice: no paragraph describing the article (2, opening 'What follows is not a case against Muzafer Sherif, the psych')
- field-authority-article/examining-the-doll-test: FAIL voice: no paragraph describing the article (1, opening 'This piece explains what the study actually did, what it act'); FAIL voice: opens speaking to the reader (A simple question, put to a young child holding two dolls id); FAIL voice: first heading does not repeat the title (What was the doll test, and what did it actually show)
- field-authority-article/exploration-of-dr-howard-gardners-nine-types-of-intelligence: FAIL voice: no paragraph describing the article (1, opening "This is the ground Achology's own School of Cognitive Behavi")
- field-authority-article/exploration-of-the-cognitive-maps-experiment-by-edward-tolman: FAIL voice: opens speaking to the reader (Leave a hungry rat in a maze with no food at the end for ten)
- field-authority-article/exploration-of-the-false-memory-experiment-by-elizabeth-loftus: FAIL voice: no paragraph describing the article (1, opening 'The difference between bending a memory and building one fro')
- field-authority-article/exploration-of-the-split-brain-experiment-by-roger-sperry: FAIL voice: first heading does not repeat the title (What the split brain experiment actually did)
- field-authority-article/exploring-self-determination-theory-key-principles-applications: FAIL voice: no paragraph describing the article (2, opening "This site's own overview of the psychology of motivation sur"); FAIL voice: opens speaking to the reader (A father starts paying his son fifty cents for every book he)
- field-authority-article/finding-lifes-purpose-with-viktor-frankls-mans-search-for-meaning: FAIL voice: no paragraph describing the article (1, opening 'Frankl was direct about what kind of evidence that was. In h')
- field-authority-article/finding-purpose-how-human-values-shape-your-lifes-direction: FAIL voice: no paragraph describing the article (3, opening 'This piece goes through what the evidence actually shows: wh')
- field-authority-article/from-roots-to-revolution: FAIL voice: opens speaking to the reader (This is the story of psychology's own journey from roots to)
- field-authority-article/gerard-egans-skilled-helper-model-using-the-3-stage-framework: FAIL voice: no paragraph describing the article (1, opening 'You started this piece mid-conversation, in the quiet after ')
- field-authority-article/helping-people-help-themselves: FAIL voice: no paragraph describing the article (2, opening 'That gap between the two acts is what this piece is actually')
- field-authority-article/history-and-timeline-of-counselling-psychology: FAIL voice: no paragraph describing the article (2, opening 'Achology already covers two people this history explains. On'); FAIL voice: opens speaking to the reader (Ask most people when counselling began. They picture a couch)
- field-authority-article/how-immediacy-shapes-engaging-and-impactful-conversations: FAIL voice: no paragraph describing the article (3, opening 'They would gently name what seems to be happening. It is hap')
- field-authority-article/how-irresponsibility-leads-to-personal-disempowerment: FAIL voice: no paragraph describing the article (2, opening 'Most real situations blend the two, rather than sitting clea')
- field-authority-article/how-philosophy-illuminates-our-understanding-of-psychology: FAIL voice: no paragraph describing the article (1, opening 'Start this piece by asking what a thought is made of, and yo')
- field-authority-article/insights-from-mary-ainsworths-the-strange-situation-study: FAIL voice: no paragraph describing the article (1, opening "Mary Ainsworth is also one of the nine names on this site's "); FAIL voice: opens speaking to the reader ("Anxious attachment." "Avoidant attachment." The phrases tur)
- field-authority-article/jean-piagets-contributions-to-developmental-psychology: FAIL voice: no paragraph describing the article (2, opening 'It is a structure that reasons differently at each stage of ')
- field-authority-article/karpman-drama-triangle: FAIL voice: no paragraph describing the article (2, opening 'This piece explains what those roles are, why the pattern is'); FAIL voice: opens speaking to the reader (Most people know the feeling before they know the name for i)
- field-authority-article/learned-helplessness-experiment-the-psychology-of-helplessness: FAIL voice: opens speaking to the reader (Picture the image most psychology courses still use to teach)
- field-authority-article/lessons-from-how-to-win-friends-influence-people: FAIL voice: no paragraph describing the article (2, opening 'Most "lessons from this book" posts leave that warning out. ')
- field-authority-article/life-coaching-listening-skills: FAIL voice: opens speaking to the reader (Most listening tips could apply to anyone, in almost any con)
- field-authority-article/maslows-hierarchy-of-needs: FAIL voice: no paragraph describing the article (1, opening 'This piece does that testing. It covers what Maslow actually'); FAIL voice: opens speaking to the reader (A pyramid. Five levels, stacked in order, food and shelter a)
- field-authority-article/mastering-the-art-of-persuasion: FAIL voice: no paragraph describing the article (1, opening 'This piece looks at both. It also looks honestly at where th')
- field-authority-article/mimicking-aggression-insights-from-the-bobo-doll-experiment: FAIL voice: no paragraph describing the article (1, opening 'This piece uses all three names throughout, for that exact r')
- field-authority-article/misattribution-of-arousal-study-insights-into-emotional-perception: FAIL voice: no paragraph describing the article (1, opening "Achology's own psychology hub follows the same rule this pie")
- field-authority-article/obedience-to-authority-stanley-milgram: FAIL voice: opens speaking to the reader (Most people can describe the finding before they can describ)
- field-authority-article/perceptions-illusion-insights-from-the-halo-effect-experiment: FAIL voice: no paragraph describing the article (1, opening 'This piece keeps the two studies separate. One is Edward Tho'); FAIL voice: opens speaking to the reader (Two students watch the same guest lecturer, on the same reco)
- field-authority-article/psychology-history-timeline: FAIL voice: no paragraph describing the article (1, opening 'What follows is a psychology history timeline built the slow')
- field-authority-article/psychology-understanding-the-blue-eyes-brown-eyes-experiment: FAIL voice: opens speaking to the reader (A teacher divided eight-year-olds by the colour of their eye)
- field-authority-article/qualities-of-a-true-leader: FAIL voice: no paragraph describing the article (2, opening 'This piece goes looking for it. It covers what the research ')
- field-authority-article/rosalynn-carter-and-mental-health-stigma: FAIL voice: opens speaking to the reader (Most people know Rosalynn Carter cared about mental health.)
- field-authority-article/sigmund-freuds-defence-mechanisms: FAIL voice: first heading does not repeat the title (What Sigmund Freud's Defence Mechanisms Actually Are, and Wh)
- field-authority-article/skills-for-highly-effective-counseling: FAIL voice: no paragraph describing the article (2, opening 'That gap is the real subject of this piece. Outcome research'); FAIL voice: opens speaking to the reader (Two trainee counsellors sit the same course. They read the s)
- field-authority-article/social-conformity-insights-from-the-asch-conformity-experiment: FAIL voice: no paragraph describing the article (1, opening 'I want to end where this piece began, back in that room with'); FAIL voice: opens speaking to the reader (Picture eight people sitting round a table for what became k)
- field-authority-article/starvation-insights-from-ancel-keys-the-minnesota-experiment: FAIL voice: opens speaking to the reader (In late 1944, thirty-six young men agreed to something unusu)
- field-authority-article/stereotyping-the-unseen-threat-to-diversity-and-inclusion: FAIL voice: opens speaking to the reader (Does stereotyping threaten diversity and inclusion? Most div)
- field-authority-article/the-complete-history-of-life-coaching-and-its-predecessors: FAIL voice: opens speaking to the reader (Ask a working life coach where their profession comes from.)
- field-authority-article/the-core-competencies-of-coaching: FAIL voice: no paragraph describing the article (3, opening 'That standard has a real founding date, a real founding hist')
- field-authority-article/the-dark-side-of-human-behavior-the-impact-of-the-zimbardo-deindividuation-study: FAIL voice: opens speaking to the reader (Put a hood over someone's face, take away their name, and pu)
- field-authority-article/the-dynamics-of-cognitive-dissonance: FAIL voice: opens speaking to the reader (What are the dynamics of cognitive dissonance? Most people k)
- field-authority-article/the-eisenhower-decision-making-matrix: FAIL voice: opens speaking to the reader (A famous quote gets attached to a famous name. A tidy story)
- field-authority-article/the-foundational-principles-of-person-centred-counselling: FAIL voice: opens speaking to the reader (Ask most people what person-centred counselling is built on)
- field-authority-article/the-impact-of-the-hawthorne-studies-on-workplace-dynamics: FAIL voice: no paragraph describing the article (1, opening 'Here is the honest complication. It is the reason this piece')
- field-authority-article/the-importance-of-self-awareness: FAIL voice: no paragraph describing the article (1, opening 'What follows is not a call to sit and stare at the wall for ')
- field-authority-article/the-lucifer-effect-10-lessons-from-philip-zimbardos-classic: FAIL voice: no paragraph describing the article (2, opening 'This piece keeps the shape most readers come looking for. It'); FAIL voice: opens speaking to the reader ("Ordinary, healthy people can be led to act in ways they wou)
- field-authority-article/the-origin-of-cognitive-therapy: FAIL voice: no paragraph describing the article (2, opening 'This piece will not do that.'); FAIL voice: opens speaking to the reader (Ask someone where cognitive therapy came from, and most peop)
- field-authority-article/the-origin-of-the-drama-triangle: FAIL voice: no paragraph describing the article (2, opening 'The full breakdown of each role, how the rotation actually p'); FAIL voice: opens speaking to the reader (Plenty of people can describe the Drama Triangle. Far fewer)
- field-authority-article/the-origins-of-humanistic-psychology: FAIL voice: no paragraph describing the article (2, opening 'Humanistic psychology stood in the middle of that split and ')
- field-authority-article/the-origins-of-positive-psychology: FAIL voice: no paragraph describing the article (2, opening 'That criticism did the field some good. It is a large part o'); FAIL voice: opens speaking to the reader (Ask when positive psychology began and most people guess a d)
- field-authority-article/the-road-to-character-10-lessons-from-david-brooks-classic: FAIL voice: no paragraph describing the article (2, opening 'Treat the borrowing this piece has been honest about as an i')
- field-authority-article/the-role-of-freedom-in-personal-autonomy-and-decision-making: FAIL voice: no paragraph describing the article (2, opening 'Go back to the friend before the big decision. "At least I\'m'); FAIL voice: opens speaking to the reader (A friend says it right before a big decision. "At least I'm)
- field-authority-article/the-smart-goal-setting-framework: FAIL voice: no paragraph describing the article (2, opening 'This piece traces the SMART goal-setting framework back to w'); FAIL voice: opens speaking to the reader (Five letters, repeated so often in meetings and performance)
- field-authority-article/the-stages-of-change-model: FAIL voice: no paragraph describing the article (2, opening 'This piece tells that real story, honestly, including the pa'); FAIL voice: opens speaking to the reader (Fifteen quotes. Fifteen different historical figures. Voltai)
- field-authority-article/the-truth-about-active-listening: FAIL voice: opens speaking to the reader (Most people think they are already good listeners. Most peop)
- field-authority-article/the-truth-about-eloquence: FAIL voice: no paragraph describing the article (1, opening 'This piece tells both stories honestly. The real one, from A'); FAIL voice: opens speaking to the reader (There is a number that gets repeated in almost every communi)
- field-authority-article/the-worlds-most-influential-psychologists: FAIL voice: no paragraph describing the article (1, opening 'Either way, the next time a list like this crosses your feed')
- field-authority-article/triggers-that-lead-to-relationship-breakdowns: FAIL voice: opens speaking to the reader (Most relationships do not end over one dramatic betrayal. Th); FAIL voice: first heading does not repeat the title (What are the triggers that lead to relationship breakdowns)
- field-authority-article/twenty-pivotal-moments-in-psychologys-history: FAIL voice: no paragraph describing the article (2, opening 'This piece skips the round number. It goes deep on four real'); FAIL voice: opens speaking to the reader (Twenty pivotal moments, ten key dates. Five turning points.)
- field-authority-article/two-factor-models-of-personality: FAIL voice: opens speaking to the reader (Personality research keeps circling back to a simple questio)
- field-authority-article/understanding-the-cognitive-load-theory-experiment: FAIL voice: opens speaking to the reader (Two people sit down to learn the same new software. One fini)
- field-authority-article/understanding-the-layers-of-identity: FAIL voice: no paragraph describing the article (3, opening 'You are not one person, not in the way this article means it')
- field-authority-article/understanding-your-core-values: FAIL voice: no paragraph describing the article (1, opening 'If you want a deeper, research-backed grounding in how to bu')
- field-authority-article/unraveling-apathy-insights-from-the-bystander-effect-study: FAIL voice: no paragraph describing the article (1, opening 'Some of the classic theory holds up well under that newer ev'); FAIL voice: opens speaking to the reader (Does the bystander effect still hold up? Most people know th)
- field-authority-article/unveiling-attachment-insights-from-harlows-monkey-experiments: FAIL voice: no paragraph describing the article (2, opening 'This piece tells both halves in one place, in the order they'); FAIL voice: opens speaking to the reader (Put a baby rhesus monkey in a cage with two mothers. One is)
- field-authority-article/voices-of-vulnerability-insights-from-the-monster-study-experiment: FAIL voice: no paragraph describing the article (2, opening 'That is one gap this piece closes. The other runs the opposi'); FAIL voice: opens speaking to the reader (Look up the Monster Study and nearly every account opens the)
- field-authority-article/what-habits-are-and-why-people-get-stuck: FAIL voice: no paragraph describing the article (2, opening 'This piece answers what habits are and why people get stuck,'); FAIL voice: opens speaking to the reader (Twenty-one days. That number shows up on almost every page a)
- field-authority-article/what-is-counselling: FAIL voice: opens speaking to the reader (Somewhere between hearing the word at work, seeing it in a l); FAIL voice: first heading does not repeat the title (What is counselling?)
- field-authority-article/what-is-counselling-psychology-a-search-for-a-definition: FAIL voice: no paragraph describing the article (1, opening 'This is the real, defensible answer to the question this pie')
- field-authority-article/what-is-the-meaning-of-life-a-comprehensive-exploration: FAIL voice: no paragraph describing the article (2, opening 'This is not an attempt to declare a winner among them. Vikto')
- instructor-article/a-diagnosis-actually-describing: counted voice: no paragraph describing the article, co (nted 1, opening 'Once you see what a diagnosis actually describing really is,')
- instructor-article/a-false-epidemic-happen-without-anyone-lying: counted voice: no paragraph describing the article, co (nted 2, opening 'Seeing them named together, as one general pattern rather th'); counted voice: opens speaking to the reader, counted (How can a false epidemic happen without anyone lying? It sou); FAIL voice: first heading does not repeat the title (How Can a False Epidemic Happen Without Anyone Lying, Exactl)
- instructor-article/a-psychiatric-diagnosis-simply-wrong: counted voice: opens speaking to the reader, counted (How often is a psychiatric diagnosis simply wrong? Wrong eno); FAIL voice: first heading does not repeat the title (How Often Is a Psychiatric Diagnosis Simply Wrong, According)
- instructor-article/ai-agree-with-everything-you-say: counted voice: opens speaking to the reader, counted (I want to admit something uncomfortable. I have asked an AI); FAIL voice: first heading does not repeat the title (Why Does AI Agree With Everything You Say?)
- instructor-article/ai-making-us-worse-thinkers: counted voice: no paragraph describing the article, co (nted 1, opening 'None of the three patterns in this article live inside the A')
- instructor-article/assumptions-damage-relationships: counted voice: no paragraph describing the article, co (nted 1, opening 'Most people go their whole lives assuming that how they see ')
- instructor-article/authentic-leadership: counted voice: opens speaking to the reader, counted (I wrote last time about what people actually need from whoev)
- instructor-article/blood-test-for-depression: counted voice: no paragraph describing the article, co (nted 1, opening 'This is not a small thing to carry if you have spent months,')
- instructor-article/bmi-decide-who-gets-eating-disorder-treatment: counted voice: no paragraph describing the article, co (nted 1, opening 'This series holds one hard line throughout. Eating disorders'); FAIL voice: first heading does not repeat the title (Why Does BMI Decide Who Gets Eating Disorder Treatment, Acco)
- instructor-article/busy-but-not-fulfilled: counted voice: opens speaking to the reader, counted (Most people I work with are busy but not fulfilled. Not many)
- instructor-article/challenging-skills-in-counselling: counted voice: opens speaking to the reader, counted (Of all the skills a helper uses, the challenging skills in c)
- instructor-article/client-resistance-in-counselling: counted voice: opens speaking to the reader, counted (Client resistance in counselling pulls a helper one of two w)
- instructor-article/consistency-in-leadership: counted voice: opens speaking to the reader, counted (I wrote last time about authentic leadership, about choosing)
- instructor-article/diagnosing-bipolar-disorder-in-children: counted voice: no paragraph describing the article, co (nted 1, opening 'Ask questions. Ask for time. I build the fuller version of P'); counted voice: opens speaking to the reader, counted (Why do professionals disagree about diagnosing bipolar disor)
- instructor-article/diagnosis-be-scientifically-weak-but-still-useful: counted voice: no paragraph describing the article, co (nted 1, opening 'None of these findings were cherry-picked to make the DSM lo'); counted voice: opens speaking to the reader, counted (Can a diagnosis be scientifically weak but still useful? Aft); FAIL voice: first heading does not repeat the title (Can a Diagnosis Be Scientifically Weak but Still Useful, Giv)
- instructor-article/diagnostic-inflation-actually-happening: counted voice: no paragraph describing the article, co (nted 2, opening 'Reaching for only one half, and calling it the whole answer,'); counted voice: opens speaking to the reader, counted (Is diagnostic inflation actually happening? Plenty of people)
- instructor-article/difference-between-change-and-transition: counted voice: opens speaking to the reader, counted (Of all the ideas I have found genuinely useful in understand)
- instructor-article/doctors-have-only-minutes-to-diagnose: counted voice: no paragraph describing the article, co (nted 1, opening 'I build the fuller version of this idea inside the Mental He')
- instructor-article/does-a-diagnosis-do-to-the-person: counted voice: no paragraph describing the article, co (nted 2, opening 'A diagnosis describes. It does not explain, and nothing here'); counted voice: opens speaking to the reader, counted (What does a diagnosis do to the person who receives it? Some)
- instructor-article/does-ai-actually-understand: counted voice: opens speaking to the reader, counted (I want to start with a confession. There have been moments w)
- instructor-article/empathy-in-counselling: counted voice: opens speaking to the reader, counted (Empathy in counselling is one of the most used phrases in th)
- instructor-article/everyone-agreeing-on-a-diagnosis: counted voice: no paragraph describing the article, co (nted 2, opening 'This article asks whether everyone agreeing on a diagnosis a'); counted voice: opens speaking to the reader, counted (Ask a room of 10 clinicians to diagnose the same patient usi); FAIL voice: first heading does not repeat the title (Why Everyone Agreeing on a Diagnosis Does Not Make It True)
- instructor-article/five-symptoms-mean-depression: counted voice: no paragraph describing the article, co (nted 2, opening 'Most people assume a number like that was worked out in a la')
- instructor-article/growth-mindset-at-work: counted voice: opens speaking to the reader, counted (I wrote last time about being kind without being a pushover,)
- instructor-article/helping-clients-tell-their-story: counted voice: opens speaking to the reader, counted (Every client who arrives at a helping relationship brings a)
- instructor-article/homosexuality-was-a-diagnosis: counted voice: no paragraph describing the article, co (nted 1, opening 'I build the fuller version of this idea inside the Mental He'); counted voice: opens speaking to the reader, counted (For decades, being gay was officially named a mental illness)
- instructor-article/hypomania-from-an-ordinary-mood-swing: counted voice: no paragraph describing the article, co (nted 2, opening 'Reviewed from a calmer place, it rarely looks the same. This'); FAIL voice: first heading does not repeat the title (How Do You Tell Hypomania From an Ordinary Mood Swing, Accor)
- instructor-article/internal-versus-external-locus-of-control: counted voice: opens speaking to the reader, counted (There is a distinction in psychology I return to more than a)
- instructor-article/is-my-grief-normal: counted voice: opens speaking to the reader, counted (Is my grief normal, or is it a disorder now? For most of hum)
- instructor-article/kind-without-being-a-pushover: counted voice: opens speaking to the reader, counted (I wrote last time about respect being given first and earned)
- instructor-article/mental-disorders-tripled-since-the-1950s: counted voice: no paragraph describing the article, co (nted 2, opening 'This article is not going to pick a side in that argument. I'); counted voice: opens speaking to the reader, counted (Since 1952, the number of named mental disorders has nearly)
- instructor-article/multiple-personality-diagnoses-spike-after-a-film: counted voice: no paragraph describing the article, co (nted 1, opening 'I build the fuller version of this idea inside the Mental He'); counted voice: opens speaking to the reader, counted (A rare diagnosis, almost unheard of for a century and a half)
- instructor-article/people-first-leadership: counted voice: opens speaking to the reader, counted (I wrote last time about why every business problem is a mind)
- instructor-article/psychological-blind-spots: counted voice: no paragraph describing the article, co (nted 1, opening 'What follows is predictable. The person defends, and the def'); counted voice: opens speaking to the reader, counted (The people who come to helpers are not, in the main, people)
- instructor-article/self-awareness-and-personal-growth: counted voice: opens speaking to the reader, counted (Every real change I have seen in another person began the sa)
- instructor-article/self-report-decide-a-diagnosis: counted voice: no paragraph describing the article, co (nted 2, opening 'There is no blood test, no brain scan, no objective measurem'); counted voice: opens speaking to the reader, counted (How much does self-report decide a diagnosis? For one of the); FAIL voice: first heading does not repeat the title (How Much Does Self-Report Decide a Diagnosis? More Than You)
- instructor-article/stages-of-building-strong-relationships: counted voice: no paragraph describing the article, co (nted 1, opening 'This is also where trust and time have to work together, bec')
- instructor-article/stages-of-human-development-and-maturity: counted voice: no paragraph describing the article, co (nted 1, opening 'Someone who spent a lifetime defending an opinion instead of')
- instructor-article/step-outside-your-comfort-zone: counted voice: opens speaking to the reader, counted (My staff sergeant called me into his office one afternoon an)
- instructor-article/telling-people-what-to-do: counted voice: opens speaking to the reader, counted (I wrote last time about learning to meet people where they a)
- instructor-article/the-definition-of-mental-disorder: counted voice: no paragraph describing the article, co (nted 2, opening 'That makes the change more interesting, not less. I want to '); counted voice: opens speaking to the reader, counted (Ask what a mental disorder actually is, and most people assu)
- instructor-article/the-dsm-5-cost-five-times-more: counted voice: no paragraph describing the article, co (nted 4, opening 'Most people hear a number like that and reach straight for a')
- instructor-article/the-dsm-call-its-own-categories-porous: counted voice: no paragraph describing the article, co (nted 2, opening 'Because its own writers watched the neat boxes blur in actua'); counted voice: opens speaking to the reader, counted (Most people picture a psychiatric diagnosis like a labelled); FAIL voice: first heading does not repeat the title (So Why Does the DSM Call Its Own Categories Porous?)
- instructor-article/the-rise-in-autism-diagnoses-real: counted voice: no paragraph describing the article, co (nted 2, opening 'Both explanations get used as weapons in a much louder publi'); counted voice: opens speaking to the reader, counted (Autism diagnoses have climbed sharply over the past few deca)
- instructor-article/the-role-of-hope-in-therapy: counted voice: opens speaking to the reader, counted (Hope tends to be treated as a feeling, something a person ei)
- instructor-article/trust-ai-even-when-its-wrong: counted voice: no paragraph describing the article, co (nted 2, opening 'This is, in my experience, the single most dangerous of the ')
- instructor-article/what-employees-want-from-their-managers: counted voice: opens speaking to the reader, counted (I wrote last time about the moment I realised that leading p)
- instructor-article/what-is-concept-creep: counted voice: no paragraph describing the article, co (nted 2, opening 'This matters far beyond academic psychology. It matters beca'); counted voice: opens speaking to the reader, counted (What is concept creep? It is a simple idea with a big effect)
- instructor-article/what-is-stepped-care: counted voice: opens speaking to the reader, counted (What is stepped care, and could it replace diagnosis for a g)
- instructor-article/why-do-people-seek-counselling: counted voice: opens speaking to the reader, counted (Why do people seek counselling? There is a gap between the r)
- quote-page/empathy-means-understanding-dissonance: FAIL voice: the quoted person is not narrated (1, e.g. 'Gerard Egan adds')
- quote-page/what-happens-when-dialogue-becomes-disrespectful: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain describes')
- quote-page/why-mistakes-are-not-the-most-effective-way: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain tells')
- quote-page/why-mutual-respect-decides-if-a-relationship-survives: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain Ramsay says')
- quote-page/why-no-single-label-can-define-who-you-are: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain Ramsay explains')
- quote-page/why-no-teacher-can-make-you-learn: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain Ramsay explains')
- quote-page/why-responsibility-starts-with-you: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain says')
- quote-page/why-we-dont-know-we-have-a-choice: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain describes')
- quote-page/why-we-end-up-going-round-and-round-in-circles: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain describes')
- quote-page/why-we-never-get-around-to-doing-anything: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain tells')
- quote-page/why-you-cant-trust-a-scared-person: FAIL voice: the quoted person is not narrated (1, e.g. 'Kain Ramsay puts it')
- quote-page/wont-be-accomplished-at-all: FAIL voice: the quoted person is not narrated (1, e.g. 'Gerard Egan explains')
```

## OWED BACK

Nothing. The 58 Cowork is fixing come to Code as pushes; each is marked `voice_standard: s130` on Chat's word once checked.

*No em or en dashes in this file; checked before writing.*
