# anagram_checker.py
from pathlib import Path
from typing import List, Set


class AnagramChecker:
    """
    Load a word list and provide:
      - is_valid_word(word): bool
      - is_anagram(word1, word2): bool
      - get_anagrams(word): List[str]

    Notes:
      * All comparisons are case-insensitive.
      * Only alphabetic words are kept from the word list.
      * This class never prints; it only returns values.
    """

    def __init__(self, wordlist_path: str | Path):
        path = Path(wordlist_path)
        if not path.exists():
            raise FileNotFoundError(f"Word list not found: {path.resolve()}")

        words: Set[str] = set()
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                w = line.strip().lower()
                if w.isalpha():
                    words.add(w)

        if not words:
            raise ValueError("Word list is empty or contained no pure alphabetic entries.")

        self._words = words

    def is_valid_word(self, word: str) -> bool:
        """Return True if 'word' exists in the loaded word list (case-insensitive)."""
        if not word or not word.isalpha():
            return False
        return word.lower() in self._words

    @staticmethod
    def is_anagram(word1: str, word2: str) -> bool:
        """
        Return True if word1 and word2 are anagrams (same letters, different order),
        ignoring case, and not exactly the same word.
        """
        if not (word1 and word2):
            return False
        a = word1.lower()
        b = word2.lower()
        if not (a.isalpha() and b.isalpha()):
            return False
        if a == b:
            return False
        return sorted(a) == sorted(b)

    def get_anagrams(self, word: str) -> List[str]:
        """
        Return all anagrams of 'word' that exist in the word list, excluding the word itself.
        """
        w = word.lower()
        if not w.isalpha():
            return []
        target_sorted = sorted(w)
        # Iterate through the loaded words and collect anagrams
        return [cand for cand in self._words if cand != w and sorted(cand) == target_sorted]