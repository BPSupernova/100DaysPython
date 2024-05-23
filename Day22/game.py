from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.screensize(canvheight=600, canvwidth=800, bg='black')
screen.setup(width=800, height=600)
screen.tracer(0)

game_active = True

player1 = Paddle()
player2 = Paddle()

player1_score = Score()
player2_score = Score()

ball = Ball()

center_line = []
for num in range(-300, 300, 30):
    dash_line = Turtle('square')
    dash_line.speed('fastest')
    dash_line.color('white')
    dash_line.penup()
    dash_line.goto(0, num)
    dash_line.setheading(90)
    dash_line.shapesize(stretch_len=0.5, stretch_wid=0.1)


player1.goto(-300, 0)
player2.goto(300, 0)

screen.listen()

screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")

screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")

player1_score.reposition_left()
player2_score.reposition_right()
player1_score.update_score()
player2_score.update_score()

while game_active:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()

    if (player1.distance(ball) < 50 and ball.xcor() < -270) or (player2.distance(ball) < 50 and ball.xcor() > 270):
        ball.collide()

    if ball.xcor() > 400:
        player1_score.increase_score()
        ball.goto(0, 0)
        ball.collide() # To switch x-cor

    if ball.xcor() < -400:
        player2_score.increase_score()
        ball.goto(0, 0)
        ball.collide() # To switch x-cor

    if player1_score.score == 11:
        game_active = False
        screen.clear()
        display_message = Turtle()
        display_message.hideturtle()
        display_message.write(f"Player 1 Won!", align ="center", font = ("FFF Forward", 36, "bold"))
    elif player2_score.score == 11:
        game_active = False
        screen.clear()
        display_message = Turtle()
        display_message.hideturtle()
        display_message.write(f"Player 2 Won!", align ="center", font = ("FFF Forward", 36, "bold"))

screen.exitonclick()