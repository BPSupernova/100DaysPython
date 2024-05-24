import turtle
from turtle import Turtle, Screen
from player import Player
from traffic import Traffic
import random
import time

turtle.colormode(255)

screen = Screen()
screen.setup(width = 600, height = 500)
screen.bgcolor('white')
screen.tracer(0)

game_active = True

crossing_turtle = Player()
passing_traffic = Traffic()

screen.listen()
screen.onkey(crossing_turtle.move_forward, "space")

while game_active:
    time.sleep(0.1)
    screen.update()
    passing_traffic.add_vehicle()
    passing_traffic.move_traffic_along()

    for vehicle in passing_traffic.vehicles:
        if vehicle.distance(crossing_turtle) < 21:
            game_active = False

    if crossing_turtle.ycor() >= 210:
        crossing_turtle.goto(0, -225)
        passing_traffic.increase_level()

screen.clear()
display_message = Turtle()
display_message.hideturtle()
display_message.write(f"Game Over", align ="center", font = ("Verdana", 36, "bold"))

screen.exitonclick()