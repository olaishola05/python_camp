import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=player.move_up, key="Up")
print(car_manager.cars_list)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating cars after every time sleep
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.goto_start()
        car_manager.increase_speed()

screen.exitonclick()
