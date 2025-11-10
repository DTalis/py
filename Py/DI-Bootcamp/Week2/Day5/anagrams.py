# anagrams.py
from pathlib import Path
from anagram_checker import AnagramChecker

DEFAULT_WORDLIST = (Path(__file__).parent / "sowpods.txt").resolve()

BANNER = """
=============================
      🔤 ANAGRAM CHECKER
=============================
1) Enter a word
2) Change word list (current: {wordlist})
3) Exit
"""

def read_single_word() -> str:
    raw = input("Enter a single word (letters only): ").strip()
    # Validate: single token, alphabetic only
    if not raw:
        raise ValueError("Empty input.")
    # More than one word?
    if len(raw.split()) != 1:
        raise ValueError("Only one word is allowed (no spaces).")
    if not raw.isalpha():
        raise ValueError("Only alphabetic characters are allowed.")
    return raw

def main():
    wordlist_path = DEFAULT_WORDLIST

    # Load initial word list (with retry on error)
    while True:
        try:
            checker = AnagramChecker(wordlist_path)
            print(f"📚 Loaded word list: {Path(wordlist_path).resolve()}")
            break
        except (FileNotFoundError, ValueError) as e:
            print(f"⚠️ {e}")
            wordlist_path = input("Enter a valid path to a word list (or 'q' to quit): ").strip()
            if wordlist_path.lower() == "q":
                return

    while True:
        print(BANNER.format(wordlist=wordlist_path))
        choice = input("Choose 1/2/3: ").strip()

        if choice == "1":
            try:
                word = read_single_word()
            except ValueError as ve:
                print(f"❌ {ve}")
                continue

            is_valid = checker.is_valid_word(word)
            anags = checker.get_anagrams(word)

            # Pretty output (all caps like the sample, but not required)
            up = word.upper()
            print("\nYOUR WORD :", f"\"{up}\"")
            print("this is a valid English word." if is_valid else "this is NOT a valid English word.")
            if anags:
                print("Anagrams for your word:", ", ".join(sorted(anags)))
            else:
                print("Anagrams for your word: (none found)")
            print()

        elif choice == "2":
            newp = input("Enter new word list path: ").strip()
            try:
                checker = AnagramChecker(newp)
                wordlist_path = newp
                print(f"✅ Switched to: {Path(wordlist_path).resolve()}")
            except (FileNotFoundError, ValueError) as e:
                print(f"❌ {e}\n(Keeping previous word list.)")

        elif choice == "3":
            print("👋 Bye!")
            return

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()