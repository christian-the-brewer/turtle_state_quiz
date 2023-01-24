from turtle import Turtle


class State(Turtle):
    def __init__(self, coords, state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(coords)
        self.color("black")
        self.write(state, align="center", font=("Arial", 10, "normal"))
