from turtle import Turtle, Screen

dot = Turtle()

def turn_and_move(dot):
    dot.forward(100)
    dot.right(90)

dot.shape('circle')
dot.color('orange')
dot.forward(50)
dot.right(90)
turn_and_move(dot)
turn_and_move(dot)
turn_and_move(dot)
dot.forward(50)
dot.right(90)
dot.left(180)
dot.forward(100)


screen = Screen()
screen.exitonclick()