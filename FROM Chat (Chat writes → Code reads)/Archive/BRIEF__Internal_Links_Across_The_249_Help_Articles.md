# FROM Chat: add the internal links across the 249 help articles

**Written:** 28 July 2026, Session 226. **From:** Claude Chat. **For:** Claude Code.

The help articles mention courses, schools, accreditation, certification, policies and the rest constantly, and almost none of those mentions link anywhere. This is the pass that fixes that. It is about links only: you add `<a>` tags around words that are already there. Add no words, remove no words, rewrite no sentences.

---

## The link map

Only these targets, only these phrases. Anything not on this list is not linked.

| When the article says | Link to |
|---|---|
| courses, our courses, all courses | /courses/ |
| the Academy, the Achology Academy | /academy/ |
| schools, the seven schools, school bundles | /academy/schools/ |
| a named school | its page in the school table below |
| a named course | its page in the course table below |
| membership, Achology membership | /membership/ |
| pricing, prices | /pricing/ |
| Access All Areas | /access-all-areas/ |
| accreditation, accredited | /accreditation/ |
| certification, certificate, certificates | /certification/ |
| the Society of Modern Applied Psychology, SoMAP | /accreditation/ |
| the Code of Ethics | /about/code-of-ethics/ |
| the manifesto | /about/manifesto/ |
| our instructors, the editorial team | /about/instructors/ |
| Kain Ramsay, named as instructor | /about/instructors/kain-ramsay/ |
| Gerard Egan, named as instructor | /about/instructors/gerard-egan/ |
| reviews, student reviews | /reviews/ |
| testimonials | /testimonials/ |
| free events | /free-events/ |
| free coaching | /free-coaching/ |
| contact us, get in touch, enquiries | /enquiries/ |
| the Knowledge Hub | /learn/ |
| workbooks | /learn/workbooks/ |
| refunds, refund policy | /policies/refund-policy/ |
| privacy, privacy policy | /policies/privacy-policy/ |
| terms, terms and conditions | /policies/terms-and-conditions/ |
| cookies, cookie policy | /policies/cookie-policy/ |
| disclaimers | /policies/disclaimers/ |
| accessibility | /policies/accessibility-statement/ |
| the trust statement | /policies/trust-statement/ |
| the policies, our legal pages | /policies/ |

Course and school slugs are read from DSRD 1 §2.3, never typed from memory. All paths are relative, in the form `/courses/`, so they survive the domain swap.

---

## The seven schools, spelled out

| Canonical name (DSRD 5) | Link to |
|---|---|
| The School of Neuro-Linguistic Programming (NLP) | /academy/neuro-linguistic-programming/ |
| The School of Cognitive Behavioural Psychology (CBP) | /academy/cognitive-behavioural-psychology/ |
| The School of Life Coaching and Professional Helping | /academy/life-coaching/ |
| The School of Person-Centred Counselling and Psychology | /academy/person-centred-counselling/ |
| The School of Mindfulness, Applied Insight and Wisdom (MIW) | /academy/mindfulness/ |
| The School of Mental Health, Wellness and Emotional Resilience | /academy/mental-health/ |
| The School of Personal Growth and Development (PGD) | /academy/personal-growth/ |

## The 28 courses, spelled out

Each course has exactly one page, at the address below. A course can appear in more than one school bundle, but its page never moves: use this table, never a bundle listing, to decide the address.

