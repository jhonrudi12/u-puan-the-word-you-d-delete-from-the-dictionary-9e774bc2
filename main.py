#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun bounty entry.

Writes a single word to /output/entry.txt: the one word to erase from
the dictionary forever, chosen by scoring a shortlist against the
judge's brief (a real word first, then funny at first sight, then the
humour coming from the word itself, then fresh, then exact).
"""

import os

# Candidates, scored 0-5 on the judge's criteria in order:
# (real word, funny at first sight, humour from the word itself,
#  fresh pick, exact one word)
CANDIDATES = {
    "colonel":       (5, 5, 5, 5, 5),
    "queue":         (5, 4, 5, 4, 5),
    "utilize":       (5, 4, 4, 3, 5),
    "Wednesday":     (5, 4, 4, 3, 5),
    "flammable":     (5, 4, 4, 3, 5),
    "mnemonic":      (5, 3, 4, 4, 5),
    "defenestration": (5, 3, 4, 4, 5),
    "moist":         (5, 4, 3, 1, 5),
    "irregardless":  (5, 4, 3, 1, 5),
    "supposably":    (4, 3, 3, 4, 4),
}

# Judge weighs the criteria most important first, so earlier
# criteria count more than later ones.
WEIGHTS = (5, 4, 3, 2, 1)


def score(word: str) -> int:
    """Weighted score of one candidate word."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[word]))


def pick_word() -> str:
    """Return the highest-scoring word; ties break to the shorter word."""
    return min(CANDIDATES, key=lambda w: (-score(w), len(w)))


def main() -> None:
    word = pick_word()
    assert 1 <= len(word) <= 77, "entry must be 1-77 characters"
    assert word.strip(), "entry must not be only whitespace"
    assert word == word.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in word and "\r" not in word, "entry must be a single line"
    assert " " not in word, "entry must be a single word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
