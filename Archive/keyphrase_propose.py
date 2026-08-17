#!/usr/bin/env python3
"""Propose a focus keyphrase for each help article, taken from its own opening.

THE RULE, as approved by Chat S232

    The focus keyphrase is the shortest phrase in the article's opening
    paragraph that names what the article is about, two to six words, and it
    must appear verbatim in the article.

This is selection, not invention: every candidate is a run of words already
written in copy Kain and Chat approved. Nothing here writes to the site.

HOW "NAMES WHAT THE ARTICLE IS ABOUT" IS DECIDED, MECHANICALLY

The title already says what the article is about, so the best phrase in the
opening is the one carrying most of the title's meaning:

  1. Take the title's content words (its words less the function words).
  2. Take every run of 2 to 6 consecutive words in the opening paragraph.
  3. Score each run by how many distinct title content words it contains.
  4. Keep the highest score; among those the shortest; among those the earliest.
  5. Reject runs starting or ending on a function word, so a phrase never opens
     with "the" or trails off on "of".

A run scoring zero means the opening shares no content word with the title.
That is an editorial signal rather than a failure of the script, so it is
listed as an exception for Chat and Kain rather than resolved here.

USAGE
    python3 keyphrase_propose.py articles.json > proposal.tsv
"""
import html
import json
import re
import sys

FUNCTION = {
    "a", "an", "the", "and", "or", "but", "if", "so", "than", "then", "that",
    "this", "these", "those", "is", "are", "was", "were", "be", "been", "being",
    "am", "do", "does", "did", "doing", "have", "has", "had", "can", "could",
    "will", "would", "shall", "should", "may", "might", "must",
    "i", "me", "my", "mine", "we", "us", "our", "ours", "you", "your", "yours",
    "it", "its", "they", "them", "their", "there", "here", "he", "she", "his",
    "her", "who", "whom", "whose", "which", "what", "when", "where", "why",
    "how", "of", "for", "in", "on", "at", "to", "by", "with", "from", "into",
    "about", "as", "up", "out", "off", "over", "under", "again", "not", "no",
    "yes", "any", "some", "each", "every", "all", "both", "more", "most",
    "other", "own", "same", "very", "just", "also", "too", "well", "still",
}

STOP_EDGE = FUNCTION  # a phrase never begins or ends on one of these


def norm(text):
    """One spelling of an apostrophe, one kind of space. Both sides of every
    comparison run through this, because a curly apostrophe against a straight
    one was failing the verbatim check on phrases that were genuinely there."""
    return " ".join(text.replace("\u2019", "'").replace("\u2018", "'").split())


WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'-]*")


def words_of(text):
    return WORD.findall(norm(text))


def word_spans(text):
    """Words with their positions, so a phrase can be lifted as the substring
    it actually is. Rejoining tokens with single spaces silently dropped the
    commas between them, and "sessions, or PALS" came back as "sessions or
    PALS", which is not in the article and failed its own verbatim check."""
    return [(m.group(0), m.start(), m.end()) for m in WORD.finditer(norm(text))]


def sentences_of(text):
    """Runs never cross a sentence boundary: "free. The Achology Knowledge Hub"
    is two half-thoughts stitched together, not a phrase anybody types."""
    return [s for s in re.split(r"(?<=[.!?])\s+", norm(text)) if s.strip()]


def opening_paragraph(html_body):
    m = re.search(r"<p\b[^>]*>(.*?)</p>", html_body, re.S | re.I)
    if not m:
        return ""
    return html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))


def propose(title, body_html):
    """Returns (phrase, note). phrase is '' when it must go to Chat."""
    opening = " ".join(opening_paragraph(body_html).split())
    if not opening:
        return "", "no opening paragraph found"

    title_content = {w.lower().strip("'") for w in words_of(title)}
    title_content -= FUNCTION
    if not title_content:
        return "", "the title carries no content words"

    best = None  # (score, -length, -index): highest score, then shortest, then earliest
    offset = 0
    for sentence in sentences_of(opening):
        spans = word_spans(sentence)
        for i in range(len(spans)):
            for n in range(2, 7):
                if i + n > len(spans):
                    break
                run = spans[i:i + n]
                lo = [w.lower().strip("'") for w, _, _ in run]
                if lo[0] in STOP_EDGE or lo[-1] in STOP_EDGE:
                    continue
                score = len(set(lo) & title_content)
                if not score:
                    continue
                key = (score, -n, -(offset + i))
                if best is None or key > best[0]:
                    # the substring as written, punctuation and all
                    best = (key, norm(sentence)[run[0][1]:run[-1][2]])
        offset += len(spans)

    if best is None:
        return "", "the opening shares no content word with the title"

    phrase = best[1].strip(" ,.;:")
    # Verbatim check. The phrase came out of the article, so this can only fail
    # on a punctuation edge, and if it does the phrase is not offered.
    flat = norm(html.unescape(re.sub(r"<[^>]+>", " ", body_html)))
    if phrase.lower() not in flat.lower():
        return "", "chosen phrase did not survive the verbatim check"
    return phrase, "from the opening"


def main():
    arts = json.load(open(sys.argv[1]))
    for a in arts:
        title = a["title"] if isinstance(a.get("title"), str) else a["title"]["rendered"]
        title = html.unescape(title)
        body = a["content"] if isinstance(a.get("content"), str) else a["content"]["rendered"]
        phrase, note = propose(title, body)
        opening = " ".join(opening_paragraph(body).split())[:160]
        print("\t".join([str(a["id"]), title, phrase, note, opening]))


if __name__ == "__main__":
    main()
