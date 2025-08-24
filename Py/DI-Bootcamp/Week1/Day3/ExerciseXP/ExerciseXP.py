print("\n---Exercise 1: Converting Lists Into Dictionaries---")
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Use zip() to pair the lists, then convert to a dictionary
my_dict = dict(zip(keys, values)) 

print(my_dict)


print("\n---Exercise 2: Cinemax #2---")
# Sample family dictionary
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def get_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15
    
total_cost = 0

print("Ticket price: ")
for member, age in family.items():
    price = get_ticket_price(age)
    print(f"{member} (age {age}): ${price}")
    total_cost += price

print(f"\nTotal Cost: ${total_cost}")

print("\n---Exercise 2: Cinemax #2. Bonus---")
def get_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

family = {}

print("Enter names and ages of family members.")
print("Type 'done' when finished.")

while True:
    name = input("Name: ")
    if name.lower() == 'done':
        break
    age_input = input(f"Age of {name}: ").strip()
    
    if age_input:
        age = int(age_input)
        family[name] = age

total_cost = 0

print("\nTicket price:")
for name, age in family.items():
    price = get_ticket_price(age)
    print(f"{name} (age {age}): ${price}")
    total_cost += price

print(f"\nTotal Cost: ${total_cost}")

print("\n---Exercise 3: Zara---")
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
#Change the value of number_stores to 2.
brand["number_stores"] = 2

#Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara caters to {', '.join(brand['type_of_clothes'])}")

#Add a new key country_creation with the value Spain.
brand['country_creation'] = "Spain"

#Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#Delete the creation_date key.
brand.pop("creation_date")

#Print the last item in international_competitors.
print(brand["international_competitors"][-1])

#Print the major colors in the US.
print(brand["major_color"]["US"])

#Print the number of keys in the dictionary.
print(len(brand))

#Print all keys of the dictionary.
print(brand.keys())

print("\n---Exercise 3: Zara. Bonus---")
#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000  # Different number to show it gets updated
}

brand.update(more_on_zara)

print(brand)


print("\n---Exercise 4: Disney Characters---")
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1. Create a dictionary that maps characters to their indices:
char_to_index = {name: index for index, name in enumerate(users)}
print(char_to_index)

#2. Create a dictionary that maps indices to characters:
index_to_char = {index: name for index, name in enumerate(users)}
print(index_to_char)

#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_users = sorted(users)
sorted_char_to_index = {name: index for index, name in enumerate(sorted_users)}
print(sorted_char_to_index)