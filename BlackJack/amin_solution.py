def black_jack():
    game_question = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
    if game_question == "n":
        print("Good Bye")
    elif game_question == "y":
        from art import logo
        import random
        #define variables
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        your_cards = [random.choice(cards), random.choice(cards)]
        computers_cards = [random.choice(cards), random.choice(cards)]
        computers_score = 0
        your_score = 0

        #define functions
        def add_card(your_cards):
            random_card = random.choice(cards)
            your_cards = your_cards.append(random_card)

        def add_card_comp(computers_cards):
            random_card_comp = random.choice(cards)
            computers_cards = computers_cards.append(random_card_comp)



        #calculate your_score
        for card in your_cards:
            your_score = your_score + card

        #print and ask
        print(f"Your Cards: {your_cards}, Your Score: {your_score}")
        print(f"Computers first card: {computers_cards[0]}")
        another = input("Type 'y' to get another card, type 'n' to pass.")

        #another == y
            #another == y
        while another == "y":
            your_score = 0
            add_card(your_cards)
            for card in your_cards:
                your_score = your_score + card
                if your_score > 21 and 11 in your_cards:
                    your_score -= 10
            print(f"Your Cards: {your_cards}, Your Score: {your_score}")
            if your_score > 21:
                print("You went over! Its a Bust! You lose!!!")
                another = "n"
            else:
                another = input("Type 'y' to get another card, type 'n' to pass.")

        #another == n
        if your_score < 17:
            print("Its not aloud to break the game now. You score has to ge at minimum equal to 17")
            print(f"Your final hand: {your_cards}, final score {your_score}")
            print("You lose!")
            black_jack()
        elif another == "n" and your_score <= 21:
            for card in computers_cards:
                computers_score += card
            while computers_score < 17:
                computers_score = 0
                add_card_comp(computers_cards)
                for card in computers_cards:
                    computers_score += card
            print(f"Your final hand: {your_cards}, final score {your_score}")
            print(f"Computers final hand: {computers_cards}, final score {computers_score}")
            if computers_score > 21:
                print("The Computer got a Bust! You win!!!")
                black_jack()
            elif your_score > computers_score:
                print("You win!!!")
                black_jack()
            elif your_score < computers_score <= 21:
                print("You lose!!!")
                black_jack()
            else:
                print("Clearly a Draw!!!")
                black_jack()
    else:
        print("Please answer either 'y' or 'n'")
        black_jack()

black_jack()









