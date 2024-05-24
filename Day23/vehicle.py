from turtle import Turtle
from random import randint
import time

class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.goto(300, randint(-200, 200))
        self.setheading(180)