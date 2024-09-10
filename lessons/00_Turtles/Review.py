import turtle
turtle.setup(width=500, height=500)

t = turtle.Turtle()

t.shape('turtle')
t.speed(1)

colors = ['red', 'blue', 'green', 'black', 'yellow']

def drawPolygon(x, y, sides, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(sides):
        t.pencolor(colors[i])
        t.forward(100)
        t.left(360/ sides)
   
drawPolygon(-100, 100, 5, t)
drawPolygon(-100, 100, 4, t)

turtle.exitonclick()

