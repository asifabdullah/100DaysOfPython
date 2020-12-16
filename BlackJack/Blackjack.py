import random
import os
import art

def deal(deck, number_of_cards, hand):
  #starting_hand = []
  for i in range(0, number_of_cards):
      hand.append(random.choice(deck))

  return hand

def hand_score(hand):
  total_score = 0
  for card in hand:
    total_score += int(card)
  if 11 in hand and total_score > 21:
    total_score -= 10
  return total_score

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_blackjack():    
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if user_choice == "y":
        clear()
        print(art.logo)
        user_hand = deal(deck = cards, number_of_cards = 2, hand = [])
        #user_hand = [10, 10]
        computer_hand = deal(deck = cards, number_of_cards = 2, hand = [])
        #computer_hand = user_hand = [10, 10]
        print(f"\tYour cards: {user_hand}, current score: {hand_score(user_hand)}")
        print(f"\tComputer's first card: {computer_hand[0]}")
        if hand_score(user_hand) >21:
            print("You Lose")
        elif hand_score(computer_hand) == 21:
            print("Computer Wins with Blackjack!")
        elif hand_score(user_hand) == 21:
            print("You Win with Blackjack!")
        else:
            is_continue = True
            while is_continue:
                user_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
                if user_choice == "y":
                    user_hand = deal(deck = cards, number_of_cards = 1, hand = user_hand)
                    user_hand_score = hand_score(user_hand)
                    computer_hand_score = hand_score(computer_hand)
                    print(f"\tYour cards: {user_hand}, current score: {hand_score(user_hand)}")
                    print(f"\tComputer's first card: {computer_hand}")
                    if user_hand_score >21 or computer_hand_score > 21:
                        print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                        print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                        if user_hand_score < computer_hand_score:
                            print("Computer went over. You win")
                        else:
                            print("You went over. You Lose")
                        is_continue = False
                    else:
                        computer_hand = deal(deck = cards, number_of_cards = 1, hand = computer_hand)
                        computer_hand_score = hand_score(computer_hand)
                        if computer_hand_score > 21:  
                            print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                            print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                            print(f"\tComputer went over. You win")
                            is_continue = False     
                elif user_choice == "n":
                    user_hand_score = hand_score(user_hand)
                    computer_hand_score = hand_score(computer_hand)
                    if user_hand_score > 21:
                        print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                        print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                        print("You Lose") 
                    elif computer_hand_score > 21:
                        print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                        print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                        print("You Win")
                    elif user_hand_score > computer_hand_score:
                        print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                        print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                        print("You win")
                    elif user_hand_score == computer_hand_score:
                        print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                        print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                        print("Draw")    
                    else:
                        print(f"\tYour final hand: {user_hand}, final score: {hand_score(user_hand)}")
                        print(f"\tComputer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
                        print("You Lose") 
                    is_continue = False    
        play_blackjack()    
    else:
        exit()


play_blackjack()