############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

import random
import os
from art import logo


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Computer has a blackjack, you lose"
    elif user_score == 0:
        return "You have a blackjack, you win"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_ended = False

    while not game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} and your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_ended = True
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                game_ended = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and your final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards} and computer's final score: {computer_score}"
    )

    print(compare(user_score, computer_score))

    while (
        input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        == "y"
    ):
        clear_screen()
        blackjack()


blackjack()
