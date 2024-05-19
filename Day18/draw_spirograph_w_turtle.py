from random import randint
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

dot = Turtle()
dot.pensize(2)
dot.speed(9)
dot.hideturtle()
dot.circle(100)


for num in range(0, 360, 10):
    dot.left(10)
    dot.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    dot.circle(100)

screen = Screen()
screen.exitonclick()