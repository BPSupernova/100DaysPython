from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

player = Snake()

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



screen.exitonclick()