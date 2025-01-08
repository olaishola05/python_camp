import random

import hangman_words as hwl
from hangman_art import logo, stages

chosen_word = random.choice(hwl.word_list)

print(logo)

END_OF_GAME = False
LIVES = 6

WORD_LENGHT = len(chosen_word)
display = []

for _ in range(0, WORD_LENGHT):
    display.append("_")
print(f"{' '.join(display)}")

while not END_OF_GAME:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display:
        print(f"You have already guessed {guess_letter}")

    for idx in range(WORD_LENGHT):
        letter = chosen_word[idx]
        if guess_letter == letter:
            display[idx] = letter

    if guess_letter not in chosen_word:
        print(f"{guess_letter} is not in the word. You lose a life.")
        LIVES -= 1
        if LIVES == 0:
            END_OF_GAME = True
            print("You Loose!")
            print(f"The word was {chosen_word}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        END_OF_GAME = True
        print("You win!")

    print(stages[LIVES])
