import turtle

import pandas

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=730, height=490)
screen.tracer(0)

# turtle that will write each correct answer
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.color("black")
turtle.penup()

# read and store data from 50_states.csv
states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

# game loops until all states are entered as answers
state_answers = []
score = 0
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    screen.update()

    # check is answer is one of the states in all the states of 50_states.csv
    if answer_state in states_list:
        x_cor = states_data[states_data["state"] == answer_state].x.item()
        y_cor = states_data[states_data["state"] == answer_state].y.item()
        turtle.goto(x=x_cor, y=y_cor)
        turtle.write(arg=answer_state, move=False, align="center", font=FONT)
        state_answers.append(answer_state)
        score = len(state_answers)

    if answer_state == "Exit":
        # generate CSV file states_to_learn.csv that contains just the names of the states that have not been guessed
        remaining_states = [state for state in states_list if state not in state_answers]
        remaining_states_data = pandas.DataFrame(remaining_states)
        remaining_states_data.to_csv("states_to_learn.csv")
        break

# find the coordinates of each state, store into 50_states.csv
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
