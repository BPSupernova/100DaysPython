from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

player = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")


game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    player.move_snake()

    if player.segments[0].distance(food) < 15:
        food.refresh_food()
        player.extend()
        scoreboard.increase_score()

    if player.segments[0].xcor() > 300 or player.segments[0].xcor() < -300 or player.segments[0].ycor() > 300 or player.segments[0].ycor() < -300:
        game_active = False
        scoreboard.game_over()

    for segment in player.segments:
        if segment == player.segments[0]:
            continue
        if player.segments[0].distance(segment) < 10:
            game_active = False
            scoreboard.game_over()

screen.exitonclick()