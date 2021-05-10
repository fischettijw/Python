# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
import pygame

import os
os.system('cls')


class player(object):
    initJumpCount = 10

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = player.initJumpCount
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount+1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 2
        elif man.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 2
        else:
            win.blit(char, (self.x, self.y))


def redrawGameWindow():
    win.blit(bg, (0, 0))  # This will draw our background image at (0,0)
    man.draw(win)
    pygame.display.update()


pygame.init()
scrn_width = 1280
scrn_height = 720
win = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("First Game with PyGame   by Joseph Fischetti")

# This goes outside the while loop, near the top of the program
imgPath = 'D:\Documents\VS Code\Python\PyGame\PyGame Tutorial\pygame_images'
# imgPath = 'D:\Documents\VS Code\Python\pygame_images'
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

man = player(300, scrn_height - 64, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < scrn_width-man.width-man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not(man.isJump):
        # if keys[pygame.K_UP] and man.y > man.vel:
        #     man.y -= man.vel
        # if keys[pygame.K_DOWN] and y < scrn_height-man.height-man.vel:
        #     man.y += man.vel
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -man.initJumpCount:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = man.initJumpCount

    redrawGameWindow()


pygame.quit()
