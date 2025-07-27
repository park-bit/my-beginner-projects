from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Your score: {self.score}", align="center", font=("Arial", 21, "normal"))
    def increasescore(self):
        self.score +=1
        self.clear()
        self.write(f"Your score: {self.score}", align="center", font=("Courier", 21, "normal"))