"""you build a rock, paper, scissors game in Python. The player types their choice, the computer picks one at random, and your program uses conditional logic to decide who wins. You practice using comparison operators, if/elif/else statements, and logical operators (and, or, not)."""

import random

print("Rock, Paper, Scissors!")
print("-" * 23)

player_choice=input("Enter your choice (rock, paper, scissors):").lower()

if player_choice!="rock" and player_choice!="paper" and player_choice!="scissors":
     print("Invalid choice. Please enter rock, paper, or scissors.")

else:
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")

    if player_choice==computer:
        print("It's tie!!!")
    elif player_choice=="rock" and computer=="paper":
        print("You win! paper covers rock.")
    elif player_choice=="paper" and computer=="scissors":
        print("You win! scissors covers paper.")
    elif player_choice=="scissors" and computer=="rock":
        print("You win! scissors covers paper.") 
    else:
        print(f"Computer wins! {computer.capitalize()} beats {player_choice}.")
   # print("You lose the game")