from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day21/data.txt") as high_score_data_file:
            self.high_score = int(high_score_data_file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        with open("Day21/data.txt", mode="w") as high_score_data_file:
            high_score_data_file.write(f"{self.high_score}")
        self.clear()
        self.write(f"Score: {self.score} '|' High Score: {self.high_score}", align ="center", font = ("Arial", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align ="center", font = ("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()