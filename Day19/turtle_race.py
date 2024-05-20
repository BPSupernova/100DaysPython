from random import randint
from turtle import Turtle, Screen 

def add_turtle_to_race(turtle, list_of_racers):
    turtle.shape('turtle')
    turtle.speed(2)
    turtle.penup()
    list_of_racers.append(turtle)

def start_race(list_of_racers, list_of_racer_colors):
    colors_assigned = 0
    for racer in list_of_racers:
        racer.teleport(-300, 100 - ((200 / 3) * colors_assigned))
        racer.color(list_of_racer_colors[colors_assigned])
        colors_assigned += 1

def move_racers(list_of_racers, list_of_racer_names, bet):
    racer_num = 0
    for racer in list_of_racers:
        racer.forward(randint(10, 25))
        if racer.xcor() >= 390:
            print(f"{list_of_racer_names[racer_num]} won the race!")
            if bet == list_of_racer_names[racer_num]:
                print("Congrats! Your guess paid off")
            else:
                print("Ohhh!! You guessed wrong, but you'll get it next time!")
            return True
        racer_num += 1
    return False

racers = []
racer_names = ['Doug', 'Jimmy', 'Tracy', 'Smith']
racer_colors = ['red', 'blue', 'green', 'purple']

race_over = False

doug = Turtle()
jimmy = Turtle()
tracy = Turtle()
smith = Turtle()

add_turtle_to_race(doug, racers)
add_turtle_to_race(jimmy, racers)
add_turtle_to_race(tracy, racers)
add_turtle_to_race(smith, racers)

print(racers)

screen =  Screen()

response = screen.textinput("We're off to the races!", "Which turtle will finish first? Doug, Jimmy, Tracy, or Smith?")

start_race(racers, racer_colors)

while  not race_over:
    race_over = move_racers(racers, racer_names, response)
screen.bye()