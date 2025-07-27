from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
scoreboard = Scoreboard(0)
player = Player(car, scoreboard)   # Pass references

screen.listen()
screen.onkeypress(player.move_turtle, "Up")
level_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.check_position()  # This now uses the correct car instance!
    car.cars()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()
