import math
import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

def drawSquare(x):
   for i in range(4):
    t.forward(x)
    t.left(90)

# drawSquare(200)

def drawEqualTriangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)

# drawEqualTriangle(200)

def drawRightTriangle(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(135)
    t.forward(math.sqrt(2 * x**2))

# drawRightTriangle(100)

def drawRect(x,y):
   for i in range(2):
      t.forward(x)
      t.left(90)
      t.forward(y)
      t.left(90)

# drawRect(125,100)
drawEqualTriangle(90)


turtle.done()

def message(input):
    print(input)

message("wassuppp")