
print("\n🌟Exercise 1: What Are You Learning?")

def display_message():
    print("I am learning about functions in Python.")

display_message()


print("\n🌟Exercise 2: Whats Your Favorite Book?")
def favorite_book (title):
    print("One of my favorite book is {title}")

favorite_book("Alice in Wonderland")



print("\n🌟Exercise 3: Some Geography")
def describe_city(city, country = "Unknown"):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")
describe_city("Moscow")


 
print("\n🌟Exercise 4: Random")
import random

user_number = int(input("Enter number from 1 to 100:"))  

def guess_numbers (user_number):
    random_number = random.randint(1, 100)

    if random_number == user_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")
  
guess_numbers(user_number)



print("\n🌟 Exercise 5: Lets Create Some Personalized Shirts!")

def make_shirt(size = "large", text = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")

#Bonus
make_shirt(size="small", text="Hello!")


print("\n🌟 Exercise 6: Magicians…")
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
def show_magicians(magician_names):
    for magition in magician_names:
        print(magition)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"


make_great(magician_names)
show_magicians(magician_names)



print("\n🌟 Exercise 7: Temperature Advice")

import random
def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10.0, 10.0), 1)
    elif season == "spring":
        return round(random.uniform(5.0, 20.0), 1)
    elif season == "summer":
        return round(random.uniform(20.0, 40.0), 1)
    elif season == "autumn":
        return round(random.uniform(5.0, 20.0), 1)
    else:
        return round(random.uniform(-10.0, 40.0), 1)


def main():
    month = int(input("Enter the month as a number (1-12): "))
    
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    elif month in [9, 10, 11]:
        season = "autumn"
    else:
        season = "unknown"

    temp = get_random_temp(season)
    print(f"\nThe temperature right now is {temp}°C.")

    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 24:
        print("Nice weather.")
    elif temp < 33:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()