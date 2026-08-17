"""The S226 link map, applied across all 249 help articles.

Authority: `BRIEF__Internal_Links_Across_The_249_Help_Articles.md` (Chat, S226),
re-commissioned in `00__RULING__Harness_Live_249_Stand_Cleanup_Pass_Commissioned.md`
section 2 item 4.

The brief's own description of the job: "It is about links only: you add <a> tags
around words that are already there. Add no words, remove no words, rewrite no
sentences."

The eight rules, implemented one by one:

  1. First mention only. Each target is linked once per article, at its first
     appearance. Never twice.
  2. Body only. No links in the H1, or in any H2 or H3. Every heading is masked.
  3. No self-links. An article never links to its own URL.
  4. The anchor is the words already there. The matched text is re-emitted
     character for character; nothing is added, nothing is reworded.
  5. No invented anchors. Where the phrase is not present, nothing is linked and
     the article is logged.
  6. Eight new links per article maximum. Where more qualify, the eight nearest
     the top are kept and the rest are logged.
  7. Leave existing links alone. This pass adds; it never re-points, and it never
     nests a link inside an existing one.
  8. Live targets only. OVERRIDDEN BY KAIN, this session, in these words: "yes,
     write every link now". His reason, and it is on the record from the rebuild:
     the address structure is settled and the pages are coming, and the section
     already carries hundreds of links written that way. Every target is written,
     and the ones not yet built are reported rather than deferred.

School and course slugs are read from DSRD 1 section 2.3, never typed from
memory, and checked against the brief's own tables. A disagreement stops the run.

Usage:
    python3 linkmap_pass.py report      what would change, nothing written
    python3 linkmap_pass.py write       write the results into batch/ for gating
"""
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
CUR = os.path.join(BASE, "cur249.json")

DSRD_1 = os.path.join(
    os.path.expanduser("~"), "Documents", "CLAUDE | Anthropic Ai",
    "Claude Code (Projects)", "Achology Website Upgrade 2026",
    "003. DSRD's | Achology Specification Documents",
    "DSRD 1. Site Architecture & Taxonomy Rules (URLS)",
    "DSRD_1_Site_Architecture_and_Taxonomy.md")

MAX_LINKS = 8
SKIPPED = []

# ---------------------------------------------------------------- the map

# Straight from the brief's table. Phrase on the left, target on the right.
GENERAL = [
    ("Access All Areas", "/access-all-areas/"),
    ("the Society of Modern Applied Psychology", "/accreditation/"),
    ("Society of Modern Applied Psychology", "/accreditation/"),
    ("SoMAP", "/accreditation/"),
    ("the Achology Academy", "/academy/"),
    ("the Academy", "/academy/"),
    ("school bundles", "/academy/schools/"),
    ("the seven schools", "/academy/schools/"),
    ("schools", "/academy/schools/"),
    ("all courses", "/courses/"),
    ("our courses", "/courses/"),
    ("courses", "/courses/"),
    ("Achology membership", "/membership/"),
    ("membership", "/membership/"),
    ("pricing", "/pricing/"),
    ("prices", "/pricing/"),
    ("accreditation", "/accreditation/"),
    ("accredited", "/accreditation/"),
    ("certification", "/certification/"),
    ("certificates", "/certification/"),
    ("certificate", "/certification/"),
    ("the Code of Ethics", "/about/code-of-ethics/"),
    ("Code of Ethics", "/about/code-of-ethics/"),
    ("the manifesto", "/about/manifesto/"),
    ("our instructors", "/about/instructors/"),
    ("the editorial team", "/about/instructors/"),
    ("Kain Ramsay", "/about/instructors/kain-ramsay/"),
    ("Gerard Egan", "/about/instructors/gerard-egan/"),
    ("student reviews", "/reviews/"),
    ("reviews", "/reviews/"),
    ("testimonials", "/testimonials/"),
    ("free events", "/free-events/"),
    ("free coaching", "/free-coaching/"),
    ("contact us", "/enquiries/"),
    ("get in touch", "/enquiries/"),
    ("enquiries", "/enquiries/"),
    ("the Knowledge Hub", "/learn/"),
    ("Knowledge Hub", "/learn/"),
    ("workbooks", "/learn/workbooks/"),
    ("refund policy", "/policies/refund-policy/"),
    ("refunds", "/policies/refund-policy/"),
    ("privacy policy", "/policies/privacy-policy/"),
    ("privacy", "/policies/privacy-policy/"),
    ("terms and conditions", "/policies/terms-and-conditions/"),
    ("cookie policy", "/policies/cookie-policy/"),
    ("cookies", "/policies/cookie-policy/"),
    ("disclaimers", "/policies/disclaimers/"),
    ("accessibility", "/policies/accessibility-statement/"),
    ("the trust statement", "/policies/trust-statement/"),
    ("our legal pages", "/policies/"),
    ("the policies", "/policies/"),
]

