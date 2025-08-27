print("\n---Challenge 1: Multiples Of A Number---")
number = int(input("Please enter the number you want to find multiples for: "))
length = int(input("Please enter how many multiples you want to generate: "))

multiples_list = []
for i in range(1, length+1):
    multiple = number * i

    multiples_list.append(multiple)

print(multiples_list) 


print("\n---Challenge 2: Remove Consecutive Duplicate Letters---")
user_string = input("Please, write a random string: ")
processed_string = ""

if len(user_string) > 0:
    processed_string += user_string[0]

for i in range(1, len(user_string)):
       
        current_letter = user_string[i]
        last_processed_letter = processed_string[-1]

        if current_letter != last_processed_letter:
            processed_string += current_letter


print(f"\nOriginal string: {user_string}")
print(f"Processed string: {processed_string}")


