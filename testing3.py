import sys
import os
import pygame
from myPyGame import *
os.system('cls')


PG_Init()

size = width, height = 640, 480
speed = [4, 2]
black = 0, 0, 0

screen = PG_DplyMode(size)

imgPath = 'D:\Documents\VS Code\Python\pygame_images'
ball = PG_ImgLoad(imgPath + '\\standing.png')

ballrect = ball.get_rect()

while 1:
    PG_Delay(10)
    for event in PG_GetEvents():
        if event.type == PG_Quit:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
