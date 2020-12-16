# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('download.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
import turtle as t
import random as rand
paint_list = [(229, 216, 103), (149, 80, 41), (206, 160, 103), (112, 166, 209), (178, 176, 19), (31, 92, 159),
              (110, 177, 128), (192, 91, 105), (10, 34, 92), (67, 39, 21), (188, 136, 151), (92, 185, 55),
              (53, 123, 26), (29, 100, 18), (206, 86, 67), (106, 32, 54), (246, 170, 160), (21, 51, 114),
              (98, 120, 172), (245, 169, 174), (180, 206, 167), (156, 189, 238), (75, 27, 43), (151, 75, 87),
              (239, 221, 7), (100, 73, 14)]

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1,number_of_dots + 1):
    tim.dot(20, rand.choice(paint_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# t.dot(20, rand.choice(paint_list))

# y = 0
# for i in range(10):
#     tim.setpos(0, y)
#     for j in range(10):
#         tim.shape("circle")
#         tim.color(rand.choice(paint_list))
#         tim.stamp()
#         tim.penup()
#         if j != 9:
#             tim.forward(50)
#     y += 30


    #print(tim.position())
screen = t.Screen()
screen.exitonclick()