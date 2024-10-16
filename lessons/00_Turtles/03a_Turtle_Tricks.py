"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

t = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

t.speed(2)
t.goto(-300,-100)
t.begin_fill()
t.pencolor('blue')
t.fillcolor('blue')

for i in range(4):
    t.forward(600)   
    t.left(90) 

t.end_fill()
t.penup()
t.goto(-200,-100)
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.pendown()

def draw_house():
    for i in range(4):
        t.forward(80)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-170,-100)
    t.begin_fill()
    t.pendown()
    t.pencolor('orange')
    t.fillcolor('orange')
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-185,-60)
    t.pencolor('white')
    t.pendown()
    for i in range(4):
        t.forward(16)
        t.left(90)
    t.penup()
    t.goto(-150,-60)
    t.pendown()
    for i in range(4):
        t.forward(16)
        t.left(90)
    t.penup()
    t.goto(-210,-30)
    t.pencolor('orange')
    t.fillcolor('orange')
    t.begin_fill()
    t.pendown()
    t.forward(105)
    t.left(120)
    t.forward(50)
    t.left(60)
    t.forward(60)
    t.left(60)
    t.forward(50)
    t.end_fill()

draw_house()

t.penup()
t.goto(-300,-160)
t.begin_fill()
t.pencolor ('black')
t.fillcolor ('black')
t.pendown()
t.left(120)

for i in range(2):
    t.forward(600)
    t.left(90)
    t.forward(50)
    t.left(90)

t.end_fill()
t.goto(-300,-135)
t.pencolor('yellow')

for i in range(15):
    t.forward(20)
    t.penup()
    t.forward(20)
    t.pendown()

t.penup()
t.goto(-300,-110)
t.fillcolor('green')
t.pencolor('green')
t.begin_fill()
t.pendown()

for i in range(2):
    t.forward(600)
    t.left(90)
    t.forward(10)
    t.left(90)
    
t.end_fill()
t.left(270)
t.forward(150)
t.left(90)
t.begin_fill()

for i in range(2):
    t.forward(600)
    t.left(90)
    t.forward(100)
    t.left(90)

t.end_fill()

turtle.exitonclick()                    # Close the window when we click on it
