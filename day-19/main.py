from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-240, y=y)
    y += 40
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            is_race_on = False
            if winner_color == user_bet:
                print(f"You won! the {winner_color} turtle is the winner")
            else:
                print(f"You lose! the {winner_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# screen.listen()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def move_clockwise():
#     #new_heading = tim.heading() - 10
#     tim.right(10)
#
#
# def move_anti_clockwise():
#     #new_heading = tim.heading() + 10
#     tim.left(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_clockwise)
# screen.onkey(key="d", fun=move_anti_clockwise)
# screen.onkey(key="c", fun=clear)


screen.exitonclick()
