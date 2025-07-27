import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move= 10
        self.move_speed=0.1

    def move(self):
        new_x= self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.7
    def scorecount(self, player1_score, player2_score, player_no):
        player=Turtle()
        player.penup()
        player.speed("fastest")
        player.pencolor("white")
        time.sleep(0.1)
        player.hideturtle()
        time.sleep(0.1)

        if player_no==1:
            player.color("white")
            player.goto(-280, 260)
            player.write(f"Player 1: {player1_score}", align="center", font=("Arial", 20, "normal"))

        if player_no==2:
            player.color("white")
            player.goto(280, 260)
            player.write(f"Player 2: {player2_score}", align="center", font=("Arial", 20, "normal"))

    def erase(self, player1_score, player2_score, player_no):
        player = Turtle()
        player.penup()
        time.sleep(0.1)
        player.speed("fastest")
        player.pencolor("black")
        player.hideturtle()
        time.sleep(0.1)
        player.clear()
        if player_no == 1:
            player.color("black")
            player.goto(-280, 260)
            player.write(f"Player 1: {player1_score}", align="center", font=("Arial", 20, "normal"))

        if player_no == 2:
            player.color("black")
            player.goto(280, 260)
            player.write(f"Player 2: {player2_score}", align="center", font=("Arial", 20, "normal"))
