from random import randint
from turtle import Turtle, Screen

dot = Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

def draw_shape(dot, num_of_sides):
    for num in range(0, num_of_sides):
        dot.right(360 / num_of_sides)
        dot.forward(100)

dot.shape('circle')
dot.color('orange')
dot.forward(50)

max_num_of_sides = 10
for num in range(3, 10):
    dot.color(colors[randint(0, len(colors) - 1)])
    draw_shape(dot, num)

screen = Screen()
screen.exitonclick()