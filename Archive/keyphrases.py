#!/usr/bin/env python3
"""Focus keyphrases for the 249 help articles, by Chat's S230 formula.

The formula, quoted from `00__RULING__Help_Article_Focus_Keyphrase_Standard.md`:

  1. Take the article's existing question title.
  2. Strip the question filler and function words: how do I, how can I, what
     is, what are, can I, do I, where, when, why, is, are, the, my, a, an, and
     similar.
  3. Keep the distinctive words that carry the question's meaning, in their
     natural order.
  4. The result is 2 to 6 words, lowercase (proper nouns keep their capitals,
     e.g. Achology).
  5. Where an Achology term from the locked register (DSRD 2 section 2.24)
     appears, use the register's exact words for it.

Exceptions are listed, never judged: a duplicate across two or more articles,
an ambiguous or empty result, or a result that will not come down to six words
without choosing which meaning to keep. Those get no keyphrase set, and travel
back to Chat.

Reads titles.tsv (id<TAB>title), writes proposed.tsv and exceptions.tsv.
Sets nothing by itself: applying is a separate, deliberate step.
"""
import re
import sys

# Step 2. Function words: question openers, auxiliaries, pronouns, articles,
# prepositions and conjunctions. Prepositions are function words and go with
# the rest, which is what "and similar" covers in the ruling. Content words
# stay, including ones that look small ("many", "free", "own"), because they
# are what a person actually types. Nothing here is chosen per article.
FILLER = {
    "how", "do", "does", "did", "doing", "can", "could", "will", "would",
    "shall", "should", "is", "are", "am", "was", "were", "be", "been", "being",
    "have", "has", "had", "get", "got",
    "what", "whats", "which", "who", "whom", "whose", "where", "when", "why",
    "i", "me", "my", "mine", "we", "us", "our", "you", "your", "yours",
    "it", "its", "they", "them", "their", "there", "that", "this", "these",
    "those", "a", "an", "the", "if", "any", "some", "exactly", "actually",
    "of", "for", "in", "on", "at", "to", "by", "with", "from", "into",
    "about", "as", "and", "or", "but", "than", "then", "so",
}

# Step 4. Proper nouns keep their capitals. These are the register's own terms
# (DSRD 2 section 2.24) plus the brand word, so the keyphrase reads the way the
# register writes it rather than the way a lowercasing pass would leave it.
KEEP_CAPS = {
    "achology", "achology.com", "achologist", "achologists", "valts", "valt",
    "pals", "cips", "somap", "dimap", "amap", "alt", "alts", "cpd", "nlp",
    "cbt", "cbp", "miw", "pgd", "ukrlp", "prn", "uk", "us", "hot",
}
CAPS_FORM = {
    "achology": "Achology", "achology.com": "Achology.com",
    "achologist": "Achologist", "achologists": "Achologists",
    "valts": "VALTS", "valt": "VALT", "pals": "PALS", "cips": "CIPS",
    "somap": "SoMAP", "dimap": "DiMAP", "amap": "AMAP", "alt": "ALT",
    "alts": "ALTs", "cpd": "CPD", "nlp": "NLP", "cbt": "CBT", "cbp": "CBP",
    "miw": "MIW", "pgd": "PGD", "ukrlp": "UKRLP", "prn": "PRN",
    "uk": "UK", "us": "US", "hot": "HOT",
}

MIN_WORDS, MAX_WORDS = 2, 6


def keyphrase(title):
    """Returns (phrase, problem). One of the two is always empty."""
    t = title.strip().rstrip("?").replace("’", "'")
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'./-]*", t)
    kept = []
    for w in words:
        low = w.lower().strip(".'")
        if low in FILLER:
            continue
        # A possessive is the same proper noun: "Achology's" keeps its capital.
        stem = low[:-2] if low.endswith("'s") else low
        if stem in KEEP_CAPS:
            kept.append(CAPS_FORM[stem] + ("'s" if stem != low else ""))
        else:
            kept.append(w.lower())
    if len(kept) < MIN_WORDS:
        return "", "the formula leaves fewer than two words"
    if len(kept) > MAX_WORDS:
        return "", ("the formula leaves %d words: %s. Cutting it to six means "
                    "choosing which part of the question to keep"
                    % (len(kept), " ".join(kept)))
    return " ".join(kept), ""


def main():
    rows = []
    for line in open(sys.argv[1] if len(sys.argv) > 1 else "titles.tsv"):
        line = line.rstrip("\n")
        if not line or "\t" not in line:
            continue
        pid, title = line.split("\t", 1)
        rows.append((pid, title))

    proposed, exceptions = [], []
    for pid, title in rows:
        phrase, problem = keyphrase(title)
        (exceptions if problem else proposed).append((pid, title, phrase or problem))

    # A duplicate is an exception on every article that shares it, not just the
    # second one: which article owns the phrase is an editorial call.
    seen = {}
    for pid, title, phrase in proposed:
        seen.setdefault(phrase, []).append(pid)
    dupes = {p for p, ids in seen.items() if len(ids) > 1}
    final = [(p, t, k) for p, t, k in proposed if k not in dupes]
    for pid, title, phrase in proposed:
        if phrase in dupes:
            exceptions.append((pid, title,
                               "duplicate keyphrase \"%s\", shared with %s"
                               % (phrase, ", ".join(x for x in seen[phrase] if x != pid))))

    with open("proposed.tsv", "w") as f:
        for pid, title, phrase in final:
            f.write("%s\t%s\t%s\n" % (pid, title, phrase))
    with open("exceptions.tsv", "w") as f:
        for pid, title, problem in exceptions:
            f.write("%s\t%s\t%s\n" % (pid, title, problem))

    print("%d articles: %d keyphrases, %d exceptions"
          % (len(rows), len(final), len(exceptions)))


if __name__ == "__main__":
    main()
