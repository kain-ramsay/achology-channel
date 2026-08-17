#!/usr/bin/env python3
"""Kain's S230 wording change across the help articles, applied mechanically.

Two replacements, both his instruction, both recorded verbatim in
NOTE__Kains_Words_Peer_To_Peer_And_Level_Names.md:

  Peer-Peer          -> Peer-to-Peer      (it reads badly aloud)
  Senior Achologist I / II -> Senior Achologist (Level One) / (Level Two)

Longest patterns run first, so "Senior Achologist I and II" is never left as
"Senior Achologist (Level One) and II". The bare "Senior I" and "Senior II"
take the full name, so every mention on the site reads the same way.

Reads a WP REST style dump on stdin, writes a TSV of id, field, new value for
only the posts that change. Sets nothing itself.
"""
import json
import re
import sys

RULES = [
    # (pattern, replacement). Order matters: longest first.
    (r"\bSenior Achologist I and II\b", "Senior Achologist (Levels One and Two)"),
    (r"\bSenior Achologist II\b", "Senior Achologist (Level Two)"),
    (r"\bSenior Achologist I\b", "Senior Achologist (Level One)"),
    (r"\bSenior II\b", "Senior Achologist (Level Two)"),
    (r"\bSenior I\b", "Senior Achologist (Level One)"),
    (r"Peer-Peer", "Peer-to-Peer"),
    (r"peer-peer", "peer-to-peer"),
]


def apply(text):
    for pat, rep in RULES:
        text = re.sub(pat, rep, text)
    return text


def main():
    arts = json.load(sys.stdin)
    changed = 0
    for a in arts:
        for field, raw in (("post_title", a["title"]["rendered"]),
                           ("post_content", a["content"]["rendered"])):
            new = apply(raw)
            if new != raw:
                changed += 1
                sys.stdout.write("%s\t%s\t%s\n"
                                 % (a["id"], field, new.replace("\n", "\\n")))
    print("%d fields changed" % changed, file=sys.stderr)


if __name__ == "__main__":
    main()
