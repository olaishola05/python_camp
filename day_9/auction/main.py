import os
from art import logo


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)
print("Welcome to the secret auction program. ")

bids = {}
bidding_finished = False


def add_bidders(name, bid):
    bids[name] = bid


def register_user_bid():
    bidder_name = input("What is your name?: \n")
    bid_amount = int(input("What's your bid?: $"))
    add_bidders(name=bidder_name, bid=bid_amount)


def find_highest_bidder(bids_record):
    highest_bid = 0
    winner = ""

    for bidder in bids_record:
        bid_amount = bids_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with highest bid of ${highest_bid}")


while not bidding_finished:
    register_user_bid()

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if more_bidders == "no":
        find_highest_bidder(bids_record=bids)
        bidding_finished = True

    elif more_bidders == "yes":
        clear_screen()
