'''#Basic Value Types
#Strings
my_name = "Diana Talis"

#chck the leght
print(len("diana"))

#indexs start from 0
print(my_name[3])

#String functions / String methods

print(my_name.lower())
print(my_name.upper())
print(my_name.capitalize())
print(my_name.title())

student = "Harry Potter"
student2 = student.replace("Harry", "Giny")
print(student2)

price = "15$"
clean_price = price.strip("$")
print(clean_price)

description = "strings are..."
print(description.upper())
description2 = description.replace("are","is") 
print(description2)

description3 = description.replace("are...","      ") 
print(description3)

print(description[0: 7])

#Numbers
age = 35
print(age+1)
print(7+ (-5))
print(10/3)
print(10%3)
division = 10 / 3
print(round(division,2))

#Type Casting
age = int(input("how old are you?"))
print(type(age))
print(age+10)

height = float(input("What is your height?"))
print(height)

#Booleans (True and False)
print(5<7)
print("5" == 5)
print(-1 != 1)

#General Useful knowlefge
my_string = " Hello World"
Python = " Python is fun"
print(my_string + Python)
print((my_string + Python)*3)

#Special characters
print("Hi User\n")

print("Hi User\t")'''

user_name = input("What's your name?")
print(f"Welcome " + user_name)
print(f"Welcome, {user_name}")

#Create a variable called first_name and a variable called last_name, and then print your full name using those two variables
first_name = input("What is your first name?")
last_name = input("What is your last name?")
print(first_name, last_name)