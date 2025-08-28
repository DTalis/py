class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self, animal_type, count = 1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self, ):
        result = f"{self.name}'s animals\n"
        for animal, count in self.animals.items():
            result += f"{animal}: {count}\n"
        
        result += "\nE-I-E-I-O!"
        return result

#Step 6
    def get_animal_types(self):
        return sorted(self.animals.keys())

#Step 7
    def get_short_info(self):
        animal_list = self.get_animal_types()
        plural_names = []

        for animal in animal_list:
            count = self.animals[animal]
            # Handle pluralization. Note: 'sheep' is a special case.
            if animal == 'sheep' or count <= 1:
                plural_names.append(animal)
            else:
                plural_names.append(animal + 's')

        # This block formats the list of animal names into a readable string.
        if len(plural_names) == 1:
            animals_str = plural_names[0]
        else:
            animals_str = ', '.join(plural_names[:-1]) + ' and ' + plural_names[-1]

        return f"{self.name}'s farm has {animals_str}."
    

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())