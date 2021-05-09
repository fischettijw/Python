"""Draw random ellipses.
"""
from graphics import *
import random
import time
import os
os.system('cls')


def main():
    win = GraphWin("Random Circles", 500, 500)
    for i in range(200):
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, b)

        radius = random.randrange(3, 40)
        x = random.randrange(radius, win.width-radius)
        y = random.randrange(radius, win.width-radius)

        # circle = Oval(Point(random.randrange(5, 20)+x, y),
        #               Point(random.randrange(5, 20)+x, 80+y))
        circle = Oval(Point(x, y), Point(140+x, 80+y))
        # circle = Circle(Point(x, y), radius)
        circle.setFill(color)
        circle.draw(win)
        time.sleep(.05)

    win.getMouse()
    win.close()


main()
