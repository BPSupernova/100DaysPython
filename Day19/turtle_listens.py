from turtle import Turtle, Screen

dot = Turtle()
screen = Screen()

def move_forwards():
    dot.forward(10)

screen.listen()
screen.onkey(key = "space", fun = move_forwards)
screen.exitonclick()
