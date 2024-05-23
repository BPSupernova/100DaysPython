from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed(8)
        self.setheading(90)

    def update_score(self):
        self.write(f"{self.score}", align ="center", font = ("FFF Forward", 36, "bold"))

    def reposition_left(self):
        self.goto(-50, 225)

    def reposition_right(self):
        self.goto(50, 225)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()