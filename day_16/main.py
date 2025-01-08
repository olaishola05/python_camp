# from turtle import Turtle, Screen
#
# teeny = Turtle()
# teeny.shape("turtle")
# teeny.color("red")
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()

# table.header = False
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ['electric', 'water', 'fire'])

table.align = 'l'


print(table)