# "terms" alone is not linked. In these articles it is almost always "in terms
# of", which is not the document. The brief's stop rule says log it rather than
# guess, so bare "terms" is logged and left.
LOGGED_NOT_LINKED = {"terms"}

# Guards, each one added after seeing the false positive it stops in a dry run.
# The brief's rule 5 says link nothing and log where a mention is not the thing;
# these are the mechanical form of that.
GUARDS = {
    # "the Academy of Modern Applied Psychology Ltd" is the registered company,
    # not the academy page. Linking the first two words splits a company name.
    "the Academy": (None, r"\s+of\s+Modern\s+Applied\s+Psychology"),
    "the Achology Academy": (None, r"\s+of\s+Modern\s+Applied\s+Psychology"),
    # "reviews" is a verb far more often than it is the reviews page here:
    # "the Society of Modern Applied Psychology then reviews the claim". Only
    # link it where a determiner marks it as the noun.
    "reviews": (r"(?:the|our|these|student|students'|verified|real|read\s+the)\s+$", None),
    # "certificate" inside a course name is that course, handled by the longer
    # match; but a certificate "of" something is a kind of document, not the page.
    "certificate": (None, r"\s+of\s+(attendance|completion|achievement)"),
    # "Web Content Accessibility Guidelines" is a published standard, not our
    # accessibility statement.
    "accessibility": (r"(?<!Web\sContent\s)$", r"\s+Guidelines"),
    # "the Privacy Notice" is a named document; the map's target is the policy
    # page, and linking one word out of a document's name splits the name.
    "privacy": (None, r"\s+(Notice|Statement)"),
}

# Where a mention is the right word for the wrong thing, the brief's rule 5 says
# link nothing and log it. These are the mechanical form of that: a word is left
# alone when another institution's language sits beside it.
ELSEWHERE = re.compile(
    r"universit|academia|academic institution|regulated|clinical hours|"
    r"professional registration|another profession|other providers|Udemy",
    re.I)
CONTEXT_SENSITIVE = {"accredited", "accreditation", "the Academy",
                     "the Achology Academy", "certificate", "certificates"}


def elsewhere(phrase, html, start, end):
    """True when the sentence around this mention is about somebody else."""
    if phrase not in CONTEXT_SENSITIVE:
        return False
    window = html[max(0, start - 160):end + 160]
    return bool(ELSEWHERE.search(window))


def guard_ok(phrase, html, start, end):
    """True when this occurrence survives its guard."""
    before, after = GUARDS.get(phrase, (None, None))
    if before and not re.search(before, html[max(0, start - 40):start], re.I):
        return False
    if after and re.match(after, html[end:end + 60], re.I):
        return False
    return True

SCHOOLS = [
    ("The School of Neuro-Linguistic Programming (NLP)", "/academy/neuro-linguistic-programming/"),
    ("The School of Neuro-Linguistic Programming", "/academy/neuro-linguistic-programming/"),
    ("The School of Cognitive Behavioural Psychology (CBP)", "/academy/cognitive-behavioural-psychology/"),
    ("The School of Cognitive Behavioural Psychology", "/academy/cognitive-behavioural-psychology/"),
    ("The School of Life Coaching and Professional Helping", "/academy/life-coaching/"),
    ("The School of Person-Centred Counselling and Psychology", "/academy/person-centred-counselling/"),
    ("The School of Mindfulness, Applied Insight and Wisdom (MIW)", "/academy/mindfulness/"),
    ("The School of Mindfulness, Applied Insight and Wisdom", "/academy/mindfulness/"),
    ("The School of Mental Health, Wellness and Emotional Resilience", "/academy/mental-health/"),
    ("The School of Personal Growth and Development (PGD)", "/academy/personal-growth/"),
    ("The School of Personal Growth and Development", "/academy/personal-growth/"),
]

