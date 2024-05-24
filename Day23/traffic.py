from turtle import Turtle
from vehicle import Vehicle
from random import randint

STARTING_MOVE_SPEED = 5
MOVE_SPEED_INCREMENT = 5

class Traffic():
    
    def __init__(self):
        self.vehicles = []
        self.level = 0
        self.level_text = Turtle()
        self.level_text.hideturtle()
        self.level_text.penup()
        self.level_text.goto(0, 220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level_text.write(f"Level: {self.level}", align ="center", font = ("Verdana", 14, "bold"))

    def increase_level(self):
        self.level += 1
        self.level_text.clear()
        self.update_scoreboard()

    def add_vehicle(self):
        chance_to_add = randint(1, 6)
        if chance_to_add == 1:
            new_vehicle = Vehicle()
            self.vehicles.append(new_vehicle)

    def move_traffic_along(self):
        for vehicle in self.vehicles:
            vehicle.forward(STARTING_MOVE_SPEED + (MOVE_SPEED_INCREMENT * self.level))