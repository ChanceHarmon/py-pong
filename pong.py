# Basic Pong game with Python

import turtle
import os
# For sound on windows
# import winsound, not os
# to play, winsound.PlaySound('soundfile.wav', winsound.SND_ASYNC)

win = turtle.Screen()
win.title('Pong by Chance')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)  # Stops window from updating, means we manually have to update the window

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # not the speed of paddle movement, speed of animation of paddle
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # default square is 20px by 20px, so stretch_wid = 100
paddle_a.penup()  # Stops turtle from drawing lines while in motion, picks up pen off of page
paddle_a.goto(-350, 0)  # X, Y coords

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # not the speed of paddle movement, speed of animation of paddle
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # default square is 20px by 20px, so stretch_wid = 100
paddle_b.penup()  # Stops turtle from drawing lines while in motion, picks up pen off of page
paddle_b.goto(350, 0)  # X, Y coords

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('green')
ball.penup()
ball.goto(0, 0)

# Ball movement
ball.dx = 0.5
ball.dy = 0.5

# Score

score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))


# paddle functions


def paddle_a_up():
    y = paddle_a.ycor()  # ycor is from the turtle module
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up, 'w')  # assigning keys to be able to move the a paddle
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# Main Game loop

while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check/ keep ball in box

    if ball.ycor() > 290:  # You check > 290 because the middle of the board is 0, less than middle is negative
        # value. Since height is 600 and ball is 20, you measure half of board minus half of ball pixel value
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay bounce.wav&')


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('afplay bounce.wav&')

    if ball.xcor() > 390:  # ball has gone past the right paddle
        ball.goto(0, 0)  # resets the ball in the middle
        ball.dx *= -1  # reverses the ball movement direction
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:  # left paddle, remember 390 because half of width is 400 - ball_width/2
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

    # Paddle and Ball Collisions
    # ball xcords need to be greater than 340 but less than 350
    # if you don't have both conditions, the ball can get stuck behind the paddle
    # second big condition is center of paddle to upper limit and center to lower limit,
    # upper limit must be less than cur ball location
    # lower limit must be greater than cur ball location
    # the ball xcords are opposite for the left paddle
    if (330 < ball.xcor() < 340) and (paddle_b.ycor() + 55 > ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(330)
        ball.dx *= -1
        os.system('afplay bounce.wav&')

    if (-330 > ball.xcor() > -340) and (paddle_a.ycor() + 55 > ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-330)
        ball.dx *= -1
        os.system('afplay bounce.wav&')
