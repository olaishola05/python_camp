def add(*args):
    # the args is a tuple
    # the args can be looped to get each item of the arg
    # the item can also be access using index args[0]
    total = sum(args)
    print(total)


add(1, 3, 5, 7, 8, 10, 50)


def calculate(n, **kwargs):
    # the kwargs: Keyword positional arguments rep a python dictionary {}
    # the kwargs can be looped to get the value or
    # be accessed using bracket notation kwargs["add"]

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(10, add=3, multiply=4)


class Car:
    def __init__(self, name, **kw):
        self.name = name
        # to avoid throwing error is not passed and returns None if not passed
        self.make = kw.get("make")
        self.model = kw.get("model")


benz = Car(name="Mercedes Benz", model=2020)
print(benz.name)