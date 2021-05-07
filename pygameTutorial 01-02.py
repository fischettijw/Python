# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
import pygame


def draw_triple_square():
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(win, (255, 255, 255), (x+10, y+10, width-20, height-20))
    pygame.draw.rect(win, (0, 255, 0), (x+20, y+20, width-40, height-40))


pygame.init()
scrn_width = 800
scrn_height = 800
win = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("First Game with PyGame   by Joseph Fischetti")

x = 50
y = 50
width = 60
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < scrn_width-width-vel:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < scrn_height-height-vel:
        y += vel

    win.fill((0, 0, 0))  # Fills the screen with black

    draw_triple_square()
    pygame.display.update()

pygame.quit()
