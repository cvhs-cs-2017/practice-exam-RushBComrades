"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
Vex = turtle.Turtle()
Vex.speed(0)
Vex.up()
Vex.goto(0,150)
Vex.down()
for x in range (100):
        Vex.forward(15)
        Vex.right((360/100))
print("done")
input()
