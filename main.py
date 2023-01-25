import turtle
import pandas as pd
from state import State

data = pd.read_csv("50_states.csv")

states = data.state.to_list()
states_guessed = []

screen = turtle.Screen()
screen.title("U.S.A. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=600)

answer_state = screen.textinput(
    title="Guess the state", prompt="Enter a state").title()
print(answer_state)
if answer_state in states:
    if answer_state not in states_guessed:
        state_data = data[data.state == answer_state]
        print("state guessed")
        print(state_data.x)
        states_guessed.append(answer_state)

        new_state = State(
            (int(state_data.x), int(state_data.y)), answer_state)


turtle.mainloop()
