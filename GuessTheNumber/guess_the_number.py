import random

def generate_random_number():
  """Choose a random number between 1 to 100 """
  random_number = random.randint(1,101)
  return random_number

from art import logo


print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

guessed_number = generate_random_number()

def comapare (guessed_number, user_input):
  if guessed_number > user_input:
    return "Too Low"
  elif guessed_number < user_input:
    return "Too High"
  else:
    return f"Your got it! The answer was {guessed_number}"

difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

if difficulty_level == "hard":
  number_of_attempt = 5
elif difficulty_level == "easy":
  number_of_attempt = 10

while number_of_attempt > 0:
  print(f"You have {number_of_attempt} attempts remaining to guess the number.")
  chosed_number = int(input("Make a guess: "))
  print(comapare(guessed_number = guessed_number, user_input = chosed_number))
  if number_of_attempt > 1:
    print("Guess Again")
  else:
    print("You are out of guesses")

  if chosed_number == guessed_number:
    number_of_attempt = 0
  else:
    number_of_attempt -= 1