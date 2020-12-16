import turtle as t
from random import randint, choice

timmy_the_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


timmy_the_turtle.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)


draw_spirograph(10)

#
# direction = [0, 90, 180, 270]
#
# timmy_the_turtle.speed(0)
# timmy_the_turtle.pensize(10)
#
#
# for _ in range(500):
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(choice(direction))

#
#
# def draw_shape(num_of_sides):
#     degree = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(degree)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()
