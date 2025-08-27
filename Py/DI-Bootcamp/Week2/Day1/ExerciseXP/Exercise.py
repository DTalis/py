print("\n🌟 Exercise 1: Cats")
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat('Meggi', 14)
cat2 = Cat('Elvin', 10)
cat3 = Cat('Geroin', 15)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    print(f"The oldest cat is {oldest.name} and he/she is {oldest.age} years old")

find_oldest_cat(cat1, cat2, cat3)

print("\n🌟 Exercise 2 : Dogs")
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} good woof!")
    def jump(self):
       print(f"{self.name} jumps {self.height * 2} cm high!")
              
davids_dog = Dog('Lady', 30)
sarahs_dog = Dog('Bob', 50)
    
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")

davids_dog.bark()
davids_dog.jump()

print()

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()   

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")



print("\n🌟 Exercise 3 : Who’s The Song Producer?")
class Song:
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

print("Singing the song:")
stairway.sing_me_a_song()
print("\n--- End of Song ---")


print("\n🌟 Exercise 4 : Afternoon At The Zoo")
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def get_animals(self):
        print("Animals in the Zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            letter = animal[0]
            if letter not in groups:
                groups[letter] = []
            groups[letter].append(animal)
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        print("Groups of animals:")
        for letter, group in groups.items():
            print(f"{letter}: {group}")

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal('Cougar'),
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Lemur")
brooklyn_safari.add_animal("Elephant")
brooklyn_safari.add_animal("Eagle")
brooklyn_safari.add_animal("Camel")

brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")

print("\nAfter selling Bear:")
brooklyn_safari.get_animals()

brooklyn_safari.sort_animals()

print("\nAnimal Groups:")
brooklyn_safari.get_groups()