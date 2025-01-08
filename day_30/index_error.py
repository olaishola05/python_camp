fruits = ['apple', 'pear', 'Orange']


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(f"The {error_message}")
    except TypeError as error_message:
        print(f"{error_message}")
    else:
        print(fruit + " pie")


make_pie(0)
