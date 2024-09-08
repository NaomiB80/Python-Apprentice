""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""
import turtle
turtle.setup(width=10, height=10)

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t.pencolor=("blue")

for i in range(6):
    t.forward(100)
    t.left(60)


