#Syntax

#def <name>:
#    indented block of code 
#return value 

"""def say_hello():
    print("Hello, I am a function output")

say_hello()"""

#doc strings 
''' def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello(username="Rick", language="FR")

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country_info(country):

    if country == "Russia":
        capital == "Moscow"
        population = 14380000

        print("Welcome to", capital,country)

    
country_info("Theed", "Naboo")

students = ["Harry", "Hermione", "Rone", "Luna"]

def welcome():
    for name in students:
        print(f"{name}, welocome to Hogarts!")
    
welcome()

l1 = [1, 2, 3, 4, 5, 6]
l1.append(3)
l1.append([7, 8, 9])
l1.extend([6, 7, 8])
print(l1)

l1=[1, 2, 3, 4, 5, 6]
l1.insert(2, 6)
print(l1)

l2 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
s = l2.count(4)
print(s)


a = ["b", "g", "a", "d", "f", "c", "h", "e"]
x = sorted(a)
print("a after sorted function")
print(a)
print(x)
b = [1, 2, 5, 8, 3]
b.sort()
print(b)

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[0:4])
print(lst[::])
print(lst[::-1])

def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello(username="Rick", language="FR")
say_hello(language="FR", username="Rick")
say_hello("Rick", language="FR")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

def calculation(a, b):
    addition = a+b
    subtraction = a-b
    return addition, subtraction


res = calculation(int(input("Print number a:")), int(input("Print number b:")))
print(res)


usernames = ["steve", "john", "dina", "polina"]
def greet_users(users):
    for user in usernames:
        print("Hello " + user.title())

greet_users(usernames)
    

def my_f1():
    print("Hello")

def my_f2():
    print("Word")

def my_f3():
    print("This is Rick!")

list_of_functions = [my_f1, my_f2, my_f3]

for func in list_of_functions:
    func()

def print_models(unprinted_designs, completed_models):
    """    
    Simulate printing each design until none are left.    
    Move each design to completed_models after printing.    
    """

    while unprinted_designs:        
        current_design = unprinted_designs.pop()            

        # Simulate creating a 3D print from the design.        
        print("Printing model: " + current_design)        
        completed_models.append(current_design)        

def show_completed_models(completed_models):    
    """
    Show all the models that were printed.
    """    
    print("\nThe following models have been printed:")   
    for completed_model in completed_models:        
        print(completed_model)        

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print("Full list of models", unprinted_designs)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def upper_string(s):
    return s.upper()


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)
print(list(map_object))


def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

def short_name(name):
    return len (name) <= 4

def say_hello(name):
    return f"Hello, {name}!"

filtered_people = filter(short_name, people)
greetings = map(say_hello, filtered_people)
print(list(greetings))

x = 10
x = x+5
print(x)

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)'''

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result