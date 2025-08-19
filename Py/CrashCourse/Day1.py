print("hello world");
age = input("Enter your age: ")
print("You are " + age + " years old")


#Python Data Types
#Exercise 1
#calculate the sum of 10 and 3.
result_1 = 10+3
print(result_1);
#Subtract 7 from 15
result_2 = 15-7
print(result_2);
#Multiply 4 by 8
result_3 = 4*8
print(result_3);
#Divide 18 by 3
result_4 = 18/3;
print(result_4)
#find how many whole times 11 can be divided by 4
result_5 = 11//4;
print(result_5)
#Find the remainder when 9 is divided by 4 using the modulus operator
result_6 = 9%4;
print(result_6)
#Raise 6 to the power of 3
result_7 = 6 ** 3
print(result_7)
#Use the negation operator to make the number 12 negative
result_8 = -12
print(result_8)

#Exercise 2
#1. Create a list of fruits and print the second fruit of your list.
Fruits = ["Apple", "Banana", "Orange", "Fig"]
print(Fruits[1]) 
#2. Create a set of numbers and try to print the last index of it.
Numbers = {1,2,3,4,5}
#print(Numbers[-1])

#3. Create a tuple of 5 Star Wars characters names and print the third name.
star_wars_characters = ("Luke Skywalker", "Darth Vader", "Leia Organa", "Yoda", "Han Solo")
print(star_wars_characters[2])
#4. Create a dictionary with the information about a woman called Alice, 23 years old that lives in New York.
Woman = {
    "Name" : "Alice",
    "Age" : 23,
    "City" : "New York"
}
print(Woman)


#Conditionals And If Statements
#Exercise 1
name = "Matt"
if name == "Matt":
    print("Your name is Matt")
elif name == John:
    print("Your name is John")
    print("Bye!")

#Exercise 2
# Prompt the user for input
secret_word = input("Guess the secret word: ")

if secret_word == "Python":
    print("Correct! You guessed the secret word!")
elif secret_word == "Java":
    print("Not quite, but close!")
else:
    print("Try again!")

 #Exercises XP
#1. Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

#2. Write a comment that says "This is a comment."
#This is a comment.

#3. Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

#4. Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 and 4 > 2:
    print("Math is fun")
#5. Assign a variable called nope to an absence of value.
nope = None
#6. Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.

#7. Calculate the length of the string "What's my length?"
string1 = len("What's my length?")
print(f"The length of the string is: {string1}")

#8. Convert the string "i am shouting" to uppercase.
string2 = "i am shouting".upper()
print(f"Uppercase_string{string2}")

#9. Convert the string "1000"to the number 1000.
number_from_string = int("1000")
print(f"The type of '1000' is {type('1000')}, and the type of the converted number is {type(number_from_string)}")

#10. Combine the number 4 with the string "real" to produce "4real".
combined_string = str(4) + "real"
print(f"The combined string is: {combined_string}")

#11. Record the output of the expression 3 * "cool".
three_times_cool = 3 * "cool"
print(three_times_cool)

#12. Record the output of the expression 1 / 0.
try: 
    result = 1/0
except ZeroDivisionError:
     print("Error")

#13. Determine the type of [].
list_type = type([])
print(f"The type of [] is: {list_type}")

#14. Ask the user for their name, and store it in a variable called name.
name1 = input("What is your name?")
print(f"Hello, {name1}!")

#15. Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!.
user_input = input("What is your number")
user_number = float(user_input)
if user_number < 0:
    print("That number is less than 0!")
elif user_number > 0:
    print("That number is greater than 0!")
else:
    print ("You picked 0!")

#16. Find the index of "l" in "apple".\
print("apple".index("l"))

#17. Check whether "y" is in "xylophone".
print("Is 'y' in 'xylophone'?", "y" in "xylophone")

#Check whether a string called my_string is all in lowercase.
my_string = input("write a srting")
print("Is the string all in lowercase?", my_string.islower())