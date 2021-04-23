# Basic Pong game with Python

import turtle

win = turtle.Screen()
win.title('Pong by Chance')
win.bgcolor('black')
win.setup(width=800, height=800)
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
ball.color('white')
ball.penup()
ball.goto(0, 0)

# paddle functions


def paddle_a_up():
    y = paddle_a.ycor()  # ycor is from the turtle module
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # ycor is from the turtle module
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # ycor is from the turtle module
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # ycor is from the turtle module
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
