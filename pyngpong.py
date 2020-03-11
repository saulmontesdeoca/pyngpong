#This is a game developed by me: Saul Mdo
#March 11th, 2020 @ midnight

import turtle

wn = turtle.Screen()

wn.title("PyngPong by Saul")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#The ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Functions
#For Paddle A
def paddleA_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddleA_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#For Paddle A
def paddleB_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddleB_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

#Main game loop

while True:
    wn.update()