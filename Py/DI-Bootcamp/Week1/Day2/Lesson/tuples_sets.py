'''numbers = (10, 20, 30, 40, 50)
number2 = tuple(numbers)
print(number2)

#number2[1] = 200 #error because tuples are imutable
print(numbers[1])

print(numbers.count(20))
print(numbers.index(20))

fruits = ("apple", "mango", "kiwi", "lime")
vegs = ("tomato", "potato", "lettuce")

fruits_vegs = fruits + vegs
print(fruits_vegs)

a,b,c,d,e = numbers
print(a)
print(b)
print(c)
print(d)
print(e)

#sets no duplicates 
my_set = {1,4,8,9}
my_set2 = set(my_set)
print(my_set, my_set2)

my_set.add(55)
print(my_set)

user_names = ["July", "John", "Joli", "Bob", "John", "Joli", "Alex"]
set_user_name = set(user_names)
clean_user_name = list(set_user_name)
print(clean_user_name)

names = {"Julia", "Israel", "Dina"}
countries = {"USA", "Brazil", "Israel"}

print(names.intersection(countries))
print(names.difference(countries))
print(countries.difference(names))'''

#create a set of your favorite colors, erite code that:
#adds a new color to the set
#Finds the common elements between two sets (use the set of your friends favorite colors )
#remove all elements from the set from favorite colors 

my_colors = ("Red", "Yellow", "White", "Black")
set_my_colors = set(my_colors)
set_my_colors.add("Pink")

friend_colors = ("Red", "Purple", "Green", "Black")
set_friend_colors = set(friend_colors)

common_elements = set_my_colors.intersection(set_friend_colors)
print(common_elements)

set_my_colors.clear()