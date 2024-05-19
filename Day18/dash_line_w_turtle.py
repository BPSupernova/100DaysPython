from turtle import Turtle, Screen

dot = Turtle()

counter = 0

dot.shape('circle')
dot.color('orange')
while counter < 5:
    dot.forward(10)
    dot.penup()
    dot.forward(10)
    dot.pendown()
    counter += 1

screen = Screen()
screen.exitonclick()