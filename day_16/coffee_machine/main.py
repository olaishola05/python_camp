from data import MENU, resources, art

machine_on = True

profit = 0


def formatted_report(stocks):
    global profit
    print()
    water_ml = stocks["water"]
    milk_ml = stocks["milk"]
    coffee_kg = stocks["coffee"]
    print(f"Water: {water_ml}ml\nMilk: {milk_ml}ml\nCoffee: {coffee_kg}kg\nMoney: ${profit}")
    print()


def formatted__message(item):
    print(f"Sorry there is not enough {item}")


def check_resources(item_ordered, stocks):
    ingredients = item_ordered['ingredients']

    for item in ingredients:
        if ingredients[item] > stocks[item]:
            formatted__message(item)
            return True
    return False


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def verify_transaction(payment, item_price):
    global profit
    if payment >= item_price:
        profit += item_price
        change = round(payment - item_price, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(item_ordered, stock, drink_name):
    print("Making coffee...")
    for item in item_ordered["ingredients"]:
        stock[item] -= item_ordered["ingredients"][item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def coffee_machine():
    global machine_on

    print(art)

    while machine_on:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if prompt == "off":
            machine_on = False

        elif prompt == "report":
            formatted_report(resources)
        else:
            if prompt in ['espresso', 'latte', 'cappuccino']:
                order = MENU[prompt]
                if check_resources(item_ordered=order, stocks=resources):
                    machine_on = False
                else:
                    money = process_coins()
                    if verify_transaction(money, order["cost"]):
                        make_coffee(item_ordered=order, stock=resources, drink_name=prompt)
            else:
                print("You have entered invalid order type")


coffee_machine()
