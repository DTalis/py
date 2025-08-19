import random
secret_number = random.randint(1, 100)
max_attempts = 7
print("\nLet's play a fun Number Guessing Game 🎲! I pick a random number between 1-100, and you have 7 attempts to guess it. Don't worry, I'll get you hints! ")

for attempts in range(1, max_attempts + 1):
    try:
        guess = int(input(f"\nAttempt #{attempts}: Enter your guess: "))
        if guess < 1 or guess > 100:
            print("That number is not between 1 and 100. Please try again.")
            continue

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess == secret_number:
        print("\nYou did it! Well done!")
        print(f"The number was {secret_number}. Let's play again?")
        break
    elif guess < secret_number:
        print("Your guess is too low. 📉 Try again!")
    else: print("Your guess is too high. 📈 Try again!")
else:
    print("\nGame over! You've used all your attempts.")
    print(f"The secret number was  {secret_number}. Let's try again!")