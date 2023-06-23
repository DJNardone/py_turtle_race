from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=600, height=400)
enter_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race?  Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = [100, 60, 20, -20, -60, -100]
race_turtles = []

for t in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=-290, y=y_start[t])
    race_turtles.append(new_turtle)

if enter_bet:
    race_on = True

while race_on:
    for t in race_turtles:
        if t.xcor() >= 280:
            race_on = False
            winner = t.pencolor()
            if winner == enter_bet:
                print(f"You Won! The {winner} turtle is victorious!")
            else:
                print(f"Sorry, You Lose! The {winner} turtle is the winner!")

        turtle_moves = random.randint(0, 10)
        t.forward(turtle_moves)

screen.exitonclick()


