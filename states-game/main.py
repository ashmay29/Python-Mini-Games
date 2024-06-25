from turtle import Turtle,Screen
import pandas as pd

turtle = Turtle()
screen = Screen()
screen.title("The States Game")
image = "states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
score = 0
guessed_correctly = []

df = pd.read_csv("states-game/50_states.csv")
all_states = df["state"].to_list()

while game_is_on:
    answer_state = screen.textinput(title="Guess the state",prompt="What's the state's name?").title()
    for state in all_states:
        if answer_state == state:
            score +=1
            guessed_correctly.append(state)
            x_cor = df['x']
            y_cor = df['y']
            turtle.goto(x_cor,y_cor)
            turtle.write(state,font=("Arial",12,"normal"))

screen.mainloop()