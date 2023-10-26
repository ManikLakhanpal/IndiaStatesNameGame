import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "./India_map.gif"
screen.addshape(image)
screen.screensize()
turtle.shape(image)

data = pandas.read_csv("./states.csv")
all_states = data["state"].to_list()
guessed_state = []

while len(guessed_state) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(all_states)} States Correct",
                                    prompt="Enter name of a state").title()
    if answer_state == "Exit":
        missed_states = [states for states in all_states if states not in guessed_state]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("./states_to_learn")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.color("green", "green")
        t.write(answer_state)

screen.exitonclick()
