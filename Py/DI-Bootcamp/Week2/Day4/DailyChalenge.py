import re
import string

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else None

    def most_common_word(self):
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        if frequency:
            return max(frequency, key=frequency.get)
        return None

    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return cls("")
class TextModification(Text):

    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned = self.text.translate(translator)
        return cleaned

    def remove_stop_words(self):
        stop_words = {
            'a', 'an', 'the', 'is', 'in', 'at', 'of', 'on', 'and', 'or', 'if', 'to', 'for', 'with', 'as', 'by', 'that'
        }
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return cleaned
