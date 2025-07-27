from Tools.demo.spreadsheet import center

FONT = ("Courier", 24, "normal")
from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()


        self.goto(0, 270)
        self.color("black")
        self.write(f"Player Level: {level}", align="center",  font=("Courier", 20, "bold"))

    def increase_score(self, level):
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Player Level: {level}", align="center",  font=("Courier", 20, "bold"))
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Player Level: {level}", align="center",  font=("Courier", 20, "bold"))
        level+=1
        score=Turtle()
        score.hideturtle()
        score.penup()
        score.goto(0, 270)
        score.color("black")
        score.write(f"Player Level: {level}", align="center", font=("Courier", 20, "bold"))

    def game_over(self):
        game=Turtle()
        game.hideturtle()
        game.penup()
        game.color("BLACK")
        game.goto(0,0)
        game.write("GAME OVER", font=("Courier", 24, "bold"))