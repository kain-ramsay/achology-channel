"""The register pass over the 249 help articles, first mention only.

Authority: `00__RULING__First_Mention_Only_Register_Pass_Mechanical.md`, Chat
S227, on Kain's ruling "yes". Its governing sentence, quoted:

    "Every locked term gives its full canonical name with the short form in
    brackets at first mention. Every later mention keeps the short form. No short
    identification is ever substituted into a running sentence. The ruled
    exceptions stand unchanged: headings, canonical course, event and document
    names, quoted article titles."

Standard: DSRD 2 section 2.24, read fresh through register.py on every run. That
section is being amended from Chat's side to carry this ruling; until it lands,
the ruling file above governs.

What this does, and only this:

  1. The first mention of a governed acronym gets its canonical name in front, in
     the register's own words: "Virtual Achologist Led Training Sessions (VALTS)".
  2. A first mention already correctly formed is left completely alone, in any
     word order that carries the full canonical name. Ruled at case c.
  3. Every later mention keeps its short form, untouched. This is the half that
     broke the sentences in the earlier attempt and is now ruled out.
  4. CCaC is replaced by "Code of Character and Conduct" everywhere, and a gloss
     bracket that repeats the words before it is deleted. Ruled for article 322.
  5. The Wiser People clause and the sentence depending on it are removed, with no
     replacement copy. Article 360 is held out of the batch for Chat's review
     before publishing, as the ruling requires.

Never touched: headings, hrefs, existing anchors, and the protected names below.

Usage:
    python3 cleanup_249.py report      what would change, nothing written
    python3 cleanup_249.py write       write the results into batch/ for gating
"""
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
import register as R  # noqa: E402

CUR = os.path.join(BASE, "cur249.json")
HELD_FOR_REVIEW = {360}

HEADINGS = re.compile(r"<(h[1-6])\b[^>]*>.*?</\1>", re.I | re.S)
ANCHOR = re.compile(r"<a\b[^>]*>.*?</a>", re.I | re.S)
TAGS = re.compile(r"<[^>]+>")

# Canonical course, event, document and company names. The ruling keeps these
# exactly as written, and every one of them carries a governed short form inside
# it, so each is masked before any matching happens.
PROTECTED_NAMES = [
    r"Group Facilitation and VALTS Host Training",
    r"VALTS Host Training",
    r"Achology CPD Handbook",
    r"CPD Handbook",
    r"Academy of Modern Applied Psychology Ltd(?:\s*\(AMAP\))?",
    r"Achology Transactions Ltd",
    r"DiMAP Host Training",
    r"ALT Community Training Session",
    r"\(ALT Community Training Session\)",
]
PROTECTED = re.compile("|".join(PROTECTED_NAMES), re.I)


def mask_text(html):
    """For the CCaC replacement only: a link's visible words are body copy and
    Chat's S226 instruction covers them ("Apply across all 249"), so only the
    addresses and the headings are out of bounds here. His ruling on article 322
    settles the one quoted title: delete the bracket, leave the words."""
    out = list(html)
    for pattern in (HEADINGS, TAGS, PROTECTED):
        for m in pattern.finditer(html):
            for i in range(m.start(), m.end()):
                out[i] = "\x00"
    return "".join(out)


def mask(html):
    """Blank the regions the ruling puts out of bounds, keeping offsets intact."""
    out = list(html)
    for pattern in (HEADINGS, ANCHOR, TAGS, PROTECTED):
        for m in pattern.finditer(html):
            for i in range(m.start(), m.end()):
                out[i] = "\x00"
    return "".join(out)


def canonical_name(row, acro):
    """The canonical name exactly as the register writes it, before its bracket."""
    i = row["full"].find("(" + acro + ")")
    if i < 0:
        return None
    words = re.findall(r"[A-Za-z'\-]+", row["full"][:i])[-8:]
    CONNECTORS = {"of", "and", "in", "for", "the", "on"}
    while words and not (words[0][:1].isupper() and words[0] not in ("The", "An", "A")):
        words.pop(0)
    out = []
    for w in words:
        if w[:1].isupper() or (out and w.lower() in CONNECTORS):
            out.append(w)
        else:
            out = []
    while out and out[-1].lower() in CONNECTORS:
        out.pop()
    return " ".join(out) or None


def _norm(words):
    """Compare names ignoring case and a trailing plural, so "Session" matches
    the register's "Sessions". Ruled at case c: any word order carrying the full
    canonical name counts as already correct."""
    return [w.lower().rstrip("s") for w in re.findall(r"[A-Za-z']+", words)]


def already_formed(html, pos, acro, name):
    """Is this bracketed acronym already preceded by its full canonical name?"""
    if not (html[pos - 1:pos] == "(" and html[pos + len(acro):pos + len(acro) + 1] == ")"):
        return False
    window = TAGS.sub(" ", html[max(0, pos - len(name) - 120):pos - 1])
    before = _norm(window)
    want = _norm(name)
    return want and before[-len(want):] == want


def formed_anywhere(html, acro, name):
    """Is the canonical name plus its bracket already somewhere in this article?
    Tags between the words are ignored, so a first mention inside a link counts."""
    words = [re.escape(w) for w in re.findall(r"[A-Za-z'\-]+", name)]
    gap = r"(?:</?[a-zA-Z][^>]*>|[\s,])*"
    pattern = gap.join(words) + r"e?s?" + gap + r"\(\s*" + re.escape(acro) + r"\s*\)"
    return bool(re.search(pattern.replace("s" + r"e?s?", r"s?e?s?"), html, re.I))


