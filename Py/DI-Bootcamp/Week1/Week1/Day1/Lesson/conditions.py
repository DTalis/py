#Conditionals 

#Syntax
#if {condition}
#(indented block) (action)

'''if 5 > 3:
        print("Hello World")

user_num = int(input("Guess a number"))
secret_number = 18

if user_num == secret_number:
    print("You win!")

elif user_num == 7:
    print("My lucky number")

elif user_num < 1:
    print("No negative numbers")

else:
    print("Try again!")'

#use the len() function to check the lenght of the name. if it is less than 5 letter print('You have a short name :)')

user_name = input("what is your name?")
number = len(user_name)
if number < 5:
    print("You have a short name")
else:
    print("you are alriaght")

Exercise
#Ask the user for their age using the input() function and store it in a variable age.
#Convert the inputted age into an integer and calculate the number of years until they turn 100.
#Display a message: "You will turn 100 in X years", where X is the number of years calculated.

user_age = int(input("How old are you?"))
user_age_100 = 100 - user_age
print(f"You will turn 100 in {user_age_100} years")'''

#Exercise
#Ask the user for a number between 1 and 100
#If the number is a divisible by three, print Fizz
#If the number is a divisible by five, print Buzz.
#If the number is a divisible by both three and five, print FizzBuzz instead.

user_number = int(input("Enter a number between 1 and 100: "))

if (user_number % 3 == 0) and (user_number % 5 == 0):
    print("FizzBuzz")
elif (user_number % 3 == 0):
    print("Fizz")
elif (user_number % 5 == 0):
    print("Buzz") 
else:
    print("You should try different number")