# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
from myPyGame import *
import os
os.system('cls')


def draw_triple_square():
    PG_Rect(win, (255, 0, 0), (x, y, width, height))
    PG_Rect(win, (255, 255, 255), (x+10, y+10, width-20, height-20))
    PG_Rect(win, (0, 255, 0), (x+20, y+20, width-40, height-40))


PG_Init()

scrn_width = 800
scrn_height = 800
win = PG_DplyMode((scrn_width, scrn_height))

PG_Caption("First Game with PyGame   by Joseph Fischetti")


width = 60
height = 60
x = (scrn_width-width)/2
y = (scrn_height-height)/2
vel = 5

isJump = False
initJumpCount = 10
jumpCount = initJumpCount

run = True

while run:
    PG_Delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = PG_KeyPressed()

    if keys[PG_K_LEFT] and x > vel:
        x -= vel
    if keys[PG_K_RIGHT] and x < scrn_width-width-vel:
        x += vel

    if not(isJump):
        if keys[PG_K_UP] and y > vel:
            y -= vel
        if keys[PG_K_DOWN] and y < scrn_height-height-vel:
            y += vel
        if keys[PG_K_SPACE]:
            isJump = True
    else:  # https://youtu.be/2-DNswzCkqk?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&t=757
        if jumpCount >= -initJumpCount:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = initJumpCount

    win.fill((0, 0, 0))  # Fills the screen with black

    draw_triple_square()
    PG_DplyUpdate()

pygame.quit()
