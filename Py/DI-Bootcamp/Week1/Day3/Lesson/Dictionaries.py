a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())

# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.


for key, value in a_dict.items():
    print(key, '->', value)

sample_dict = { 
    "class": { 
        "student": { 
            "name": "Mike",
            "marks": { 
                "physics": 70,
                "history": 80
            }
        }
    }
}
history_value = sample_dict["class"]["student"]["marks"]["history"]
print(history_value)

rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}
print(rick_dict.items())

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
print("Original dictionary:", sample_dict)
for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]

print("Final dictionary: ", sample_dict)
