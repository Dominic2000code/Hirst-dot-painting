import random


def create_rectangular_dot_painting(t, colors_list):
    t.speed("fastest")
    t.setheading(230)  # modify this value to get an angle that fits the page
    t.penup()
    t.hideturtle()
    t.forward(340)  # modify this value to get a stating point that fits the page
    t.setheading(0)
    x_coordinate, y_coordinate = t.position()

    move_up_by = y_coordinate
    for _ in range(11):
        for _ in range(10):
            t.pendown()
            t.dot(20, random.choice(colors_list))
            t.penup()
            t.forward(50)
        move_up_by += 50
        t.goto(x=x_coordinate, y=move_up_by)
