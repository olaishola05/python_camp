from turtle import Turtle, Screen
import random

is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles_list = []

for turtle_idx in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_idx])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_idx])
    turtles_list.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
