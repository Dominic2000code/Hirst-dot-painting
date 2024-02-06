import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_bank = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_bank.append((r, g, b))
#
# print(color_bank)

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8),
              (233, 66, 34)]

t = Turtle()
turtle.colormode(255)
t.speed("fastest")
t.setheading(230)  # modify this value to get an angle that fits the page
t.penup()
t.hideturtle()
t.forward(340)  # modify this value to get a stating point that fits the page
t.setheading(0)
x_coordinate, y_coordinate = t.position()

move_up_by = y_coordinate
for _ in range(10):
    for _ in range(10):
        t.pendown()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
    move_up_by += 50
    t.goto(x=x_coordinate, y=move_up_by)

screen = Screen()
screen.exitonclick()
