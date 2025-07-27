import time

from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on=True
snake=Snake()
food=Food()
scb = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        scb.increasescore()
        snake.extend()

    if snake.head.xcor()>280 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-290:
        game_is_on = False
        tim=Turtle()
        tim.penup()
        tim.hideturtle()
        tim.color("white")
        tim.write("GAME OVER", align="center", font=("Courier", 21, "bold"))

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on = False
            tim = Turtle()
            tim.penup()
            tim.hideturtle()
            tim.color("white")
            tim.write("GAME OVER", align="center", font=("Courier", 21, "bold"))


screen.exitonclick()


















screen.exitonclick()