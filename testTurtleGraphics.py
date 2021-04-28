import time
import turtle

ts = turtle.Screen()
ts.title("Joseph Fischetti")
ts.bgcolor("yellow")
t = turtle.Turtle()
tt = turtle.Turtle()

t.pendown()
t.pencolor("cyan")
t.width(5)
t.speed(10)


for i in range(4):
    t.forward(100)
    t.right(90)
t.hideturtle()


ts.exitonclick()
# ts.mainloop( )
