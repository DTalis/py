import random

secret_number = random.randint(1, 100)
max_attempts = 7
round_number = 1

print("\nLet's play a fun Number Guessing Game 🎲! I pick a random number between 1-100, and you have 7 attempts to guess it. Don't worry, I'll get you hints! ")

while True:
    print(f"\n--- Round {round_number} ---")
    print(f"You have {max_attempts} attempts to guess it!")
    
    player_won = False
    for attempts in range(1, max_attempts + 1):
        try:
            guess = int(input(f"\nAttempt #{attempts}: Enter your guess: "))
            if guess < 1 or guess > 100:
                print("That number is not between 1 and 100. Please try again.")
                continue
        except ValueError:

            print("Invalid input! Please enter a whole number.")
            continue

        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            print(f"The number was {secret_number}.")
            player_won = True
            # The 'break' statement stops the 'for' loop immediately.
            break
        elif guess < secret_number:
            print("Your guess is too low. 📉 Try again!")
        else: 
            print("Your guess is too high. 📈 Try again!")

    if player_won:
        print("Thanks for playing!")
        break
    else:
        print(f"\nGame over for this round! You've used all your {max_attempts} attempts.")
        print("Don't give up! You get another round with one more attempt.")
        max_attempts += 1
        round_number += 1
