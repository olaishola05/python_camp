import os
from art import logo


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def printSymbols(math_operations):
    for symbol in operations:
        print(symbol)


def calculate(symbol, n1, n2):
    return operations[symbol](n1, n2)


answer = 0

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    is_calculating = True
    num1 = float(input("What's the first number?: "))
    printSymbols(math_operations=operations)

    while is_calculating:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = calculate(symbol=operation, n1=num1, n2=num2)

        print(f"{num1} {operation} {num2} = {answer}")

        user_choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ).lower()
        if user_choice == "y":
            num1 = answer

        else:
            is_calculating = False
            clear_screen()
            calculator()


calculator()
