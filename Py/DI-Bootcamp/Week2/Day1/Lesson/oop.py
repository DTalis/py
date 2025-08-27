#OOP: OBJECT ORIENTED PROGRAMING

#Class = a blueprint of the object, where we will define what are the properties and behaviors of the object

#syntax

class Dog:
    
    #the constructor function
    def __init__(self, breed, nickname, color, age, is_trained=False):
        print(self)
        self.breed = breed
        self.nickname = nickname
        self.color = color
        self.age = age
        self.is_trained = is_trained
        self.dogs_years_age = age * 7
        if age == None:
            self.dogs_years_age = None
        else:
            self.dogs_years_age = self.age * 7
#Method
def bark(self):
    print(f"{self.nickname} is barking")

#creating an object from the class Dog:
dog1 = Dog('chowchow', 'lion', 'orange', 5)
dog2 = Dog('collie', 'laddy', 'bege and white', 15, True)
dog2.is_servise_dog = True


Dog.bark(dog3)

print(dog1.color) #dot notation to access the attributes of the object

print(dog1.__dict__)
print(dog2.__dict__)


# self is the internal dictionary that has the properties from the class
# {breed: -----, nickname: -------, color: -------}

#create a new attribute to the Dog class called "is_trained" the value is a boolean and the default is False
#then run the code again. What happens with the objects that were created before this new attribute was added?

dog3 = Dog("labrador", "Rax", "gold", 7, True)
dog3.bark()
Dog.bark(dog3)

def rename(self,new_name):
    self.nickname = new_name

dog3.rename("Bob")

print(dog3.nickname)

my_dogs = [dog1, dog2, dog3]
    for dog in my_dogs


class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

  def change_name(self, new_name):
    self.name = new_name

first_person = Person("John", 36)
first_person.show_details()       # Hello my name is John

first_person.change_name("Mike")
first_person.show_details() 

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

