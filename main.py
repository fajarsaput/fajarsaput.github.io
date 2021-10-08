import turtle

turtle.bgcolor("black")
turtle.pensize(4)

a=turtle.Turtle()
a.penup()
a.goto(-240,45)
a.pendown()
a.color("yellow")
style=('courier',80,'italic')
a.write('I',font=style,align='center')

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red","red")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.0)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()

a=turtle.Turtle()
a.penup()
a.goto(240,45)
a.pendown()
a.color("yellow")
style=('courier',80,'italic')
a.write('YOU',font=style,align='center')