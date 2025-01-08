import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

quote = pandas.read_csv("50_states.csv")
all_states = quote.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What is another state name?: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]  # list comprehension
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)

        missing_dict = {
            "states": missing_states
        }

        df = pandas.DataFrame(missing_dict)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        tinie = turtle.Turtle()
        tinie.hideturtle()
        tinie.penup()

        state = quote[quote.state == answer_state]
        tinie.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
        tinie.write(answer_state)
