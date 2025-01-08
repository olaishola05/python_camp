from turtle import Turtle

MOVING_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)

    def go_up(self):
        new_y = self.ycor() + MOVING_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVING_DISTANCE
        self.goto(self.xcor(), new_y)
