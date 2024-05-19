from random import randint
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

dot = Turtle()
dot.pensize(10)
dot.speed(9)

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

def walk_in_a_path(dot, direction_indicator):
    if direction_indicator == 1:
        dot.left(90)
        dot.forward(25)
    elif direction_indicator == 2:
        dot.right(90)
        dot.forward(25)
    elif direction_indicator == 3:
        dot.right(90)
        dot.forward(25)
    else:
        dot.forward(25)

def draw_shape(dot, num_of_sides):
    for num in range(0, num_of_sides):
        dot.right(360 / num_of_sides)
        dot.forward(100)

for num in range(3, 50):
    dot.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    walk_in_a_path(dot, randint(1, 5))

screen = Screen()
screen.exitonclick()