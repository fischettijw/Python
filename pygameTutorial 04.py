# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
import pygame

import os
os.system('cls')


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))  # This will draw our background image at (0,0)

    if walkCount+1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 2
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 2
    else:
        win.blit(char, (x, y))

    pygame.display.update()


pygame.init()
scrn_width = 1280
scrn_height = 720
win = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("First Game with PyGame   by Joseph Fischetti")

# This goes outside the while loop, near the top of the program
imgPath = 'D:\Documents\VS Code\Python\pygame_images'
walkRight = [pygame.image.load(imgPath + '\R1.png'), pygame.image.load(imgPath + '\R2.png'),
             pygame.image.load(
                 imgPath + '\R3.png'), pygame.image.load(imgPath + '\R4.png'),
             pygame.image.load(
                 imgPath + '\R5.png'), pygame.image.load(imgPath + '\R6.png'),
             pygame.image.load(
                 imgPath + '\R7.png'), pygame.image.load(imgPath + '\R8.png'),
             pygame.image.load(imgPath + '\R9.png')]
walkLeft = [pygame.image.load(imgPath + '\L1.png'), pygame.image.load(imgPath + '\L2.png'),
            pygame.image.load(
                imgPath + '\L3.png'), pygame.image.load(imgPath + '\L4.png'),
            pygame.image.load(
                imgPath + '\L5.png'), pygame.image.load(imgPath + '\L6.png'),
            pygame.image.load(
                imgPath + '\L7.png'), pygame.image.load(imgPath + '\L8.png'),
            pygame.image.load(imgPath + '\L9.png')]
bg = pygame.image.load(imgPath + '\\game_background_1280X720.jpeg')
char = pygame.image.load(imgPath + '\\standing.png')

clock = pygame.time.Clock()
width = 64
height = 64
x = scrn_width/4
y = scrn_height - height
vel = 5

isJump = False
initJumpCount = 10
jumpCount = initJumpCount
left = False
right = False
walkCount = 0


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < scrn_width-width-vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < scrn_height-height-vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -initJumpCount:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = initJumpCount

    redrawGameWindow()


pygame.quit()
