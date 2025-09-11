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
   
def addSquares(iRange,x,y):
  for i in range(iRange):
    drawSquare(x)
    x = x+y

# addSquares(5,25,25)

def squareFractal2():
  length = 5
  for i in range(60):
    drawSquare(length)
    length += 5
    t.left(5)
# squareFractal2()

def drawStar(length):
  for i in range(5):
    t.forward(length)
    t.right(144)

# drawStar(100)

def starFractal():
  length = 15
  for i in range(60):
    drawStar(length)
    t.right(5)
    length += 10

# starFractal()

turtle.done()