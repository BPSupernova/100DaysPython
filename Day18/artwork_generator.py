import turtle
from turtle import Turtle, Screen
import colorgram
from random import randint

turtle.colormode(255)

dot = Turtle()
dot.speed(9)
dot.penup()
dot.hideturtle()

rgb_colors = []
colors = colorgram.extract('Day18/image.png', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    if r > 200 or g > 200 or b > 200:
        continue
    rgb_colors.append(new_color)

for num in range(0, 550, 50):
    for num2 in range(0, 550, 50):
        dot.setposition(-250 + num2, -250 + num)
        dot.dot(25, rgb_colors[randint(0, len(rgb_colors) - 1)])

screen = Screen()
# print(screen.canvheight)
# print(screen.canvwidth)
screen.exitonclick()