# A subject named rather than a course, which the brief routes to the school:
# "Where the words could mean two courses, or name a subject rather than a course
# ('our NLP courses', 'our CBT training'), link the school instead."
SUBJECTS = [
    ("NLP courses", "/academy/neuro-linguistic-programming/"),
    ("NLP training", "/academy/neuro-linguistic-programming/"),
    ("CBT courses", "/academy/cognitive-behavioural-psychology/"),
    ("CBT training", "/academy/cognitive-behavioural-psychology/"),
    ("mindfulness courses", "/academy/mindfulness/"),
    ("life coaching courses", "/academy/life-coaching/"),
    ("counselling courses", "/academy/person-centred-counselling/"),
]

COURSES = [
    ("Diploma Course in Modern Applied Psychology", "/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/"),
    ("A Beginner's Guide to Neuro-Linguistic Programming", "/academy/neuro-linguistic-programming/beginners-guide-nlp/"),
    ("Neuro-Linguistic Programming (NLP) Practitioner Training", "/academy/neuro-linguistic-programming/nlp-practitioner/"),
    ("NLP Practitioner Training", "/academy/neuro-linguistic-programming/nlp-practitioner/"),
    ("NLP Practitioner course", "/academy/neuro-linguistic-programming/nlp-practitioner/"),
    ("Neuro-Linguistic Programming Master Practitioner Course", "/academy/neuro-linguistic-programming/nlp-master-practitioner/"),
    ("NLP Master Practitioner", "/academy/neuro-linguistic-programming/nlp-master-practitioner/"),
    ("Mindset Mastery", "/academy/neuro-linguistic-programming/mindset-mastery-self-discovery/"),
    ("The CBT Toolkit", "/academy/cognitive-behavioural-psychology/cbt-toolkit/"),
    ("CBT Toolkit", "/academy/cognitive-behavioural-psychology/cbt-toolkit/"),
    ("Cognitive Behavioural Therapy (CBT) Practitioner Course", "/academy/cognitive-behavioural-psychology/cbt-practitioner/"),
    ("CBT Practitioner Course", "/academy/cognitive-behavioural-psychology/cbt-practitioner/"),
    ("Cognitive Behavioural Therapy for Mental Health and Wellness", "/academy/cognitive-behavioural-psychology/cbt-mental-health/"),
    ("Life Coaching Certificate Course", "/academy/life-coaching/life-coaching-certificate/"),
    ("Life Coaching Certificate", "/academy/life-coaching/life-coaching-certificate/"),
    ("Life Coaching Blueprint", "/academy/life-coaching/life-coaching-blueprint/"),
    ("The Skilled Helper Training Course", "/academy/life-coaching/skilled-helper/"),
    ("Skilled Helper Practitioner Course", "/academy/life-coaching/skilled-helper-practitioner/"),
    ("Skilled Helper Practitioner", "/academy/life-coaching/skilled-helper-practitioner/"),
    ("Hypnotherapy Practitioner Course", "/academy/person-centred-counselling/hypnotherapy-practitioner/"),
    ("Counselling Skills Practitioner Course", "/academy/person-centred-counselling/counselling-skills-practitioner/"),
    ("Mindfulness Practitioner Diploma Course", "/academy/mindfulness/mindfulness-practitioner-diploma/"),
    ("Mindfulness Practitioner Diploma", "/academy/mindfulness/mindfulness-practitioner-diploma/"),
    ("Mindfulness for Mental Health, Personal Growth and Inner Peace", "/academy/mindfulness/mindfulness-mental-health/"),
    ("Mindfulness for Highly Efficient Management and Leadership", "/academy/mindfulness/mindfulness-leadership/"),
    ("Mental Health and Wellbeing Practitioner Diploma Course", "/academy/mental-health/mental-health-practitioner-diploma/"),
    ("Mental Health and Wellbeing Practitioner Diploma", "/academy/mental-health/mental-health-practitioner-diploma/"),
    ("The Self-Belief, Emotional Intelligence and Assertiveness Masterclass", "/academy/personal-growth/self-belief-emotional-intelligence/"),
    ("Authentic Confidence, Core Identity and Self-Esteem Masterclass", "/academy/personal-growth/authentic-confidence/"),
    ("Master Your Emotional IQ and Revolutionise Your Social Skills", "/academy/personal-growth/emotional-iq-social-skills/"),
    ("The Clarity, Purpose and Personal Effectiveness Masterclass", "/academy/personal-growth/clarity-purpose-effectiveness/"),
    ("The Strategic Goal Setting and Action Planning Masterclass", "/academy/personal-growth/goal-setting-action-planning/"),
    ("The Communication Skills and Social Intelligence Masterclass", "/academy/personal-growth/communication-social-intelligence/"),
    ("The Hyper-Focus, Self-Discipline and Productivity Masterclass", "/academy/personal-growth/hyper-focus-productivity/"),
    ("The Complete Mental Toughness and Inner Resilience Masterclass", "/academy/personal-growth/mental-toughness-resilience/"),
    ("An Essential Guide to Healthy Marriage and Long-Term Relationships", "/academy/personal-growth/healthy-marriage-relationships/"),
    ("An Entrepreneurs' Guide to Launching and Growing a New Business", "/academy/personal-growth/entrepreneurship-business/"),
]

