
print("\n🌟Challenge 1: Sorting")
my_list = input("Enter words separated by commas: ")
print(f"Your list is: {my_list}")

words = my_list.split(',')

words.sort()

sorted_string = ','.join(words)

print(sorted_string)


print("\n🌟Challenge 2: Longest Word")
def longest_word(sentence):
    each_word = sentence.split()
    longest = ""
    max_length = 0
    for word in each_word:
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    return longest

# Get sentence input from the user
user_sentence = input("Enter a sentence: ")

# Find and print the longest word
print(longest_word(user_sentence)) s