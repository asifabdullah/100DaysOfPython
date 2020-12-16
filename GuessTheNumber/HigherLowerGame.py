from game_data import data
from art import logo,vs
from replit import clear

# This function will pick a random value
# from the data dictionary
def pick_single_data():
  from random import randint
  data_index = randint(0,len(data)-1)
  return data[data_index]


def higher_lower_game (first_data, second_data, score):
  print(logo)
  if score != 0:
    print(f"You're right! Current Score: {score}")

  print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}")
  #print(first_data['follower_count'])
  print(vs)
  print(f"Compare B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}")
  #print(second_data['follower_count'])
  user_input = input("Who has more follower? Type 'A' or 'B': ").lower()

  if first_data['follower_count'] > second_data['follower_count'] and user_input == "a":
    return True
  elif first_data['follower_count'] < second_data['follower_count'] and user_input == "b":
    return True
  else:
    return False

score = 0   
data_1 = pick_single_data()
data_2 = pick_single_data()

while higher_lower_game(data_1,data_2,score):
  score += 1
  data_1 = data_2
  data_2 = pick_single_data()
  clear()

clear()
print(logo)
print(f"Sorry, that's wrong. Final Score: {score}")