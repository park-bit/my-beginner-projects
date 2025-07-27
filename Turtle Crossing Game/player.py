from scoreboard import Scoreboard
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
cars=CarManager()
scoreboard=Scoreboard(0)

class Player(Turtle):
    def __init__(self, car_manager, scoreboard):
        super().__init__()
        self.level_count=0
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.car_manager = car_manager
        self.scoreboard = scoreboard

    def move_turtle(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def check_position(self):
        if self.ycor()==FINISH_LINE_Y:
            self.goto(0, 300)
            self.goto(STARTING_POSITION)
            self.scoreboard.increase_score(self.level_count)
            self.level_count+=1
            self.car_manager.level_up()



