"""Step 3:  In MyFile.py, define a function for the turtle program that will draw
a regular polygon with 'n' sides."""
n  = int(input())
import turtle
def meme(o):
    Vex = turtle.Turtle()
    Vex.speed(0)
    for x in range (n):
        Vex.forward(1)
        Vex.right((360/n))
meme(n)
