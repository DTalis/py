
print("\n🌟 Exercise 1: Pets")
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

    def sing(self, sounds):
        return f'{sounds}'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass  # No unique methods for Siamese for now

# Step 2: Create a list of cat instances
bengal_obj = Bengal(name="Elvin", age=10)
chartreux_obj = Chartreux(name="Meggi", age=14)
siamese_obj = Siamese(name="Geroin", age=15)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance with the list of cats
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()



print("\n🌟 Exercise 2: Dogs")
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark (self):
        return f"{self.name} is barking!"
    
    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self, other_dog):
        self_strength = self.run_speed() * self.weight
        other_dog_strength = other_dog.run_speed() * other_dog.weight
        
        if self_strength > other_dog_strength:
            return f'{self.name} wins the fight!'
        elif self_strength < other_dog_strength:
            return f'{other_dog.name} wins the fight!'
        else:
            return 'It\'s a tie!'
dog1 = Dog("Rey", 5, 25)
dog2 = Dog("Penelope", 10, 60)
dog3 = Dog("Frodo", 10, 3)

# Step 3: Test Dog Methods
print("\nTest bark() method")
print(dog1.bark())
print(dog2.bark()) 
print(dog3.bark())

print("\nTest run speed method")
print(f"{dog1.name}'s run speed: {dog1.run_speed()}")
print(f"{dog2.name}'s run speed: {dog2.run_speed()}")
print(f"{dog3.name}'s run speed: {dog3.run_speed()}")

print("\nTest fight method")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))


print("\n🌟 Exercise 3: Dogs Domesticated")
#In a new Python file according to the task

print("\n🌟 Exercise 4: Family And Person Classes")


class Person:
    def __init__(self, first_name, age, last_name = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    
    def is_18(self):
        return self.age >= 18
    
'''Step 2: Create the Family Class

Define a Family class with:
A last_name attribute
A members list that will store Person objects (should be initialized as an empty list)'''

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members.append(person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"You are over 18, your parents should accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member with the name {first_name} found.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for person in self.members:
            print(f"{person.first_name}, age: {person.age}")

# Step 1: Create a Family
my_family = Family("Smith")

# Step 2: Add members to the family
my_family.born("Alexander", 55)
my_family.born("Kate", 52)
my_family.born("David", 19)
my_family.born("Liza", 15)

# Step 3: Check if a member is allowed to go out
my_family.check_majority("David")  
my_family.check_majority("Liza")  

# Step 4: Display family details
my_family.family_presentation()

