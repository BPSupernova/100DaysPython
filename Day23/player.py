from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.goto(0, -225)
        self.setheading(90)

    def move_forward(self):
        self.forward(25)