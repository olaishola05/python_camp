# High and Lower game intsructions


from random import choice
import os
from game_data import data
from art import logo, vs


def generate_users():
    return choice(quote)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_user_info(text, user):
    print(f"{text}: {user["name"]}, a {user["description"]}, from {user["country"]}")


def compare_followers(user1, user2, guess):
    if user1["follower_count"] > user2["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def high_lower():
    print(logo)
    is_game_over = False
    score = 0
    user = generate_users()

    while not is_game_over:
        random_user = user
        user = generate_users()

        while random_user == user:
            user = generate_users()

        print_user_info("Compare A", random_user)

        print(vs)
        print_user_info("Against B", user)

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = compare_followers(random_user, user, user_guess)

        clear_screen()
        print(logo)

        if user["follower_count"] == random_user["follower_count"]:
            continue
        else:
            if result:
                score += 1
                print(f"You're right! Current score: {score}")

            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_game_over = True


high_lower()
