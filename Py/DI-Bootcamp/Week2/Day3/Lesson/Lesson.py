#type of inchritance
#Single
#Multilevel
#Multiple child

from datetime import datetime, date
class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_date = birth_date

    @staticmethod
    def format_name(name):
        return name.capitalize()
    
    @staticmethod
    def parse_birthdate(date):
        return datetime.strptime(data_str, "%d-%m-%y")
    
    @classmethod
    def from_age(cls. first_name, last_name, age:int):
    current_year = datetime.today().year
    birth_year = currect_year - age
    birth_date = f"1-01-{birth_year}"
    return cls(first_name, last_name, birth_date)
    
p1 = Person("john", "snow de silva", "21-08-1990")
print(p1.birth_date)
print(p1.first_name)
print(p1.last_name)
print(p1.birth_date)

print(datetime.now())


class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val())
print(MyClass.get_count())

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())
print(MyClass.get_count())



