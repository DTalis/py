import random

while True:
    user_string = input("Please enter a string that is exactly 10 characters long: ")

    string_length = len(user_string)

    if string_length < 10:
        print("String not long enough.")
    elif string_length > 10:
        print("String too long.")
    else:
        print("Perfect string!")
        print(f"\nFirst character: {user_string[0]}")
        print(f"Last character: {user_string[-1]}")
        
        print("\nBuilding the string character by character:")
        
        progressive_string = ""
        
        for char in user_string:
            progressive_string += char
            print(progressive_string)
            
        characters = list(user_string)
        
        random.shuffle(characters)
        
        jumbled_string = "".join(characters)
        
        print(f"\nJumbled string: {jumbled_string}")
        
        break
