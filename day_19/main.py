from turtle import Turtle, Screen

tinie = Turtle()
screen = Screen()


def move_forward():
    tinie.forward(10)


def move_backward():
    tinie.backward(10)


def turn_left():
    new_heading = tinie.heading() + 10
    tinie.setheading(new_heading)


def turn_right():
    new_heading = tinie.heading() - 10
    tinie.setheading(new_heading)


def clear():
    tinie.clear()
    tinie.penup()
    tinie.home()
    tinie.pendown()


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
