from ExerciaseXP import Dog

import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        # Prints the dog's bark and sets trained to True
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # Prints a message when multiple dogs play together
        dog_names = [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together!")

    def do_a_trick(self):
        # If the dog is trained, prints a random trick from the list
        if self.trained:
            tricks = [
                "does a roll",
                "stands on his back legs",
                "gives hand",
            ]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained to do any tricks yet.")
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and weighs {self.weight} kg. Trained: {self.trained}'
    

dog1 = PetDog("Rey", 5, 25)
dog2 = PetDog("Penelope", 10, 60, trained=True)
dog3 = PetDog("Frodo", 10, 3)

dog1.train()

dog1.play(dog2, dog3)

dog1.do_a_trick()
dog2.do_a_trick()
dog3.do_a_trick()


