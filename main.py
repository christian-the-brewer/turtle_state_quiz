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

game = True
while len(states_guessed) < 50 and game:
    answer_state = screen.textinput(
        title=f"{len(states_guessed)}/50 Correct", prompt="Guess a state!").title()
    print(answer_state)
    if answer_state == "Exit" or answer_state == "Quit":
        game = False
        break
    if answer_state in states:
        if answer_state not in states_guessed:
            state_data = data[data.state == answer_state]
            print("state guessed")
            print(state_data.x)
            states_guessed.append(answer_state)
            new_state = State(
                (int(state_data.x), int(state_data.y)), answer_state)

missing_states = []
for state in states:
    if state not in states_guessed:
        missing_states.append(state)

missed_states = pd.DataFrame(missing_states)
missed_states.to_csv("missed_states.csv")

turtle.mainloop()
