from math import ceil


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {ceil(number_of_cans)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