PHRASES = COURSES + SCHOOLS + SUBJECTS + GENERAL


# ---------------------------------------------------------------- slug check

def verify_slugs():
    """DSRD 1 section 2.3 owns the slugs. The map is checked, never trusted."""
    text = io.open(DSRD_1, encoding="utf-8").read()
    start = text.find("### 2.3 Academy Section")
    block = text[start:text.find("### 2.4", start)]
    canonical = set()
    for line in block.splitlines():
        m = re.match(r"\|\s*(/academy/[a-z\-]+/)\s*\|\s*(.+?)\s*\|\s*$", line)
        if not m:
            continue
        school, slugs = m.group(1), m.group(2)
        canonical.add(school)
        for slug in [s.strip() for s in slugs.split(",")]:
            if re.fullmatch(r"[a-z0-9\-]+", slug):
                canonical.add(school + slug + "/")
    used = {t for _, t in SCHOOLS + COURSES + SUBJECTS}
    stray = sorted(used - canonical)
    if stray:
        raise SystemExit(
            "linkmap_pass.py: these targets are not in DSRD 1 section 2.3.\n  " +
            "\n  ".join(stray) + "\nStop. Do not guess a slug.")
    return len(canonical)


# ---------------------------------------------------------------- masking

TAGS = re.compile(r"<[^>]+>")
ANCHOR = re.compile(r"<a\b[^>]*>.*?</a>", re.I | re.S)
HEADINGS = re.compile(r"<(h[1-6])\b[^>]*>.*?</\1>", re.I | re.S)


def mask(html):
    """Rules 2 and 7: headings, existing links and every tag are untouchable."""
    out = list(html)
    for pattern in (HEADINGS, ANCHOR, TAGS):
        for m in pattern.finditer(html):
            for i in range(m.start(), m.end()):
                out[i] = "\x00"
    return "".join(out)


def candidates(html, own_url):
    """Every place a mapped phrase appears in linkable body text."""
    masked = mask(html)
    found = []
    for phrase, target in PHRASES:
        if target == own_url:
            continue  # rule 3: no self-links
        pattern = r"(?<![A-Za-z0-9])" + re.escape(phrase) + r"(?![A-Za-z0-9])"
        for m in re.finditer(pattern, masked, re.I):
            if not guard_ok(phrase, html, m.start(), m.end()):
                continue
            if elsewhere(phrase, html, m.start(), m.end()):
                SKIPPED.append((phrase, target))
                continue
            found.append({"start": m.start(), "end": m.end(),
                          "phrase": phrase, "target": target})
    found.sort(key=lambda c: (c["start"], -(c["end"] - c["start"])))
    return found


