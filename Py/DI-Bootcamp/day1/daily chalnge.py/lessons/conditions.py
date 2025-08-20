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
    print("you are alriaght")'''

#Exercise
user_number = int(input("Number between 1 to 100"))
user_number_3 = user_number % 3
user_number_5 = user_number % 5
if user_number_3 == 0:
    print("Fizz")