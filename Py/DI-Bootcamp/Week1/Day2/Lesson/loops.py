#sequences that we can loop through it
#strings
#lists
#tuples
#sets
#range

for char in "student":
    print(char)

fruits = ["apple", "mango", "kiwi", "lime"]
for each_fruit in fruits:
    print(f"I love {each_fruit}")

print(list(range(3, 11, 3)))


student = "Hermione"
for i in range(len(student)):
    if i == 5:
     print(i)

#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.

print(list(range(1, 21)))

for i in range(1, 21):
    print(i)

numbers = []
for i in range(1, 21):
    numbers.append(i)

for i in numbers:
    if numbers.index(i) % 2 == 0:
        print(i)

while i <= 10:
    print("Hello")
    i+=1

#List1 = [5, 10, 15, 20, 25, 50, 20]


#find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [5, 10, 15, 20, 25, 50, 20]

# The value we are looking for
value_to_find = 20

# The value we will replace it with
new_value = 200

# Since we know the value exists, we can directly find its index.
# The .index() method will find the index of the first occurrence of the value.
index_to_update = list1.index(value_to_find)

# Use the found index to update the list.
list1[index_to_update] = new_value

# Print the updated list to show the result.
print(f"The updated list is: {list1}")

a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a)
print(b)
print(c)
print(d)

number = int(input("Print a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

number = 1
while number < 10:
    print(number)
    number += 1

active = True

while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")