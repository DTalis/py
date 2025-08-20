#Exercise1
print("\n---Exercise 1 : Hello World---")
print("\nHello world" * 4)

#Exersice2
print("\n---Exercise 2 : Some Math---")
print((99^3)*8)

#Exersice3
print("\n---Exercise 3 : What Is The Output ?---")
print(5 < 3)
print(3 == 3)
print(3 == "3")
print("3 > 3")       #wrong line, check with teacher
print("Hello" == "hello")

#Exersice4
print("\n---Exercise 4 : Your Computer Brand---")
computer_brand = "Mac"
print(f"I have a {computer_brand} computer.")

#Exersice5
print("\n---Exercise 5 : Your Information---")
name = "Diana"
age = 33
shoe_size = 39
info = f"Hi! My name is {name}. I'm {age} years old. My shoe size is {shoe_size}. Nice to meet you!"
print(info)

#Exersice6
print("\n---Exercise 6 : A & B---")
'''Create two variables, a and b.
Each variable’s value should be a number.
If a is bigger than b, have your code print "Hello World".'''
a = 20
b = 15
if a > b:
    print("Hello world")

#Exersice7
print("\n---Exercise 7 : Odd Or Even---")
'''Write code that asks the user for a number and determines whether this number is odd or even.'''
user_number = int(input("Enter a whole number: "))
if user_number % 2 == 0:
    print(f"The number {user_number} is even.")
else:
    print(f"The number {user_number} is odd.")

#Exersice8
print("\n--- Exercise 8 : What’s Your Name ?---")
'''Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.'''
my_name = "Diana"
user_name = input("What is your name? ")

if my_name == user_name:
    print("We have the same names! *It should be a funny joke here, but I didn't create it*")
else:
    print("Our names are not the same! *It should be a funny joke here, but I didn't create it*")

#Exersice9
print("\n--- Exercise 9 : Tall Enough To Ride A Roller Coaster---")
'''Write code that will ask the user for their height in centimeters.
If they are over 145 cm, print a message that states they are tall enough to ride.
If they are not tall enough, print a message that says they need to grow some more to ride.'''
user_height = int(input("What is your height in centimeters? "))
if user_height > 145:
    print("Congratulations! You are tall enough to ride.")
else:
    print("Sorry, but you need to grow some more to ride")