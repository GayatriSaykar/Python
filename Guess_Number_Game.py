 #  Add dependencies
import random

 # Set up the game
secret_number = random.randint(1, 20)
max_guesses = 5
guess_count = 0

print("I'm thinking of a number between 1 and 20.")
print(f"You have {max_guesses} guesses. Good luck!")

 # Ask the player to guess
while guess_count < max_guesses:
    guess_count += 1
    guess = int(input(f"\nGuess #{guess_count}: "))

     # Check the guess and give feedback
    if guess == secret_number:
        print(f"Correct! You got it in {guess_count} guesses.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

 # Announce the result
else:
    print(f"\nOut of guesses! The number was {secret_number}.")