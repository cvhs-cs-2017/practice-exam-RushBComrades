""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle
Vex = turtle.Turtle()
Vex.color("Blue")
Vex.speed(0)
Vex.up()
Vex.goto(0,-90)
Vex.down()
Vex.circle(180)
Vex.up()
Vex.goto(-60,80)
Vex.down()
Vex.circle(40)
Vex.up()
Vex.goto(60,80)
Vex.down()
Vex.circle(40)
Vex.up()
Vex.goto(60,30)
Vex.down()
Vex.right(90)
for x in range(180):
    Vex.forward(1)
    Vex.right(1)
Vex.right(90)
Vex.forward(118)
input()
from MyFile.py import meme
meme(input())
