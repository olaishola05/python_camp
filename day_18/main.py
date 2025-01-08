import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
teemo = Turtle()

teemo.shape("arrow")
# teemo.width(15)
teemo.speed("fastest")


# for _ in range(4):
#     teemo.forward(100)
#     teemo.right(90)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)  # immutable
    return rgb_tuple


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         teemo.forward(100)
#         teemo.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     teemo.color(random.choice(colors))
#     draw_shape(shape_side_n)


directions = [0, 90, 180, 270]


# Random Walk
# for _ in range(200):
#     teemo.color(random_color())
#     teemo.forward(30)
#     teemo.setheading(random.choice(directions))

# Spirograph

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        teemo.color(random_color())
        teemo.circle(100)
        teemo.setheading(teemo.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