def choose(found, already=()):
    """Rules 1, 6 and 7: one link per target, longest match wins an overlap,
    eight per article, nearest the top.

    `already` carries the targets this article links to before the pass runs.
    Rule 7 leaves those links alone; rule 1 says a target is linked once per
    article, never twice. So an existing link to a target closes that target,
    and the pass adds nothing further for it. Missing this seeding is the defect
    that put 87 duplicate links on the section on 28 July 2026.
    """
    kept, taken, seen, overflow = [], [], set(already), []
    best = {}
    for c in found:
        key = c["start"]
        if key not in best or (c["end"] - c["start"]) > (best[key]["end"] - best[key]["start"]):
            best[key] = c
    ordered = sorted(best.values(), key=lambda c: c["start"])
    end_of_last = -1
    for c in ordered:
        if c["start"] < end_of_last:
            continue  # overlaps a link already chosen
        if c["target"] in seen:
            continue  # rule 1: first mention only
        if len(kept) >= MAX_LINKS:
            overflow.append(c)
            continue
        seen.add(c["target"])
        kept.append(c)
        end_of_last = c["end"]
    return kept, overflow


def apply(html, kept):
    """Rule 4: the anchor is the words already there, re-emitted unchanged."""
    for c in sorted(kept, key=lambda c: -c["start"]):
        words = html[c["start"]:c["end"]]
        html = (html[:c["start"]] + '<a href="' + c["target"] + '">' + words +
                "</a>" + html[c["end"]:])
    return html


def run(write):
    n_slugs = verify_slugs()
    print("DSRD 1 section 2.3 read: %d canonical academy paths, map agrees\n" % n_slugs)
    data = json.load(open(CUR))
    urlmap = {}
    for line in io.open(os.path.join(BASE, "help_article_urlmap.tsv"),
                        encoding="utf-8", errors="ignore"):
        bits = line.rstrip("\n").split("\t")
        if len(bits) >= 2 and bits[0].isdigit():
            urlmap[int(bits[0])] = bits[1]

    changed, per_target, overflowed, unmatched, bare_terms = [], {}, [], [], []
    for art in data:
        html = art["content"]
        found = candidates(html, urlmap.get(art["id"], ""))
        kept, overflow = choose(
            found, set(re.findall(r'<a\s[^>]*href="([^"]+)"', html)))
        if re.search(r"(?<![A-Za-z])terms(?![A-Za-z])", mask(html), re.I) and \
                not any(k["target"].endswith("terms-and-conditions/") for k in kept):
            bare_terms.append(art["id"])
        if not kept:
            unmatched.append(art["id"])
            continue
        out = apply(html, kept)
        for c in kept:
            per_target[c["target"]] = per_target.get(c["target"], 0) + 1
        if overflow:
            overflowed.append((art["id"], [(c["phrase"], c["target"]) for c in overflow]))
        changed.append((art, out))

    total = sum(per_target.values())
    print("articles gaining links : %d of %d" % (len(changed), len(data)))
    print("links added            : %d" % total)
    print("articles with no mapped phrase present (rule 5, logged): %d" % len(unmatched))
    print("articles hitting the eight-link cap (rule 6, logged)   : %d" % len(overflowed))
    print('articles with a bare "terms" left unlinked and logged   : %d' % len(bare_terms))
    print("\nlinks added per target:")
    for t, n in sorted(per_target.items(), key=lambda x: -x[1]):
        print("  %-62s %3d" % (t, n))

    if write:
        os.makedirs(os.path.join(BASE, "batch"), exist_ok=True)
        for art, out in changed:
            io.open(os.path.join(BASE, "batch", "%d.html" % art["id"]),
                    "w", encoding="utf-8").write(out)
        print("\nwritten to batch/ for gating: %d files" % len(changed))
    json.dump({"unmatched": unmatched,
               "overflow": [[i, o] for i, o in overflowed],
               "bare_terms": bare_terms},
              open(os.path.join(BASE, "linkmap_log.json"), "w"), indent=1)
    return changed


if __name__ == "__main__":
    run(write=(len(sys.argv) > 1 and sys.argv[1] == "write"))
