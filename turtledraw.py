# Modules
# See:  https://docs.python.org/2/library/turtle.html
import turtle
import math

def drawsquare(length):
    franklin = turtle.Turtle()
    franklin.shape('turtle')
    franklin.color('blue')
    # 1-10, 1=slowest, 10=fastest, 0=instant
    franklin.speed(0)
    #
    for j in range(36):
        for i in range(4):
            franklin.forward(length)
            franklin.right(90)
        franklin.left(10)

def drawcircle(radius):
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('pink')
    angie.circle(radius)

def drawtriangle(length):
    george = turtle.Turtle()
    george.shape('triangle')
    george.color('green')
    #for i in range(1,4):
    #    george.forward(length)
    #    george.left(360 - (30 * i))
    george.penup()
    george.forward(length)
    george.pendown()
    george.forward(length)
    george.left(90)
    george.forward(length)
    george.left(135)
    george.forward(math.sqrt(length**2 + length**2))

# Global
window = turtle.Screen()
window.bgcolor('red')
#
drawsquare(100)
drawcircle(100)
drawtriangle(100)
window.exitonclick()

