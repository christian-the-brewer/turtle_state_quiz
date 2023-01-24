import turtle
import pandas as pd
from state import State

data = pd.read_csv("50_states.csv")
states = data.state.to_list()


screen = turtle.Screen()
screen.title("U.S.A. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the state", prompt="Enter a state").title()
print(answer_state)
if answer_state in states:
    pass


turtle.mainloop()
