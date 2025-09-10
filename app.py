import turtle
from turtle import *
t = Turtle()
t.shape("turtle")
t.speed(0)
def drawSquare(x):
   for i in range(4):
    t.forward(x)
    t.left(90)


def squareFractal(x,deg):
  for i in range(x):
    drawSquare(100)
    t.left(deg)   

# squareFractal(60,5)

def doubleSquare(x,y):
  for i in range(x):
    drawSquare(y)
    y = y * 2

# doubleSquare(5,5)
   

turtle.done()