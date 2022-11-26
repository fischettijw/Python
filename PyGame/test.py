import pygame
import os
os.system('cls')

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # This takes: window/surface, color, rect
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()  # This updates the screen so we can see our rectangle

pygame.quit()
