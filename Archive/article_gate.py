"""The gate every rebuilt help article passes before it is written to the site.

Checks the standards agreed with Kain on 2026-07-28, plus the ones already in the
documents. It fails loudly rather than warning, because a warning gets skimmed.
"""
import json, os, re, sys

TAG = re.compile(r"<[^>]+>")
HEAD = re.compile(r"<(h[1-6])\b[^>]*>.*?</\1>", re.I | re.S)
ANCHOR = re.compile(r"<a\b[^>]*>.*?</a>", re.I | re.S)

EXPANSIONS = {
    "VALTS": "Virtual Achologist Led Training Session",
    # Kain, S230: "Peer-Peer is terrible on audio ... use the term peer-to-peer
    # instead." Swept across the 249 the same day; the register in DSRD 2 §2.24
    # still carries the old form and Chat is updating it.
    "PALS": "Peer-to-Peer Applied Learning Session",
    "CIPS": "Competency Improvement Practice Session",
    "CCaC": "Code of Character and Conduct",
    "SoMAP": "Society of Modern Applied Psychology",
    "DiMAP": "Diploma Course in Modern Applied Psychology",
    "CPD": "continuing professional development",
    "UKRLP": "UK Register of Learning Providers",
    "NLP": "Neuro-Linguistic Programming",
    "CBT": "Cognitive Behavioural Therapy",
    "CBP": "Cognitive Behavioural Psychology",
}

BANNED = ["transform your life", "life-changing", "revolutionary", "world-class",
          "cutting-edge", "state-of-the-art", "unlock your potential", "empower",
          "holistic", "scientifically proven", "guaranteed results", "proven results"]

TELLS = ["delve", "tapestry", "realm", "seamless", "in today's", "it's worth noting",
         "at the end of the day", "plays a crucial role", "a testament to", "dive into",
         "furthermore", "moreover", "in conclusion", "cornerstone of our", "pivotal",
         "synergy", "leverage", "robust", "myriad", "plethora"]


BASE = os.path.dirname(os.path.abspath(__file__))


def known_urls(path=None):
    path = path or os.path.join(BASE, "urlmap.tsv")
    urls = set()
    for line in open(path):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 2:
            urls.add(parts[1])
    return urls


def check(pid, html, urls, title=""):
    fails = []
    text = re.sub(r"\s+", " ", TAG.sub(" ", html)).strip()
    words = len(text.split())

    if not html.lstrip().startswith("<p>"):
        fails.append("does not open with a paragraph")
    opening = TAG.sub("", html.split("</p>")[0]).strip()
    if not opening.startswith("So "):
        fails.append("no opening line in the reader's words")
    elif "?" not in opening.split(".")[0][:160]:
        fails.append("opening line is not a question")

    if words < 320:
        fails.append(f"too thin at {words} words")
    if words > 1500:
        fails.append(f"too long at {words} words")

    # /help/ links must point at a live article; /learn/ links are checked against the
    # URL structure in DSRD 1 section 2.4, because the Hub is specced ahead of being stocked
    CATEGORIES = ("psychology", "helping-people", "mental-wellness", "motivation",
                  "personal-growth", "general-interest", "wisdom-for-life")
    LEARN = [
        r"^/learn/$",
        r"^/learn/(articles|book-notes|quotes|workbooks)/$",
        r"^/learn/(" + "|".join(CATEGORIES) + r")/$",
        r"^/learn/(" + "|".join(CATEGORIES) + r")/(articles|book-notes|quotes|workbooks)/$",
        r"^/learn/(" + "|".join(CATEGORIES) + r")/(articles|book-notes|quotes|workbooks)/[a-z0-9-]+/$",
        r"^/learn/tags/[a-z0-9-]+/$",
        r"^/learn/authors/[a-z0-9-]+/$",
    ]
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith("/help/") and href not in urls:
            fails.append(f"link target does not exist: {href}")
        if href.startswith("/learn/") and not any(re.match(p, href) for p in LEARN):
            fails.append(f"not a DSRD 1 section 2.4 URL: {href}")

    # full name before any short form, ignoring headings and quoted article titles
    body = HEAD.sub(" ", html)
    body = ANCHOR.sub(lambda m: " " if "?" in TAG.sub("", m.group(0)) else m.group(0), body)
    bt = TAG.sub(" ", body)
    for ac, full in EXPANSIONS.items():
        m = re.search(r"\b" + ac + r"\b", bt)
        if not m:
            continue
        f = bt.lower().find(full.lower())
        if f == -1 or f > m.start():
            fails.append(f"{ac} used before its full name")

    low = text.lower()
    for b in BANNED:
        if b in low:
            fails.append(f"banned phrase: {b}")
    for t in TELLS:
        if t in low:
            fails.append(f"machine-written tell: {t}")
    if "—" in text:
        fails.append("em-dash")
    if re.search(r"\b(we|our|us|We|Our|Us)\b", text):   # not "US", as in US dollars
        fails.append("first person")
    if re.search(r"\bAchology member\b", text):
        fails.append("says 'Achology member'; should read 'member of Achology'")
    if html.count("(") != html.count(")"):
        fails.append("unbalanced brackets")
    if html.count("<a ") != html.count("</a>"):
        fails.append("unterminated link")
    if re.search(r"<p>\s*[a-z]", html):
        fails.append("paragraph starts lower case")

    return words, fails


if __name__ == "__main__":
    urls = known_urls()
    data = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "cur249.json"))
    only = {int(x) for x in sys.argv[2:]} if len(sys.argv) > 2 else None
    bad = 0
    for a in data:
        if only and a["id"] not in only:
            continue
        w, fails = check(a["id"], a["content"], urls, a.get("title", ""))
        if fails:
            bad += 1
            print(f'[{a["id"]}] {w}w  {a.get("title","")[:44]}')
            for f in fails:
                print(f"      {f}")
    print(f"\narticles failing the gate: {bad}")
