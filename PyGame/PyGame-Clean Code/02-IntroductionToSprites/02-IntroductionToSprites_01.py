# https://www.youtube.com/watch?v=hDu8mcAlY4E&list=PL8ui5HK3oSiHnIdi0XIAVXHAeulNmBrLy&index=3

import pygame
import sys
import random
import os

from pygame.version import PygameVersion
os.system('cls')


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()

    def shoot(self, sound_path):
        self.gunshot = pygame.mixer.Sound(sound_path)
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# General Setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('An Introduction to Sprites')

# Gane Screen
screen_width = 1920 - 120
screen_height = 1080 - 120
screen = pygame.display.set_mode((screen_width, screen_height))
path = 'D:\\Documents\\VS Code\\Python\\PyGame\\PyGame-Clean Code\\02-IntroductionToSprites\\'
background = pygame.image.load(path+'\BG.jpg')
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair(path+'\crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(40):
    new_target = Target(path + 'target.png', random.randrange(0,
                        screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot(path+'\gunshot.mp3')

    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.flip()
    clock.tick(60)