def fix_acronyms(html, idx, log):
    """Rule: canonical name at the first mention. Later mentions are untouched."""
    for acro in sorted(idx, key=len, reverse=True):
        row = idx[acro]
        name = canonical_name(row, acro)
        if not name:
            continue
        masked = mask(html)
        hits = [m.start() for m in
                re.finditer(r"(?<![A-Za-z])" + re.escape(acro) + r"(?![A-Za-z])", masked)]
        if not hits:
            continue
        first = hits[0]
        if already_formed(html, first, acro, name) or formed_anywhere(html, acro, name):
            continue
        # "A Competency Improvement Practice Sessions (CIPS) credit" is not
        # English. Where the canonical name is plural and the sentence has put an
        # indefinite article in front of it, the fix is a wording decision, which
        # Rule 5 keeps out of my hands. Logged for Chat, left alone.
        if re.search(r"\b(a|an|A|An)\s+$", TAGS.sub(" ", html[max(0, first - 6):first])) \
                and name.rstrip().endswith("s"):
            log.append("NEEDS CHAT: indefinite article before a plural name, %s" % acro)
            continue
        if html[first - 1:first] == "(" and html[first + len(acro):first + len(acro) + 1] == ")":
            html = html[:first - 1] + name + " (" + acro + ")" + html[first + len(acro) + 1:]
        else:
            html = html[:first] + name + " (" + acro + ")" + html[first + len(acro):]
        log.append("first mention formed: %s (%s)" % (name, acro))
    return html


CCAC_FULL = "Code of Character and Conduct"


def fix_ccac(html, log):
    """Chat S226: replace every CCaC with the full name, and delete a gloss
    bracket that becomes a repetition of the words immediately before it."""
    if "CCaC" not in html:
        return html
    html = re.sub(r",\s*or\s+CCaC\s*,", "", html)
    masked = mask_text(html)
    spans = []
    for m in re.finditer(r"\s*\(\s*CCaC\s*\)|(?<![A-Za-z])CCaC(?![A-Za-z])", masked):
        spans.append((m.start(), m.end()))
    for start, end in reversed(spans):
        chunk = html[start:end]
        before = html[max(0, start - len(CCAC_FULL) - 6):start]
        if "(" in chunk and _norm(before)[-len(_norm(CCAC_FULL)):] == _norm(CCAC_FULL):
            html = html[:start] + html[end:]
            log.append("CCaC gloss bracket removed as a repetition")
        else:
            html = html[:start] + chunk.replace("CCaC", CCAC_FULL) + html[end:]
            log.append("CCaC replaced with the full name")
    return html


WISER_CLAUSE = re.compile(r",\s*and active status in the Wiser People Professional Directory", re.I)
WISER_SENTENCE = re.compile(
    r"\s*Masters who do not meet the annual requirements lose the status,\s*"
    r"because the directory's value depends on everyone in it being an active,\s*"
    r"practising professional\.", re.I)


def fix_wiser(html, log):
    """DSRD 2 section 2.24: "The Wiser People directory is not built. No help
    article tells a reader they can join or be listed in it, and any existing
    sentence that does is removed rather than softened." Chat ruled: remove the
    clause and the sentence that depends on it, with no replacement copy."""
    if "Wiser People" not in html:
        return html
    out = WISER_CLAUSE.sub("", html)
    out = WISER_SENTENCE.sub("", out)
    if out != html:
        log.append("Wiser People clause and its dependent sentence removed")
    if "Wiser People" in out:
        log.append("WARNING: a Wiser People mention remains and needs eyes")
    return out


def run(write):
    data = json.load(open(CUR))
    idx = R.index()
    changed, logs, held = [], {}, []
    for art in data:
        html = art["content"]
        log = []
        out = fix_ccac(html, log)
        out = fix_wiser(out, log)
        out = fix_acronyms(out, idx, log)
        if out == html:
            continue
        logs[art["id"]] = log
        if art["id"] in HELD_FOR_REVIEW:
            held.append((art, out))
        else:
            changed.append((art, out))

    kinds = {}
    for log in logs.values():
        for line in log:
            key = line.split(":")[0]
            kinds[key] = kinds.get(key, 0) + 1
    print("articles the pass changes : %d of %d" % (len(changed) + len(held), len(data)))
    print("held back for Chat's review: %s" % (sorted(a["id"] for a, _ in held) or "none"))
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print("  %-46s %d" % (k, v))

    if write:
        os.makedirs(os.path.join(BASE, "batch"), exist_ok=True)
        for art, out in changed:
            io.open(os.path.join(BASE, "batch", "%d.html" % art["id"]),
                    "w", encoding="utf-8").write(out)
        print("\nwritten to batch/ for gating: %d files" % len(changed))
        for art, out in held:
            io.open(os.path.join(BASE, "held_%d.html" % art["id"]),
                    "w", encoding="utf-8").write(out)
    return changed, held, logs


if __name__ == "__main__":
    run(write=(len(sys.argv) > 1 and sys.argv[1] == "write"))