| # | Canonical name (DSRD 5) | Link to |
|---|---|---|
| 001 | Diploma Course in Modern Applied Psychology (DiMAP) | /academy/neuro-linguistic-programming/diploma-modern-applied-psychology/ |
| 002 | A Beginner's Guide to Neuro-Linguistic Programming (NLP) | /academy/neuro-linguistic-programming/beginners-guide-nlp/ |
| 003 | Neuro-Linguistic Programming (NLP) Practitioner Training | /academy/neuro-linguistic-programming/nlp-practitioner/ |
| 004 | Neuro-Linguistic Programming Master Practitioner Course | /academy/neuro-linguistic-programming/nlp-master-practitioner/ |
| 005 | Mindset Mastery: The Ultimate NLP-Based Guide to Self-Discovery | /academy/neuro-linguistic-programming/mindset-mastery-self-discovery/ |
| 006 | The CBT Toolkit: Core Principles and Real-World Applications | /academy/cognitive-behavioural-psychology/cbt-toolkit/ |
| 007 | Cognitive Behavioural Therapy (CBT) Practitioner Course | /academy/cognitive-behavioural-psychology/cbt-practitioner/ |
| 008 | Cognitive Behavioural Therapy for Mental Health and Wellness | /academy/cognitive-behavioural-psychology/cbt-mental-health/ |
| 009 | Life Coaching Certificate Course (Beginner to Advanced) | /academy/life-coaching/life-coaching-certificate/ |
| 010 | Life Coaching Blueprint: The Complete Process and Practices | /academy/life-coaching/life-coaching-blueprint/ |
| 011 | The Skilled Helper Training Course (with Prof. Gerard Egan) | /academy/life-coaching/skilled-helper/ |
| 012 | Skilled Helper Practitioner Course (Advanced to Expert) | /academy/life-coaching/skilled-helper-practitioner/ |
| 013 | Hypnotherapy Practitioner Course (Beginner to Advanced) | /academy/person-centred-counselling/hypnotherapy-practitioner/ |
| 014 | Counselling Skills Practitioner Course (Beginner to Advanced) | /academy/person-centred-counselling/counselling-skills-practitioner/ |
| 015 | Mindfulness Practitioner Diploma Course (Beginner to Expert) | /academy/mindfulness/mindfulness-practitioner-diploma/ |
| 016 | Mindfulness for Mental Health, Personal Growth and Inner Peace | /academy/mindfulness/mindfulness-mental-health/ |
| 017 | Mindfulness for Highly Efficient Management and Leadership | /academy/mindfulness/mindfulness-leadership/ |
| 018 | Mental Health and Wellbeing Practitioner Diploma Course | /academy/mental-health/mental-health-practitioner-diploma/ |
| 019 | The Self-Belief, Emotional Intelligence and Assertiveness Masterclass | /academy/personal-growth/self-belief-emotional-intelligence/ |
| 020 | Authentic Confidence, Core Identity and Self-Esteem Masterclass | /academy/personal-growth/authentic-confidence/ |
| 021 | Master Your Emotional IQ and Revolutionise Your Social Skills | /academy/personal-growth/emotional-iq-social-skills/ |
| 022 | The Clarity, Purpose and Personal Effectiveness Masterclass | /academy/personal-growth/clarity-purpose-effectiveness/ |
| 023 | The Strategic Goal Setting and Action Planning Masterclass | /academy/personal-growth/goal-setting-action-planning/ |
| 024 | The Communication Skills and Social Intelligence Masterclass | /academy/personal-growth/communication-social-intelligence/ |
| 025 | The Hyper-Focus, Self-Discipline and Productivity Masterclass | /academy/personal-growth/hyper-focus-productivity/ |
| 026 | The Complete Mental Toughness and Inner Resilience Masterclass | /academy/personal-growth/mental-toughness-resilience/ |
| 027 | An Essential Guide to Healthy Marriage and Long-Term Relationships | /academy/personal-growth/healthy-marriage-relationships/ |
| 028 | An Entrepreneurs' Guide to Launching and Growing a New Business | /academy/personal-growth/entrepreneurship-business/ |

**Matching a course or school mention.** Articles rarely write a course's full canonical name. Link the mention when the words used point to exactly one course in the table above and no other: "the NLP Practitioner course" is 003, "the Life Coaching Certificate" is 009, "the Skilled Helper Practitioner course" is 012. Where the words could mean two courses, or name a subject rather than a course ("our NLP courses", "our CBT training"), link the school instead. Where neither is certain, link nothing and log it. Never guess between two courses.

---

## The rules

1. **First mention only.** Each target is linked once per article, at its first appearance. Never twice.
2. **Body only.** No links in the H1, or in any H2 or H3.
3. **No self-links.** An article never links to its own URL.
4. **The anchor is the words already there.** No "click here", no "read more", no added phrase.
5. **No invented anchors.** Where the phrase is not present, link nothing and log the article.
6. **Eight new links per article maximum.** Where more qualify, keep the eight nearest the top and log the rest.
7. **Leave existing links alone.** This pass adds; it does not re-point.
8. **Live targets only.** Write a link only where the target returns 200 today. Where a target is specified but not yet built, log the article and the intended path on a deferred list instead. Those go in as each page ships.

---

## Definition of done

The pass is complete when every one of the 249 articles has been read, every qualifying mention has been either linked or logged, and the deferred list has been returned. Not when the links "look right".

## The stop rule

If a mention does not fit the map, or a rule contradicts what you find in an article, stop and write it to TO Chat. Do not decide it yourself, do not extend the map, and do not link a target that is not on it, however obviously useful it seems.

## Deliver the whole pass, then show it

Run this across all 249 articles and complete it. When it is finished, open 20 of the edited articles at random in Kain's Safari browser so he can review them, and report in TO Chat: the total links added, the count per category, the unmatched mentions, and the deferred list.
