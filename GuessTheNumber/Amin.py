#The guessing game
import random
from art import logo
print(logo)
welcome = print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.choice(range(1,101))
hard_lifes = 5
easy_lifes = 10
playing = True

def number_of_guesses():
    global hard_lifes
    global easy_lifes
    if guess != number and level == "hard":
        hard_lifes -= 1
        return hard_lifes
    elif guess != number and level == "easy":
        easy_lifes -= 1
        return easy_lifes



if level == "easy":
    guess = int(input(f"You have {easy_lifes} attempts remaining to guess the number.\n Make a guess: "))
elif level == "hard":
    guess = int(input(f"You have {hard_lifes} attempts remaining to guess the number.\n Make a guess: "))
else:
    print("Pls type 'easy' or 'hard'!")
    print(level)


if guess == number:
    print("You did it! The number is correct!!!")
    playing = False


while playing:
    number_of_guesses()
    if hard_lifes == 0 or easy_lifes == 0:
        print(f"You are dead!\n The number was {number}")
        playing = False
    elif guess > number and level == "easy":
        print("Too high.\n Guess again.")
        guess = int(input(f"You have {easy_lifes} attempts remaining to guess the number.\n Make a guess: "))
    elif guess > number and level == "hard":
        print("Too high.\n Guess again.")
        guess = int(input(f"You have {hard_lifes} attempts remaining to guess the number.\n Make a guess: "))
    elif guess < number and level == "easy":
        print("Too low.\n Guess again.")
        guess = int(input(f"You have {easy_lifes} attempts remaining to guess the number.\n Make a guess: "))
    elif guess < number and level == "hard":
        print("Too low.\n Guess again.")
        guess = int(input(f"You have {hard_lifes} attempts remaining to guess the number.\n Make a guess: "))
    elif guess == number:
        print("You did it! The number is correct!!!")
        playing = False







