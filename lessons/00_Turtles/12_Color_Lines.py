"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 

forward=100
left=90
colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
    tina.color(color)
    tina.forward(forward)
    tina.left(left)

tina.penup()
tina.goto(-200,0)

forward=100
left=90
colors = [ 'black', 'orange', 'red', 'blue']    # define a list of colors

tina.pendown()
for color in colors:                            # loop through the colors
    tina.color(color)
    tina.forward(forward)
    tina.left(left)
# 2) Make another square, but put the colors in reverse order, using a negative index. 

tina.done()