from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGTH = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):  # start from last_item, stop at 0 and step by -1
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGTH:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGTH)
