#This is a game developed by me: Saul Mdo
#March 11th, 2020 @ midnight

import turtle

wn = turtle.Screen()

wn.title("PyngPong by Saul")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Main game loop

while True:
    wn.update()