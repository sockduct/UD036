import turtle
import math

def myinitials():
    bob = turtle.Turtle()
    # Start of J - Top
    bob.forward(75)
    bob.right(180)
    bob.forward(25)
    bob.left(90)
    bob.forward(75)
    bob.right(90)
    bob.penup()
    bob.forward(50)
    bob.left(90)
    bob.pendown()
    bob.circle(25,180)
    bob.penup()
    bob.forward(75)
    bob.right(90)
    bob.forward(25 + 10)
    # Start of R
    bob.pendown()
    bob.right(90)
    bob.forward(100)
    bob.right(180)
    bob.forward(100)
    bob.right(90)
    bob.forward(30)
    bob.right(180)
    bob.circle(25,-180)
    bob.right(180)
    bob.forward(30)
    bob.right(180)
    bob.forward(30)
    bob.right(60)
    rleg = math.sqrt(50**2 + 25**2)
    bob.forward(rleg)
    bob.penup()
    bob.left(60)
    bob.forward(10)
    # Start of S
    bob.pendown()
    bob.forward(25)
    bob.circle(25,180)
    bob.right(180)
    bob.circle(25,-180)
    bob.right(180)
    bob.forward(25)
    bob.hideturtle()

# Main
window = turtle.Screen()
#
myinitials()
#
window.exitonclick()

