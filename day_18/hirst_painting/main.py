import turtle as t
import random

t.colormode(255)
tino = t.Turtle()
tino.speed("fastest")

rgb_colors = [(232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21),
              (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115),
              (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218),
              (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220),
              (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]


def hirst_paintings():
    tino.penup()
    tino.hideturtle()
    tino.setheading(225)
    tino.forward(300)
    tino.setheading(0)
    number_dots = 100

    for dot_count in range(1, number_dots + 1):
        tino.dot(20, random.choice(rgb_colors))
        tino.forward(50)
        if dot_count % 10 == 0:
            tino.setheading(90)
            tino.forward(50)
            tino.setheading(180)
            tino.forward(500)
            tino.setheading(0)


hirst_paintings()

screen = t.Screen()
screen.exitonclick()
