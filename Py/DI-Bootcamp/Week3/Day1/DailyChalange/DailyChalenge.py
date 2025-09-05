import pandas as pd

class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []  # Part 2: Initialize family list

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)
class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        # Put at beginning if age > 60 or priority is True
        if person.age > 60 or person.priority:
            # Manually shift elements to the right
            new_list = [None] * (len(self.humans) + 1)
            new_list[0] = person
            for i in range(len(self.humans)):
                new_list[i + 1] = self.humans[i]
            self.humans = new_list
        else:
            # Add at end
            self.humans += [person]

    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return -1  # Not found

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 != -1 and index2 != -1:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if len(self.humans) == 0:
            return None
        next_person = self.humans[0]
        # Shift list left manually
        new_list = [None] * (len(self.humans) - 1)
        for i in range(1, len(self.humans)):
            new_list[i - 1] = self.humans[i]
        self.humans = new_list
        return next_person

    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                person = self.humans[i]
                # Remove the person manually
                new_list = [None] * (len(self.humans) - 1)
                index = 0
                for j in range(len(self.humans)):
                    if j != i:
                        new_list[index] = self.humans[j]
                        index += 1
                self.humans = new_list
                return person
        return None

    def sort_by_age(self):
        # Custom sort: priority > older > younger
        priority_list = []
        non_priority_list = []

        for person in self.humans:
            if person.priority:
                priority_list += [person]
            else:
                non_priority_list += [person]

        # Sort each list by age descending using bubble sort
        def bubble_sort_by_age_desc(lst):
            n = len(lst)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if lst[j].age < lst[j + 1].age:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]

        bubble_sort_by_age_desc(priority_list)
        bubble_sort_by_age_desc(non_priority_list)

        self.humans = priority_list + non_priority_list
    def rearrange_queue(self):
        i = 0
        while i < len(self.humans) - 1:
            current = self.humans[i]
            next_person = self.humans[i + 1]
            if next_person in current.family:
                # Find a non-family member to swap with
                found = False
                for j in range(i + 2, len(self.humans)):
                    if self.humans[j] not in current.family:
                        # Swap positions
                        self.humans[i + 1], self.humans[j] = self.humans[j], self.humans[i + 1]
                        found = True
                        break
                if not found:
                    # Can't rearrange further
                    i += 1
            else:
                i += 1
    def to_table(self):
        data = []
        for person in self.humans:
            data.append({
                "ID": person.id_number,
                "Name": person.name,
                "Age": person.age,
                "Priority": person.priority,
                "Blood Type": person.blood_type,
                "Family Members": [member.name for member in person.family]
            })
        df = pd.DataFrame(data)
        return df
    
# Create people
alice = Human("001", "Alice", 65, False, "A")
bob = Human("002", "Bob", 30, True, "B")
charlie = Human("003", "Charlie", 25, False, "O")
dana = Human("004", "Dana", 45, False, "AB")

# Add family members
alice.add_family_member(charlie)  # Alice and Charlie are family

# Create queue and add people
queue = Queue()
queue.add_person(alice)
queue.add_person(bob)
queue.add_person(charlie)
queue.add_person(dana)

df = queue.to_table()
print(df)

# Rearrange to avoid family members together
queue.rearrange_queue()

# Print queue names
for person in queue.humans:
    print(person.name)
