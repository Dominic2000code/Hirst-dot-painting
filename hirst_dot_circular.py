import random
import math


def create_circular_dot_painting(t, color_list):
    t.hideturtle()
    num_dots = 36  # Number of dots in the circular motion
    radius = 250  # Radius of the circular motion

    while radius >= 0:
        if radius == 10:
            t.penup()
            t.goto(0, 0)  # Move to center
            t.dot(20, random.choice(color_list))  # Draw a single dot
        else:
            for _ in range(num_dots):
                t.penup()
                angle = math.radians(_ * (360 / num_dots))  # Convert degrees to radians
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                t.goto(x, y)
                t.dot(20, random.choice(color_list))
        if radius == 70:
            num_dots = 12
        else:
            num_dots -= 3
        radius -= 30
