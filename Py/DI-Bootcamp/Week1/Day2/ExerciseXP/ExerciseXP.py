
print("\n---Exercise 1: Favorite Numbers---")

my_fav_numbers = {1, 7, 13, 18}
my_fav_numbers.add(17)
my_fav_numbers.add(45)
print(my_fav_numbers)

my_fav_numbers.remove(45)
print(my_fav_numbers)

Friend_fav_numbers = {5, 7, 13, 88}
our_fav_numbers = my_fav_numbers.union(Friend_fav_numbers)
print(our_fav_numbers)


print("\n---Exercise 2: Tuple---")

## This exercise will cause an error because tuples are immutable


print("\n---Exercise 3: List Manipulation---")
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.

list = ["Banana", "Apples", "Oranges", "Blueberries"]
print(list) #original list

list.remove("Banana")
print(list)

list.remove("Blueberries")
print(list)

list.append("Kiwi")
print(list)

list.insert(0, "Apples")
print(list)

apple_count = list.count("Apples")
print(apple_count)

list.clear()
print(list)

print(f"Final state of the list : {list}")


print("\n---Exercise 4: Floats---")
#Create a list containing the following sequence of mixed floats and integers: 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.

list = []
start_number = 1.5
while start_number <= 5:
    list.append(start_number)
    start_number += 0.5

print(list)


print("\n---Exercise 5: For Loop---")
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.

for number1 in range(1, 20):
    print(number1)

for number1 in range(1, 21, 2):
    print(number1)


print("\n---Exercise 6: While Loop---")
#Write a while loop that keeps asking the user to enter their name.
#Stop the loop if the user’s input is your name.

name = "Diana"
while True:
    user_name = input("What is my name? ")
    if user_name == name:
        print("This is correct!")
        break
else:
    print("Try again!")

    
print("\n---Exercise 7: Favorite Fruits---")
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print: "You chose one of your favorite fruits! Enjoy!"
#If not, print:"You chose a new fruit. I hope you enjoy it!"

fav_fruit = input("What are your favourite fruits? ")
fav_fruit = [fav_fruit]

fav_fruit1 = input("Enter the name of any fruit ")

if fav_fruit1 in fav_fruit:
    print("You chose one of your favorite fruits! Enjoy!")

else:
    print("You chose a new fruit. I hope you enjoy it!")



print("\n---Exercise 8: Pizza Toppings---")
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print: "Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10.00
topping_cost = 2.50

while True:
    topping = input("Enter a topping you'd like to add (or type 'quit' to finish): ")

    if topping == 'quit':
        break

    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

total_cost = base_price + (len(toppings) * topping_cost)

print("\n--- Your Pizza Order ---")
print(f"Base price: ${base_price:}")
print(f"Cost per topping: ${topping_cost:}")
print(f"Total cost: ${total_cost:}")


print("\n---Exercise 9: Cinemax Tickets---")
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.

total_cost_tickets = 0
Number_of_people = int(input("How many visitors?"))

for i in range(Number_of_people):
    age = int(input(f"Enter the age of person number {i + 1}: "))

    if age < 3:
        ticket_price = 0
        print("Your ticket is free")

    elif 3 < age < 13:
        ticket_price = 10
        print("Your ticket costs 10$")
    elif age >= 13:
        ticket_price = 15
        print("Your ticket costs 15$")

    total_cost_tickets += ticket_price

print(f"\nThe total price for all tickets is: ${total_cost_tickets}")


print("\n---Exercise 10: Sandwich Orders---")
#Using the list:sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
#The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
#Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
#Print a message for each sandwich made, such as: "I made your Tuna sandwich."
#Print the final list of all finished sandwiches.


sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

finished_sandwiches = []

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("Finished sandwiches:", finished_sandwiches)

