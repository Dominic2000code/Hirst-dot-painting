from turtle import Turtle, Screen, setup, colormode
from hirst_dot_rectangular import create_rectangular_dot_painting
from hirst_dot_circular import create_circular_dot_painting

t = Turtle()
setup(width=550, height=570)
colormode(255)

color_list = [(243, 250, 246), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15),
              (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8),
              (233, 66, 34)]

create_rectangular_dot_painting(t, color_list)
# create_circular_dot_painting(t, color_list)

screen = Screen()
screen.exitonclick()
