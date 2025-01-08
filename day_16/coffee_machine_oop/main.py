from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffee_machine():
    is_machine_on = True

    while is_machine_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()

        if choice == "off":
            is_machine_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            if choice in options.split('/'):
                drink = menu.find_drink(choice)

                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                # else:
                #     is_machine_on = False

            else:
                print(f"You have entered invalid order type of {choice}")


coffee_machine()
