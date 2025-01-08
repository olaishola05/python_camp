import random as r

choose = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n ")
)

# Rules

# • Rock wins against scissors.
# • Scissors win against paper.
# • Paper wins against rock.

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice_art = [rock, paper, scissors]
computer_choice = r.randint(0, 2)

if choose >= 3 or choose < 0:
    print("Invalid input")
else:
    print("You Choose:")
    print(choice_art[choose])
    print("Computer chose:")
    print(choice_art[computer_choice])

    if choose == computer_choice:
        print("It's a draw")
    elif choose == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choose == 2:
        print("You lose!")
    elif choose > computer_choice:
        print("You win!")
    elif computer_choice > choose:
        print("You lose!")
