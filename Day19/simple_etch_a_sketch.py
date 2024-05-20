from turtle import Turtle, Screen

dot = Turtle()
screen = Screen()

def move_forwards():
    dot.forward(10)

def move_backwards():
    dot.backward(10)

def turn_counter_clockwise():
    dot.left(15)

def turn_clockwise():
    dot.right(15)

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(screen.reset, "c")
screen.exitonclick()