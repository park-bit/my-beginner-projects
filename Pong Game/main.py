import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
both = l_paddle or r_paddle

# handlers for key state
r_up_pressed = False
r_down_pressed = False
l_up_pressed = False
l_down_pressed = False


# Key press/release handlers
def r_up_press():
    global r_up_pressed
    r_up_pressed = True


def r_up_release():
    global r_up_pressed
    r_up_pressed = False


def r_down_press():
    global r_down_pressed
    r_down_pressed = True


def r_down_release():
    global r_down_pressed
    r_down_pressed = False


def l_up_press():
    global l_up_pressed
    l_up_pressed = True


def l_up_release():
    global l_up_pressed
    l_up_pressed = False


def l_down_press():
    global l_down_pressed
    l_down_pressed = True


def l_down_release():
    global l_down_pressed
    l_down_pressed = False


# Keyboard bindings
screen.listen()
screen.onkeypress(r_up_press, "Up")
screen.onkeyrelease(r_up_release, "Up")
screen.onkeypress(r_down_press, "Down")
screen.onkeyrelease(r_down_release, "Down")
screen.onkeypress(l_up_press, "w")
screen.onkeyrelease(l_up_release, "w")
screen.onkeypress(l_down_press, "s")
screen.onkeyrelease(l_down_release, "s")

p1score = 0
p2score = 0
score1 = ball.scorecount(p1score, p2score, 1)
score2 = ball.scorecount(p1score, p2score, 2)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Continuous movement: move paddles if the key is held down
    if r_up_pressed:
        r_paddle.go_up()
    if r_down_pressed:
        r_paddle.go_down()
    if l_up_pressed:
        l_paddle.go_up()
    if l_down_pressed:
        l_paddle.go_down()

    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball missed (scores)
    if ball.xcor() > 360:
        ball.speed("fastest")
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        ball.clear()
        ball.erase(p1score, p2score, 1)
        p1score += 1
        ball.scorecount(p1score, p2score, 1)

    elif ball.xcor() < -360:
        ball.speed("fastest")
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        ball.clear()
        ball.erase(p1score, p2score, 2)
        p2score += 1
        ball.scorecount(p1score, p2score, 2)

screen.exitonclick()
