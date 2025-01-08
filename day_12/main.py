import random
from art import logo
import os


def welcome_msg():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def generate_number():
    """Generate number from 1 to 100 and returns an array of numbers"""
    numbers = []
    for number in range(1, 101):
        numbers.append(number)
    return numbers


def answer():
    return random.randint(1, 100)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


EASY = 10
HARD = 5


def set_difficulty_level():
    global EASY, HARD

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY
    else:
        return HARD


def check_answer(answer, guess, lives):
    """The function check if the guess equals the answer

    Args:
        answer (int): random generated number
        guess (int): user guess
        lives (int): lives based on difficulty level

    Returns:
        int: returns updated lives
    """
    if guess > answer:
        print("Too high, Guess again")
        return lives - 1
    elif guess < answer:
        print("Too low, Guess again")
        return lives - 1
    elif guess == answer:
        print(f"Yey! You guessed right! and the {answer}")


def number_game():
    print(logo)
    welcome_msg()

    # number = random.choice(generate_number())
    number = answer()
    print(number)
    game_over = False
    lives = set_difficulty_level()
    guess = 0
    while guess != number and not game_over:

        if lives == 0:
            print("You've run out of lives, you loose!")
            game_over = True
        else:
            print(f"You have {lives} attempts remaining to guess the number")

            guess = int(input("Make a Guess: "))
            lives = check_answer(answer=number, guess=guess, lives=lives)

    while (
        input(
            "Do you want to play a number guessing Game again? Type 'y' or 'n': "
        ).lower()
        == "y"
    ):
        clear_screen()
        number_game()


number_game()
