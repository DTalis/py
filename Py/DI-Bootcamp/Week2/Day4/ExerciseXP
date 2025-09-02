print("\n🌟 Exercise 1: Random Sentence Generator")
import random

def get_words_from_file(file_path):

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_list = content.split()
            return word_list
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_random_sentence(length, word_file='words.txt'):

    words = get_words_from_file(word_file)
    if not words:
        return "No words available to create a sentence."

    selected_words = [random.choice(words) for _ in range(length)]
    sentence = ' '.join(selected_words).lower()
    return sentence


def main():

    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence from a word list.")
    
    try:
        user_input = input("Enter the desired sentence length (2-20): ")
        sentence_length = int(user_input)

        if 2 <= sentence_length <= 20:
            sentence = get_random_sentence(sentence_length)
            print("\nGenerated sentence:")
            print(sentence)
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()

print("\n🌟 Exercise 2: Working With JSON")
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)


salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)


data["company"]["employee"]["birth_date"] = "1992-05-13" 

with open("modified_employee.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified JSON saved in 'modified_employee.json'")
