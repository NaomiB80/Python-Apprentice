"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
# def getRandomColor():
#     return "#%06X" % (random.randint(0, 0xFFFFFF))


# colors = ["red", "blue", "green", "yellow", "orange"]


# def getNextColor(i):
#     return colors[i % len(colors)]

turtle.setup (width=600, height=600) 
window = turtle.Screen()

baseSize = 150  # the size of the black part of the star
flameSize = 200  # the length of the flaming arms

t = turtle.Turtle() 

t.goto(30,20)

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(25):
    t.pencolor("red")

    t.fillcolor("yellow") 
   
    t.begin_fill()

    t.forward(70) 

    t.left(130) 

    t.forward(flameSize) 

    t.right(40) 

    t.forward(flameSize) 

    t.right(70) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 
