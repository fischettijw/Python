#https://docs.python.org/3.3/library/turtle.html?highlight=turtle
import turtle

ts = turtle.Screen()
ts.title("Joseph Fischetti")
ts.bgcolor("cyan")
t = turtle.Turtle()
t.speed(0)

t.color("red","yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()

t.hideturtle()
ts.exitonclick()