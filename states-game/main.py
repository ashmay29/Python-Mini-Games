from turtle import Turtle,Screen
import pandas as pd

turtle = Turtle()
screen = Screen()
screen.title("The States Game")
image = "states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
guessed_correctly = []
forgotten_states = []

df = pd.read_csv("states-game/50_states.csv")
all_states = df["state"].to_list()

while len(guessed_correctly)< len(all_states):
    answer_state = screen.textinput(title=f"{score}/50 States correct",prompt="What's the state's name?").title()

    if answer_state =="Exit":
        for state in all_states:
            if state not in guessed_correctly:
                forgotten_states.append(state)
        new_data = pd.DataFrame(forgotten_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        score +=1
        guessed_correctly.append(answer_state)
        state_data = df[df["state"] == answer_state]
        t.goto(int(state_data['x']),int(state_data['y']))
        t.write(answer_state,font=("Arial",12,"normal"))